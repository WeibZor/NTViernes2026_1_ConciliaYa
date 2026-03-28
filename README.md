# ConciliaYa - Sistema de Reconciliación de Datos

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Descripción

ConciliaYa es una plataforma integral de reconciliación y gestión de datos diseñada para automatizar procesos de validación, sincronización y exportación de información. El sistema permite generar, simular y procesar grandes volúmenes de datos sintéticos para testing y análisis.

## 🎯 Características Principales

- **Generación de Datos Sintéticos**: Creación de datasets realistas para testing y análisis
- **Simulación de Usuarios**: Generación de perfiles de usuario con información completa
- **Exportación de Datos**: Facilidades para exportar datos en múltiples formatos
- **Gestión de Roles**: Soporte para diferentes roles de usuario (Admin, Usuario, Supervisor)
- **Validación de Documentos**: Soporte para múltiples tipos de identificación (DNI, CUIT, CE, RUC)

## 🚀 Inicio Rápido

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/usuario/conciliaya.git
cd conciliaya
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

### Uso Básico

```python
from Ivan_Molina import generar_datos_usuario

# Generar 1000 registros de usuarios
datos = generar_datos_usuario(num_registros=1000, semilla=42)

# Exportar a DataFrame de Pandas
import pandas as pd
df = pd.DataFrame(datos)
df.to_csv('usuarios.csv', index=False)
```

## 📁 Estructura del Proyecto

```
Proyecto Integrador/
├── Andrés Pachecho/
│   └── andrespacheco.py
├── Andrés Torres/
│   └── andrestorres.py
├── Franklin Chaverra/
│   └── franklinchaverra.py
├── Ivan Molina/
│   └── HU 28. Simulación y exportación de datos (Usuario).py
├── Juan Garcés/
│   └── juangarces.py
├── Maicol Montoya/
│   └── maicolmontoya.py
└── README.md
```

## 🛠️ Dependencias

- **pandas**: Manipulación y análisis de datos
- **random**: Generación de datos aleatorios
- **datetime**: Manejo de fechas y tiempos

## 👥 Equipo de Desarrollo

- Andrés Pachecho
- Andrés Torres
- Franklin Chaverra
- Ivan Molina
- Juan Garcés
- Maicol Montoya

## 📖 Documentación

Consulta la [documentación completa](docs/) para obtener información detallada sobre:
- API de funciones
- Guía de contribución
- Ejemplos avanzados

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el repositorio
2. Crea una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 📧 Contacto

Para preguntas o sugerencias, por favor abre un issue en el repositorio o contacta al equipo de desarrollo.

## 🙏 Reconocimientos

Proyecto desarrollado como parte del programa de formación integral.

---

**Última actualización**: Marzo 2026
