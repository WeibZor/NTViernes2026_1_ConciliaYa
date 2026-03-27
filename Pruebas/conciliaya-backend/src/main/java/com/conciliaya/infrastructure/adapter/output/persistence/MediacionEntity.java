package com.conciliaya.infrastructure.adapter.output.persistence;

import jakarta.persistence.*;
import java.time.LocalDateTime;

/**
 * Entidad JPA que representa las mediaciones en la base de datos.
 * Mapea la tabla 'mediaciones' de la base de datos.
 */
@Entity
@Table(name = "mediaciones")
public class MediacionEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "conflicto_id", nullable = false)
    private ConflictoEntity conflicto;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "mediador_id", nullable = false)
    private UsuarioEntity mediador;

    @Column(name = "fecha_inicio", nullable = false)
    private LocalDateTime fechaInicio;

    @Column(name = "fecha_finalizacion")
    private LocalDateTime fechaFinalizacion;

    @Column(name = "resultado", columnDefinition = "TEXT")
    private String resultado;

    @Column(name = "acuerdos", columnDefinition = "TEXT")
    private String acuerdos;

    @Column(name = "fecha_creacion", nullable = false)
    private LocalDateTime fechaCreacion;

    @Column(name = "fecha_actualizacion")
    private LocalDateTime fechaActualizacion;

    @Column(name = "completada", nullable = false)
    private Boolean completada;

    // Constructores
    public MediacionEntity() {
    }

    public MediacionEntity(ConflictoEntity conflicto, UsuarioEntity mediador) {
        this.conflicto = conflicto;
        this.mediador = mediador;
        this.fechaInicio = LocalDateTime.now();
        this.fechaCreacion = LocalDateTime.now();
        this.completada = false;
    }

    // Getters and Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public ConflictoEntity getConflicto() { return conflicto; }
    public void setConflicto(ConflictoEntity conflicto) { this.conflicto = conflicto; }
    public UsuarioEntity getMediador() { return mediador; }
    public void setMediador(UsuarioEntity mediador) { this.mediador = mediador; }
    public LocalDateTime getFechaInicio() { return fechaInicio; }
    public void setFechaInicio(LocalDateTime fechaInicio) { this.fechaInicio = fechaInicio; }
    public LocalDateTime getFechaFinalizacion() { return fechaFinalizacion; }
    public void setFechaFinalizacion(LocalDateTime fechaFinalizacion) { this.fechaFinalizacion = fechaFinalizacion; }
    public String getResultado() { return resultado; }
    public void setResultado(String resultado) { this.resultado = resultado; }
    public String getAcuerdos() { return acuerdos; }
    public void setAcuerdos(String acuerdos) { this.acuerdos = acuerdos; }
    public LocalDateTime getFechaCreacion() { return fechaCreacion; }
    public void setFechaCreacion(LocalDateTime fechaCreacion) { this.fechaCreacion = fechaCreacion; }
    public LocalDateTime getFechaActualizacion() { return fechaActualizacion; }
    public void setFechaActualizacion(LocalDateTime fechaActualizacion) { this.fechaActualizacion = fechaActualizacion; }
    public Boolean getCompletada() { return completada; }
    public void setCompletada(Boolean completada) { this.completada = completada; }

    @PreUpdate
    protected void onUpdate() {
        fechaActualizacion = LocalDateTime.now();
    }
}
