import React, { useState } from 'react';
import {
  Upload,
  TrendingUp,
  AlertCircle,
  Sparkles,
  BookOpen,
} from 'lucide-react';
import { pastPapersData } from '../../data/mockData';

interface PaperAnalyzerProps {
  onNavigateTab: (tab: any) => void;
}

export const PaperAnalyzer: React.FC<PaperAnalyzerProps> = ({ onNavigateTab }) => {
  const [selectedPaperId, setSelectedPaperId] = useState<string>(pastPapersData[0].id);
  const [isAnalyzingCustom, setIsAnalyzingCustom] = useState(false);
  const [uploadedFileName, setUploadedFileName] = useState<string | null>(null);

  const selectedPaper =
    pastPapersData.find((p) => p.id === selectedPaperId) || pastPapersData[0];

  const handleSimulatedUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setUploadedFileName(e.target.files[0].name);
      setIsAnalyzingCustom(true);
      setTimeout(() => {
        setIsAnalyzingCustom(false);
      }, 1000);
    }
  };

  return (
    <div className="space-y-8 animate-in fade-in duration-300">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-extrabold text-white flex items-center gap-2">
            <TrendingUp className="w-5 h-5 text-indigo-400" />
            Important Topic & Past-Paper Analyzer
          </h2>
          <p className="text-xs text-slate-400 mt-0.5">
            Heuristic question frequency analysis across historical university exam sessions.
          </p>
        </div>

        {/* Ethical Disclaimer Badge */}
        <div className="px-4 py-2 rounded-2xl bg-amber-500/10 border border-amber-500/25 text-xs text-amber-300 flex items-center gap-2.5">
          <AlertCircle className="w-4 h-4 shrink-0" />
          <span>
            <strong>Guidance Indicator:</strong> Pattern analysis for revision prioritization, not a guarantee of exam questions.
          </span>
        </div>
      </div>

      {/* Select Paper / Upload Area */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-5">
        {pastPapersData.map((paper) => (
          <div
            key={paper.id}
            onClick={() => setSelectedPaperId(paper.id)}
            className={`p-6 rounded-3xl border cursor-pointer transition-all ${
              selectedPaperId === paper.id
                ? 'bg-slate-900/90 border-indigo-500 shadow-xl shadow-indigo-500/10 ring-1 ring-indigo-500/50'
                : 'glass-panel hover:border-white/10'
            }`}
          >
            <span className="text-[10px] font-bold uppercase tracking-wider text-indigo-400">
              {paper.subjectCode}
            </span>
            <h4 className="text-base font-bold text-white mt-1">{paper.subjectName}</h4>
            <div className="text-xs text-slate-400 mt-1">{paper.sessionYear}</div>
            <div className="mt-4 text-xs font-semibold text-emerald-400">
              ✓ {paper.keyTopics.length} Core Recurring Topics Mapped
            </div>
          </div>
        ))}

        {/* Custom Upload Paper Dropzone */}
        <label className="p-6 rounded-3xl border border-dashed border-slate-700/80 hover:border-indigo-400 bg-slate-900/30 hover:bg-slate-900/60 cursor-pointer transition-all flex flex-col items-center justify-center text-center space-y-2 group">
          <Upload className="w-7 h-7 text-slate-400 group-hover:text-indigo-400 transition" />
          <div>
            <div className="text-sm font-bold text-slate-200">Upload University Paper</div>
            <div className="text-xs text-slate-400">PDF, JPG or DOCX</div>
          </div>
          <input
            type="file"
            accept=".pdf,.png,.jpg,.jpeg,.doc,.docx"
            onChange={handleSimulatedUpload}
            className="hidden"
          />
          {uploadedFileName && (
            <span className="text-xs text-indigo-300 font-semibold truncate max-w-[200px]">
              {uploadedFileName}
            </span>
          )}
        </label>
      </div>

      {isAnalyzingCustom && (
        <div className="p-4 rounded-2xl bg-indigo-950/60 border border-indigo-500/30 text-xs text-indigo-300 flex items-center gap-3 animate-pulse">
          <Sparkles className="w-4 h-4 text-indigo-400" />
          <span>Analyzing uploaded examination questions, grouping recurring terms, and calculating frequency weights...</span>
        </div>
      )}

      {/* Topics Frequency Breakdown & Visual Bars */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
        {/* Left: Topic Frequency Table & Graph (7 Cols) */}
        <div className="lg:col-span-7 glass-panel rounded-3xl p-6 sm:p-8 space-y-5">
          <div className="flex items-center justify-between border-b border-white/[0.06] pb-4">
            <div>
              <h3 className="text-base font-bold text-white flex items-center gap-2">
                <TrendingUp className="w-4 h-4 text-emerald-400" />
                Recurring Topic Frequency Distribution
              </h3>
              <p className="text-xs text-slate-400 mt-0.5">
                Evaluated against {selectedPaper.sessionYear}
              </p>
            </div>
            <span className="text-xs font-bold text-indigo-400 bg-indigo-950/80 px-3 py-1 rounded-xl border border-indigo-800">
              {selectedPaper.totalMarks} Total Marks
            </span>
          </div>

          <div className="space-y-4">
            {selectedPaper.keyTopics.map((topicItem, idx) => (
              <div key={idx} className="space-y-2">
                <div className="flex items-center justify-between text-xs">
                  <div className="flex items-center gap-2.5">
                    <span className="w-6 h-6 rounded-lg bg-slate-800 flex items-center justify-center text-xs font-bold text-slate-300">
                      {idx + 1}
                    </span>
                    <span className="font-semibold text-slate-200">
                      {topicItem.topic}
                    </span>
                  </div>
                  <div className="flex items-center gap-2">
                    <span className="text-xs text-amber-400 font-bold">
                      ~{topicItem.averageMarks} Marks
                    </span>
                    <span
                      className={`text-[10px] font-bold px-2.5 py-0.5 rounded-full ${
                        topicItem.frequencyScore >= 90
                          ? 'bg-emerald-500/20 text-emerald-300'
                          : 'bg-indigo-500/20 text-indigo-300'
                      }`}
                    >
                      {topicItem.frequencyScore}% Recurrence
                    </span>
                  </div>
                </div>

                {/* Frequency Bar */}
                <div className="w-full bg-slate-800/80 rounded-full h-2 overflow-hidden">
                  <div
                    className={`h-full rounded-full transition-all duration-700 ${
                      topicItem.frequencyScore >= 90
                        ? 'bg-gradient-to-r from-emerald-500 to-teal-400'
                        : 'bg-gradient-to-r from-indigo-500 to-purple-500'
                    }`}
                    style={{ width: `${topicItem.frequencyScore}%` }}
                  />
                </div>

                <div className="flex justify-between text-[11px] text-slate-400 px-1">
                  <span>Unit {topicItem.unit}</span>
                  <span>Appeared in {topicItem.recurrenceCount} of last 5 papers</span>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Right: Sample Question Bank (5 Cols) */}
        <div className="lg:col-span-5 glass-panel rounded-3xl p-6 sm:p-8 space-y-5">
          <div className="border-b border-white/[0.06] pb-4">
            <h3 className="text-base font-bold text-white flex items-center gap-2">
              <BookOpen className="w-4 h-4 text-purple-400" />
              Verified Repeated Exam Questions
            </h3>
            <p className="text-xs text-slate-400 mt-0.5">
              Exact question patterns repeatedly set by university examiners.
            </p>
          </div>

          <div className="space-y-3.5">
            {selectedPaper.sampleQuestions.map((q, qIdx) => (
              <div
                key={qIdx}
                className="p-4 rounded-2xl bg-slate-800/40 border border-white/[0.06] space-y-2"
              >
                <div className="text-[10px] font-bold uppercase tracking-wider text-indigo-400">
                  Repeated Question #{qIdx + 1}
                </div>
                <p className="text-xs text-slate-200 leading-relaxed font-mono">
                  {q}
                </p>
              </div>
            ))}
          </div>

          <div className="pt-2 flex flex-col gap-2.5">
            <button
              onClick={() => onNavigateTab('resources')}
              className="w-full py-3 rounded-2xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold transition shadow-lg shadow-indigo-600/20 cursor-pointer"
            >
              View Solved Answers in Resource Hub
            </button>
            <button
              onClick={() => onNavigateTab('quizzes')}
              className="w-full py-2.5 rounded-2xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold transition cursor-pointer"
            >
              Take Quiz on These High-Yield Topics
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
