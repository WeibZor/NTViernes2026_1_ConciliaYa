import React, { useEffect, useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { FileText, Search, Plus, CircleDot, X, BarChart3, RefreshCw, Zap, Trash2, Edit3 } from 'lucide-react';
import tipoConflictoRepository from '../repositories/tipoConflictoRepository.js';
import Pagination from '../components/Pagination.jsx';
import useRoleAccess from '../hooks/useRoleAccess.js';

const TipoConflicto = () => {
  const [tiposConflicto, setTiposConflicto] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [loading, setLoading] = useState(true);
  const [currentPage, setCurrentPage] = useState(1);
  const [showModal, setShowModal] = useState(false);
  const [creating, setCreating] = useState(false);
  const [numRegistros, setNumRegistros] = useState(1000);
  const [newTipo, setNewTipo] = useState({ nombre: '', descripcion: '', activo: true });
  const [summary, setSummary] = useState(null);
  const [queries, setQueries] = useState({ activos: [], laborales: [], ultimos: [] });
  const [groupings, setGroupings] = useState({ porActivo: [], porNombre: [] });
  const [editingTipo, setEditingTipo] = useState(null);
  const { user, permissions } = useRoleAccess();
  const ITEMS_PER_PAGE = 6;

  const loadTiposConflicto = async (query = '') => {
    setLoading(true);
    const data = query ? await tipoConflictoRepository.search(query) : await tipoConflictoRepository.getAll();
    setTiposConflicto(data || []);
    setCurrentPage(1);
    setLoading(false);
  };

  const loadSummary = async () => {
    const data = await tipoConflictoRepository.getSummary();
    setSummary(data);
  };

  const loadQueries = async () => {
    const activos = await tipoConflictoRepository.getQueries('activos');
    const laborales = await tipoConflictoRepository.getQueries('laborales');
    const ultimos = await tipoConflictoRepository.getQueries('ultimos_180_dias');
    setQueries({ activos, laborales, ultimos });
  };

  const loadGroupings = async () => {
    const porActivo = await tipoConflictoRepository.getGroupings('por_activo');
    const porNombre = await tipoConflictoRepository.getGroupings('por_nombre');
    setGroupings({ porActivo, porNombre });
  };

  const refreshAll = async (query = '') => {
    setLoading(true);
    await loadTiposConflicto(query);
    await loadSummary();
    await loadQueries();
    await loadGroupings();
    setLoading(false);
  };

  useEffect(() => {
    if (user) {
      refreshAll(searchQuery);
    }
  }, [user, searchQuery]);

  const handleSimulate = async () => {
    setLoading(true);
    await tipoConflictoRepository.simulate(numRegistros);
    await refreshAll();
  };

  const handleClean = async () => {
    setLoading(true);
    await tipoConflictoRepository.clean();
    await refreshAll();
  };

  const handleCreateTipo = async (e) => {
    e.preventDefault();
    if (!newTipo.nombre || !newTipo.descripcion) return;

    setCreating(true);
    try {
      await tipoConflictoRepository.create({
        ...newTipo,
        fechaAlta: new Date().toISOString(),
      });
      setNewTipo({ nombre: '', descripcion: '', activo: true });
      setShowModal(false);
      await refreshAll();
    } catch (error) {
      console.error('Error creando tipo:', error);
    } finally {
      setCreating(false);
    }
  };

  const handleDeleteTipo = async (id) => {
    const confirmDelete = window.confirm('¿Eliminar este tipo de conflicto?');
    if (!confirmDelete) return;
    setLoading(true);
    await tipoConflictoRepository.delete(id);
    await refreshAll();
  };

  const handleToggleActivo = async (tipo) => {
    const updated = { ...tipo, activo: !tipo.activo };
    setLoading(true);
    await tipoConflictoRepository.update(tipo.id, updated);
    await refreshAll();
  };

  const handleEditTipo = (tipo) => {
    setEditingTipo(tipo);
    setNewTipo({ nombre: tipo.nombre, descripcion: tipo.descripcion, activo: tipo.activo });
    setShowModal(true);
  };

  const handleUpdateTipo = async (e) => {
    e.preventDefault();
    if (!editingTipo) return;
    setCreating(true);
    try {
      await tipoConflictoRepository.update(editingTipo.id, {
        ...newTipo,
        fechaAlta: editingTipo.fechaAlta,
      });
      setEditingTipo(null);
      setNewTipo({ nombre: '', descripcion: '', activo: true });
      setShowModal(false);
      await refreshAll();
    } catch (error) {
      console.error('Error actualizando tipo:', error);
    } finally {
      setCreating(false);
    }
  };

  const paginatedTipos = tiposConflicto.slice(
    (currentPage - 1) * ITEMS_PER_PAGE,
    currentPage * ITEMS_PER_PAGE
  );

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-6">
      <div className="max-w-7xl mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="mb-8"
        >
          <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4 mb-6">
            <div className="flex items-center space-x-3">
              <FileText className="w-8 h-8 text-indigo-600" />
              <div>
                <h1 className="text-3xl font-bold text-gray-900">Tipos de Conflicto</h1>
                <p className="text-sm text-gray-500">Gestiona, crea, limpia y consulta los datos directamente desde la UI.</p>
              </div>
            </div>
            <div className="flex flex-wrap gap-3">
              <button
                onClick={handleSimulate}
                className="flex items-center gap-2 bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded-lg transition"
              >
                <Zap className="w-4 h-4" />
                Simular
              </button>
              <button
                onClick={handleClean}
                className="flex items-center gap-2 bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg transition"
              >
                <RefreshCw className="w-4 h-4" />
                Limpiar
              </button>
              <button
                onClick={() => { setShowModal(true); setEditingTipo(null); setNewTipo({ nombre: '', descripcion: '', activo: true }); }}
                className="flex items-center gap-2 bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-lg transition"
              >
                <Plus className="w-4 h-4" />
                Crear Tipo
              </button>
            </div>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-3 gap-4 mb-6">
            <div className="bg-white rounded-xl shadow-sm p-5">
              <p className="text-sm font-medium text-gray-500">Registros simulados</p>
              <input
                type="number"
                value={numRegistros}
                onChange={(e) => setNumRegistros(Math.max(1, parseInt(e.target.value) || 1))}
                className="mt-3 w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-indigo-500 focus:border-indigo-500"
                min="1"
                max="10000"
              />
            </div>
            <div className="bg-white rounded-xl shadow-sm p-5">
              <p className="text-sm font-medium text-gray-500">Buscar</p>
              <div className="relative mt-3">
                <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 w-5 h-5" />
                <input
                  type="text"
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  placeholder="Buscar por nombre o descripción"
                  className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-indigo-500 focus:border-indigo-500"
                />
              </div>
            </div>
            <div className="bg-white rounded-xl shadow-sm p-5">
              <p className="text-sm font-medium text-gray-500">Acciones</p>
              <div className="mt-3 flex flex-col gap-2">
                <button
                  onClick={refreshAll}
                  className="w-full text-left px-4 py-2 border border-gray-200 rounded-lg hover:bg-gray-50"
                >Recargar datos</button>
                <button
                  onClick={() => setSearchQuery('')}
                  className="w-full text-left px-4 py-2 border border-gray-200 rounded-lg hover:bg-gray-50"
                >Limpiar búsqueda</button>
              </div>
            </div>
          </div>
        </motion.div>

        {summary && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8"
          >
            <div className="bg-white rounded-xl shadow-md p-6">
              <p className="text-sm font-medium text-gray-500">Total Registros</p>
              <p className="mt-2 text-3xl font-bold text-gray-900">{summary.rows}</p>
            </div>
            <div className="bg-white rounded-xl shadow-md p-6">
              <p className="text-sm font-medium text-gray-500">Total Columnas</p>
              <p className="mt-2 text-3xl font-bold text-gray-900">{summary.columns}</p>
            </div>
            <div className="bg-white rounded-xl shadow-md p-6">
              <p className="text-sm font-medium text-gray-500">Activos encontrados</p>
              <p className="mt-2 text-3xl font-bold text-gray-900">{queries.activos?.length ?? 0}</p>
            </div>
          </motion.div>
        )}

        <AnimatePresence>
          {loading ? (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="flex justify-center items-center h-64"
            >
              <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600"></div>
            </motion.div>
          ) : (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6 mb-8"
            >
              {paginatedTipos.map((tipo) => (
                <motion.div
                  key={tipo.id}
                  initial={{ opacity: 0, scale: 0.97 }}
                  animate={{ opacity: 1, scale: 1 }}
                  className="bg-white rounded-3xl shadow-sm p-6 border border-gray-200"
                >
                  <div className="flex items-start justify-between gap-3 mb-4">
                    <div>
                      <h3 className="text-xl font-semibold text-gray-900">{tipo.nombre}</h3>
                      <p className="text-xs uppercase tracking-[0.2em] text-gray-400">ID {tipo.id}</p>
                    </div>
                    <span className={`rounded-full px-3 py-1 text-xs font-semibold ${tipo.activo ? 'bg-emerald-100 text-emerald-800' : 'bg-rose-100 text-rose-800'}`}>
                      {tipo.activo ? 'Activo' : 'Inactivo'}
                    </span>
                  </div>
                  <p className="text-gray-600 mb-4">{tipo.descripcion}</p>
                  <p className="text-sm text-gray-500 mb-4">Creado: {new Date(tipo.fechaAlta).toLocaleString()}</p>
                  <div className="flex flex-wrap gap-2">
                    <button
                      onClick={() => handleEditTipo(tipo)}
                      className="inline-flex items-center gap-2 px-3 py-2 text-sm font-medium rounded-full bg-yellow-50 text-yellow-800 hover:bg-yellow-100"
                    >
                      <Edit3 className="w-4 h-4" />
                      Editar
                    </button>
                    <button
                      onClick={() => handleToggleActivo(tipo)}
                      className="inline-flex items-center gap-2 px-3 py-2 text-sm font-medium rounded-full bg-indigo-50 text-indigo-700 hover:bg-indigo-100"
                    >
                      <CircleDot className="w-4 h-4" />
                      {tipo.activo ? 'Desactivar' : 'Activar'}
                    </button>
                    <button
                      onClick={() => handleDeleteTipo(tipo.id)}
                      className="inline-flex items-center gap-2 px-3 py-2 text-sm font-medium rounded-full bg-rose-50 text-rose-700 hover:bg-rose-100"
                    >
                      <Trash2 className="w-4 h-4" />
                      Eliminar
                    </button>
                  </div>
                </motion.div>
              ))}
            </motion.div>
          )}
        </AnimatePresence>

        {!loading && tiposConflicto.length > ITEMS_PER_PAGE && (
          <Pagination
            currentPage={currentPage}
            totalPages={Math.ceil(tiposConflicto.length / ITEMS_PER_PAGE)}
            onPageChange={setCurrentPage}
          />
        )}

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
          <div className="bg-white rounded-xl shadow-md p-6">
            <h2 className="text-lg font-semibold text-gray-900 mb-4">Consultas de ejemplo</h2>
            <div className="space-y-4">
              <div>
                <p className="text-sm font-medium text-gray-500">Activos</p>
                <pre className="mt-2 p-4 bg-gray-50 rounded-lg text-xs text-gray-700 overflow-auto h-48">{JSON.stringify(queries.activos || [], null, 2)}</pre>
              </div>
              <div>
                <p className="text-sm font-medium text-gray-500">Laborales</p>
                <pre className="mt-2 p-4 bg-gray-50 rounded-lg text-xs text-gray-700 overflow-auto h-48">{JSON.stringify(queries.laborales || [], null, 2)}</pre>
              </div>
            </div>
          </div>
          <div className="bg-white rounded-xl shadow-md p-6">
            <h2 className="text-lg font-semibold text-gray-900 mb-4">Agrupaciones de ejemplo</h2>
            <div className="space-y-4">
              <div>
                <p className="text-sm font-medium text-gray-500">Por activo</p>
                <pre className="mt-2 p-4 bg-gray-50 rounded-lg text-xs text-gray-700 overflow-auto h-48">{JSON.stringify(groupings.porActivo || [], null, 2)}</pre>
              </div>
              <div>
                <p className="text-sm font-medium text-gray-500">Por nombre</p>
                <pre className="mt-2 p-4 bg-gray-50 rounded-lg text-xs text-gray-700 overflow-auto h-48">{JSON.stringify(groupings.porNombre || [], null, 2)}</pre>
              </div>
            </div>
          </div>
        </div>

        <AnimatePresence>
          {showModal && (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="fixed inset-0 bg-black bg-opacity-40 flex items-center justify-center z-50 p-4"
            >
              <motion.div
                initial={{ scale: 0.95, opacity: 0 }}
                animate={{ scale: 1, opacity: 1 }}
                exit={{ scale: 0.95, opacity: 0 }}
                className="w-full max-w-xl bg-white rounded-3xl shadow-2xl p-6"
              >
                <div className="flex items-center justify-between mb-6">
                  <div>
                    <h2 className="text-xl font-semibold text-gray-900">{editingTipo ? 'Editar tipo de conflicto' : 'Crear tipo de conflicto'}</h2>
                    <p className="text-sm text-gray-500">Guarda cambios directamente en la base de datos simulada del backend.</p>
                  </div>
                  <button onClick={() => { setShowModal(false); setEditingTipo(null); }} className="text-gray-500 hover:text-gray-700">
                    <X className="w-6 h-6" />
                  </button>
                </div>
                <form onSubmit={editingTipo ? handleUpdateTipo : handleCreateTipo} className="space-y-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">Nombre</label>
                    <input
                      value={newTipo.nombre}
                      onChange={(e) => setNewTipo({ ...newTipo, nombre: e.target.value })}
                      className="w-full rounded-2xl border border-gray-200 px-4 py-3 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                      placeholder="Ej: Laboral"
                      required
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">Descripción</label>
                    <textarea
                      value={newTipo.descripcion}
                      onChange={(e) => setNewTipo({ ...newTipo, descripcion: e.target.value })}
                      rows="4"
                      className="w-full rounded-2xl border border-gray-200 px-4 py-3 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                      placeholder="Descripción del tipo de conflicto"
                      required
                    />
                  </div>
                  <div className="flex items-center gap-3">
                    <input
                      id="activo-tipo"
                      type="checkbox"
                      checked={newTipo.activo}
                      onChange={(e) => setNewTipo({ ...newTipo, activo: e.target.checked })}
                      className="h-4 w-4 text-indigo-600 border-gray-300 rounded"
                    />
                    <label htmlFor="activo-tipo" className="text-sm text-gray-700">Activo</label>
                  </div>
                  <div className="flex justify-end gap-3 pt-4">
                    <button
                      type="button"
                      onClick={() => { setShowModal(false); setEditingTipo(null); }}
                      className="px-4 py-2 rounded-2xl border border-gray-200 text-gray-700 hover:bg-gray-50"
                    >Cancelar</button>
                    <button
                      type="submit"
                      disabled={creating}
                      className="px-4 py-2 rounded-2xl bg-indigo-600 text-white hover:bg-indigo-700 disabled:opacity-50"
                    >{creating ? 'Guardando...' : editingTipo ? 'Actualizar' : 'Crear'}</button>
                  </div>
                </form>
              </motion.div>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </div>
  );
};

export default TipoConflicto;
