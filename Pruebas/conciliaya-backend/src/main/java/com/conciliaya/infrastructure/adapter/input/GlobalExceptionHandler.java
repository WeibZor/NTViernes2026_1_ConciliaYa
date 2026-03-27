package com.conciliaya.infrastructure.adapter.input;

import com.conciliaya.infrastructure.adapter.input.dto.ApiResponse;
import com.conciliaya.infrastructure.exception.ConciliaYaException;
import com.conciliaya.infrastructure.exception.ErrorValidacionException;
import com.conciliaya.infrastructure.exception.RecursoNoEncontradoException;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.FieldError;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.context.request.WebRequest;

import java.util.HashMap;
import java.util.Map;

/**
 * Controlador global para el manejo de excepciones.
 * Proporciona respuestas HTTP consistentes para diferentes tipos de errores.
 */
@ControllerAdvice
public class GlobalExceptionHandler {

    /**
     * Maneja excepciones de validación de argumentos (MethodArgumentNotValidException).
     */
    @ExceptionHandler(MethodArgumentNotValidException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public ResponseEntity<ApiResponse<?>> handleValidationException(
            MethodArgumentNotValidException ex, 
            WebRequest request) {
        
        Map<String, String> errores = new HashMap<>();
        ex.getBindingResult().getAllErrors().forEach((error) -> {
            String fieldName = ((FieldError) error).getField();
            String errorMessage = error.getDefaultMessage();
            errores.put(fieldName, errorMessage);
        });

        ApiResponse<?> respuesta = ApiResponse.error("VALIDACION_ERROR", "Error de validación en los datos");
        return new ResponseEntity<>(respuesta, HttpStatus.BAD_REQUEST);
    }

    /**
     * Maneja excepciones de recurso no encontrado.
     */
    @ExceptionHandler(RecursoNoEncontradoException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public ResponseEntity<ApiResponse<?>> handleRecursoNoEncontrado(
            RecursoNoEncontradoException ex, 
            WebRequest request) {
        
        ApiResponse<?> respuesta = ApiResponse.error(ex.getCodigo(), ex.getMessage());
        return new ResponseEntity<>(respuesta, HttpStatus.NOT_FOUND);
    }

    /**
     * Maneja excepciones personalizadas de ConciliaYa.
     */
    @ExceptionHandler(ConciliaYaException.class)
    public ResponseEntity<ApiResponse<?>> handleConciliaYaException(
            ConciliaYaException ex, 
            WebRequest request) {
        
        ApiResponse<?> respuesta = ApiResponse.error(ex.getCodigo(), ex.getMessage());
        
        // Determinar el código de estado HTTP basado en el tipo de excepción
        HttpStatus status = determinarHttpStatus(ex);
        return new ResponseEntity<>(respuesta, status);
    }

    /**
     * Maneja excepciones de IllegalArgumentException (errores de validación de negocio).
     */
    @ExceptionHandler(IllegalArgumentException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public ResponseEntity<ApiResponse<?>> handleIllegalArgument(
            IllegalArgumentException ex, 
            WebRequest request) {
        
        ApiResponse<?> respuesta = ApiResponse.error("ARGUMENTO_INVALIDO", ex.getMessage());
        return new ResponseEntity<>(respuesta, HttpStatus.BAD_REQUEST);
    }

    /**
     * Maneja todas las excepciones genéricas no capturadas.
     */
    @ExceptionHandler(Exception.class)
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    public ResponseEntity<ApiResponse<?>> handleGlobalException(
            Exception ex, 
            WebRequest request) {
        
        ApiResponse<?> respuesta = ApiResponse.error("ERROR_INTERNO", 
                "Error interno del servidor. Por favor, intente más tarde.");
        
        ex.printStackTrace(); // Loguear el error
        return new ResponseEntity<>(respuesta, HttpStatus.INTERNAL_SERVER_ERROR);
    }

    /**
     * Determina el código de estado HTTP basado en el tipo de excepción.
     */
    private HttpStatus determinarHttpStatus(ConciliaYaException ex) {
        if (ex instanceof RecursoNoEncontradoException) {
            return HttpStatus.NOT_FOUND;
        } else if (ex instanceof ErrorValidacionException) {
            return HttpStatus.BAD_REQUEST;
        } else if (ex.getCodigo().equals("VIOLACION_REGLA_NEGOCIOS")) {
            return HttpStatus.CONFLICT;
        } else if (ex.getCodigo().equals("ERROR_INTEGRACION_EXTERNA")) {
            return HttpStatus.SERVICE_UNAVAILABLE;
        }
        return HttpStatus.INTERNAL_SERVER_ERROR;
    }
}
