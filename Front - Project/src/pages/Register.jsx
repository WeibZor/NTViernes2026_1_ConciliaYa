import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext.jsx';
import { registerUser, findUserByDocument } from '../services/userService.js';

export default function Register() {
  const [form, setForm] = useState({ nombres: '', tipoDocumento: 'CC', documento: '', edad: '' });
  const [error, setError] = useState('');
  const { register } = useAuth();
  const navigate = useNavigate();

  const handleChange = (event) => {
    const { name, value } = event.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if (!form.nombres.trim() || !form.documento.trim() || !form.edad.trim()) {
      setError('Todos los campos son obligatorios.');
      return;
    }
    if (findUserByDocument(form.documento.trim())) {
      setError('Ya existe un usuario con ese documento.');
      return;
    }
    const newUser = registerUser({
      nombres: form.nombres.trim(),
      tipoDocumento: form.tipoDocumento,
      documento: form.documento.trim(),
      edad: Number(form.edad)
    });
    register(newUser);
    navigate('/dashboard');
  };

  return (
    <div className="page-center">
      <form className="form-card" onSubmit={handleSubmit}>
        <h2>Registro de usuario</h2>
        {error && <p className="error-text">{error}</p>}
        <label>
          Nombres completos
          <input name="nombres" value={form.nombres} onChange={handleChange} placeholder="Ingresa tus nombres" />
        </label>
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
          <input name="documento" value={form.documento} onChange={handleChange} placeholder="Número de documento" />
        </label>
        <label>
          Edad
          <input type="number" name="edad" value={form.edad} onChange={handleChange} placeholder="Edad" />
        </label>
        <button type="submit">Crear perfil</button>
      </form>
    </div>
  );
}
