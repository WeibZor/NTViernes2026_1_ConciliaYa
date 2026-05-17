package com.example.demo.model;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "mediacion")
public class Mediacion {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "conflicto_id", nullable = false)
    private Conflicto conflicto;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "usuario_mediador_id", nullable = false)
    private Usuario usuarioMediador;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "estado_conflicto_id", nullable = false)
    private EstadoConflicto estadoConflicto;

    @Column(name = "fecha_programada")
    private LocalDateTime fechaProgramada;

    @Column(length = 200)
    private String lugar;

    @Column(length = 1000)
    private String observaciones;

    @Column(length = 200)
    private String resultado;

    @Column(name = "fecha_registro", nullable = false)
    private LocalDateTime fechaRegistro = LocalDateTime.now();

    @Column(nullable = false)
    private Boolean activo = true;

    public Mediacion() {
    }

    public Long getId() {
        return id;
    }

    public Conflicto getConflicto() {
        return conflicto;
    }

    public void setConflicto(Conflicto conflicto) {
        this.conflicto = conflicto;
    }

    public Usuario getUsuarioMediador() {
        return usuarioMediador;
    }

    public void setUsuarioMediador(Usuario usuarioMediador) {
        this.usuarioMediador = usuarioMediador;
    }

    public EstadoConflicto getEstadoConflicto() {
        return estadoConflicto;
    }

    public void setEstadoConflicto(EstadoConflicto estadoConflicto) {
        this.estadoConflicto = estadoConflicto;
    }

    public LocalDateTime getFechaProgramada() {
        return fechaProgramada;
    }

    public void setFechaProgramada(LocalDateTime fechaProgramada) {
        this.fechaProgramada = fechaProgramada;
    }

    public String getLugar() {
        return lugar;
    }

    public void setLugar(String lugar) {
        this.lugar = lugar;
    }

    public String getObservaciones() {
        return observaciones;
    }

    public void setObservaciones(String observaciones) {
        this.observaciones = observaciones;
    }

    public String getResultado() {
        return resultado;
    }

    public void setResultado(String resultado) {
        this.resultado = resultado;
    }

    public LocalDateTime getFechaRegistro() {
        return fechaRegistro;
    }

    public void setFechaRegistro(LocalDateTime fechaRegistro) {
        this.fechaRegistro = fechaRegistro;
    }

    public Boolean getActivo() {
        return activo;
    }

    public void setActivo(Boolean activo) {
        this.activo = activo;
    }
}
