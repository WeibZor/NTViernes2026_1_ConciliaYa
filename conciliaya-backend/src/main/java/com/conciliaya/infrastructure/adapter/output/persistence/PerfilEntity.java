package com.conciliaya.infrastructure.adapter.output.persistence;

import jakarta.persistence.*;

/**
 * Entidad JPA que representa los perfiles de usuario en la base de datos.
 * Mapea la tabla 'perfiles' de la base de datos.
 */
@Entity
@Table(name = "perfiles")
public class PerfilEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "nombre", nullable = false, unique = true, length = 100)
    private String nombre;

    @Column(name = "descripcion", columnDefinition = "TEXT")
    private String descripcion;

    @Column(name = "activo", nullable = false)
    private Boolean activo;

    // Constructores
    public PerfilEntity() {
    }

    public PerfilEntity(String nombre, String descripcion) {
        this.nombre = nombre;
        this.descripcion = descripcion;
        this.activo = true;
    }

    // Getters and Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }
    public String getDescripcion() { return descripcion; }
    public void setDescripcion(String descripcion) { this.descripcion = descripcion; }
    public Boolean getActivo() { return activo; }
    public void setActivo(Boolean activo) { this.activo = activo; }
}
