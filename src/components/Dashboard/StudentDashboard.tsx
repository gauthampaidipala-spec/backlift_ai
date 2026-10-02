import React from 'react';
import {
  Calendar,
  Clock,
  AlertTriangle,
  Sparkles,
  ArrowRight,
  CheckCircle2,
  Timer,
  Zap,
  Flame,
  Award,
} from 'lucide-react';
import { StudentProfile, Backlog, RecoveryFactorBreakdown, StudyPlanItem } from '../../types';

interface StudentDashboardProps {
  student: StudentProfile;
  backlogs: Backlog[];
  recoveryScore: number;
  gradeBadge: string;
  factors: RecoveryFactorBreakdown[];
  todaysPlan: StudyPlanItem[];
  weakTopics: string[];
  onNavigateTab: (tab: any) => void;
  onTogglePlanItem: (itemId: string) => void;
  onTriggerMissedDay: () => void;
}

export const StudentDashboard: React.FC<StudentDashboardProps> = ({
  student,
  backlogs,
  recoveryScore,
  gradeBadge,
  todaysPlan,
  weakTopics,
  onNavigateTab,
  onTogglePlanItem,
  onTriggerMissedDay,
}) => {
  const sortedBacklogs = [...backlogs].sort((a, b) => b.priorityScore - a.priorityScore);
  const highestPriority = sortedBacklogs[0];

  const today = new Date();
  const nearestBacklog = [...backlogs].sort(
    (a, b) => new Date(a.targetExamDate).getTime() - new Date(b.targetExamDate).getTime()
  )[0];

  let daysToNearestExam = 0;
  if (nearestBacklog) {
    const diff = new Date(nearestBacklog.targetExamDate).getTime() - today.getTime();
    daysToNearestExam = Math.max(1, Math.ceil(diff / (1000 * 60 * 60 * 24)));
  }

  // Study progress today
  const completedToday = todaysPlan.filter((p) => p.isCompleted).length;
  const totalToday = todaysPlan.length;
  const todayPercentage = totalToday > 0 ? Math.round((completedToday / totalToday) * 100) : 0;

  // SVG Gauge calculations
  const radius = 64;
  const circumference = 2 * Math.PI * radius;
  const strokeDashoffset = circumference - (recoveryScore / 100) * circumference;

  return (
    <div className="space-y-8 animate-in fade-in duration-300">
      {/* 1. Hero 3D Turnaround Card with Circular Score Dial */}
      <div className="relative overflow-hidden rounded-3xl glass-panel p-6 sm:p-8 border border-white/[0.08] shadow-2xl">
        {/* Ambient Gradient Glows */}
        <div className="absolute top-0 right-0 w-96 h-96 bg-indigo-600/15 rounded-full blur-3xl -z-10" />
        <div className="absolute bottom-0 left-1/3 w-80 h-80 bg-purple-600/10 rounded-full blur-3xl -z-10" />

        <div className="flex flex-col lg:flex-row items-center justify-between gap-8">
          {/* Left Text & Priority Recommendation */}
          <div className="space-y-4 max-w-xl text-left">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/10 border border-indigo-500/25 text-indigo-300 text-xs font-bold tracking-wide">
              <Sparkles className="w-3.5 h-3.5 text-indigo-400" />
              <span>Academic Recovery Turnaround</span>
            </div>

            <div className="space-y-1">
              <h1 className="text-2xl sm:text-3xl font-black text-white tracking-tight">
                Welcome back, {student.name.split(' ')[0]}
              </h1>
              <p className="text-sm text-slate-400 leading-relaxed">
                Your personalized recovery roadmap is active. Staying consistent today moves you into the exam safe zone.
              </p>
            </div>

            {highestPriority && (
              <div className="p-4 rounded-2xl bg-white/[0.03] border border-white/[0.06] space-y-2">
                <div className="flex items-center gap-2">
                  <span className="w-2 h-2 rounded-full bg-amber-400 animate-pulse" />
                  <span className="text-[11px] font-bold uppercase tracking-wider text-amber-300">
                    Highest Priority Focus Today
                  </span>
                </div>
                <div className="text-sm font-extrabold text-white">
                  {highestPriority.subjectName} ({highestPriority.subjectCode})
                </div>
                <p className="text-xs text-slate-400">
                  Target Exam in <strong className="text-slate-200">{daysToNearestExam} days</strong> •{' '}
                  <strong className="text-indigo-300">{highestPriority.credits} Credits</strong> • Current Preparation is at{' '}
                  <strong className="text-emerald-400">{highestPriority.prepPercentage}%</strong>.
                </p>
              </div>
            )}

            <div className="flex flex-wrap gap-3 pt-1">
              <button
                onClick={() => onNavigateTab('timer')}
                className="flex items-center gap-2 px-5 py-2.5 rounded-2xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold shadow-lg shadow-indigo-600/30 transition-all hover:scale-102 cursor-pointer"
              >
                <Timer className="w-4 h-4" />
                <span>Start 25m Focus Session</span>
              </button>
              <button
                onClick={() => onNavigateTab('chatbot')}
                className="flex items-center gap-2 px-5 py-2.5 rounded-2xl bg-slate-800/80 hover:bg-slate-700 text-slate-200 text-xs font-bold border border-white/[0.08] transition cursor-pointer"
              >
                <Sparkles className="w-4 h-4 text-purple-400" />
                <span>Ask AI Coach</span>
              </button>
            </div>
          </div>

          {/* Right: 3D Circular Recovery Gauge */}
          <div className="relative flex flex-col items-center justify-center p-6 rounded-3xl bg-slate-950/40 border border-white/[0.06] shadow-xl shrink-0">
            <div className="relative w-44 h-44 flex items-center justify-center">
              <svg className="w-full h-full transform -rotate-90" viewBox="0 0 160 160">
                {/* Background Ring */}
                <circle
                  cx="80"
                  cy="80"
                  r={radius}
                  stroke="currentColor"
                  strokeWidth="12"
                  className="text-slate-800/60"
                  fill="transparent"
                />
                {/* Active Progress Ring with Gradient */}
                <circle
                  cx="80"
                  cy="80"
                  r={radius}
                  stroke="url(#scoreGradient)"
                  strokeWidth="12"
                  strokeDasharray={circumference}
                  strokeDashoffset={strokeDashoffset}
                  strokeLinecap="round"
                  className="transition-all duration-1000 ease-out"
                  fill="transparent"
                />
                <defs>
                  <linearGradient id="scoreGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stopColor="#6366F1" />
                    <stop offset="50%" stopColor="#8B5CF6" />
                    <stop offset="100%" stopColor="#10B981" />
                  </linearGradient>
                </defs>
              </svg>

              {/* Center Content */}
              <div className="absolute flex flex-col items-center justify-center text-center">
                <span className="text-[10px] uppercase font-bold text-slate-400 tracking-wider">
                  Recovery
                </span>
                <span className="text-4xl font-black text-white tracking-tight my-0.5">
                  {recoveryScore}
                </span>
                <span className="text-[10px] font-bold text-indigo-300 bg-indigo-500/10 px-2 py-0.5 rounded-full border border-indigo-500/20">
                  {gradeBadge}
                </span>
              </div>
            </div>

            <div className="mt-4 text-center">
              <span className="text-xs font-semibold text-slate-300">
                Turnaround Diagnostic
              </span>
              <p className="text-[10px] text-slate-500 mt-0.5">
                Internal planning indicator
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* 2. Key Metric Stat Cards (3 Spacious Cards) */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
        {/* Card 1: Nearest Exam */}
        <div className="glass-panel-interactive p-6 rounded-3xl space-y-3">
          <div className="flex items-center justify-between text-slate-400">
            <span className="text-xs font-bold uppercase tracking-wider">Nearest Exam</span>
            <Calendar className="w-4 h-4 text-amber-400" />
          </div>
          <div className="flex items-baseline gap-2">
            <span className="text-3xl font-black text-amber-400">{daysToNearestExam}</span>
            <span className="text-xs font-bold text-slate-300">Days Remaining</span>
          </div>
          <div className="text-xs text-slate-300 font-semibold truncate">
            {nearestBacklog ? nearestBacklog.subjectName : 'No pending papers'}
          </div>
          <div className="w-full bg-slate-800/80 rounded-full h-1.5 overflow-hidden">
            <div
              className="h-full bg-amber-400 rounded-full"
              style={{ width: `${Math.min(100, Math.max(15, 100 - daysToNearestExam * 2))}%` }}
            />
          </div>
        </div>

        {/* Card 2: Today's Target */}
        <div className="glass-panel-interactive p-6 rounded-3xl space-y-3">
          <div className="flex items-center justify-between text-slate-400">
            <span className="text-xs font-bold uppercase tracking-wider">Today's Focus</span>
            <Clock className="w-4 h-4 text-emerald-400" />
          </div>
          <div className="flex items-baseline gap-2">
            <span className="text-3xl font-black text-emerald-400">{completedToday}</span>
            <span className="text-xs font-bold text-slate-300">/ {totalToday} Sprints Completed</span>
          </div>
          <div className="flex justify-between text-xs text-slate-400">
            <span>Target: {student.dailyStudyHours} hrs/day</span>
            <span className="font-semibold text-emerald-400">{todayPercentage}% Done</span>
          </div>
          <div className="w-full bg-slate-800/80 rounded-full h-1.5 overflow-hidden">
            <div
              className="h-full bg-emerald-500 rounded-full transition-all duration-700"
              style={{ width: `${todayPercentage}%` }}
            />
          </div>
        </div>

        {/* Card 3: Active Backlogs */}
        <div className="glass-panel-interactive p-6 rounded-3xl space-y-3">
          <div className="flex items-center justify-between text-slate-400">
            <span className="text-xs font-bold uppercase tracking-wider">Active Backlogs</span>
            <AlertTriangle className="w-4 h-4 text-rose-400" />
          </div>
          <div className="flex items-baseline gap-2">
            <span className="text-3xl font-black text-rose-400">{backlogs.length}</span>
            <span className="text-xs font-bold text-slate-300">Pending Subjects</span>
          </div>
          <div className="text-xs text-slate-400 flex items-center justify-between">
            <span>{backlogs.filter(b => b.status === 'critical').length} Urgent Attention</span>
            <button
              onClick={() => onNavigateTab('backlogs')}
              className="text-indigo-400 hover:text-indigo-300 font-bold"
            >
              Manage →
            </button>
          </div>
          <div className="w-full bg-slate-800/80 rounded-full h-1.5 overflow-hidden">
            <div
              className="h-full bg-indigo-500 rounded-full"
              style={{ width: `${Math.min(100, backlogs.length * 25)}%` }}
            />
          </div>
        </div>
      </div>

      {/* 3. Clean Two-Column Layout: Today's Action Checklist vs Backlog Priority Overview */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
        {/* Left 7 Columns: Today's Focus Sprint */}
        <div className="lg:col-span-7 space-y-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2.5">
              <Zap className="w-4 h-4 text-amber-400" />
              <h3 className="text-base font-extrabold text-white">Today's Study Action Sprint</h3>
            </div>
            <div className="flex items-center gap-2">
              <button
                onClick={onTriggerMissedDay}
                className="px-3 py-1.5 text-xs font-bold rounded-xl bg-amber-500/10 hover:bg-amber-500/20 text-amber-300 border border-amber-500/30 transition flex items-center gap-1.5 cursor-pointer"
                title="Automatically rebalance missed schedule over future days"
              >
                🔄 Missed Yesterday?
              </button>
              <button
                onClick={() => onNavigateTab('planner')}
                className="text-xs font-bold text-indigo-400 hover:text-indigo-300 flex items-center gap-1 cursor-pointer"
              >
                Calendar
                <ArrowRight className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>

          <div className="space-y-3">
            {todaysPlan.length === 0 ? (
              <div className="p-8 rounded-3xl glass-panel text-center text-xs text-slate-400">
                No study tasks scheduled for today. Generate an adaptive plan in the Study Planner.
              </div>
            ) : (
              todaysPlan.map((item) => (
                <div
                  key={item.id}
                  className={`p-4 rounded-2xl border transition-all flex items-center justify-between gap-4 ${
                    item.isCompleted
                      ? 'bg-slate-900/30 border-white/[0.04] opacity-50'
                      : 'glass-panel hover:border-indigo-500/30'
                  }`}
                >
                  <div className="flex items-center gap-3.5">
                    <button
                      onClick={() => onTogglePlanItem(item.id)}
                      className={`w-6 h-6 rounded-lg flex items-center justify-center border transition cursor-pointer ${
                        item.isCompleted
                          ? 'bg-emerald-500 border-emerald-500 text-slate-950 font-bold'
                          : 'border-slate-600 hover:border-indigo-400'
                      }`}
                    >
                      {item.isCompleted && <CheckCircle2 className="w-4 h-4" />}
                    </button>
                    <div>
                      <div className="flex items-center gap-2">
                        <span className="text-xs font-bold text-white">
                          {item.subjectName}
                        </span>
                        <span className="text-[10px] text-slate-400 bg-slate-800/80 px-2 py-0.5 rounded-full">
                          {item.timeSlot}
                        </span>
                        {item.isRescheduled && (
                          <span className="text-[9px] font-bold text-amber-400 bg-amber-400/10 px-1.5 py-0.5 rounded border border-amber-400/20">
                            Rebalanced
                          </span>
                        )}
                      </div>
                      <p className="text-xs text-slate-300 mt-1 font-medium">
                        {item.topicTitle} ({item.allocatedMinutes} mins)
                      </p>
                    </div>
                  </div>

                  <div className="flex items-center gap-2">
                    <button
                      onClick={() => onNavigateTab('timer')}
                      className="p-2 rounded-xl text-slate-400 hover:text-indigo-400 hover:bg-slate-800 transition cursor-pointer"
                      title="Launch timer for this task"
                    >
                      <Timer className="w-4 h-4" />
                    </button>
                  </div>
                </div>
              ))
            )}
          </div>
        </div>

        {/* Right 5 Columns: Backlog Priority Triage & Weak Topics */}
        <div className="lg:col-span-5 space-y-6">
          <div className="space-y-3">
            <div className="flex items-center justify-between">
              <h3 className="text-base font-extrabold text-white flex items-center gap-2">
                <AlertTriangle className="w-4 h-4 text-amber-400" />
                Priority Backlogs
              </h3>
              <button
                onClick={() => onNavigateTab('backlogs')}
                className="text-xs font-bold text-indigo-400 hover:text-indigo-300 cursor-pointer"
              >
                All ({backlogs.length})
              </button>
            </div>

            <div className="space-y-3">
              {sortedBacklogs.slice(0, 3).map((b) => (
                <div
                  key={b.id}
                  className="p-4 rounded-2xl glass-panel space-y-2.5"
                >
                  <div className="flex items-start justify-between gap-2">
                    <div>
                      <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400">
                        {b.subjectCode} • {b.credits} Credits • Sem {b.semester}
                      </span>
                      <h4 className="text-xs font-bold text-white mt-0.5">
                        {b.subjectName}
                      </h4>
                    </div>
                    <span
                      className={`text-[9px] font-bold px-2 py-0.5 rounded-full border ${
                        b.status === 'critical'
                          ? 'bg-rose-500/15 text-rose-300 border-rose-500/30'
                          : b.status === 'high'
                          ? 'bg-amber-500/15 text-amber-300 border-amber-500/30'
                          : 'bg-emerald-500/15 text-emerald-300 border-emerald-500/30'
                      }`}
                    >
                      Priority {b.priorityScore}
                    </span>
                  </div>

                  <div className="space-y-1">
                    <div className="flex justify-between text-[11px]">
                      <span className="text-slate-400">Preparation</span>
                      <span className="font-semibold text-slate-200">{b.prepPercentage}%</span>
                    </div>
                    <div className="w-full bg-slate-800 rounded-full h-1.5 overflow-hidden">
                      <div
                        className="h-full bg-indigo-500 rounded-full transition-all duration-500"
                        style={{ width: `${b.prepPercentage}%` }}
                      />
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Weak Topic Detector Widget */}
          <div className="p-5 rounded-3xl glass-panel space-y-3 border border-amber-500/20">
            <div className="flex items-center justify-between">
              <span className="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <AlertTriangle className="w-3.5 h-3.5" />
                Weak Topic Detector
              </span>
              <span className="text-[10px] text-slate-400 font-semibold">AI Diagnostic</span>
            </div>
            <p className="text-xs text-slate-400 leading-relaxed">
              Auto-flagged from recent quizzes & attempt logs:
            </p>
            <div className="space-y-2 pt-1">
              {weakTopics.slice(0, 3).map((topic, i) => (
                <div
                  key={i}
                  className="p-2.5 rounded-xl bg-amber-500/10 border border-amber-500/20 text-xs text-amber-200 flex items-center justify-between gap-2"
                >
                  <span className="truncate">⚠️ {topic}</span>
                  <button
                    onClick={() => onNavigateTab('chatbot')}
                    className="text-[10px] font-bold text-indigo-400 hover:text-indigo-300 whitespace-nowrap cursor-pointer"
                  >
                    Explain →
                  </button>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
