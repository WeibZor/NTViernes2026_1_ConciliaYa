import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import { Sparkles, Database, FileText, CheckCircle2, ArrowRight, ArrowUpRight, Play, Zap, RefreshCw } from 'lucide-react';
import usuarioRepository from '../repositories/usuarioRepository.js';
import tipoConflictoRepository from '../repositories/tipoConflictoRepository.js';
import conflictoRepository from '../repositories/conflictoRepository.js';
import estadoConflictoRepository from '../repositories/estadoConflictoRepository.js';
import perfilRepository from '../repositories/perfilRepository.js';
import mediacionRepository from '../repositories/mediacionRepository.js';

const pythonFlowCode = `# importar simulaciones y limpieza
from usuario.HU_28_Simulacion_Usuario import simular_y_exportar_usuarios, recargar_y_validar_usuarios
from usuario.HU_26_Limpieza_Usuario import limpiar_usuarios
from usuario.HU_27_Descripcion_Usuario import descripcion_usuarios
from usuario.HU_29_Query_Usuario import consultas_usuario
from usuario.HU_30_Agrupacion_Usuario import agrupaciones_usuario

from tipoconflicto.HU_23_Simulacion_TipoConflicto import simular_y_exportar_tipos_conflicto, recargar_y_validar_tipos_conflicto
from tipoconflicto.HU_21_Limpieza_TipoConflicto import limpiar_tipos_conflicto
from tipoconflicto.HU_22_Descripcion_TipoConflicto import descripcion_tipos_conflicto
from tipoconflicto.HU_24_Query_TipoConflicto import consultas_tipos_conflicto
from tipoconflicto.HU_25_Agrupacion_TipoConflicto import agrupaciones_tipos_conflicto

usuario_original = simular_y_exportar_usuarios(num_registros=1000, semilla=42)
usuario_limpio = limpiar_usuarios(usuario_original)
descripcion_usuarios(usuario_limpio)
consultas_resultado = consultas_usuario(usuario_limpio)
agrupaciones_resultado = agrupaciones_usuario(usuario_limpio)

tipoconflicto_original = simular_y_exportar_tipos_conflicto(num_registros=1000, semilla=42)
tipoconflicto_limpio = limpiar_tipos_conflicto(tipoconflicto_original)
descripcion_tipos_conflicto(tipoconflicto_limpio)
consultas_tipoconflicto_resultado = consultas_tipos_conflicto(tipoconflicto_limpio)
agrupaciones_tipoconflicto_resultado = agrupaciones_tipos_conflicto(tipoconflicto_limpio)
`;

const apiSnippet = `GET /api/usuarios
GET /api/usuarios/filter?search=...
POST /api/usuarios
PUT /api/usuarios/{id}
DELETE /api/usuarios/{id}

GET /api/tipoconflictos
GET /api/tipoconflictos/filter?search=...
POST /api/tipoconflictos/simulate
POST /api/tipoconflictos/clean
POST /api/tipoconflictos
PUT /api/tipoconflictos/{id}
DELETE /api/tipoconflictos/{id}
`;

