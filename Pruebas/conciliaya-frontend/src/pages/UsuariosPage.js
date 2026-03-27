import React, { useState, useEffect } from 'react';
import { UsuarioService } from '../services/apiService';
import { toast } from 'react-toastify';
import UsuarioCard from '../components/UsuarioCard';
import '../styles/UsuariosPage.css';

/**
 * Página que lista todos los usuarios.
 */
function UsuariosPage() {
  const [usuarios, setUsuarios] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    cargarUsuarios();
  }, []);

  const cargarUsuarios = async () => {
    try {
      setLoading(true);
      const response = await UsuarioService.obtenerTodos();
      setUsuarios(response.datos || []);
    } catch (error) {
      toast.error('Error al cargar usuarios');
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  const handleEliminar = async (id) => {
    if (window.confirm('¿Estás seguro de eliminar este usuario?')) {
      try {
        await UsuarioService.eliminar(id);
        toast.success('Usuario eliminado');
        cargarUsuarios();
      } catch (error) {
        toast.error('Error al eliminar usuario');
      }
    }
  };

  return (
    <div className="usuarios-page">
      <h1>Usuarios</h1>

      {loading ? (
        <div className="loading">Cargando usuarios...</div>
      ) : usuarios.length === 0 ? (
        <div className="empty-state">
          <p>No hay usuarios registrados</p>
        </div>
      ) : (
        <div className="usuarios-grid">
          {usuarios.map(usuario => (
            <UsuarioCard
              key={usuario.id}
              usuario={usuario}
              onEliminar={handleEliminar}
            />
          ))}
        </div>
      )}
    </div>
  );
}

export default UsuariosPage;
