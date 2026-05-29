import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import {
  BarChart3, TrendingUp, PieChart, Activity,
  Users, MessageSquare, DollarSign, Calendar,
  ImageIcon, RefreshCw
} from 'lucide-react';
import conflictoRepository from '../repositories/conflictoRepository.js';
import mediacionRepository from '../repositories/mediacionRepository.js';
import usuarioRepository from '../repositories/usuarioRepository.js';
import publicacionesRepository from '../repositories/publicacionesRepository.js';

// ─── Imports de las gráficas generadas por Python ───────────────────────────
import tortaEstadoConflicto    from '../assets/graficos/torta_estado_conflicto_activos.png';
import barrasPerfilesTipo      from '../assets/graficos/barras_perfiles_por_tipo.png';
import tortaTiposConflicto     from '../assets/graficos/torta_tipos_conflicto_activos.png';
import mapaCalorUsuarios       from '../assets/graficos/mapa_calor_usuarios_docperfil.png';
import mapaCalorConflictos     from '../assets/graficos/mapa_calor_conflictos_tipo_estado.png';
import mapaCalorMediaciones    from '../assets/graficos/mapa_calor_mediaciones_sede_resultado.png';

// ─── Metadatos de cada gráfico ───────────────────────────────────────────────
const GRAFICOS = [
  {
    src: tortaEstadoConflicto,
    titulo: 'Estados de Conflicto',
    subtitulo: 'Distribución de estados activos',
    icono: PieChart,
    color: 'cyan',
    span: 1,
  },
  {
    src: barrasPerfilesTipo,
    titulo: 'Perfiles por Tipo',
    subtitulo: 'Cantidad de registros por perfil',
    icono: BarChart3,
    color: 'indigo',
    span: 1,
  },
  {
    src: tortaTiposConflicto,
    titulo: 'Tipos de Conflicto',
    subtitulo: 'Proporción de tipos activos',
    icono: PieChart,
    color: 'emerald',
    span: 1,
  },
  {
    src: mapaCalorUsuarios,
    titulo: 'Usuarios: Documento × Perfil',
    subtitulo: 'Combinaciones más frecuentes',
    icono: Users,
    color: 'violet',
    span: 2,
  },
  {
    src: mapaCalorConflictos,
    titulo: 'Conflictos: Tipo × Estado',
    subtitulo: 'Densidad de casos por cruce',
    icono: Activity,
    color: 'amber',
    span: 2,
  },
  {
    src: mapaCalorMediaciones,
    titulo: 'Mediaciones: Sede × Resultado',
    subtitulo: '¿Dónde se logran más acuerdos?',
    icono: Calendar,
    color: 'pink',
    span: 2,
  },
];

// ─── Colores Tailwind por categoría ─────────────────────────────────────────
const COLOR_MAP = {
  cyan:   { badge: 'bg-cyan-500/20 text-cyan-300',   icon: 'bg-cyan-500/20',   dot: 'bg-cyan-400'   },
  indigo: { badge: 'bg-indigo-500/20 text-indigo-300', icon: 'bg-indigo-500/20', dot: 'bg-indigo-400' },
  emerald:{ badge: 'bg-emerald-500/20 text-emerald-300', icon: 'bg-emerald-500/20', dot: 'bg-emerald-400' },
  violet: { badge: 'bg-violet-500/20 text-violet-300', icon: 'bg-violet-500/20', dot: 'bg-violet-400' },
  amber:  { badge: 'bg-amber-500/20 text-amber-300',  icon: 'bg-amber-500/20',  dot: 'bg-amber-400'  },
  pink:   { badge: 'bg-pink-500/20 text-pink-300',    icon: 'bg-pink-500/20',   dot: 'bg-pink-400'   },
};

