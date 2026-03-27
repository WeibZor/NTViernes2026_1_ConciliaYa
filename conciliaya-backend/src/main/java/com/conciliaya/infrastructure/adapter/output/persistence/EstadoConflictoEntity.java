package com.conciliaya.infrastructure.adapter.output.persistence;

import jakarta.persistence.*;
import java.time.LocalDateTime;

/**
 * Entidad JPA que representa los estados de conflictos en la base de datos.
 * Mapea la tabla 'estados_conflicto' de la base de datos.
 */
@Entity
@Table(name = "estados_conflicto")
public class EstadoConflictoEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "nombre", nullable = false, unique = true, length = 100)
    private String nombre;

    @Column(name = "descripcion", columnDefinition = "TEXT")
    private String descripcion;

    @Column(name = "orden", nullable = false)
    private Integer orden;

    @Column(name = "fecha_creacion", nullable = false)
    private LocalDateTime fechaCreacion;

    @Column(name = "fecha_actualizacion")
    private LocalDateTime fechaActualizacion;

    // Constructores
    public EstadoConflictoEntity() {
    }

    public EstadoConflictoEntity(String nombre, String descripcion, Integer orden) {
        this.nombre = nombre;
        this.descripcion = descripcion;
        this.orden = orden;
        this.fechaCreacion = LocalDateTime.now();
    }

    // Getters and Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }
    public String getDescripcion() { return descripcion; }
    public void setDescripcion(String descripcion) { this.descripcion = descripcion; }
    public Integer getOrden() { return orden; }
    public void setOrden(Integer orden) { this.orden = orden; }
    public LocalDateTime getFechaCreacion() { return fechaCreacion; }
    public void setFechaCreacion(LocalDateTime fechaCreacion) { this.fechaCreacion = fechaCreacion; }
    public LocalDateTime getFechaActualizacion() { return fechaActualizacion; }
    public void setFechaActualizacion(LocalDateTime fechaActualizacion) { this.fechaActualizacion = fechaActualizacion; }

    @PreUpdate
    protected void onUpdate() {
        fechaActualizacion = LocalDateTime.now();
    }
}
