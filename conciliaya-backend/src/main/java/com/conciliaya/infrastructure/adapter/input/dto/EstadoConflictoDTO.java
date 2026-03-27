package com.conciliaya.infrastructure.adapter.input.dto;

import java.io.Serializable;

/**
 * DTO para representar un EstadoConflicto en las respuestas.
 */
public class EstadoConflictoDTO implements Serializable {

    private static final long serialVersionUID = 1L;

    private Long id;
    private String nombre;
    private String descripcion;
    private Integer orden;

    // Constructor
    public EstadoConflictoDTO() {
    }

    public EstadoConflictoDTO(Long id, String nombre) {
        this.id = id;
        this.nombre = nombre;
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
}
