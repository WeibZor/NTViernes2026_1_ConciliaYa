import api from './apiClient.js';

class ConflictosApi {
  async getAll(params = {}) {
    const response = await api.get('/conflictos', { params });
    return response.data;
  }
  async getById(id) {
    const response = await api.get(`/conflictos/${id}`);
    return response.data;
  }
  async create(data) {
    const response = await api.post('/conflictos', data);
    return { data: response.data, status: 201 };
  }
  async update(id, data) {
    const response = await api.put(`/conflictos/${id}`, data);
    return { data: response.data };
  }
  async delete(id) {
    await api.delete(`/conflictos/${id}`);
    return { data: { message: 'Conflicto eliminado' } };
  }
}
export default new ConflictosApi();
