import api from './apiClient.js';

class MediacionesApi {
  async getAll(params = {}) {
    const response = await api.get('/mediaciones', { params });
    return response.data;
  }
  async getById(id) {
    const response = await api.get(`/mediaciones/${id}`);
    return response.data;
  }
  async create(data) {
    const response = await api.post('/mediaciones', data);
    return { data: response.data, status: 201 };
  }
  async update(id, data) {
    const response = await api.put(`/mediaciones/${id}`, data);
    return { data: response.data };
  }
  async delete(id) {
    await api.delete(`/mediaciones/${id}`);
    return { data: { message: 'Mediación eliminada' } };
  }
}
export default new MediacionesApi();