// ─── Componente de tarjeta para cada gráfico ────────────────────────────────
const GraficoCard = ({ src, titulo, subtitulo, icono: Icono, color, span, index }) => {
  const c = COLOR_MAP[color] || COLOR_MAP.cyan;
  const isWide = span === 2;

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: index * 0.08 }}
      className={`glass rounded-3xl border border-white/10 p-6 shadow-2xl ${isWide ? 'xl:col-span-2' : ''}`}
    >
      {/* Encabezado */}
      <div className="flex items-center justify-between gap-3 mb-5">
        <div className="flex items-center gap-3">
          <div className={`p-2 rounded-xl ${c.icon}`}>
            <Icono className={`h-5 w-5 ${c.badge.split(' ')[1]}`} />
          </div>
          <div>
            <h3 className="text-base font-semibold text-white leading-tight">{titulo}</h3>
            <p className="text-xs text-gray-500 mt-0.5">{subtitulo}</p>
          </div>
        </div>
        <span className={`text-xs font-medium px-3 py-1 rounded-full ${c.badge}`}>
          Python · matplotlib
        </span>
      </div>

      {/* Imagen */}
      <div className="w-full rounded-2xl overflow-hidden bg-white/5 flex items-center justify-center min-h-[200px]">
        <img
          src={src}
          alt={titulo}
          className="w-full h-auto object-contain rounded-2xl"
          onError={(e) => {
            e.target.style.display = 'none';
            e.target.nextSibling.style.display = 'flex';
          }}
        />
        {/* Fallback si la imagen no carga */}
        <div
          className="hidden flex-col items-center gap-2 py-12 text-gray-600"
          style={{ display: 'none' }}
        >
          <ImageIcon className="h-10 w-10 opacity-40" />
          <span className="text-sm">Ejecutar main.py para generar</span>
        </div>
      </div>
    </motion.div>
  );
};

// ─── Tarjeta de KPI ──────────────────────────────────────────────────────────
const StatCard = ({ icon: Icon, title, value, subtitle, color = 'cyan' }) => {
  const c = COLOR_MAP[color] || COLOR_MAP.cyan;
  return (
    <div className={`glass rounded-3xl border border-white/10 p-6 shadow-2xl`}>
      <div className="flex items-center justify-between">
        <div>
          <p className="text-sm font-medium text-gray-400 uppercase tracking-wider">{title}</p>
          <p className="text-3xl font-bold text-white mt-1">{value}</p>
          {subtitle && <p className="text-sm text-gray-400 mt-1">{subtitle}</p>}
        </div>
        <div className={`p-3 rounded-2xl ${c.icon}`}>
          <Icon className={`h-8 w-8 ${c.badge.split(' ')[1]}`} />
        </div>
      </div>
    </div>
  );
};

