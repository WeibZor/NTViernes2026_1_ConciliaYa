package com.conciliaya.infrastructure.adapter.input.dto;

import jakarta.validation.constraints.*;
import java.io.Serializable;

/**
 * DTO para crear o actualizar una Mediacion.
 */
public class MediacionDTO implements Serializable {

    private static final long serialVersionUID = 1L;

    private Long id;

    @NotNull(message = "El conflicto es obligatorio")
    private Long conflictoId;

    @NotNull(message = "El mediador es obligatorio")
    private Long mediadorId;

    @Size(max = 2000, message = "El resultado no puede exceder 2000 caracteres")
    private String resultado;

    @Size(max = 3000, message = "Los acuerdos no pueden exceder 3000 caracteres")
    private String acuerdos;

    private Boolean completada;

    // Constructor
    public MediacionDTO() {
    }

    // Getters and Setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Long getConflictoId() {
        return conflictoId;
    }

    public void setConflictoId(Long conflictoId) {
        this.conflictoId = conflictoId;
    }

    public Long getMediadorId() {
        return mediadorId;
    }

    public void setMediadorId(Long mediadorId) {
        this.mediadorId = mediadorId;
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

    public Boolean getCompletada() {
        return completada;
    }

    public void setCompletada(Boolean completada) {
        this.completada = completada;
    }
}
