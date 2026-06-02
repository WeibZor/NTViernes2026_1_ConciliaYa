import api from './apiClient.js';

// authApi conectado al backend Spring Boot real (sin JWT)
class AuthApi {

  async login(credentials) {
    // credentials: { email, password }
    const response = await api.post('/auth/login', {
      correo: credentials.email,
      password: credentials.password,
    });
    // Guardar sesión en localStorage (sin token JWT)
    const userSession = {
      id: response.data.id,
      nombre: response.data.nombre,
      correo: response.data.correo,
      perfilId: response.data.perfilId,
    };
    localStorage.setItem('userSession', JSON.stringify(userSession));
    return { data: { user: userSession } };
  }

  async register(userData) {
    const response = await api.post('/auth/register', {
      nombre: userData.nombre,
      apellido: userData.apellido,
      correo: userData.email || userData.correo,
      password: userData.password,
    });
    return { data: response.data };
  }

  async logout() {
    localStorage.removeItem('userSession');
    return { data: { message: 'Logout exitoso' } };
  }

  async getCurrentUser() {
    const userSession = localStorage.getItem('userSession');
    if (!userSession) {
      throw { response: { status: 401, data: { message: 'No autenticado' } } };
    }
    return { data: JSON.parse(userSession) };
  }
}

export default new AuthApi();
