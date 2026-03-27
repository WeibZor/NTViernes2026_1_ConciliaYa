package com.conciliaya.infrastructure.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.reactive.function.client.WebClient;

/**
 * Configuración de WebClient para cliente HTTP reactivo.
 * Usado para integración con servicios externos como FastAPI.
 */
@Configuration
public class WebClientConfig {

    /**
     * Configura un WebClient con timeout y manejo de errores.
     */
    @Bean
    public WebClient webClient() {
        return WebClient.builder()
                .connectTimeout(java.time.Duration.ofSeconds(5))
                .build();
    }
}
