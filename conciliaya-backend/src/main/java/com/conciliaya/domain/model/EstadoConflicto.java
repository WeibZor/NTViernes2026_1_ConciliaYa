package com.conciliaya.domain.model;

import java.io.Serializable;
import java.time.LocalDateTime;

/**
 * Entidad de dominio que representa los estados posibles de un conflicto.
 * Define el ciclo de vida de los conflictos.
 */
public class EstadoConflicto implements Serializable {
    
    private static final long serialVersionUID = 1L;
    
    private Long id;
    private String nombre;
    private String descripcion;
    private Integer orden;
    private LocalDateTime fechaCreacion;
    private LocalDateTime fechaActualizacion;

    // Constructor
    public EstadoConflicto() {
    }

    public EstadoConflicto(String nombre, String descripcion, Integer orden) {
        this.nombre = nombre;
        this.descripcion = descripcion;
        this.orden = orden;
        this.fechaCreacion = LocalDateTime.now();
    }

    // Getters and Setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }

    public Integer getOrden() {
        return orden;
    }

    public void setOrden(Integer orden) {
        this.orden = orden;
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

    @Override
    public String toString() {
        return "EstadoConflicto{" +
                "id=" + id +
                ", nombre='" + nombre + '\'' +
                ", orden=" + orden +
                '}';
    }
}
