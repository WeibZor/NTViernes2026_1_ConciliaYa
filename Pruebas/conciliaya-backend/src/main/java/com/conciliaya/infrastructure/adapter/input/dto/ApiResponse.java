package com.conciliaya.infrastructure.adapter.input.dto;

import java.io.Serializable;
import java.time.LocalDateTime;

/**
 * Respuesta API estándar para todas las respuestas del servidor.
 * Proporciona una estructura consistente para éxito y error.
 */
public class ApiResponse<T> implements Serializable {

    private static final long serialVersionUID = 1L;

    private boolean exito;
    private String mensaje;
    private T datos;
    private String codigo;
    private LocalDateTime timestamp;

    /**
     * Respuesta exitosa con datos.
     */
    public static <T> ApiResponse<T> exitoso(T datos, String mensaje) {
        ApiResponse<T> respuesta = new ApiResponse<>();
        respuesta.exito = true;
        respuesta.datos = datos;
        respuesta.mensaje = mensaje;
        respuesta.timestamp = LocalDateTime.now();
        return respuesta;
    }

    /**
     * Respuesta exitosa sin datos.
     */
    public static <T> ApiResponse<T> exitoso(String mensaje) {
        return exitoso(null, mensaje);
    }

    /**
     * Respuesta de error.
     */
    public static <T> ApiResponse<T> error(String codigo, String mensaje) {
        ApiResponse<T> respuesta = new ApiResponse<>();
        respuesta.exito = false;
        respuesta.codigo = codigo;
        respuesta.mensaje = mensaje;
        respuesta.timestamp = LocalDateTime.now();
        return respuesta;
    }

    /**
     * Respuesta de error sin código.
     */
    public static <T> ApiResponse<T> error(String mensaje) {
        return error("ERROR", mensaje);
    }

    // Getters and Setters
    public boolean isExito() {
        return exito;
    }

    public void setExito(boolean exito) {
        this.exito = exito;
    }

    public String getMensaje() {
        return mensaje;
    }

    public void setMensaje(String mensaje) {
        this.mensaje = mensaje;
    }

    public T getDatos() {
        return datos;
    }

    public void setDatos(T datos) {
        this.datos = datos;
    }

    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public LocalDateTime getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(LocalDateTime timestamp) {
        this.timestamp = timestamp;
    }
}
