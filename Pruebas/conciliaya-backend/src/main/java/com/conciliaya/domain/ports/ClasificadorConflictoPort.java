package com.conciliaya.domain.ports;

/**
 * Puerto para la clasificación de conflictos.
 * Integración con el microservicio FastAPI en Python.
 * Responsable de determinar el tipo de conflicto basándose en su descripción.
 */
public interface ClasificadorConflictoPort {

    /**
     * Clasifica un conflicto basándose en su descripción.
     * Envía la descripción al servicio Python y recibe el tipo identificado.
     * 
     * @param descripcion la descripción del conflicto a clasificar
     * @return el ID del tipo de conflicto identificado
     * @throws RuntimeException si hay error en la comunicación con el servicio
     */
    Long clasificarConflicto(String descripcion);

    /**
     * Clasifica un conflicto y devuelve información detallada.
     * 
     * @param descripcion la descripción del conflicto
     * @return un objeto con la clasificación detallada
     * @throws RuntimeException si hay error en la comunicación
     */
    ClassificacionResponse clasificarConflictoDetallado(String descripcion);

    /**
     * Valida la conectividad con el servicio de clasificación.
     * 
     * @return true si el servicio está disponible
     */
    boolean esServicioDisponible();

    /**
     * Objeto de respuesta de la clasificación.
     */
    class ClassificacionResponse {
        private Long tipoConflictoId;
        private String tipoConflictoNombre;
        private Double confianza;
        private String justificacion;

        public ClassificacionResponse() {
        }

        public ClassificacionResponse(Long tipoConflictoId, String tipoConflictoNombre, Double confianza) {
            this.tipoConflictoId = tipoConflictoId;
            this.tipoConflictoNombre = tipoConflictoNombre;
            this.confianza = confianza;
        }

        // Getters and Setters
        public Long getTipoConflictoId() {
            return tipoConflictoId;
        }

        public void setTipoConflictoId(Long tipoConflictoId) {
            this.tipoConflictoId = tipoConflictoId;
        }

        public String getTipoConflictoNombre() {
            return tipoConflictoNombre;
        }

        public void setTipoConflictoNombre(String tipoConflictoNombre) {
            this.tipoConflictoNombre = tipoConflictoNombre;
        }

        public Double getConfianza() {
            return confianza;
        }

        public void setConfianza(Double confianza) {
            this.confianza = confianza;
        }

        public String getJustificacion() {
            return justificacion;
        }

        public void setJustificacion(String justificacion) {
            this.justificacion = justificacion;
        }
    }
}
