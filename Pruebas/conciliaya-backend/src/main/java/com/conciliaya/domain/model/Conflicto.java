package com.conciliaya.domain.model;

import java.io.Serializable;
import java.time.LocalDateTime;

/**
 * Entidad de dominio que representa los conflictos vecinales.
 * Contiene la información central del sistema de gestión de conflictos.
 */
public class Conflicto implements Serializable {
    
    private static final long serialVersionUID = 1L;
    
    private Long id;
    private String titulo;
    private String descripcion;
    private String ubicacion;
    private Usuario usuarioReportante;
    private Usuario usuarioInvolucrado;
    private TipoConflicto tipoConflicto;
    private EstadoConflicto estadoConflicto;
    private LocalDateTime fechaReporte;
    private LocalDateTime fechaActualizacion;
    private String observaciones;
    private Integer prioridad; // 1 (baja) a 5 (alta)

    // Constructor
    public Conflicto() {
    }

    public Conflicto(String titulo, String descripcion, String ubicacion, 
                     Usuario usuarioReportante, TipoConflicto tipoConflicto) {
        this.titulo = titulo;
        this.descripcion = descripcion;
        this.ubicacion = ubicacion;
        this.usuarioReportante = usuarioReportante;
        this.tipoConflicto = tipoConflicto;
        this.fechaReporte = LocalDateTime.now();
        this.prioridad = 3; // Prioridad media por defecto
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

    public Usuario getUsuarioReportante() {
        return usuarioReportante;
    }

    public void setUsuarioReportante(Usuario usuarioReportante) {
        this.usuarioReportante = usuarioReportante;
    }

    public Usuario getUsuarioInvolucrado() {
        return usuarioInvolucrado;
    }

    public void setUsuarioInvolucrado(Usuario usuarioInvolucrado) {
        this.usuarioInvolucrado = usuarioInvolucrado;
    }

    public TipoConflicto getTipoConflicto() {
        return tipoConflicto;
    }

    public void setTipoConflicto(TipoConflicto tipoConflicto) {
        this.tipoConflicto = tipoConflicto;
    }

    public EstadoConflicto getEstadoConflicto() {
        return estadoConflicto;
    }

    public void setEstadoConflicto(EstadoConflicto estadoConflicto) {
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

    public String getObservaciones() {
        return observaciones;
    }

    public void setObservaciones(String observaciones) {
        this.observaciones = observaciones;
    }

    public Integer getPrioridad() {
        return prioridad;
    }

    public void setPrioridad(Integer prioridad) {
        if (prioridad < 1 || prioridad > 5) {
            throw new IllegalArgumentException("La prioridad debe estar entre 1 y 5");
        }
        this.prioridad = prioridad;
    }

    /**
     * Valida que el conflicto tenga datos requeridos.
     * @return true si es válido
     */
    public boolean esValido() {
        return titulo != null && !titulo.isBlank() &&
               descripcion != null && !descripcion.isBlank() &&
               usuarioReportante != null &&
               tipoConflicto != null;
    }

    @Override
    public String toString() {
        return "Conflicto{" +
                "id=" + id +
                ", titulo='" + titulo + '\'' +
                ", ubicacion='" + ubicacion + '\'' +
                ", prioridad=" + prioridad +
                '}';
    }
}
