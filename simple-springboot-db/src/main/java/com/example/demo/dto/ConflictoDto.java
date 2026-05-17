package com.example.demo.dto;

public class ConflictoDto {

    private Long id;
    private Long usuarioDemandanteId;
    private Long usuarioDemandadoId;
    private Long tipoConflictoId;
    private Long estadoConflictoId;
    private String asunto;
    private String descripcion;
    private Double montoReclamado;

    public ConflictoDto() {
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Long getUsuarioDemandanteId() {
        return usuarioDemandanteId;
    }

    public void setUsuarioDemandanteId(Long usuarioDemandanteId) {
        this.usuarioDemandanteId = usuarioDemandanteId;
    }

    public Long getUsuarioDemandadoId() {
        return usuarioDemandadoId;
    }

    public void setUsuarioDemandadoId(Long usuarioDemandadoId) {
        this.usuarioDemandadoId = usuarioDemandadoId;
    }

    public Long getTipoConflictoId() {
        return tipoConflictoId;
    }

    public void setTipoConflictoId(Long tipoConflictoId) {
        this.tipoConflictoId = tipoConflictoId;
    }

    public Long getEstadoConflictoId() {
        return estadoConflictoId;
    }

    public void setEstadoConflictoId(Long estadoConflictoId) {
        this.estadoConflictoId = estadoConflictoId;
    }

    public String getAsunto() {
        return asunto;
    }

    public void setAsunto(String asunto) {
        this.asunto = asunto;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }

    public Double getMontoReclamado() {
        return montoReclamado;
    }

    public void setMontoReclamado(Double montoReclamado) {
        this.montoReclamado = montoReclamado;
    }
}
