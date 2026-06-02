import api from './apiClient.js';

class PerfilesApi {
  async getAll() {
    const response = await api.get('/perfiles');
    return response.data;
  }
  async getById(id) {
    const response = await api.get(`/perfiles/${id}`);
    return response.data;
  }
  async create(data) {
    const response = await api.post('/perfiles', data);
    return { data: response.data, status: 201 };
  }
  async update(id, data) {
    const response = await api.put(`/perfiles/${id}`, data);
    return { data: response.data };
  }
  async delete(id) {
    await api.delete(`/perfiles/${id}`);
    return { data: { message: 'Perfil eliminado' } };
  }
}
export default new PerfilesApi();
