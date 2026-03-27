import axios from 'axios';

/**
 * Servicio API para comunicación con el backend.
 * Centraliza todas las llamadas HTTP a la API REST.
 */

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8080/api';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json'
  }
});

/**
 * Interceptor para manejar errores de forma global
 */
apiClient.interceptors.response.use(
  response => response,
  error => {
    console.error('Error en API:', error.response?.data || error.message);
    return Promise.reject(error);
  }
);

/**
 * ==================== CONFLICTOS ====================
 */

export const ConflictoService = {
  /**
   * Obtiene todos los conflictos
   */
  obtenerTodos: async () => {
    try {
      const response = await apiClient.get('/conflictos');
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  /**
   * Obtiene un conflicto por ID
   */
  obtenerPorId: async (id) => {
    try {
      const response = await apiClient.get(`/conflictos/${id}`);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  /**
   * Crea un nuevo conflicto
   */
  crear: async (conflictoData) => {
    try {
      const response = await apiClient.post('/conflictos', conflictoData);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  /**
   * Actualiza un conflicto existente
   */
  actualizar: async (id, conflictoData) => {
    try {
      const response = await apiClient.put(`/conflictos/${id}`, conflictoData);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  /**
   * Elimina un conflicto
   */
  eliminar: async (id) => {
    try {
      const response = await apiClient.delete(`/conflictos/${id}`);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  /**
   * Obtiene conflictos filtrados por estado
   */
  obtenerPorEstado: async (estadoId) => {
    try {
      const response = await apiClient.get(`/conflictos/por-estado/${estadoId}`);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  /**
   * Obtiene conflictos ordenados por prioridad
   */
  obtenerPorPrioridad: async () => {
    try {
      const response = await apiClient.get('/conflictos/por-prioridad');
      return response.data;
    } catch (error) {
      throw error;
    }
  }
};

/**
 * ==================== USUARIOS ====================
 */

export const UsuarioService = {
  /**
   * Obtiene todos los usuarios
   */
  obtenerTodos: async () => {
    try {
      const response = await apiClient.get('/usuarios');
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  /**
   * Obtiene un usuario por ID
   */
  obtenerPorId: async (id) => {
    try {
      const response = await apiClient.get(`/usuarios/${id}`);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  /**
   * Crea un nuevo usuario
   */
  crear: async (usuarioData) => {
    try {
      const response = await apiClient.post('/usuarios', usuarioData);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  /**
   * Actualiza un usuario
   */
  actualizar: async (id, usuarioData) => {
    try {
      const response = await apiClient.put(`/usuarios/${id}`, usuarioData);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  /**
   * Elimina un usuario
   */
  eliminar: async (id) => {
    try {
      const response = await apiClient.delete(`/usuarios/${id}`);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  /**
   * Busca usuario por email
   */
  obtenerPorEmail: async (email) => {
    try {
      const response = await apiClient.get(`/usuarios/email/${email}`);
      return response.data;
    } catch (error) {
      throw error;
    }
  }
};

/**
 * ==================== MEDIACIONES ====================
 */

export const MediacionService = {
  /**
   * Obtiene todas las mediaciones
   */
  obtenerTodas: async () => {
    try {
      const response = await apiClient.get('/mediaciones');
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  /**
   * Crea una nueva mediación
   */
  crear: async (mediacionData) => {
    try {
      const response = await apiClient.post('/mediaciones', mediacionData);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  /**
   * Finaliza una mediación
   */
  finalizar: async (id, resultadoData) => {
    try {
      const response = await apiClient.put(`/mediaciones/${id}/finalizar`, resultadoData);
      return response.data;
    } catch (error) {
      throw error;
    }
  }
};

export default apiClient;
