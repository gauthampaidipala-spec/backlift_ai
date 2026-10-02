import React, { useState, useEffect } from 'react';
import {
  Timer as TimerIcon,
  Play,
  Pause,
  RotateCcw,
  Flame,
  Sparkles,
} from 'lucide-react';
import { Backlog, StudentProfile } from '../../types';
import confetti from 'canvas-confetti';

interface FocusTimerProps {
  student: StudentProfile;
  backlogs: Backlog[];
  onLogStudyMinutes: (minutes: number, subjectCode: string) => void;
}

export const FocusTimer: React.FC<FocusTimerProps> = ({
  student,
  backlogs,
  onLogStudyMinutes,
}) => {
  const [selectedSubjectCode, setSelectedSubjectCode] = useState<string>(
    backlogs[0]?.subjectCode || 'MATH201'
  );
  const [mode, setMode] = useState<'focus' | 'shortBreak' | 'longBreak'>('focus');
  const [timeLeft, setTimeLeft] = useState<number>(25 * 60);
  const [isRunning, setIsRunning] = useState<boolean>(false);
  const [completedSessionsCount, setCompletedSessionsCount] = useState<number>(0);

  const DURATIONS = {
    focus: 25 * 60,
    shortBreak: 5 * 60,
    longBreak: 15 * 60,
  };

  useEffect(() => {
    let interval: any = null;
    if (isRunning && timeLeft > 0) {
      interval = setInterval(() => {
        setTimeLeft((prev) => prev - 1);
      }, 1000);
    } else if (isRunning && timeLeft === 0) {
      setIsRunning(false);
      handleSessionCompleted();
    }
    return () => clearInterval(interval);
  }, [isRunning, timeLeft]);

  const handleSessionCompleted = () => {
    if (mode === 'focus') {
      onLogStudyMinutes(25, selectedSubjectCode);
      setCompletedSessionsCount((c) => c + 1);
      confetti({ particleCount: 70, spread: 70 });
      setMode('shortBreak');
      setTimeLeft(DURATIONS.shortBreak);
    } else {
      setMode('focus');
      setTimeLeft(DURATIONS.focus);
    }
  };

  const handleModeSwitch = (newMode: 'focus' | 'shortBreak' | 'longBreak') => {
    setIsRunning(false);
    setMode(newMode);
    setTimeLeft(DURATIONS[newMode]);
  };

  const handleReset = () => {
    setIsRunning(false);
    setTimeLeft(DURATIONS[mode]);
  };

  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  const totalDuration = DURATIONS[mode];
  const progressRatio = (totalDuration - timeLeft) / totalDuration;
  const radius = 110;
  const circumference = 2 * Math.PI * radius;
  const strokeDashoffset = circumference - progressRatio * circumference;

  return (
    <div className="space-y-8 max-w-4xl mx-auto animate-in fade-in duration-300">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-extrabold text-white flex items-center gap-2">
            <TimerIcon className="w-5 h-5 text-indigo-400" />
            Pomodoro Focus Engine
          </h2>
          <p className="text-xs text-slate-400 mt-0.5">
            Structured 25-minute deep study sprints with zero distraction to overcome backlog procrastination.
          </p>
        </div>

        <div className="flex items-center gap-2 px-3.5 py-1.5 rounded-2xl glass-panel text-xs text-slate-300">
          <Flame className="w-4 h-4 text-amber-500 animate-pulse" />
          <span>
            <strong className="text-white">{completedSessionsCount}</strong> Sprints Finished Today
          </span>
        </div>
      </div>

      {/* Main 3D Zen Timer Card */}
      <div className="relative glass-panel rounded-3xl p-8 sm:p-12 text-center space-y-8 shadow-2xl overflow-hidden border border-white/[0.08]">
        {/* Ambient Glow */}
        <div
          className={`absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-96 h-96 rounded-full blur-3xl -z-10 transition-all duration-700 ${
            mode === 'focus'
              ? 'bg-indigo-600/15'
              : mode === 'shortBreak'
              ? 'bg-emerald-600/15'
              : 'bg-purple-600/15'
          }`}
        />

        {/* Mode Switcher */}
        <div className="inline-flex p-1.5 rounded-2xl bg-slate-900/80 border border-white/[0.06] gap-1 shadow-inner">
          <button
            onClick={() => handleModeSwitch('focus')}
            className={`px-5 py-2 rounded-xl text-xs font-bold transition-all cursor-pointer ${
              mode === 'focus'
                ? 'bg-indigo-600 text-white shadow-lg shadow-indigo-600/30'
                : 'text-slate-400 hover:text-white'
            }`}
          >
            25m Focus Sprint
          </button>
          <button
            onClick={() => handleModeSwitch('shortBreak')}
            className={`px-5 py-2 rounded-xl text-xs font-bold transition-all cursor-pointer ${
              mode === 'shortBreak'
                ? 'bg-emerald-600 text-white shadow-lg shadow-emerald-600/30'
                : 'text-slate-400 hover:text-white'
            }`}
          >
            5m Short Break
          </button>
          <button
            onClick={() => handleModeSwitch('longBreak')}
            className={`px-5 py-2 rounded-xl text-xs font-bold transition-all cursor-pointer ${
              mode === 'longBreak'
                ? 'bg-purple-600 text-white shadow-lg shadow-purple-600/30'
                : 'text-slate-400 hover:text-white'
            }`}
          >
            15m Long Break
          </button>
        </div>

        {/* Tagged Subject Selector */}
        {mode === 'focus' && (
          <div className="space-y-2 max-w-md mx-auto">
            <span className="text-[11px] uppercase font-bold tracking-wider text-slate-400">
              Study Subject Log:
            </span>
            <div className="flex flex-wrap justify-center gap-2">
              {backlogs.map((b) => (
                <button
                  key={b.id}
                  onClick={() => setSelectedSubjectCode(b.subjectCode)}
                  className={`px-3.5 py-1.5 rounded-full text-xs font-semibold border transition-all cursor-pointer ${
                    selectedSubjectCode === b.subjectCode
                      ? 'bg-indigo-600/30 text-indigo-300 border-indigo-500 shadow-sm'
                      : 'bg-slate-900/60 text-slate-400 border-white/[0.06] hover:text-white'
                  }`}
                >
                  {b.subjectCode}
                </button>
              ))}
            </div>
          </div>
        )}

        {/* 3D Circular Clock Dial */}
        <div className="relative w-64 h-64 sm:w-72 sm:h-72 mx-auto flex items-center justify-center">
          <svg className="w-full h-full transform -rotate-90" viewBox="0 0 260 260">
            {/* Background Circle */}
            <circle
              cx="130"
              cy="130"
              r={radius}
              stroke="currentColor"
              strokeWidth="12"
              className="text-slate-800/40"
              fill="transparent"
            />
            {/* Active Progress Circle */}
            <circle
              cx="130"
              cy="130"
              r={radius}
              stroke={
                mode === 'focus' ? '#6366F1' : mode === 'shortBreak' ? '#10B981' : '#A855F7'
              }
              strokeWidth="12"
              strokeDasharray={circumference}
              strokeDashoffset={strokeDashoffset}
              strokeLinecap="round"
              className="transition-all duration-500 ease-out"
              fill="transparent"
            />
          </svg>

          {/* Time Text Center */}
          <div className="absolute flex flex-col items-center justify-center">
            <span className="text-5xl sm:text-6xl font-black text-white tracking-tight font-mono">
              {formatTime(timeLeft)}
            </span>
            <span className="text-xs text-slate-400 mt-2 font-medium">
              {mode === 'focus' ? `Focusing on ${selectedSubjectCode}` : 'Breathe & Rest'}
            </span>
          </div>
        </div>

        {/* Timer Control Buttons */}
        <div className="flex items-center justify-center gap-4">
          <button
            onClick={() => setIsRunning(!isRunning)}
            className={`flex items-center gap-2.5 px-8 py-3.5 rounded-2xl text-xs font-bold transition-all shadow-xl hover:scale-102 cursor-pointer ${
              isRunning
                ? 'bg-slate-800 hover:bg-slate-700 text-amber-400 border border-white/[0.08]'
                : 'bg-indigo-600 hover:bg-indigo-500 text-white shadow-indigo-600/30'
            }`}
          >
            {isRunning ? (
              <>
                <Pause className="w-4 h-4" /> <span>Pause</span>
              </>
            ) : (
              <>
                <Play className="w-4 h-4 fill-white" /> <span>Start Focus</span>
              </>
            )}
          </button>

          <button
            onClick={handleReset}
            className="p-3.5 rounded-2xl bg-slate-800/80 hover:bg-slate-700 text-slate-400 hover:text-white border border-white/[0.06] transition cursor-pointer"
            title="Reset Timer"
          >
            <RotateCcw className="w-4 h-4" />
          </button>
        </div>

        <p className="text-xs text-slate-500 max-w-sm mx-auto">
          "25 minutes of continuous focus on one specific topic dissolves anxiety and restores academic control."
        </p>
      </div>
    </div>
  );
};
