package com.conciliaya.infrastructure.adapter.input.dto;

import jakarta.validation.constraints.*;
import java.io.Serializable;

/**
 * DTO para crear o actualizar un Conflicto.
 */
public class ConflictoDTO implements Serializable {

    private static final long serialVersionUID = 1L;

    private Long id;

    @NotBlank(message = "El título es obligatorio")
    @Size(min = 10, max = 200, message = "El título debe tener entre 10 y 200 caracteres")
    private String titulo;

    @NotBlank(message = "La descripción es obligatoria")
    @Size(min = 20, max = 2000, message = "La descripción debe tener entre 20 y 2000 caracteres")
    private String descripcion;

    @NotBlank(message = "La ubicación es obligatoria")
    private String ubicacion;

    @NotNull(message = "El usuario reportante es obligatorio")
    private Long usuarioReportanteId;

    private Long usuarioInvolucradoId;

    private Long tipoConflictoId;

    private Long estadoConflictoId;

    @Min(value = 1, message = "La prioridad debe ser mínimo 1")
    @Max(value = 5, message = "La prioridad debe ser máximo 5")
    private Integer prioridad;

    private String observaciones;

    // Constructor
    public ConflictoDTO() {
    }

    // Getters and Setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }

    public String getUbicacion() {
        return ubicacion;
    }

    public void setUbicacion(String ubicacion) {
        this.ubicacion = ubicacion;
    }

    public Long getUsuarioReportanteId() {
        return usuarioReportanteId;
    }

    public void setUsuarioReportanteId(Long usuarioReportanteId) {
        this.usuarioReportanteId = usuarioReportanteId;
    }

    public Long getUsuarioInvolucradoId() {
        return usuarioInvolucradoId;
    }

    public void setUsuarioInvolucradoId(Long usuarioInvolucradoId) {
        this.usuarioInvolucradoId = usuarioInvolucradoId;
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

    public Integer getPrioridad() {
        return prioridad;
    }

    public void setPrioridad(Integer prioridad) {
        this.prioridad = prioridad;
    }

    public String getObservaciones() {
        return observaciones;
    }

    public void setObservaciones(String observaciones) {
        this.observaciones = observaciones;
    }
}
