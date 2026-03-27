import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

// Páginas
import HomePage from './pages/HomePage';
import ConflictosPage from './pages/ConflictosPage';
import UsuariosPage from './pages/UsuariosPage';
import CrearConflictoPage from './pages/CrearConflictoPage';

// Estilos
import './styles/App.css';

/**
 * Componente principal de la aplicación.
 * Configura el enrutamiento y la estructura general.
 */
function App() {
  return (
    <Router>
      <div className="app">
        {/* Navegación */}
        <nav className="navbar">
          <div className="navbar-container">
            <Link to="/" className="navbar-logo">
              ConciliaYa
            </Link>
            <ul className="nav-menu">
              <li className="nav-item">
                <Link to="/" className="nav-links">
                  Inicio
                </Link>
              </li>
              <li className="nav-item">
                <Link to="/conflictos" className="nav-links">
                  Conflictos
                </Link>
              </li>
              <li className="nav-item">
                <Link to="/usuarios" className="nav-links">
                  Usuarios
                </Link>
              </li>
              <li className="nav-item">
                <Link to="/crear-conflicto" className="nav-links nav-links-btn">
                  Reportar Conflicto
                </Link>
              </li>
            </ul>
          </div>
        </nav>

        {/* Contenido principal */}
        <main className="main-content">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/conflictos" element={<ConflictosPage />} />
            <Route path="/crear-conflicto" element={<CrearConflictoPage />} />
            <Route path="/usuarios" element={<UsuariosPage />} />
          </Routes>
        </main>

        {/* Notificaciones */}
        <ToastContainer
          position="bottom-right"
          autoClose={5000}
          hideProgressBar={false}
          newestOnTop
          closeOnClick
          rtl={false}
          pauseOnFocusLoss
          draggable
          pauseOnHover
          theme="light"
        />
      </div>
    </Router>
  );
}

export default App;