// ─── Página principal ────────────────────────────────────────────────────────
const Estadisticas = () => {
  const [stats, setStats] = useState({
    totalConflictos: 0,
    conflictosActivos: 0,
    mediacionesProgramadas: 0,
    mediacionesCompletadas: 0,
    totalUsuarios: 0,
    publicacionesRecientes: 0,
    montoTotal: 0,
    conflictosPorTipo: [],
    conflictosPorEstado: [],
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => { loadStats(); }, []);

  const loadStats = async () => {
    setLoading(true);
    try {
      const [conflictos, mediaciones, usuarios, publicaciones] = await Promise.all([
        conflictoRepository.getAll(),
        mediacionRepository.getAll(),
        usuarioRepository.getAll(),
        publicacionesRepository.getAll(),
      ]);

      const conflictosActivos     = conflictos.filter(c => c.activo).length;
      const mediacionesProgramadas = mediaciones.filter(m => !m.resultado).length;
      const mediacionesCompletadas = mediaciones.filter(m => m.resultado).length;
      const publicacionesRecientes = publicaciones.filter(p => {
        return new Date(p.fechaCreacion) > new Date(Date.now() - 7 * 24 * 60 * 60 * 1000);
      }).length;
      const montoTotal = conflictos.reduce((s, c) => s + (c.montoReclamado || 0), 0);

      const tiposCount  = {};
      const estadosCount = {};
      conflictos.forEach(c => {
        tiposCount[c.tipoConflictoId]   = (tiposCount[c.tipoConflictoId]   || 0) + 1;
        estadosCount[c.estadoConflictoId] = (estadosCount[c.estadoConflictoId] || 0) + 1;
      });

      setStats({
        totalConflictos: conflictos.length,
        conflictosActivos,
        mediacionesProgramadas,
        mediacionesCompletadas,
        totalUsuarios: usuarios.length,
        publicacionesRecientes,
        montoTotal,
        conflictosPorTipo:   Object.entries(tiposCount).map(([id, c]) => ({ tipo: `Tipo ${id}`, cantidad: c })),
        conflictosPorEstado: Object.entries(estadosCount).map(([id, c]) => ({ estado: `Estado ${id}`, cantidad: c })),
      });
    } catch (error) {
      console.error('Error loading stats:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="space-y-6">

      {/* ── Encabezado ── */}
      <div className="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
        <div>
          <div className="inline-flex items-center gap-2 rounded-full bg-gradient-to-r from-cyan-500 to-sky-500 px-4 py-2 text-white shadow-xl shadow-cyan-500/20">
            <BarChart3 className="h-5 w-5" />
            <span>Estadísticas</span>
          </div>
          <h1 className="mt-3 text-3xl font-bold text-white">Análisis empresarial</h1>
          <p className="max-w-2xl text-gray-400 mt-2">
            Métricas clave del sistema · Gráficos generados desde el pipeline de datos Python.
          </p>
        </div>
        <div className="inline-flex items-center gap-2 rounded-2xl bg-white/5 px-5 py-3 text-sm text-gray-300 shadow-xl">
          <TrendingUp className="h-4 w-4 text-green-300" />
          Dashboard avanzado
        </div>
      </div>

      {/* ── Banner informativo ── */}
      <div className="glass rounded-3xl border border-white/10 p-5 shadow-2xl">
        <div className="flex flex-col gap-3 md:flex-row md:items-center md:justify-between">
          <div>
            <h2 className="text-base font-semibold text-white">Indicadores clave</h2>
            <p className="text-sm text-gray-400">
              Las gráficas se generan ejecutando <code className="text-cyan-400 bg-white/5 px-1.5 py-0.5 rounded-lg text-xs">main.py</code> · Los KPIs se calculan en tiempo real desde la base de datos local.
            </p>
          </div>
          <div className="inline-flex items-center gap-2 rounded-2xl bg-white/5 px-4 py-2.5 text-sm text-gray-300">
            <Activity className="h-4 w-4 text-cyan-300" />
            Informe de desempeño
          </div>
        </div>
      </div>

      {/* ── KPIs ── */}
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <StatCard icon={MessageSquare} title="Total Conflictos"
          value={loading ? '…' : stats.totalConflictos}
          subtitle={`${stats.conflictosActivos} activos`} color="cyan" />
        <StatCard icon={Calendar} title="Mediaciones"
          value={loading ? '…' : stats.mediacionesProgramadas + stats.mediacionesCompletadas}
          subtitle={`${stats.mediacionesCompletadas} completadas`} color="indigo" />
        <StatCard icon={Users} title="Usuarios"
          value={loading ? '…' : stats.totalUsuarios}
          subtitle="Registrados" color="emerald" />
        <StatCard icon={DollarSign} title="Monto Total"
          value={loading ? '…' : `$${stats.montoTotal.toLocaleString()}`}
          subtitle="Reclamado" color="amber" />
      </div>

      {/* ── Gráficas Python — fila 1: tortas y barras (3 columnas) ── */}
      <div className="grid gap-4 xl:grid-cols-3">
        {GRAFICOS.slice(0, 3).map((g, i) => (
          <GraficoCard key={g.titulo} {...g} span={1} index={i} />
        ))}
      </div>

      {/* ── Gráficas Python — fila 2: mapas de calor (2 columnas) ── */}
      <div className="grid gap-4 xl:grid-cols-2">
        {GRAFICOS.slice(3).map((g, i) => (
          <GraficoCard key={g.titulo} {...g} span={2} index={i + 3} />
        ))}
      </div>

      {/* ── Pie de sección ── */}
      <div className="glass rounded-3xl border border-white/10 p-6 shadow-2xl">
        <div className="flex items-center justify-between gap-3 mb-2">
          <div>
            <p className="text-sm uppercase tracking-[0.2em] text-gray-500">Actividad reciente</p>
            <h3 className="mt-1 text-xl font-semibold text-white">Publicaciones esta semana</h3>
          </div>
          <div className="inline-flex items-center gap-2 rounded-2xl bg-white/5 px-3 py-2 text-sm text-gray-300">
            <MessageSquare className="h-4 w-4 text-pink-400" />
            {loading ? '…' : stats.publicacionesRecientes} posts
          </div>
        </div>
        <p className="text-sm text-gray-400">
          Los KPIs se calculan automáticamente desde la base de datos local.
          Las gráficas son generadas por el pipeline Python y se actualizan al volver a ejecutar <code className="text-cyan-400 bg-white/5 px-1.5 py-0.5 rounded-lg text-xs">main.py</code>.
        </p>
      </div>

    </motion.div>
  );
};

export default Estadisticas;
