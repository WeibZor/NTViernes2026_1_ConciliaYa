package com.conciliaya.domain.model;

import java.io.Serializable;
import java.time.LocalDateTime;

/**
 * Entidad de dominio que representa las mediaciones de conflictos.
 * Registra el proceso de resolución de conflictos.
 */
public class Mediacion implements Serializable {
    
    private static final long serialVersionUID = 1L;
    
    private Long id;
    private Conflicto conflicto;
    private Usuario mediador;
    private LocalDateTime fechaInicio;
    private LocalDateTime fechaFinalizacion;
    private String resultado;
    private String acuerdos;
    private LocalDateTime fechaCreacion;
    private LocalDateTime fechaActualizacion;
    private Boolean completada;

    // Constructor
    public Mediacion() {
    }

    public Mediacion(Conflicto conflicto, Usuario mediador) {
        this.conflicto = conflicto;
        this.mediador = mediador;
        this.fechaInicio = LocalDateTime.now();
        this.fechaCreacion = LocalDateTime.now();
        this.completada = false;
    }

    // Getters and Setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Conflicto getConflicto() {
        return conflicto;
    }

    public void setConflicto(Conflicto conflicto) {
        this.conflicto = conflicto;
    }

    public Usuario getMediador() {
        return mediador;
    }

    public void setMediador(Usuario mediador) {
        this.mediador = mediador;
    }

    public LocalDateTime getFechaInicio() {
        return fechaInicio;
    }

    public void setFechaInicio(LocalDateTime fechaInicio) {
        this.fechaInicio = fechaInicio;
    }

    public LocalDateTime getFechaFinalizacion() {
        return fechaFinalizacion;
    }

    public void setFechaFinalizacion(LocalDateTime fechaFinalizacion) {
        this.fechaFinalizacion = fechaFinalizacion;
    }

    public String getResultado() {
        return resultado;
    }

    public void setResultado(String resultado) {
        this.resultado = resultado;
    }

    public String getAcuerdos() {
        return acuerdos;
    }

    public void setAcuerdos(String acuerdos) {
        this.acuerdos = acuerdos;
    }

    public LocalDateTime getFechaCreacion() {
        return fechaCreacion;
    }

    public void setFechaCreacion(LocalDateTime fechaCreacion) {
        this.fechaCreacion = fechaCreacion;
    }

    public LocalDateTime getFechaActualizacion() {
        return fechaActualizacion;
    }

    public void setFechaActualizacion(LocalDateTime fechaActualizacion) {
        this.fechaActualizacion = fechaActualizacion;
    }

    public Boolean getCompletada() {
        return completada;
    }

    public void setCompletada(Boolean completada) {
        this.completada = completada;
    }

    @Override
    public String toString() {
        return "Mediacion{" +
                "id=" + id +
                ", conflicto=" + conflicto +
                ", mediador=" + mediador +
                ", completada=" + completada +
                '}';
    }
}
