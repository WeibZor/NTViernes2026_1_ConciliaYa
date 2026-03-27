import React, { useState, useEffect } from 'react';
import { ConflictoService } from '../services/apiService';
import { toast } from 'react-toastify';
import ConflictoCard from '../components/ConflictoCard';
import '../styles/ConflictosPage.css';

/**
 * Página que lista todos los conflictos.
 * Permite filtrar y ordenar conflictos.
 */
function ConflictosPage() {
  const [conflictos, setConflictos] = useState([]);
  const [filtroEstado, setFiltroEstado] = useState('todos');
  const [ordenamiento, setOrdenamiento] = useState('fecha');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    cargarConflictos();
  }, [filtroEstado, ordenamiento]);

  const cargarConflictos = async () => {
    try {
      setLoading(true);

      let response;
      if (filtroEstado === 'todos') {
        response = await ConflictoService.obtenerTodos();
      } else if (filtroEstado === 'prioridad') {
        response = await ConflictoService.obtenerPorPrioridad();
      } else {
        response = await ConflictoService.obtenerPorEstado(filtroEstado);
      }

      setConflictos(response.datos || []);
    } catch (error) {
      toast.error('Error al cargar conflictos');
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  const handleEliminar = async (id) => {
    if (window.confirm('¿Estás seguro de que deseas eliminar este conflicto?')) {
      try {
        await ConflictoService.eliminar(id);
        toast.success('Conflicto eliminado exitosamente');
        cargarConflictos();
      } catch (error) {
        toast.error('Error al eliminar el conflicto');
        console.error(error);
      }
    }
  };

  return (
    <div className="conflictos-page">
      <h1>Conflictos Vecinales</h1>

      <div className="filtros">
        <select
          value={filtroEstado}
          onChange={(e) => setFiltroEstado(e.target.value)}
          className="filtro-select"
        >
          <option value="todos">Todos los estados</option>
          <option value="prioridad">Ordenar por prioridad</option>
          <option value="1">Nuevo</option>
          <option value="2">En revisión</option>
          <option value="3">En mediación</option>
          <option value="4">Resuelto</option>
        </select>
      </div>

      {loading ? (
        <div className="loading">Cargando conflictos...</div>
      ) : conflictos.length === 0 ? (
        <div className="empty-state">
          <p>No hay conflictos para mostrar</p>
        </div>
      ) : (
        <div className="conflictos-grid">
          {conflictos.map((conflicto) => (
            <ConflictoCard
              key={conflicto.id}
              conflicto={conflicto}
              onEliminar={handleEliminar}
            />
          ))}
        </div>
      )}
    </div>
  );
}

export default ConflictosPage;
