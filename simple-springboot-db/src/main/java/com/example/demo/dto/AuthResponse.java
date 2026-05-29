package com.example.demo.dto;

public class AuthResponse {
    private String token;
    private Long id;
    private String nombre;
    private String correo;
    private Long perfilId;

    public AuthResponse(String token, Long id, String nombre, String correo, Long perfilId) {
        this.token = token;
        this.id = id;
        this.nombre = nombre;
        this.correo = correo;
        this.perfilId = perfilId;
    }

    public String getToken() { return token; }
    public Long getId() { return id; }
    public String getNombre() { return nombre; }
    public String getCorreo() { return correo; }
    public Long getPerfilId() { return perfilId; }
}
