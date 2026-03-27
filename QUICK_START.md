# 🚀 Guía Rápida de Inicio - ConciliaYa

Esta guía te ayudará a configurar y ejecutar **ConciliaYa** en tu máquina local en menos de 10 minutos.

## ⚡ Inicio Rápido (5 minutos)

### Requisitos Mínimos
- ✅ Java 17+
- ✅ Node.js 16+
- ✅ Python 3.9+
- ✅ PostgreSQL o MySQL
- ✅ Git

### Paso 1: Clonar o Descargar el Proyecto

```bash
# Descargar el archivo ZIP y extraerlo
# O clonar si está en un repositorio
cd "Proyecto integrador"
```

### Paso 2: Configurar la Base de Datos

**PostgreSQL:**
```sql
-- Crear database
CREATE DATABASE conciliaya;

-- Conectarse con usuario postgres
-- La aplicación creará las tablas automáticamente
```

**MySQL:**
```sql
-- Crear database
CREATE DATABASE conciliaya CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Las tablas se crearán automáticamente
```

### Paso 3: Iniciar en Terminal 1 - Microservice (FastAPI)

```bash
cd conciliaya-classifier

# Windows
python -m venv env && env\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000

# Linux/Mac
python3 -m venv env && source env/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

✅ Verificar: http://localhost:8000/docs

### Paso 4: Iniciar en Terminal 2 - Backend (Spring Boot)

```bash
cd conciliaya-backend

# Editar application.yml con tus credenciales de BD
# spring.datasource.url: jdbc:postgresql://localhost:5432/conciliaya
# spring.datasource.username: tu_usuario
# spring.datasource.password: tu_contraseña

# Ejecutar
mvn spring-boot:run
```

✅ Verificar: http://localhost:8080/api/conflictos

### Paso 5: Iniciar en Terminal 3 - Frontend (React)

```bash
cd conciliaya-frontend

# Copiar archivo de entorno
# cp .env.example .env

# Instalar dependencias
npm install

# Iniciar
npm start
```

✅ Verificar: http://localhost:3000

---

## 📝 Configuración por Componente

### Backend (application.yml)

**PostgreSQL:**
```yaml
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/conciliaya
    username: postgres
    password: password
    driver-class-name: org.postgresql.Driver
```

**MySQL:**
```yaml
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/conciliaya?useSSL=false&serverTimezone=UTC
    username: root
    password: password
    driver-class-name: com.mysql.cj.jdbc.Driver
```

### Frontend (.env)

```env
REACT_APP_API_URL=http://localhost:8080/api
REACT_APP_ENV=development
```

---

## 🧪 Pruebas Rápidas

### 1. Crear un Conflicto (Backend)

```bash
curl -X POST http://localhost:8080/api/conflictos \
  -H "Content-Type: application/json" \
  -d '{
    "descripcion": "Ruido excesivo por música a altas horas",
    "ubicacion": "Departamento 3B",
    "prioridad": 3,
    "usuarioReportanteId": 1,
    "tipoConflictoId": 1
  }'
```

### 2. Listar Conflictos

```bash
curl http://localhost:8080/api/conflictos
```

### 3. Clasificar Conflicto (Microservice)

```bash
curl -X POST http://localhost:8000/api/v1/classify-conflict \
  -H "Content-Type: application/json" \
  -d '{"descripcion": "Problema de agua en la entrada del edificio"}'
```

---

## 🐛 Solución de Problemas

| Problema | Solución |
|----------|----------|
| **Puerto 8080 en uso** | `netstat -ano \| findstr :8080` (Windows) y matar proceso, o cambiar puerto en `application.yml` |
| **BaseDatos no conecta** | Verificar credenciales, que PostgreSQL/MySQL corra, y firewall |
| **Frontend no entra** | Verificar `REACT_APP_API_URL` en `.env` apunte a `http://localhost:8080/api` |
| **Microservice no responde** | Verificar que uvicorn está corriendo en puerto 8000 |
| **Módulos no encontrados** | `npm install` (frontend) y `mvn clean install` (backend) |

---

## 📊 Endpoints Principales

### Conflictos
- `GET /api/conflictos` - Listar todos
- `POST /api/conflictos` - Crear
- `PUT /api/conflictos/{id}` - Actualizar
- `DELETE /api/conflictos/{id}` - Eliminar

### Usuarios
- `GET /api/usuarios` - Listar todos
- `POST /api/usuarios` - Crear
- `GET /api/usuarios/{id}` - Obtener uno

### Microservice (FastAPI)
- `POST /api/v1/classify-conflict` - Clasificar
- `GET /health` - Health check
- `GET /api/v1/tipos-conflicto` - Tipos disponibles

---

## 📚 Documentación Completa

Para documentación detallada ver:
- [README.md General](./README.md)
- [Backend README](./conciliaya-backend/README.md)
- [Frontend README](./conciliaya-frontend/README.md)
- [Microservice README](./conciliaya-classifier/README.md)

---

## ✅ Checklist de Verificación

- [ ] Base de datos creada y accesible
- [ ] Terminal 1: Microservice (FastAPI) corriendo en puerto 8000
- [ ] Terminal 2: Backend (Spring Boot) corriendo en puerto 8080
- [ ] Terminal 3: Frontend (React) corriendo en puerto 3000
- [ ] Poder acceder a http://localhost:3000 en navegador
- [ ] Crear un conflicto desde la interfaz
- [ ] Ver conflicto listado en la página principal

---

## 🎯 Próximos Pasos

1. **Ver Documentación**: Revisar README de cada componente
2. **Crear Conflictos**: Usar la interfaz para crear conflictos
3. **Explorar API**: Usar Swagger en http://localhost:8080/swagger-ui.html
4. **Agregar Tests**: Implementar tests unitarios
5. **Seguridad**: Agregar autenticación con Spring Security + JWT

---

¡**Listo!** 🎉 Ahora tienes ConciliaYa corriendo en tu máquina local.
