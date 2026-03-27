# GUÍA DE CONFIGURACIÓN - ConciliaYa

Este documento describe todas las configuraciones necesarias para ejecutar ConciliaYa en diferentes entornos.

---

## 🔧 Backend - Spring Boot

### Archivo: `conciliaya-backend/src/main/resources/application.yml`

#### 1. Configuración para PostgreSQL (Producción)

```yaml
spring:
  application:
    name: conciliaya-backend
    
  # Configuración JPA/Hibernate
  jpa:
    database-platform: org.hibernate.dialect.PostgreSQLDialect
    hibernate:
      ddl-auto: update  # Valores: validate, update, create, create-drop
    show-sql: false
    properties:
      hibernate:
        format_sql: true
        jdbc.batch_size: 20
        order_inserts: true
        order_updates: true

  # Configuración de Base de Datos - PostgreSQL
  datasource:
    url: jdbc:postgresql://localhost:5432/conciliaya
    username: postgres
    password: tu_contraseña_segura  # CAMBIAR EN PRODUCCIÓN
    driver-class-name: org.postgresql.Driver
    hikari:
      maximum-pool-size: 10
      minimum-idle: 5
      connection-timeout: 20000
      idle-timeout: 300000

# Integración con Microservice
microservice:
  clasificador:
    url: http://localhost:8000
    endpoint: /api/v1/classify-conflict
    timeout-ms: 5000

# Servidor
server:
  port: 8080
  servlet:
    context-path: /api
  compression:
    enabled: true
    min-response-size: 1024

# Logging
logging:
  level:
    root: WARN
    com.conciliaya: INFO
    org.springframework.web: WARN
    org.hibernate: WARN
  pattern:
    console: "%d{yyyy-MM-dd HH:mm:ss} - %msg%n"
    file: "%d{yyyy-MM-dd HH:mm:ss} [%thread] %-5level %logger{36} - %msg%n"
  file:
    name: logs/conciliaya.log
    max-size: 10MB
    max-history: 10

# Actuator para monitoreo
management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics
  endpoint:
    health:
      show-details: always
```

#### 2. Configuración para MySQL

```yaml
spring:
  jpa:
    database-platform: org.hibernate.dialect.MySQL8Dialect
    hibernate:
      ddl-auto: update

  datasource:
    url: jdbc:mysql://localhost:3306/conciliaya?useSSL=false&serverTimezone=UTC&allowPublicKeyRetrieval=true
    username: root
    password: tu_contraseña_segura  # CAMBIAR EN PRODUCCIÓN
    driver-class-name: com.mysql.cj.jdbc.Driver
    hikari:
      maximum-pool-size: 10
      minimum-idle: 5
      connection-timeout: 20000
```

#### 3. Configuración para Ambiente de Testing (H2)

```yaml
spring:
  jpa:
    database-platform: org.hibernate.dialect.H2Dialect
    hibernate:
      ddl-auto: create-drop

  datasource:
    url: jdbc:h2:mem:testdb
    username: sa
    password:
    driver-class-name: org.h2.Driver

microservice:
  clasificador:
    url: http://localhost:8000
    timeout-ms: 10000

server:
  port: 8080
```

---

## 🎨 Frontend - React

### Archivo: `conciliaya-frontend/.env`

#### Desarrollo Local

```env
# API Backend
REACT_APP_API_URL=http://localhost:8080/api

# Ambiente
REACT_APP_ENV=development

# Debug (opcional)
REACT_APP_DEBUG=true
```

#### Producción

```env
# API Backend (URL de producción)
REACT_APP_API_URL=https://api.conciliaya.com/api

# Ambiente
REACT_APP_ENV=production

# Debug
REACT_APP_DEBUG=false
```

#### Testing

```env
REACT_APP_API_URL=http://localhost:8080/api
REACT_APP_ENV=test
REACT_APP_DEBUG=false
```

### Archivo: `conciliaya-frontend/package.json`

```json
{
  "name": "conciliaya-frontend",
  "version": "1.0.0",
  "private": true,
  "homepage": "/",
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject",
    "build:prod": "REACT_APP_ENV=production npm run build"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.16.0",
    "axios": "^1.5.0",
    "react-toastify": "^9.1.3"
  },
  "devDependencies": {
    "react-scripts": "5.0.1"
  },
  "browserslist": {
    "production": [">0.2%", "not dead", "not op_mini all"],
    "development": ["last 1 chrome version", "last 1 firefox version", "last 1 safari version"]
  }
}
```

---

## 🐍 Microservice - FastAPI

### Archivo: `.env` (Opcional)

```env
# Configuración del Servidor
UVICORN_HOST=0.0.0.0
UVICORN_PORT=8000
UVICORN_RELOAD=true

# Logging
LOG_LEVEL=INFO

# Ambiente
ENVIRONMENT=development
```

### Ejecución Local (Desarrollo)

```bash
# Activar entorno virtual
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar con reload (desarrollo)
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Acceder a:
# - API: http://localhost:8000
# - Swagger UI: http://localhost:8000/docs
# - ReDoc: http://localhost:8000/redoc
```

