import React from 'react';
import '../styles/ConflictoCard.css';

/**
 * Componente reutilizable para mostrar un conflicto.
 * Implementa presentación limpia y reutilizable.
 */
function ConflictoCard({ conflicto, onEliminar }) {
  const getPrioridadColor = (prioridad) => {
    switch (prioridad) {
      case 1:
        return 'baja';
      case 2:
        return 'baja-media';
      case 3:
        return 'media';
      case 4:
        return 'alta-media';
      case 5:
        return 'alta';
      default:
        return 'media';
    }
  };

  const getPrioridadText = (prioridad) => {
    const textos = {
      1: 'Baja',
      2: 'Baja-Media',
      3: 'Media',
      4: 'Alta-Media',
      5: 'Alta'
    };
    return textos[prioridad] || 'Media';
  };

  return (
    <div className="conflicto-card">
      <div className="card-header">
        <h3>{conflicto.titulo}</h3>
        <span className={`prioridad ${getPrioridadColor(conflicto.prioridad)}`}>
          {getPrioridadText(conflicto.prioridad)}
        </span>
      </div>

      <div className="card-body">
        <p className="descripcion">{conflicto.descripcion}</p>

        <div className="detalles">
          <div className="detalle">
            <label>Ubicación:</label>
            <span>{conflicto.ubicacion}</span>
          </div>

          {conflicto.tipoConflicto && (
            <div className="detalle">
              <label>Tipo:</label>
              <span>{conflicto.tipoConflicto.nombre}</span>
            </div>
          )}

          {conflicto.estadoConflicto && (
            <div className="detalle">
              <label>Estado:</label>
              <span className="estado">{conflicto.estadoConflicto.nombre}</span>
            </div>
          )}

          <div className="detalle">
            <label>Reportado por:</label>
            <span>{conflicto.usuarioReportante?.nombreCompleto}</span>
          </div>
        </div>

        {conflicto.observaciones && (
          <div className="observaciones">
            <label>Observaciones:</label>
            <p>{conflicto.observaciones}</p>
          </div>
        )}
      </div>

      <div className="card-footer">
        <button className="btn btn-primary">Ver Detalles</button>
        <button className="btn btn-danger"
                onClick={() => onEliminar(conflicto.id)}>
          Eliminar
        </button>
      </div>
    </div>
  );
}

export default ConflictoCard;
