import React, { useState } from 'react';
import {
  Flame,
  Award,
  FileDown,
  RotateCcw,
  Sparkles,
  Info,
  ChevronDown,
  User,
} from 'lucide-react';
import { StudentProfile, RecoveryFactorBreakdown } from '../types';

interface NavbarProps {
  student: StudentProfile;
  recoveryScore: number;
  recoveryFactors: RecoveryFactorBreakdown[];
  gradeBadge: string;
  onOpenReportModal: () => void;
  onResetData: () => void;
  onOpenOnboarding: () => void;
}

export const Navbar: React.FC<NavbarProps> = ({
  student,
  recoveryScore,
  recoveryFactors,
  gradeBadge,
  onOpenReportModal,
  onResetData,
  onOpenOnboarding,
}) => {
  const [showFactorMenu, setShowFactorMenu] = useState(false);

  // Score styling
  let scoreBadgeColor = 'text-amber-400 bg-amber-500/10 border-amber-500/25';
  let scoreGlow = 'rgba(245, 158, 11, 0.15)';
  if (recoveryScore >= 75) {
    scoreBadgeColor = 'text-emerald-400 bg-emerald-500/10 border-emerald-500/25';
    scoreGlow = 'rgba(16, 185, 129, 0.15)';
  } else if (recoveryScore < 50) {
    scoreBadgeColor = 'text-rose-400 bg-rose-500/10 border-rose-500/25';
    scoreGlow = 'rgba(244, 63, 94, 0.15)';
  }

  return (
    <header className="sticky top-0 z-40 w-full bg-[#080c15]/80 backdrop-blur-xl border-b border-white/[0.06] px-4 sm:px-8 py-3.5 transition-all">
      <div className="max-w-7xl mx-auto flex items-center justify-between gap-4">
        {/* Brand Logo with 3D feel */}
        <div className="flex items-center gap-3">
          <div className="relative flex items-center justify-center w-10 h-10 rounded-2xl bg-gradient-to-br from-indigo-500 via-indigo-600 to-purple-600 shadow-lg shadow-indigo-500/25 border border-white/20 transform-gpu hover:scale-105 transition-all">
            <span className="font-black text-sm text-white tracking-wider">BL</span>
            <div className="absolute -top-1 -right-1 w-2.5 h-2.5 bg-emerald-400 rounded-full border-2 border-[#080c15]" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className="font-extrabold text-lg tracking-tight text-white">
                BackLift<span className="text-indigo-400 font-normal">.AI</span>
              </span>
              <span className="hidden sm:inline-block text-[10px] font-semibold tracking-wider uppercase px-2 py-0.5 rounded-full bg-indigo-500/10 text-indigo-300 border border-indigo-500/20">
                Academic Turnaround
              </span>
            </div>
            <p className="text-[11px] text-slate-400 hidden sm:block">
              Intelligent Recovery & Study Management
            </p>
          </div>
        </div>

        {/* Center / Right Metrics & Quick Actions */}
        <div className="flex items-center gap-2.5 sm:gap-3.5">
          {/* Study Streak */}
          <div className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-slate-900/60 border border-white/[0.07] text-slate-200">
            <Flame className="w-4 h-4 text-amber-500 animate-pulse" />
            <span className="text-xs font-bold text-amber-400">{student.streakDays}</span>
            <span className="text-[11px] text-slate-400 hidden md:inline">Days</span>
          </div>

          {/* Recovery Score Pill */}
          <div className="relative">
            <button
              onClick={() => setShowFactorMenu(!showFactorMenu)}
              className={`flex items-center gap-2 px-3.5 py-1.5 rounded-xl border text-xs font-bold transition-all hover:scale-102 ${scoreBadgeColor}`}
              style={{ boxShadow: `0 4px 20px ${scoreGlow}` }}
            >
              <Award className="w-4 h-4" />
              <span>Score: {recoveryScore}</span>
              <span className="hidden md:inline text-[10px] font-medium opacity-80">• {gradeBadge}</span>
              <ChevronDown className="w-3 h-3 opacity-60 ml-0.5" />
            </button>

            {/* Diagnostic Factor Breakdown Popover */}
            {showFactorMenu && (
              <div className="absolute right-0 mt-3 w-80 sm:w-96 rounded-3xl bg-slate-900/95 backdrop-blur-2xl border border-white/10 p-5 shadow-2xl z-50 animate-in fade-in zoom-in-95 duration-200">
                <div className="flex items-start justify-between gap-2 border-b border-slate-800 pb-3">
                  <div>
                    <h4 className="text-sm font-bold text-white flex items-center gap-2">
                      <Sparkles className="w-4 h-4 text-indigo-400" />
                      Academic Recovery Diagnostic
                    </h4>
                    <p className="text-[11px] text-slate-400 mt-0.5">
                      Multi-factor heuristic analysis of your turnaround status.
                    </p>
                  </div>
                  <button
                    onClick={() => setShowFactorMenu(false)}
                    className="text-xs text-slate-400 hover:text-white p-1"
                  >
                    ✕
                  </button>
                </div>

                <div className="space-y-3.5 my-4">
                  {recoveryFactors.map((factor, idx) => (
                    <div key={idx} className="space-y-1">
                      <div className="flex justify-between text-xs">
                        <span className="font-medium text-slate-300">
                          {factor.label}
                        </span>
                        <span className="font-bold text-indigo-300">
                          {factor.score}/{factor.maxScore}
                        </span>
                      </div>
                      <div className="w-full bg-slate-800 rounded-full h-1.5 overflow-hidden">
                        <div
                          className={`h-full rounded-full transition-all duration-500 ${
                            factor.status === 'positive'
                              ? 'bg-emerald-500'
                              : factor.status === 'warning'
                              ? 'bg-amber-500'
                              : 'bg-rose-500'
                          }`}
                          style={{ width: `${factor.score}%` }}
                        />
                      </div>
                      <p className="text-[10px] text-slate-400">
                        {factor.impactDescription}
                      </p>
                    </div>
                  ))}
                </div>

                <div className="rounded-xl bg-indigo-950/40 border border-indigo-800/40 p-3 text-[11px] text-indigo-200/90 flex gap-2.5">
                  <Info className="w-4 h-4 text-indigo-400 shrink-0 mt-0.5" />
                  <span>
                    <strong>Internal Planning Indicator:</strong> Calibrated to guide study focus, not an official guarantee of passing.
                  </span>
                </div>
              </div>
            )}
          </div>

          {/* Recovery Report Button */}
          <button
            onClick={onOpenReportModal}
            className="hidden sm:flex items-center gap-1.5 px-3 py-1.5 text-xs font-semibold rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white shadow-md shadow-indigo-600/20 transition-all hover:scale-102"
          >
            <FileDown className="w-3.5 h-3.5" />
            <span>Report</span>
          </button>

          {/* Profile / Edit Button */}
          <button
            onClick={onOpenOnboarding}
            className="flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium text-slate-300 hover:text-white bg-slate-900/60 hover:bg-slate-800 border border-white/[0.07] rounded-xl transition"
            title="Edit Profile & Backlogs"
          >
            <User className="w-3.5 h-3.5 text-slate-400" />
            <span className="hidden md:inline">{student.name.split(' ')[0]}</span>
          </button>

          {/* Reset Demo Data Button */}
          <button
            onClick={onResetData}
            className="p-1.5 text-slate-400 hover:text-rose-400 hover:bg-rose-500/10 rounded-xl transition"
            title="Reset Sample Demo Data"
          >
            <RotateCcw className="w-4 h-4" />
          </button>
        </div>
      </div>
    </header>
  );
};
