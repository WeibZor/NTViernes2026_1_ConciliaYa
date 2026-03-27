# ConciliaYa Frontend - React

Frontend para la aplicación de gestión de conflictos vecinales ConciliaYa.

## 🚀 Características

- Interfaz moderna y responsiva
- Gestión de conflictos (CRUD)
- Gestión de usuarios
- Reportar nuevos conflictos
- Clasificación automática
- Sistema de notificaciones (toast)
- Navegación intuitiva con React Router

## 📋 Requisitos

- Node.js 14+
- npm (incluido con Node.js)

## 🔧 Instalación

1. **Instalar dependencias**

```bash
npm install
```

2. **Configurar variables de entorno**

Crear archivo `.env`:

```bash
cp .env.example .env
```

Editar `.env`:

```
REACT_APP_API_URL=http://localhost:8080/api
```

## 🏃 Ejecución

### Modo desarrollo

```bash
npm start
```

La aplicación se abrirá en `http://localhost:3000`

### Compilar para producción

```bash
npm run build
```

## 📁 Estructura del Proyecto

```
src/
├── components/           # Componentes reutilizables
│   ├── ConflictoCard.js
│   └── UsuarioCard.js
├── pages/               # Páginas principales
│   ├── HomePage.js
│   ├── ConflictosPage.js
│   ├── CrearConflictoPage.js
│   └── UsuariosPage.js
├── services/            # Servicios API
│   └── apiService.js
├── hooks/               # Custom hooks
├── styles/              # Estilos CSS
├── App.js              # Componente principal
├── index.js            # Punto de entrada
└── public/             # Archivos estáticos
```

## 🔌 API Integration

El servicio `apiService.js` maneja todas las comunicaciones con el backend:

```javascript
import { ConflictoService, UsuarioService } from './services/apiService';

// Obtener conflictos
const conflictos = await ConflictoService.obtenerTodos();

// Crear conflicto
await ConflictoService.crear(conflictoData);

// Obtener usuarios
const usuarios = await UsuarioService.obtenerTodos();
```

## 🎨 Diseño

- **Colors**: Colores definidos en CSS variables para fácil personalización
- **Componentes**: Componentes reutilizables y modularizados
- **Responsive**: Diseño móvil-first que se adapta a todos los tamaños

## 📦 Dependencias Principales

- `react`: Librería UI
- `react-dom`: Renderizado DOM
- `react-router-dom`: Enrutamiento
- `axios`: Cliente HTTP
- `react-toastify`: Notificaciones

## 🧪 Testing

```bash
npm test
```

## 📱 Responsive Design

La aplicación es completamente responsiva:
- Desktop (>1200px)
- Tablet (768px-1200px)
- Mobile (<768px)

## ♿ Accesibilidad

- Etiquetas semánticas HTML
- ARIA labels donde sea necesario
- Contraste de colores adecuado
- Navegación por teclado

## 🚨 Manejo de Errores

Sistema de notificaciones con react-toastify:
- Errores
- Éxitos
- Advertencias
- Información

## 🔐 Autenticación

Actualmente sin autenticación (próxima fase).

## 📈 Performance

- Code splitting automático
- Lazy loading de componentes
- Optimización de re-renders

## 🐛 Debugging

Usar React Developer Tools:
- Chrome Extension
- Firefox Extension

## 📝 Notas

- El archivo `.env` no debe ser commiteado a git
- Las credenciales deben estar en variables de entorno
- El backend debe estar corriendo en `http://localhost:8080`

## 🤝 Contribución

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crear rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abrir Pull Request

## 📞 Soporte

Para preguntas o problemas, contacta al equipo de desarrollo.

---

**Versión**: 1.0.0  
**Última actualización**: Marzo 2024  
**Autor**: ConciliaYa Team
