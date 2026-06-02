import api from './apiClient.js';

class UsuariosApi {
  async getAll(params = {}) {
    const response = await api.get('/usuarios', { params });
    return response.data;
  }
  async getById(id) {
    const response = await api.get(`/usuarios/${id}`);
    return response.data;
  }
  async create(data) {
    const response = await api.post('/usuarios', data);
    return { data: response.data, status: 201 };
  }
  async update(id, data) {
    const response = await api.put(`/usuarios/${id}`, data);
    return { data: response.data };
  }
  async delete(id) {
    await api.delete(`/usuarios/${id}`);
    return { data: { message: 'Usuario eliminado' } };
  }
}
export default new UsuariosApi();
