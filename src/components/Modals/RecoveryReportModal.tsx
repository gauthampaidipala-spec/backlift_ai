import React from 'react';
import {
  Printer,
  Download,
  Award,
  CheckCircle2,
  Calendar,
  AlertTriangle,
  Flame,
} from 'lucide-react';
import { StudentProfile, Backlog, RecoveryFactorBreakdown } from '../../types';

interface RecoveryReportModalProps {
  isOpen: boolean;
  onClose: () => void;
  student: StudentProfile;
  backlogs: Backlog[];
  recoveryScore: number;
  gradeBadge: string;
  factors: RecoveryFactorBreakdown[];
}

export const RecoveryReportModal: React.FC<RecoveryReportModalProps> = ({
  isOpen,
  onClose,
  student,
  backlogs,
  recoveryScore,
  gradeBadge,
  factors,
}) => {
  if (!isOpen) return null;

  const handlePrint = () => {
    window.print();
  };

  const totalTopics = backlogs.reduce((acc, b) => acc + b.topics.length, 0);
  const completedTopics = backlogs.reduce(
    (acc, b) => acc + b.topics.filter((t) => t.isCompleted).length,
    0
  );

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md">
      <div className="w-full max-w-3xl bg-slate-900 border border-slate-800 rounded-3xl p-6 sm:p-8 shadow-2xl space-y-6 max-h-[90vh] overflow-y-auto">
        {/* Modal Actions Header */}
        <div className="flex items-center justify-between border-b border-slate-800 pb-4 print:hidden">
          <div className="flex items-center gap-2">
            <Award className="w-5 h-5 text-indigo-400" />
            <h3 className="text-base font-bold text-white">
              Official Academic Recovery Progress Report
            </h3>
          </div>
          <div className="flex items-center gap-2">
            <button
              onClick={handlePrint}
              className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold shadow-md transition"
            >
              <Printer className="w-3.5 h-3.5" />
              <span>Print / Save as PDF</span>
            </button>
            <button
              onClick={onClose}
              className="p-1.5 rounded-lg text-slate-400 hover:text-white"
            >
              ✕
            </button>
          </div>
        </div>

        {/* Printable Document Sheet */}
        <div className="p-6 bg-slate-950 rounded-2xl border border-slate-800/80 space-y-6 text-slate-200">
          {/* Institution & Logo Header */}
          <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center border-b border-slate-800 pb-4 gap-2">
            <div>
              <div className="text-lg font-black tracking-tight text-white">
                BackLift<span className="text-indigo-400">.AI</span> Academic Turnaround Network
              </div>
              <div className="text-xs text-slate-400">
                Student Recovery Progress & Diagnostic Assessment Sheet
              </div>
            </div>
            <div className="text-right text-xs text-slate-400">
              <div>Generated: {new Date().toLocaleDateString()}</div>
              <div className="text-[10px] text-indigo-400 font-mono">
                REF: BL-REC-{Date.now().toString().slice(-6)}
              </div>
            </div>
          </div>

          {/* Student Profile Overview */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 p-4 rounded-xl bg-slate-900 border border-slate-800 text-xs">
            <div>
              <span className="text-slate-500 block">Student Name</span>
              <strong className="text-white text-sm">{student.name}</strong>
            </div>
            <div>
              <span className="text-slate-500 block">College / Program</span>
              <span className="text-slate-200 font-medium">
                {student.degree} (Sem {student.semester})
              </span>
            </div>
            <div>
              <span className="text-slate-500 block">Total Focus Hours</span>
              <span className="text-emerald-400 font-bold">
                {student.totalHoursStudied} Hours Logged
              </span>
            </div>
            <div>
              <span className="text-slate-500 block">Consistency Streak</span>
              <span className="text-amber-400 font-bold">
                🔥 {student.streakDays} Consecutive Days
              </span>
            </div>
          </div>

          {/* Current Academic Recovery Score Box */}
          <div className="p-5 rounded-2xl bg-gradient-to-r from-indigo-950/40 to-slate-900 border border-indigo-500/30 flex flex-col sm:flex-row items-center justify-between gap-4">
            <div>
              <span className="text-xs font-bold uppercase tracking-wider text-indigo-400">
                Internal Recovery Status
              </span>
              <div className="text-2xl font-black text-white mt-0.5">
                {recoveryScore} / 100 ({gradeBadge})
              </div>
              <p className="text-xs text-slate-400 mt-1">
                Completed {completedTopics} of {totalTopics} syllabus units across all active backlogs.
              </p>
            </div>
            <div className="text-xs text-right max-w-xs text-slate-400 leading-relaxed">
              *Certified internal diagnostic planning indicator to evaluate study milestone attainment.
            </div>
          </div>

          {/* Subject Breakdown Table */}
          <div className="space-y-2">
            <h4 className="text-xs font-bold uppercase tracking-wider text-slate-400">
              Active Backlog Status & Exam Proximity
            </h4>
            <div className="overflow-x-auto">
              <table className="w-full text-xs text-left">
                <thead className="bg-slate-900 text-slate-400 border-b border-slate-800">
                  <tr>
                    <th className="py-2.5 px-3">Subject Name</th>
                    <th className="py-2.5 px-3">Code</th>
                    <th className="py-2.5 px-3">Credits</th>
                    <th className="py-2.5 px-3">Exam Date</th>
                    <th className="py-2.5 px-3">Prep Level</th>
                    <th className="py-2.5 px-3">Status</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-800">
                  {backlogs.map((b) => (
                    <tr key={b.id}>
                      <td className="py-2.5 px-3 font-semibold text-white">
                        {b.subjectName}
                      </td>
                      <td className="py-2.5 px-3 text-slate-400">{b.subjectCode}</td>
                      <td className="py-2.5 px-3 text-slate-300">{b.credits}</td>
                      <td className="py-2.5 px-3 text-amber-300 font-mono">
                        {b.targetExamDate}
                      </td>
                      <td className="py-2.5 px-3 text-emerald-400 font-bold">
                        {b.prepPercentage}%
                      </td>
                      <td className="py-2.5 px-3">
                        <span className="text-[10px] uppercase font-bold text-indigo-400 bg-indigo-950 px-2 py-0.5 rounded">
                          Priority {b.priorityScore}
                        </span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>

          {/* Mentor Signature & Accountability Block */}
          <div className="pt-6 border-t border-slate-800 flex justify-between items-end text-xs text-slate-400">
            <div>
              <div className="w-36 border-b border-slate-700 pb-1 text-slate-300 font-mono">
                {student.name}
              </div>
              <span className="text-[10px] text-slate-500">Student Signature</span>
            </div>

            <div className="text-right">
              <div className="w-44 border-b border-slate-700 pb-1 text-slate-300 font-mono">
                Academic Faculty Mentor
              </div>
              <span className="text-[10px] text-slate-500">Department Advisor Seal</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
