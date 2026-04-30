import { createContext, useContext, useEffect, useState } from 'react';
import { getUserFromStorage, saveSession, removeSession } from '../services/storageService.js';
import { findUserByDocument } from '../services/userService.js';

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(getUserFromStorage());
  const [error, setError] = useState('');

  useEffect(() => {
    if (user) {
      saveSession(user);
    }
  }, [user]);

  const login = ({ tipoDocumento, documento }) => {
    const found = findUserByDocument(tipoDocumento, documento);
    if (!found) {
      setError('Tipo o número de documento no encontrados. Verifique sus datos.');
      return false;
    }
    setUser(found);
    setError('');
    return true;
  };

  const logout = () => {
    setUser(null);
    removeSession();
  };

  const register = (userData) => {
    setUser(userData);
    saveSession(userData);
  };

  return (
    <AuthContext.Provider value={{ user, error, login, logout, register, setError }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}
