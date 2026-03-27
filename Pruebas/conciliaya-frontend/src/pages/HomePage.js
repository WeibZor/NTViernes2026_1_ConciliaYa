import React, { useState, useEffect } from 'react';
import { ConflictoService, UsuarioService } from '../services/apiService';
import '../styles/HomePage.css';

/**
 * Página principal de ConciliaYa.
 * Muestra un resumen de conflictos y usuarios.
 */
function HomePage() {
  const [stats, setStats] = useState({
    totalConflictos: 0,
    totalUsuarios: 0,
    conflictosActivos: 0,
    conflictosResueltos: 0
  });

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    cargarEstadisticas();
  }, []);

  const cargarEstadisticas = async () => {
    try {
      setLoading(true);

      // Obtener conflictos
      const conflictosResponse = await ConflictoService.obtenerTodos();
      const conflictos = conflictosResponse.datos || [];

      // Obtener usuarios
      const usuariosResponse = await UsuarioService.obtenerTodos();
      const usuarios = usuariosResponse.datos || [];

      // Calcular estadísticas
      const conflictosActivos = conflictos.filter(
        c => c.estadoConflicto?.nombre !== 'Resuelto'
      ).length;

      const conflictosResueltos = conflictos.filter(
        c => c.estadoConflicto?.nombre === 'Resuelto'
      ).length;

      setStats({
        totalConflictos: conflictos.length,
        totalUsuarios: usuarios.length,
        conflictosActivos,
        conflictosResueltos
      });
    } catch (error) {
      console.error('Error cargando estadísticas:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="home-page">
      <header className="home-header">
        <h1>¡Bienvenido a ConciliaYa!</h1>
        <p className="subtitle">
          Sistema de Gestión de Conflictos Vecinales
        </p>
      </header>

      {loading ? (
        <div className="loading">Cargando...</div>
      ) : (
        <div className="stats-container">
          <div className="stat-card">
            <div className="stat-icon conflictos">📋</div>
            <div className="stat-content">
              <h3>Total de Conflictos</h3>
              <p className="stat-number">{stats.totalConflictos}</p>
            </div>
          </div>

          <div className="stat-card">
            <div className="stat-icon usuarios">👥</div>
            <div className="stat-content">
              <h3>Usuarios Registrados</h3>
              <p className="stat-number">{stats.totalUsuarios}</p>
            </div>
          </div>

          <div className="stat-card">
            <div className="stat-icon activos">⏱️</div>
            <div className="stat-content">
              <h3>Conflictos Activos</h3>
              <p className="stat-number">{stats.conflictosActivos}</p>
            </div>
          </div>

          <div className="stat-card">
            <div className="stat-icon resueltos">✅</div>
            <div className="stat-content">
              <h3>Conflictos Resueltos</h3>
              <p className="stat-number">{stats.conflictosResueltos}</p>
            </div>
          </div>
        </div>
      )}

      <section className="features">
        <h2>Características Principales</h2>
        <div className="features-grid">
          <div className="feature">
            <h4>📝 Reportar Conflictos</h4>
            <p>Reporta conflictos vecinales de manera rápida y sencilla. La clasificación se realiza automáticamente.</p>
          </div>
          <div className="feature">
            <h4>🤝 Mediación</h4>
            <p>Asigna mediadores profesionales para resolver conflictos de forma amigable.</p>
          </div>
          <div className="feature">
            <h4>📊 Seguimiento</h4>
            <p>Realiza seguimiento del estado de tus conflictos en tiempo real.</p>
          </div>
          <div className="feature">
            <h4>⚡ Clasificación Automática</h4>
            <p>Sistema inteligente que clasifica automáticamente los conflictos en categorías.</p>
          </div>
        </div>
      </section>
    </div>
  );
}

export default HomePage;
