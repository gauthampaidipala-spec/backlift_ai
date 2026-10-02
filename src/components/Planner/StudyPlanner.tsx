import React, { useState } from 'react';
import {
  Calendar as CalendarIcon,
  RotateCcw,
  Sparkles,
  CheckCircle2,
  Clock,
  AlertCircle,
  Zap,
  Filter,
} from 'lucide-react';
import { StudyPlanItem, Backlog, StudentProfile } from '../../types';
import { generateAdaptiveStudyPlan, rebalanceMissedDayPlan } from '../../services/priorityEngine';
import confetti from 'canvas-confetti';

interface StudyPlannerProps {
  plan: StudyPlanItem[];
  backlogs: Backlog[];
  student: StudentProfile;
  onUpdatePlan: (newPlan: StudyPlanItem[]) => void;
  onToggleItem: (id: string) => void;
  onNavigateTab: (tab: any) => void;
}

export const StudyPlanner: React.FC<StudyPlannerProps> = ({
  plan,
  backlogs,
  student,
  onUpdatePlan,
  onToggleItem,
  onNavigateTab,
}) => {
  const [selectedDateFilter, setSelectedDateFilter] = useState<string>('all');
  const [smartRevisionMode, setSmartRevisionMode] = useState<boolean>(false);
  const [showMissedModal, setShowMissedModal] = useState<boolean>(false);
  const [missedDateInput, setMissedDateInput] = useState<string>(
    new Date(Date.now() - 24 * 60 * 60 * 1000).toISOString().split('T')[0]
  );
  const [rebalanceAlert, setRebalanceAlert] = useState<string | null>(null);

  const uniqueDates = Array.from(new Set(plan.map((p) => p.date))).sort();

  const handleRegeneratePlan = () => {
    const fresh = generateAdaptiveStudyPlan(backlogs, student.dailyStudyHours);
    onUpdatePlan(fresh);
    confetti({ particleCount: 50, spread: 60 });
  };

  const handleMissedDaySubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const { updatedPlan, rescheduledCount } = rebalanceMissedDayPlan(
      plan,
      missedDateInput
    );

    if (rescheduledCount > 0) {
      onUpdatePlan(updatedPlan);
      setRebalanceAlert(
        `Successfully rebalanced ${rescheduledCount} missed topics across your upcoming days without overloading daily hours!`
      );
      confetti({ particleCount: 60, spread: 70 });
    } else {
      setRebalanceAlert(
        `No incomplete topics were found on ${missedDateInput}. Your schedule is already on track!`
      );
    }
    setShowMissedModal(false);
  };

  const filteredPlan = plan.filter((item) => {
    if (selectedDateFilter === 'all') return true;
    return item.date === selectedDateFilter;
  });

  return (
    <div className="space-y-8 animate-in fade-in duration-300">
      {/* Top Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-extrabold text-white flex items-center gap-2">
            <CalendarIcon className="w-5 h-5 text-indigo-400" />
            AI Adaptive Study Planner
          </h2>
          <p className="text-xs text-slate-400 mt-0.5">
            Syllabus-balanced daily study timetables calibrated to your {student.dailyStudyHours} available daily hours.
          </p>
        </div>

        <div className="flex flex-wrap items-center gap-3">
          <button
            onClick={() => setSmartRevisionMode(!smartRevisionMode)}
            className={`flex items-center gap-2 px-4 py-2 rounded-2xl text-xs font-bold border transition-all cursor-pointer ${
              smartRevisionMode
                ? 'bg-purple-600/25 border-purple-500 text-purple-300 shadow-md shadow-purple-600/20'
                : 'glass-panel text-slate-400 hover:text-white'
            }`}
          >
            <Zap className="w-3.5 h-3.5 text-purple-400" />
            <span>Smart Revision {smartRevisionMode ? 'ON' : 'OFF'}</span>
          </button>

          <button
            onClick={() => setShowMissedModal(true)}
            className="flex items-center gap-1.5 px-4 py-2 rounded-2xl bg-amber-500/15 hover:bg-amber-500/25 text-amber-300 border border-amber-500/30 text-xs font-bold transition hover:scale-102 cursor-pointer"
          >
            <RotateCcw className="w-3.5 h-3.5" />
            <span>Missed-Day Recovery</span>
          </button>

          <button
            onClick={handleRegeneratePlan}
            className="flex items-center gap-1.5 px-4 py-2 rounded-2xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold shadow-lg shadow-indigo-600/20 transition hover:scale-102 cursor-pointer"
          >
            <Sparkles className="w-3.5 h-3.5" />
            <span>Recalibrate</span>
          </button>
        </div>
      </div>

      {/* Alert Notification */}
      {rebalanceAlert && (
        <div className="p-4 rounded-2xl bg-indigo-950/60 border border-indigo-500/30 text-xs text-indigo-200 flex items-start justify-between gap-3 animate-in fade-in">
          <div className="flex items-center gap-2">
            <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
            <span>{rebalanceAlert}</span>
          </div>
          <button
            onClick={() => setRebalanceAlert(null)}
            className="text-indigo-400 hover:text-white cursor-pointer"
          >
            ✕
          </button>
        </div>
      )}

      {/* Date Filter Pills */}
      <div className="flex items-center gap-2 overflow-x-auto pb-1">
        <Filter className="w-3.5 h-3.5 text-slate-500 shrink-0" />
        <button
          onClick={() => setSelectedDateFilter('all')}
          className={`px-3.5 py-1.5 rounded-xl text-xs font-semibold whitespace-nowrap transition cursor-pointer ${
            selectedDateFilter === 'all'
              ? 'bg-indigo-600 text-white shadow-md'
              : 'glass-panel text-slate-400 hover:text-white'
          }`}
        >
          All 7 Days Sprint
        </button>
        {uniqueDates.map((dateStr) => {
          const dateObj = new Date(dateStr);
          const dayName = dateObj.toLocaleDateString('en-US', { weekday: 'short' });
          const isToday = dateStr === new Date().toISOString().split('T')[0];

          return (
            <button
              key={dateStr}
              onClick={() => setSelectedDateFilter(dateStr)}
              className={`px-3.5 py-1.5 rounded-xl text-xs font-semibold whitespace-nowrap transition cursor-pointer ${
                selectedDateFilter === dateStr
                  ? 'bg-indigo-600 text-white shadow-md'
                  : 'glass-panel text-slate-400 hover:text-white'
              }`}
            >
              {dayName} ({dateStr.slice(5)}) {isToday && '• Today'}
            </button>
          );
        })}
      </div>

      {/* Schedule Items List */}
      <div className="space-y-3.5">
        {filteredPlan.length === 0 ? (
          <div className="p-10 rounded-3xl glass-panel text-center text-slate-400">
            No study sessions found for this date.
          </div>
        ) : (
          filteredPlan.map((item) => (
            <div
              key={item.id}
              className={`p-5 rounded-3xl border transition-all flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 ${
                item.isCompleted
                  ? 'bg-slate-900/30 border-white/[0.04] opacity-50'
                  : 'glass-panel hover:border-indigo-500/30'
              }`}
            >
              <div className="flex items-start sm:items-center gap-4">
                <button
                  onClick={() => onToggleItem(item.id)}
                  className={`w-6 h-6 rounded-lg flex items-center justify-center border mt-0.5 sm:mt-0 transition cursor-pointer ${
                    item.isCompleted
                      ? 'bg-emerald-500 border-emerald-500 text-slate-950 font-bold'
                      : 'border-slate-600 hover:border-indigo-400'
                  }`}
                  title={item.isCompleted ? 'Mark uncompleted' : 'Mark completed'}
                >
                  {item.isCompleted && <CheckCircle2 className="w-4 h-4" />}
                </button>

                <div>
                  <div className="flex flex-wrap items-center gap-2">
                    <span className="text-xs font-bold text-white">
                      {item.subjectName}
                    </span>
                    <span className="text-[10px] font-semibold text-indigo-400 bg-indigo-950/80 border border-indigo-800/80 px-2 py-0.5 rounded-full">
                      {item.timeSlot}
                    </span>
                    <span className="text-[10px] text-slate-400 bg-slate-800 px-2 py-0.5 rounded-full">
                      {item.date}
                    </span>
                    {item.isRescheduled && (
                      <span className="text-[9px] font-bold text-amber-400 bg-amber-400/10 px-2 py-0.5 rounded border border-amber-400/20">
                        🔄 Rebalanced Task
                      </span>
                    )}
                  </div>
                  <h4 className={`text-sm font-semibold mt-1 ${item.isCompleted ? 'line-through text-slate-500' : 'text-slate-200'}`}>
                    {item.topicTitle}
                  </h4>
                  <div className="text-xs text-slate-400 mt-1 flex items-center gap-2">
                    <Clock className="w-3.5 h-3.5" />
                    <span>Duration: {item.allocatedMinutes} mins Focus Session</span>
                  </div>
                </div>
              </div>

              <div className="flex items-center gap-2.5 self-end sm:self-center">
                <button
                  onClick={() => onNavigateTab('timer')}
                  className="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold transition cursor-pointer"
                >
                  Launch Timer
                </button>
                <button
                  onClick={() => onNavigateTab('chatbot')}
                  className="px-4 py-2 rounded-xl bg-indigo-600/20 hover:bg-indigo-600/30 text-indigo-300 border border-indigo-500/20 text-xs font-semibold transition cursor-pointer"
                >
                  Explain
                </button>
              </div>
            </div>
          ))
        )}
      </div>

      {/* Missed-Day Recovery Modal */}
      {showMissedModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md">
          <div className="w-full max-w-md glass-panel rounded-3xl p-6 sm:p-8 shadow-2xl space-y-5 border border-white/10">
            <div className="flex justify-between items-center border-b border-white/[0.06] pb-3">
              <h3 className="text-base font-bold text-white flex items-center gap-2">
                <RotateCcw className="w-4 h-4 text-amber-400" />
                Missed-Day Recovery Engine
              </h3>
              <button
                onClick={() => setShowMissedModal(false)}
                className="text-xs text-slate-400 hover:text-white cursor-pointer"
              >
                ✕
              </button>
            </div>

            <p className="text-xs text-slate-300 leading-relaxed">
              Did personal emergencies, sickness, or exhaustion cause you to miss a day?
              <strong> Do not panic or abandon your timetable.</strong> BackLift AI will redistribute your unstudied topics smoothly across your remaining schedule.
            </p>

            <form onSubmit={handleMissedDaySubmit} className="space-y-4 pt-1">
              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-1">
                  Which Date Did You Miss?
                </label>
                <input
                  type="date"
                  required
                  value={missedDateInput}
                  onChange={(e) => setMissedDateInput(e.target.value)}
                  className="w-full bg-slate-800/80 border border-slate-700 rounded-xl px-3.5 py-2 text-sm text-white focus:outline-none focus:border-amber-400"
                />
              </div>

              <div className="p-3.5 rounded-2xl bg-amber-500/10 border border-amber-500/20 text-xs text-amber-300 flex items-start gap-2.5">
                <AlertCircle className="w-4 h-4 shrink-0 mt-0.5" />
                <span>
                  The rebalancing algorithm compresses missed sessions into 60-minute recovery blocks spread across future days to keep daily load sustainable.
                </span>
              </div>

              <div className="flex justify-end gap-3 pt-2 border-t border-white/[0.06]">
                <button
                  type="button"
                  onClick={() => setShowMissedModal(false)}
                  className="px-4 py-2 text-xs font-semibold text-slate-400 hover:text-white cursor-pointer"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-5 py-2 text-xs font-bold text-slate-950 bg-amber-400 hover:bg-amber-300 rounded-xl shadow-lg shadow-amber-400/20 transition cursor-pointer"
                >
                  Execute Rebalancing
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