const Demo = () => {
  const [counts, setCounts] = useState({
    usuarios: 0,
    tipos: 0,
    conflictos: 0,
    estados: 0,
    perfiles: 0,
    mediaciones: 0,
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadCounts = async () => {
      setLoading(true);
      const [usuarios, tipos, conflictos, estados, perfiles, mediaciones] = await Promise.all([
        usuarioRepository.getAll(),
        tipoConflictoRepository.getAll(),
        conflictoRepository.getAll(),
        estadoConflictoRepository.getAll(),
        perfilRepository.getAll(),
        mediacionRepository.getAll(),
      ]);

      setCounts({
        usuarios: usuarios.length,
        tipos: tipos.length,
        conflictos: conflictos.length,
        estados: estados.length,
        perfiles: perfiles.length,
        mediaciones: mediaciones.length,
      });
      setLoading(false);
    };

    loadCounts();
  }, []);

  const quickActions = [
    { label: 'Usuarios', description: 'Simula, limpia y administra usuarios con backend y frontend integrados.', path: '/usuarios', icon: Play },
    { label: 'Tipos de Conflicto', description: 'Simula tipos, limpia datos y edita registros usando backend.', path: '/tipos-conflicto', icon: Zap },
    { label: 'Estados de Conflicto', description: 'CRUD local con futuros endpoints backend.', path: '/estados-conflicto', icon: FileText },
    { label: 'Perfiles', description: 'Gestiona roles y perfiles; base lista para backend.', path: '/perfiles', icon: CheckCircle2 },
    { label: 'Conflictos', description: 'Estructura conflictos con filtros por tipo y estado.', path: '/conflictos', icon: Database },
    { label: 'Mediaciones', description: 'Controla mediaciones y su vínculo con conflictos y usuarios.', path: '/mediaciones', icon: ArrowRight },
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-indigo-950 p-6 text-slate-100">
      <div className="mx-auto max-w-7xl space-y-8">
        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="rounded-3xl border border-white/10 bg-slate-900/80 p-8 shadow-2xl shadow-cyan-500/10">
          <div className="flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between">
            <div>
              <div className="inline-flex items-center gap-3 rounded-full bg-cyan-500/10 px-4 py-2 text-cyan-300">
                <Sparkles className="h-5 w-5" />
                Demo de integración
              </div>
              <h1 className="mt-4 text-4xl font-bold text-white">Mostrar la integración del sistema</h1>
              <p className="mt-3 max-w-2xl text-slate-300">Demuestra cómo se enlazan las operaciones del frontend con los datos y los HUs de Python. Aquí puedes ver tablas, control de entidades y los scripts que ejecutan las historias de usuario.</p>
            </div>
            <div className="grid w-full max-w-sm gap-3 sm:grid-cols-2">
              <div className="rounded-3xl border border-white/10 bg-slate-950/90 p-5 text-center">
                <p className="text-sm uppercase tracking-[0.24em] text-slate-400">Usuarios</p>
                <p className="mt-2 text-3xl font-semibold text-white">{loading ? '...' : counts.usuarios}</p>
              </div>
              <div className="rounded-3xl border border-white/10 bg-slate-950/90 p-5 text-center">
                <p className="text-sm uppercase tracking-[0.24em] text-slate-400">Tipos</p>
                <p className="mt-2 text-3xl font-semibold text-white">{loading ? '...' : counts.tipos}</p>
              </div>
              <div className="rounded-3xl border border-white/10 bg-slate-950/90 p-5 text-center">
                <p className="text-sm uppercase tracking-[0.24em] text-slate-400">Conflictos</p>
                <p className="mt-2 text-3xl font-semibold text-white">{loading ? '...' : counts.conflictos}</p>
              </div>
              <div className="rounded-3xl border border-white/10 bg-slate-950/90 p-5 text-center">
                <p className="text-sm uppercase tracking-[0.24em] text-slate-400">Mediaciones</p>
                <p className="mt-2 text-3xl font-semibold text-white">{loading ? '...' : counts.mediaciones}</p>
              </div>
            </div>
          </div>
        </motion.div>

        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="grid gap-4 lg:grid-cols-2">
          {quickActions.map((action) => {
            const Icon = action.icon;
            return (
              <Link key={action.path} to={action.path} className="group rounded-3xl border border-white/10 bg-slate-900/70 p-6 transition hover:-translate-y-1 hover:border-cyan-500/30 hover:bg-slate-800/90">
                <div className="flex items-center justify-between gap-4">
                  <div>
                    <p className="text-sm text-cyan-300">{action.label}</p>
                    <p className="mt-2 text-lg font-semibold text-white">{action.description}</p>
                  </div>
                  <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-cyan-500/10 text-cyan-300 transition group-hover:bg-cyan-500/20">
                    <Icon className="h-6 w-6" />
                  </div>
                </div>
                <div className="mt-5 flex items-center gap-2 text-sm text-slate-400">
                  <ArrowRight className="h-4 w-4" />
                  Ir a sección
                </div>
              </Link>
            );
          })}
        </motion.div>

        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="grid gap-4 xl:grid-cols-[1.2fr_0.8fr]">
          <div className="rounded-3xl border border-white/10 bg-slate-900/80 p-6 shadow-2xl shadow-slate-900/40">
            <h2 className="text-2xl font-semibold text-white">Tablas del sistema</h2>
            <div className="mt-6 grid gap-4 sm:grid-cols-2">
              <div className="rounded-3xl border border-white/10 bg-slate-950/70 p-4">
                <p className="text-xs uppercase tracking-[0.2em] text-slate-400">Perfil</p>
                <p className="mt-3 text-xl font-semibold text-white">{loading ? '...' : counts.perfiles}</p>
                <p className="mt-2 text-sm text-slate-400">Tabla de roles y permisos lista para integrar con backend.</p>
              </div>
              <div className="rounded-3xl border border-white/10 bg-slate-950/70 p-4">
                <p className="text-xs uppercase tracking-[0.2em] text-slate-400">Estado Conflicto</p>
                <p className="mt-3 text-xl font-semibold text-white">{loading ? '...' : counts.estados}</p>
                <p className="mt-2 text-sm text-slate-400">Estados de equipo para conflictos: activo, cerrado, en proceso.</p>
              </div>
              <div className="rounded-3xl border border-white/10 bg-slate-950/70 p-4">
                <p className="text-xs uppercase tracking-[0.2em] text-slate-400">Conflictos</p>
                <p className="mt-3 text-xl font-semibold text-white">{loading ? '...' : counts.conflictos}</p>
                <p className="mt-2 text-sm text-slate-400">Registros de conflictos vinculados a tipos y estados.</p>
              </div>
              <div className="rounded-3xl border border-white/10 bg-slate-950/70 p-4">
                <p className="text-xs uppercase tracking-[0.2em] text-slate-400">Mediaciones</p>
                <p className="mt-3 text-xl font-semibold text-white">{loading ? '...' : counts.mediaciones}</p>
                <p className="mt-2 text-sm text-slate-400">Sesiones de mediación asociadas a conflictos y moderadores.</p>
              </div>
            </div>
          </div>
          <div className="rounded-3xl border border-white/10 bg-slate-900/80 p-6 shadow-2xl shadow-slate-900/40">
            <h2 className="text-2xl font-semibold text-white">Estado de integración</h2>
            <div className="mt-6 space-y-4">
              <div className="rounded-3xl border border-white/10 bg-slate-950/70 p-4">
                <p className="text-sm font-semibold text-cyan-300">Backend disponible</p>
                <p className="mt-2 text-sm text-slate-400">Usuarios y Tipos de Conflicto ya usan rutas FastAPI reales. El resto funciona con la base local y está preparado para backend futuro.</p>
              </div>
              <div className="rounded-3xl border border-white/10 bg-slate-950/70 p-4">
                <p className="text-sm font-semibold text-cyan-300">Demostración en vivo</p>
                <p className="mt-2 text-sm text-slate-400">Usa los botones de arriba para mostrar creación, edición, eliminación, simulación y limpieza directamente en la UI.</p>
              </div>
              <div className="rounded-3xl border border-white/10 bg-slate-950/70 p-4">
                <p className="text-sm font-semibold text-cyan-300">Código Python</p>
                <p className="mt-2 text-sm text-slate-400">El backend carga los HUs de Python para generar datos, limpiarlos, describirlos y crear consultas.</p>
              </div>
            </div>
          </div>
        </motion.div>

        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="rounded-3xl border border-white/10 bg-slate-900/80 p-6 shadow-2xl shadow-slate-900/40">
          <div className="flex items-center justify-between gap-4">
            <div>
              <h2 className="text-2xl font-semibold text-white">Código Python ejecutado</h2>
              <p className="mt-2 text-slate-400">Fragmentos del flujo que genera datos en el backend y construye los HUs de Usuario y TipoConflicto.</p>
            </div>
            <div className="inline-flex items-center gap-2 rounded-full bg-cyan-500/10 px-4 py-2 text-cyan-300">
              <Play className="h-4 w-4" /> Python
            </div>
          </div>
          <pre className="mt-5 max-h-72 overflow-auto rounded-3xl border border-white/10 bg-slate-950/80 p-4 text-sm text-slate-200"><code>{pythonFlowCode}</code></pre>
        </motion.div>

        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="rounded-3xl border border-white/10 bg-slate-900/80 p-6 shadow-2xl shadow-slate-900/40">
          <div className="flex items-center justify-between gap-4">
            <div>
              <h2 className="text-2xl font-semibold text-white">API disponible</h2>
              <p className="mt-2 text-slate-400">Este es el contrato que el frontend usa para unir la UI con los HUs del backend.</p>
            </div>
            <div className="inline-flex items-center gap-2 rounded-full bg-slate-700/80 px-4 py-2 text-slate-200">
              <Database className="h-4 w-4" /> API
            </div>
          </div>
          <pre className="mt-5 max-h-72 overflow-auto rounded-3xl border border-white/10 bg-slate-950/80 p-4 text-sm text-slate-200"><code>{apiSnippet}</code></pre>
        </motion.div>
      </div>
    </div>
  );
};

export default Demo;
