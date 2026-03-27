package com.conciliaya.infrastructure.adapter.output.http;

import com.conciliaya.domain.ports.ClasificadorConflictoPort;
import com.conciliaya.infrastructure.exception.IntegracionExternaException;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Component;
import org.springframework.web.reactive.function.client.WebClient;
import org.springframework.web.reactive.function.client.WebClientResponseException;
import reactor.core.publisher.Mono;

/**
 * Adaptador HTTP que implementa el puerto ClasificadorConflictoPort.
 * Integración con el microservicio FastAPI en Python para clasificación de conflictos.
 * 
 * Responsabilidades:
 * - Comunicación con el servicio externo (FastAPI)
 * - Manejo de errores de comunicación
 * - Conversión de respuestas
 * - Validación de disponibilidad del servicio
 */
@Component
public class ClasificadorConflictoAdapter implements ClasificadorConflictoPort {

    private final WebClient webClient;
    private final String fastApiUrl;
    private final String classifierEndpoint;
    private final long timeout;

    public ClasificadorConflictoAdapter(WebClient webClient,
                                        @Value("${fastapi.url}") String fastApiUrl,
                                        @Value("${fastapi.classifier-endpoint}") String classifierEndpoint,
                                        @Value("${fastapi.timeout}") long timeout) {
        this.webClient = webClient;
        this.fastApiUrl = fastApiUrl;
        this.classifierEndpoint = classifierEndpoint;
        this.timeout = timeout;
    }

    @Override
    public Long clasificarConflicto(String descripcion) {
        ClassificacionResponse response = clasificarConflictoDetallado(descripcion);
        return response.getTipoConflictoId();
    }

    @Override
    public ClassificacionResponse clasificarConflictoDetallado(String descripcion) {
        validarDescripcion(descripcion);

        try {
            ClassificacionRequest request = new ClassificacionRequest(descripcion);
            String url = fastApiUrl + classifierEndpoint;

            ClassificacionResponse response = webClient.post()
                    .uri(url)
                    .bodyValue(request)
                    .retrieve()
                    .bodyToMono(ClassificacionResponse.class)
                    .timeout(java.time.Duration.ofMillis(timeout))
                    .block();

            if (response == null) {
                throw new IntegracionExternaException("FastAPI", "Respuesta vacía del servicio");
            }

            return response;

        } catch (WebClientResponseException.ServiceUnavailable e) {
            throw new IntegracionExternaException("FastAPI", "Servicio no disponible", e);
        } catch (WebClientResponseException e) {
            throw new IntegracionExternaException("FastAPI", 
                    "Error en la respuesta: " + e.getStatusCode(), e);
        } catch (Exception e) {
            throw new IntegracionExternaException("FastAPI", "Error en la comunicación: " + e.getMessage(), e);
        }
    }

    @Override
    public boolean esServicioDisponible() {
        try {
            String url = fastApiUrl + "/health";
            
            HttpStatus status = webClient.get()
                    .uri(url)
                    .retrieve()
                    .toBodilessEntity()
                    .timeout(java.time.Duration.ofMillis(timeout))
                    .map(response -> response.getStatusCode())
                    .block();

            return status != null && status.is2xxSuccessful();

        } catch (Exception e) {
            return false;
        }
    }

    /**
     * Valida que la descripción sea válida.
     */
    private void validarDescripcion(String descripcion) {
        if (descripcion == null || descripcion.isBlank()) {
            throw new IllegalArgumentException("La descripción del conflicto es requerida");
        }
        if (descripcion.length() < 20) {
            throw new IllegalArgumentException("La descripción debe tener al menos 20 caracteres");
        }
    }

    /**
     * Clase para la solicitud al servicio FastAPI.
     */
    public static class ClassificacionRequest {
        private String descripcion;

        public ClassificacionRequest(String descripcion) {
            this.descripcion = descripcion;
        }

        public String getDescripcion() {
            return descripcion;
        }

        public void setDescripcion(String descripcion) {
            this.descripcion = descripcion;
        }
    }
}
