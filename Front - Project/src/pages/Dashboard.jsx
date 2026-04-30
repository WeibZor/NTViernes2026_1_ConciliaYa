import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext.jsx';

export default function Dashboard() {
  const { user } = useAuth();

  return (
    <div className="page-center">
      <section className="card-card">
        <h2>Panel de usuario</h2>
        <p>Bienvenido, <strong>{user.nombres}</strong>.</p>
        <ul className="info-list">
          <li>Documento: {user.documento}</li>
          <li>Tipo: {user.tipoDocumento}</li>
          <li>Edad: {user.edad}</li>
          <li>Rol: {user.rol}</li>
        </ul>
        <Link to="/expenses" className="primary-button">Ver mis gastos</Link>
      </section>
    </div>
  );
}
