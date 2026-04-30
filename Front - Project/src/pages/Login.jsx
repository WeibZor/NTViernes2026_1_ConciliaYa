import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext.jsx';

export default function Login() {
  const [form, setForm] = useState({ tipoDocumento: 'CC', documento: '' });
  const { login, error, setError } = useAuth();
  const navigate = useNavigate();

  const handleChange = (event) => {
    const { name, value } = event.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if (!form.documento.trim() || !form.tipoDocumento.trim()) {
      setError('Debe seleccionar el tipo de documento e ingresar el número.');
      return;
    }
    const ok = login({ tipoDocumento: form.tipoDocumento, documento: form.documento.trim() });
    if (ok) {
      navigate('/dashboard');
    }
  };

  return (
    <div className="page-center">
      <form className="form-card" onSubmit={handleSubmit}>
        <h2>Inicio de sesión</h2>
        {error && <p className="error-text">{error}</p>}
        <label>
          Tipo de documento
          <select name="tipoDocumento" value={form.tipoDocumento} onChange={handleChange}>
            <option value="CC">CC</option>
            <option value="TI">TI</option>
            <option value="PASAPORTE">Pasaporte</option>
            <option value="CE">CE</option>
            <option value="NIT">NIT</option>
          </select>
        </label>
        <label>
          Documento
          <input
            type="text"
            name="documento"
            value={form.documento}
            onChange={handleChange}
            placeholder="Número de documento"
          />
        </label>
        <button type="submit">Entrar</button>
      </form>
    </div>
  );
}
