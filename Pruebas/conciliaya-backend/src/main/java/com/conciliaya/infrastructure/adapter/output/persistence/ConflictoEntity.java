package com.conciliaya.infrastructure.adapter.output.persistence;

import jakarta.persistence.*;
import java.time.LocalDateTime;

/**
 * Entidad JPA que representa a los conflictos en la base de datos.
 * Mapea la tabla 'conflictos' de la base de datos.
 */
@Entity
@Table(name = "conflictos")
public class ConflictoEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "titulo", nullable = false, length = 200)
    private String titulo;

    @Column(name = "descripcion", nullable = false, columnDefinition = "TEXT")
    private String descripcion;

    @Column(name = "ubicacion", nullable = false, length = 255)
    private String ubicacion;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "usuario_reportante_id", nullable = false)
    private UsuarioEntity usuarioReportante;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "usuario_involucrado_id")
    private UsuarioEntity usuarioInvolucrado;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "tipo_conflicto_id")
    private TipoConflictoEntity tipoConflicto;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "estado_conflicto_id")
    private EstadoConflictoEntity estadoConflicto;

    @Column(name = "fecha_reporte", nullable = false)
    private LocalDateTime fechaReporte;

    @Column(name = "fecha_actualizacion")
    private LocalDateTime fechaActualizacion;

    @Column(name = "observaciones", columnDefinition = "TEXT")
    private String observaciones;

    @Column(name = "prioridad", nullable = false)
    private Integer prioridad;

    // Constructores
    public ConflictoEntity() {
    }

    public ConflictoEntity(String titulo, String descripcion, String ubicacion, UsuarioEntity usuarioReportante) {
        this.titulo = titulo;
        this.descripcion = descripcion;
        this.ubicacion = ubicacion;
        this.usuarioReportante = usuarioReportante;
        this.fechaReporte = LocalDateTime.now();
        this.prioridad = 3;
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

    public UsuarioEntity getUsuarioReportante() {
        return usuarioReportante;
    }

    public void setUsuarioReportante(UsuarioEntity usuarioReportante) {
        this.usuarioReportante = usuarioReportante;
    }

    public UsuarioEntity getUsuarioInvolucrado() {
        return usuarioInvolucrado;
    }

    public void setUsuarioInvolucrado(UsuarioEntity usuarioInvolucrado) {
        this.usuarioInvolucrado = usuarioInvolucrado;
    }

    public TipoConflictoEntity getTipoConflicto() {
        return tipoConflicto;
    }

    public void setTipoConflicto(TipoConflictoEntity tipoConflicto) {
        this.tipoConflicto = tipoConflicto;
    }

    public EstadoConflictoEntity getEstadoConflicto() {
        return estadoConflicto;
    }

    public void setEstadoConflicto(EstadoConflictoEntity estadoConflicto) {
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
        this.prioridad = prioridad;
    }

    @PreUpdate
    protected void onUpdate() {
        fechaActualizacion = LocalDateTime.now();
    }
}
