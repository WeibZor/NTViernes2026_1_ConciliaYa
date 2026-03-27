import React from 'react';
import '../styles/UsuarioCard.css';

/**
 * Componente para mostrar un usuario.
 */
function UsuarioCard({ usuario, onEliminar }) {
  return (
    <div className="usuario-card">
      <div className="card-header">
        <h3>{usuario.nombreCompleto}</h3>
        {usuario.activo && <span className="estado-activo">Activo</span>}
      </div>

      <div className="card-body">
        <div className="detalle">
          <label>Email:</label>
          <span>{usuario.email}</span>
        </div>
        <div className="detalle">
          <label>Teléfono:</label>
          <span>{usuario.telefono}</span>
        </div>
        <div className="detalle">
          <label>Dirección:</label>
          <span>{usuario.direccion}</span>
        </div>
        <div className="detalle">
          <label>Documento:</label>
          <span>{usuario.numeroDocumento}</span>
        </div>
      </div>

      <div className="card-footer">
        <button className="btn btn-primary">Ver Perfil</button>
        <button className="btn btn-danger" onClick={() => onEliminar(usuario.id)}>
          Eliminar
        </button>
      </div>
    </div>
  );
}

export default UsuarioCard;
