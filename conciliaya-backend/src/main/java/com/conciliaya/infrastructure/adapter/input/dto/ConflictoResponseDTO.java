package com.conciliaya.infrastructure.adapter.input.dto;

import java.io.Serializable;
import java.time.LocalDateTime;

/**
 * DTO de respuesta para un Conflicto.
 * Contiene toda la información del conflicto para ser enviada al cliente.
 */
public class ConflictoResponseDTO implements Serializable {

    private static final long serialVersionUID = 1L;

    private Long id;
    private String titulo;
    private String descripcion;
    private String ubicacion;
    private UsuarioResponseDTO usuarioReportante;
    private UsuarioResponseDTO usuarioInvolucrado;
    private TipoConflictoDTO tipoConflicto;
    private EstadoConflictoDTO estadoConflicto;
    private LocalDateTime fechaReporte;
    private LocalDateTime fechaActualizacion;
    private Integer prioridad;
    private String observaciones;

    // Constructor
    public ConflictoResponseDTO() {
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

    public UsuarioResponseDTO getUsuarioReportante() {
        return usuarioReportante;
    }

    public void setUsuarioReportante(UsuarioResponseDTO usuarioReportante) {
        this.usuarioReportante = usuarioReportante;
    }

    public UsuarioResponseDTO getUsuarioInvolucrado() {
        return usuarioInvolucrado;
    }

    public void setUsuarioInvolucrado(UsuarioResponseDTO usuarioInvolucrado) {
        this.usuarioInvolucrado = usuarioInvolucrado;
    }

    public TipoConflictoDTO getTipoConflicto() {
        return tipoConflicto;
    }

    public void setTipoConflicto(TipoConflictoDTO tipoConflicto) {
        this.tipoConflicto = tipoConflicto;
    }

    public EstadoConflictoDTO getEstadoConflicto() {
        return estadoConflicto;
    }

    public void setEstadoConflicto(EstadoConflictoDTO estadoConflicto) {
        this.estadoConflicto = estadoConflicto;
    }

    public LocalDateTime getFechaReporte() {
        return fechaReporte;
    }

    public void setFechaReporte(LocalDateTime fechaReporte) {
        this.fechaReporte = fechaReporte;
    }

    public LocalDateTime getFechaActualizacion() {
        return fechaActualizacion;
    }

    public void setFechaActualizacion(LocalDateTime fechaActualizacion) {
        this.fechaActualizacion = fechaActualizacion;
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
