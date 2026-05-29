package com.example.demo.dto;

import com.fasterxml.jackson.annotation.JsonProperty;

public class UsuarioDto {

    private Long id;
    private String nombre;
    private String apellido;
    private String correo;
    private String telefono;
    private Long perfilId;

    // Solo para escritura (POST/PUT), nunca se devuelve en la respuesta
    @JsonProperty(access = JsonProperty.Access.WRITE_ONLY)
    private String password;

    public UsuarioDto() {}

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }
    public String getApellido() { return apellido; }
    public void setApellido(String apellido) { this.apellido = apellido; }
    public String getCorreo() { return correo; }
    public void setCorreo(String correo) { this.correo = correo; }
    public String getTelefono() { return telefono; }
    public void setTelefono(String telefono) { this.telefono = telefono; }
    public Long getPerfilId() { return perfilId; }
    public void setPerfilId(Long perfilId) { this.perfilId = perfilId; }
    public String getPassword() { return password; }
    public void setPassword(String password) { this.password = password; }
}