### Ejecución en Producción

```bash
# Iniciar Uvicorn sin reload
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4

# Con Gunicorn (alternativa)
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

---

## 🗄️ Base de Datos

### PostgreSQL

#### Instalación (Windows)

```bash
# Descargar de https://www.postgresql.org/download/windows/
# Durante instalación:
# - Usuario por defecto: postgres
# - Contraseña: (definida durante instalación)
# - Puerto: 5432

# Conectarse
psql -U postgres -h localhost

# Crear database
CREATE DATABASE conciliaya;

# Ejecutar script inicial
psql -U postgres -d conciliaya -f database-init.sql
```

#### Instalación (Linux - Ubuntu)

```bash
# Instalar PostgreSQL
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib

# Iniciar servicio
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Crear usuario
sudo -u postgres createuser --interactive
sudo -u postgres createdb conciliaya

# Ejecutar script
sudo -u postgres psql -d conciliaya -f database-init.sql
```

### MySQL

#### Instalación (Windows)

```bash
# Descargar de https://dev.mysql.com/downloads/mysql/
# Durante instalación:
# - Usuario: root
# - Contraseña: (definida durante instalación)
# - Puerto: 3306

# Conectarse
mysql -u root -p

# Crear database
CREATE DATABASE conciliaya CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# Ejecutar script
mysql -u root -p conciliaya < database-init.sql
```

---

## 🌐 Variables de Entorno Generales

### Para Todo el Sistema

```bash
# Rutas (según tu estructura)
export PROYECTO_HOME=/path/to/Proyecto integrador
export BACKEND_HOME=$PROYECTO_HOME/conciliaya-backend
export FRONTEND_HOME=$PROYECTO_HOME/conciliaya-frontend
export MICROSERVICE_HOME=$PROYECTO_HOME/conciliaya-classifier

# Java
export JAVA_HOME=/path/to/java17
export MAVEN_HOME=/path/to/maven

# Node.js
export NODE_HOME=/path/to/nodejs

# Python
export PYTHON_HOME=/path/to/python3.9
```

---

## 🔐 Seguridad - Nota Importante

### Credenciales por Defecto

```
❌ NUNCA usar en producción las siguientes credenciales:
   - Usuario BD: postgres / root
   - Contraseña: password / admin
   - Usuario Admin: admin@conciliaya.com
```

### Para Producción

1. **Cambiar todas las contraseñas**
   ```sql
   ALTER USER postgres WITH PASSWORD 'nueva_contrasena_segura';
   UPDATE usuarios SET email = 'nuevo_admin@tudominio.com' WHERE id = 1;
   ```

2. **Implementar Spring Security** (futura fase)
   - JWT tokens para autenticación
   - Roles y permisos
   - CORS configurado

3. **HTTPS obligatorio**
   - Certificados SSL/TLS
   - Nginx/Apache como proxy reverso

4. **Validação de entrada**
   - DTOs con validaciones
   - OWASP Top 10 considerados

---

## 📋 Checklist de Configuración

### Antes de Iniciar Desarrollo

- [ ] Java 17 instalado
- [ ] Node.js 16+ instalado
- [ ] Python 3.9+ instalado
- [ ] PostgreSQL/MySQL instalado y corriendo
- [ ] Base de datos creada
- [ ] Script database-init.sql ejecutado
- [ ] `application.yml` configurado con credenciales BD
- [ ] `.env` configurado en frontend
- [ ] Requirements.txt instalado en microservice

### Antes de Producción

- [ ] Todas las credenciales cambiadas
- [ ] HTTPS habilitado
- [ ] Logging configurado
- [ ] Backups de BD programados
- [ ] Monitoreo activado
- [ ] Tests todas las funcionalidades
- [ ] Documentación actualizada
- [ ] Usuarios de sistemas creados (no usar admin genérico)

---

## 🚀 Comandos Rápidos

### Backend

```bash
cd conciliaya-backend

# Instalar dependencias
mvn clean install

# Ejecutar
mvn spring-boot:run

# Ejecutar tests
mvn test

# Compilar JAR
mvn clean package
```

### Frontend

```bash
cd conciliaya-frontend

# Instalar
npm install

# Desarrollo
npm start

# Producción
npm run build

# Tests
npm test
```

### Microservice

```bash
cd conciliaya-classifier

# Crear entorno virtual
python -m venv venv

# Activar
source venv/bin/activate

# Instalar
pip install -r requirements.txt

# Ejecutar
uvicorn main:app --reload --port 8000
```

---

## 📞 Soporte de Configuración

Si tienes problemas con la configuración:

1. **Revisa los logs**: `logs/conciliaya.log`
2. **Verifica puertos**: `netstat -ano | findstr :8080`
3. **Comprueba BD**: `mysql -u root -p -e "SHOW DATABASES;"`
4. **Revisa firewall**: Abre puertos 8080, 3000, 8000, 5432/3306
5. **Valida .env**: Asegúrate de que todas las variables estén definidas

---

Última actualización: Diciembre 2024
Versión: 1.0.0
