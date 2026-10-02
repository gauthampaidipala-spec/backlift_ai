import React from 'react';
import {
  Building2,
  Users,
  AlertTriangle,
  Award,
  Info,
  ShieldCheck,
} from 'lucide-react';
import { sampleCampusMetrics } from '../../data/mockData';

export const CollegeDashboard: React.FC = () => {
  return (
    <div className="space-y-8 animate-in fade-in duration-300">
      {/* Top Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center gap-2">
            <h2 className="text-xl font-extrabold text-white flex items-center gap-2">
              <Building2 className="w-5 h-5 text-amber-400" />
              BackLift Campus: Institutional Faculty & Dean Portal
            </h2>
            <span className="text-[10px] font-bold uppercase tracking-wider text-amber-400 bg-amber-400/10 px-2.5 py-0.5 rounded-full border border-amber-400/20">
              B2B Demo View
            </span>
          </div>
          <p className="text-xs text-slate-400 mt-0.5">
            Aggregated, anonymized student academic risk telemetry for university retention & accreditation bodies.
          </p>
        </div>

        <div className="px-4 py-2 rounded-2xl glass-panel text-xs text-indigo-300 flex items-center gap-2.5 border border-indigo-500/25">
          <Info className="w-4 h-4 text-indigo-400 shrink-0" />
          <span>
            <strong>Sample Data Notice:</strong> All metrics displayed are simulated demonstration data.
          </span>
        </div>
      </div>

      {/* Aggregate Institutional KPI Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        <div className="glass-panel p-6 rounded-3xl space-y-2">
          <div className="flex justify-between text-xs text-slate-400 font-bold uppercase">
            <span>Enrolled Students</span>
            <Users className="w-4 h-4 text-indigo-400" />
          </div>
          <div className="text-3xl font-black text-white">440</div>
          <p className="text-xs text-slate-400">Across 3 Engineering Branches</p>
        </div>

        <div className="glass-panel p-6 rounded-3xl space-y-2">
          <div className="flex justify-between text-xs text-slate-400 font-bold uppercase">
            <span>Active Backlog Cases</span>
            <AlertTriangle className="w-4 h-4 text-rose-400" />
          </div>
          <div className="text-3xl font-black text-rose-400">113</div>
          <p className="text-xs text-slate-400">25.6% Batch Risk Rate</p>
        </div>

        <div className="glass-panel p-6 rounded-3xl space-y-2">
          <div className="flex justify-between text-xs text-slate-400 font-bold uppercase">
            <span>Turnaround Rate</span>
            <Award className="w-4 h-4 text-emerald-400" />
          </div>
          <div className="text-3xl font-black text-emerald-400">62.8%</div>
          <p className="text-xs text-emerald-400/80">Average Recovery Progress</p>
        </div>

        <div className="glass-panel p-6 rounded-3xl space-y-2">
          <div className="flex justify-between text-xs text-slate-400 font-bold uppercase">
            <span>Dropout Prevention</span>
            <ShieldCheck className="w-4 h-4 text-teal-400" />
          </div>
          <div className="text-3xl font-black text-teal-400">+18%</div>
          <p className="text-xs text-teal-400/80">Projected Year-Back Reduction</p>
        </div>
      </div>

      {/* Department Breakdown & Critical Subject Bottlenecks */}
      <div className="space-y-4">
        <h3 className="text-sm font-bold uppercase tracking-wider text-slate-300">
          Departmental Failure Hotspots & Subject Bottlenecks
        </h3>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {sampleCampusMetrics.map((dept, idx) => (
            <div
              key={idx}
              className="glass-panel rounded-3xl p-6 sm:p-7 space-y-5 flex flex-col justify-between"
            >
              <div className="space-y-4">
                <div className="flex items-start justify-between">
                  <div>
                    <h4 className="text-base font-extrabold text-white">
                      {dept.department}
                    </h4>
                    <p className="text-xs text-slate-400 mt-1">
                      {dept.studentsWithBacklogs} of {dept.totalStudents} students need intervention
                    </p>
                  </div>
                  <span className="text-xs font-black text-indigo-400 bg-indigo-950/80 px-2.5 py-1 rounded-xl border border-indigo-800">
                    ARS: {dept.averageRecoveryScore}
                  </span>
                </div>

                <div className="space-y-2.5 pt-2 border-t border-white/[0.06]">
                  <div className="text-[10px] font-bold uppercase tracking-wider text-slate-500">
                    Top Bottleneck Subjects:
                  </div>
                  {dept.bottleneckSubjects.map((sub, sIdx) => (
                    <div
                      key={sIdx}
                      className="p-3 rounded-2xl bg-slate-800/40 border border-white/[0.06] flex items-center justify-between text-xs"
                    >
                      <div>
                        <div className="font-semibold text-slate-200">{sub.name}</div>
                        <div className="text-[10px] text-slate-400">{sub.code} • {sub.enrolledBacklogs} enrolled backlogs</div>
                      </div>
                      <span className="text-xs font-bold text-rose-400">
                        {sub.failureRate}% Fail
                      </span>
                    </div>
                  ))}
                </div>
              </div>

              <div className="pt-3 border-t border-white/[0.06] text-xs text-slate-400">
                Early mentor intervention alerts scheduled for Week 8.
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
