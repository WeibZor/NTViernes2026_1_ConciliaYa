import db from '../database/localDatabase.js';
import api from '../api/apiClient.js';

const USE_BACKEND = true;

async function backendOrFallback(backendFn, fallbackFn) {
  if (!USE_BACKEND) return await fallbackFn();

  try {
    return await backendFn();
  } catch (error) {
    console.warn('Backend API no disponible, usando fallback local:', error.message || error);
    return await fallbackFn();
  }
}

class TipoConflictoRepository {
  async getAll() {
    return backendOrFallback(
      async () => {
        const response = await api.get('/tipoconflictos');
        return response.data;
      },
      async () => {
        await this.simulateDelay();
        return db.getCollection('tiposConflicto');
      }
    );
  }

  async getById(id) {
    return backendOrFallback(
      async () => {
        const response = await api.get('/tipoconflictos/filter', { params: { id } });
        return response.data.find(t => t.id === id) || null;
      },
      async () => {
        await this.simulateDelay();
        const tipos = db.getCollection('tiposConflicto');
        return tipos.find(t => t.id === id) || null;
      }
    );
  }

  async create(data) {
    return backendOrFallback(
      async () => {
        const response = await api.post('/tipoconflictos', data);
        return response.data;
      },
      async () => {
        await this.simulateDelay();
        return db.addToCollection('tiposConflicto', data);
      }
    );
  }

  async update(id, data) {
    return backendOrFallback(
      async () => {
        const response = await api.put(`/tipoconflictos/${id}`, data);
        return response.data;
      },
      async () => {
        await this.simulateDelay();
        return db.updateInCollection('tiposConflicto', id, data);
      }
    );
  }

  async delete(id) {
    return backendOrFallback(
      async () => {
        await api.delete(`/tipoconflictos/${id}`);
        return true;
      },
      async () => {
        await this.simulateDelay();
        return db.removeFromCollection('tiposConflicto', id);
      }
    );
  }

  async search(query) {
    return backendOrFallback(
      async () => {
        const response = await api.get('/tipoconflictos/filter', { params: { search: query } });
        return response.data;
      },
      async () => {
        await this.simulateDelay();
        const tipos = db.getCollection('tiposConflicto');
        const lowerQuery = query.toLowerCase();
        return tipos.filter(t =>
          t.nombre.toLowerCase().includes(lowerQuery) ||
          t.descripcion.toLowerCase().includes(lowerQuery)
        );
      }
    );
  }

  async filter(filters) {
    return backendOrFallback(
      async () => {
        const response = await api.get('/tipoconflictos/filter', { params: filters });
        return response.data;
      },
      async () => {
        await this.simulateDelay();
        let tipos = db.getCollection('tiposConflicto');

        if (filters.activo !== undefined) {
          tipos = tipos.filter(t => t.activo === filters.activo);
        }
        if (filters.search) {
          const lowerSearch = filters.search.toLowerCase();
          tipos = tipos.filter(t =>
            t.nombre.toLowerCase().includes(lowerSearch) ||
            t.descripcion.toLowerCase().includes(lowerSearch)
          );
        }
        return tipos;
      }
    );
  }

  async simulate(numRegistros = 1000) {
    return backendOrFallback(
      async () => {
        const response = await api.post('/tipoconflictos/simulate', { num_registros: numRegistros });
        return response.data.data;
      },
      async () => {
        await this.simulateDelay();
        // Fallback simulation logic if needed
        return [];
      }
    );
  }

  async clean() {
    return backendOrFallback(
      async () => {
        const response = await api.post('/tipoconflictos/clean');
        return response.data.data;
      },
      async () => {
        await this.simulateDelay();
        return db.getCollection('tiposConflicto');
      }
    );
  }

  async getQueries(queryType) {
    return backendOrFallback(
      async () => {
        const response = await api.get(`/tipoconflictos/queries/${queryType}`);
        return response.data;
      },
      async () => {
        await this.simulateDelay();
        return [];
      }
    );
  }

  async getGroupings(groupType) {
    return backendOrFallback(
      async () => {
        const response = await api.get(`/tipoconflictos/groupings/${groupType}`);
        return response.data;
      },
      async () => {
        await this.simulateDelay();
        return [];
      }
    );
  }

  async getSummary() {
    return backendOrFallback(
      async () => {
        const response = await api.get('/tipoconflictos/summary');
        return response.data;
      },
      async () => {
        await this.simulateDelay();
        return { rows: 0, columns: 0, sample: { head: [], tail: [] } };
      }
    );
  }

  async simulateDelay() {
    return new Promise(resolve => setTimeout(resolve, Math.random() * 500 + 200));
  }
}

export default new TipoConflictoRepository();