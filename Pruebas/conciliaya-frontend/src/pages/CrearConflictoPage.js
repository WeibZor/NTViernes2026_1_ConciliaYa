import React, { useState } from 'react';
import { ConflictoService, UsuarioService } from '../services/apiService';
import { toast } from 'react-toastify';
import { useNavigate } from 'react-router-dom';
import '../styles/CrearConflictoPage.css';

/**
 * Página para crear un nuevo conflicto.
 * Incluye validación de campos y clasificación automática.
 */
function CrearConflictoPage() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    titulo: '',
    descripcion: '',
    ubicacion: '',
    usuarioReportanteId: '',
    prioridad: 3
  });

  const [usuarios, setUsuarios] = useState([]);
  const [loading, setLoading] = useState(false);
  const [enviando, setEnviando] = useState(false);

  React.useEffect(() => {
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

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const validarFormulario = () => {
    if (!formData.titulo.trim()) {
      toast.error('El título es obligatorio');
      return false;
    }
    if (formData.titulo.length < 10) {
      toast.error('El título debe tener al menos 10 caracteres');
      return false;
    }
    if (!formData.descripcion.trim()) {
      toast.error('La descripción es obligatoria');
      return false;
    }
    if (formData.descripcion.length < 20) {
      toast.error('La descripción debe tener al menos 20 caracteres');
      return false;
    }
    if (!formData.ubicacion.trim()) {
      toast.error('La ubicación es obligatoria');
      return false;
    }
    if (!formData.usuarioReportanteId) {
      toast.error('Debes seleccionar un usuario reportante');
      return false;
    }
    return true;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!validarFormulario()) {
      return;
    }

    try {
      setEnviando(true);
      await ConflictoService.crear(formData);
      toast.success('¡Conflicto reportado exitosamente!');
      
      // Limpiar formulario
      setFormData({
        titulo: '',
        descripcion: '',
        ubicacion: '',
        usuarioReportanteId: '',
        prioridad: 3
      });

      // Redirigir a conflictos después de 2 segundos
      setTimeout(() => navigate('/conflictos'), 2000);
    } catch (error) {
      if (error.response?.data?.codigo === 'VALIDACION_ERROR') {
        toast.error('Error de validación en los datos');
      } else {
        toast.error('Error al crear el conflicto');
      }
      console.error(error);
    } finally {
      setEnviando(false);
    }
  };

  return (
    <div className="crear-conflicto-page">
      <div className="form-container">
        <h1>Reportar un Conflicto</h1>
        <p className="subtitle">Complete el formulario para reportar un nuevo conflicto vecinal</p>

        <form onSubmit={handleSubmit} className="conflicto-form">
          <div className="form-group">
            <label htmlFor="titulo">Título *</label>
            <input
              type="text"
              id="titulo"
              name="titulo"
              value={formData.titulo}
              onChange={handleChange}
              placeholder="Ej: Ruido nocturno consistente"
              maxLength="200"
              disabled={enviando}
            />
            <small>Mínimo 10 caracteres</small>
          </div>

          <div className="form-group">
            <label htmlFor="descripcion">Descripción *</label>
            <textarea
              id="descripcion"
              name="descripcion"
              value={formData.descripcion}
              onChange={handleChange}
              placeholder="Describe detalladamente el conflicto..."
              rows="6"
              maxLength="2000"
              disabled={enviando}
            />
            <small>Mínimo 20 caracteres, máximo 2000</small>
          </div>

          <div className="form-group">
            <label htmlFor="ubicacion">Ubicación *</label>
            <input
              type="text"
              id="ubicacion"
              name="ubicacion"
              value={formData.ubicacion}
              onChange={handleChange}
              placeholder="Ej: Calle Principal 123, Apto 5B"
              disabled={enviando}
            />
          </div>

          <div className="form-group">
            <label htmlFor="usuarioReportanteId">Usuario Reportante *</label>
            <select
              id="usuarioReportanteId"
              name="usuarioReportanteId"
              value={formData.usuarioReportanteId}
              onChange={handleChange}
              disabled={enviando || loading}
            >
              <option value="">Selecciona un usuario</option>
              {usuarios.map(usuario => (
                <option key={usuario.id} value={usuario.id}>
                  {usuario.nombreCompleto} ({usuario.email})
                </option>
              ))}
            </select>
          </div>

          <div className="form-group">
            <label htmlFor="prioridad">Prioridad</label>
            <select
              id="prioridad"
              name="prioridad"
              value={formData.prioridad}
              onChange={handleChange}
              disabled={enviando}
            >
              <option value="1">Baja</option>
              <option value="2">Baja-Media</option>
              <option value="3">Media</option>
              <option value="4">Alta-Media</option>
              <option value="5">Alta</option>
            </select>
            <small>La prioridad ayuda a determinar el orden de atención</small>
          </div>

          <div className="form-actions">
            <button
              type="submit"
              className="btn btn-primary"
              disabled={enviando || loading}
            >
              {enviando ? 'Reportando...' : 'Reportar Conflicto'}
            </button>
            <button
              type="button"
              className="btn btn-secondary"
              onClick={() => navigate('/')}
              disabled={enviando}
            >
              Cancelar
            </button>
          </div>

          <div className="form-note">
            <p>
              <strong>Nota:</strong> El sistema clasificará automáticamente tu conflicto
              basándose en la descripción que proporcionas. Sé lo más detallado posible
              para una mejor clasificación.
            </p>
          </div>
        </form>
      </div>
    </div>
  );
}

export default CrearConflictoPage;
