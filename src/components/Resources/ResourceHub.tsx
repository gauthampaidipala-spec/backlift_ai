import React, { useState } from 'react';
import {
  BookOpen,
  Video,
  FileText,
  Star,
  ExternalLink,
  Sparkles,
  Filter,
} from 'lucide-react';
import { Backlog } from '../../types';
import { sampleResources } from '../../data/mockData';

interface ResourceHubProps {
  backlogs: Backlog[];
  weakTopics: string[];
  onNavigateTab: (tab: any) => void;
}

export const ResourceHub: React.FC<ResourceHubProps> = ({
  backlogs,
  weakTopics,
  onNavigateTab,
}) => {
  const [selectedSubjectFilter, setSelectedSubjectFilter] = useState<string>('all');
  const [selectedTypeFilter, setSelectedTypeFilter] = useState<string>('all');

  const filteredResources = sampleResources.filter((res) => {
    if (selectedSubjectFilter !== 'all' && res.subjectCode !== selectedSubjectFilter) {
      return false;
    }
    if (selectedTypeFilter !== 'all' && res.type !== selectedTypeFilter) {
      return false;
    }
    return true;
  });

  return (
    <div className="space-y-8 animate-in fade-in duration-300">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-extrabold text-white flex items-center gap-2">
            <BookOpen className="w-5 h-5 text-emerald-400" />
            Curated Study Resource Hub
          </h2>
          <p className="text-xs text-slate-400 mt-0.5">
            Verified topper handwritten notes, high-yield video lessons, and formula cheat sheets.
          </p>
        </div>

        <button
          onClick={() => onNavigateTab('quizzes')}
          className="flex items-center gap-1.5 px-4 py-2.5 rounded-2xl bg-indigo-600/20 hover:bg-indigo-600/30 text-indigo-300 border border-indigo-500/30 text-xs font-bold transition cursor-pointer"
        >
          <Sparkles className="w-4 h-4 text-indigo-400" />
          <span>Test Knowledge on Resources</span>
        </button>
      </div>

      {/* Weakness Matching Recommendation Banner */}
      {weakTopics.length > 0 && (
        <div className="p-6 rounded-3xl glass-panel border border-emerald-500/25 space-y-3">
          <div className="flex items-center gap-2">
            <Sparkles className="w-4 h-4 text-emerald-400" />
            <h3 className="text-xs font-bold uppercase tracking-wider text-emerald-300">
              Resource Recommendation Engine • Targeted Weakness Fix
            </h3>
          </div>
          <p className="text-xs text-slate-300 leading-relaxed">
            Based on your quiz errors in <strong className="text-amber-300">{weakTopics[0]}</strong>, we prioritized these study materials:
          </p>
          <div className="flex flex-wrap items-center gap-3 pt-1">
            <a
              href="https://example.com/maths2-topper-notes.pdf"
              target="_blank"
              rel="noreferrer"
              className="inline-flex items-center gap-2 px-4 py-2 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-xs font-semibold text-emerald-300 border border-emerald-500/30 transition cursor-pointer"
            >
              <FileText className="w-3.5 h-3.5" />
              <span>Topper Formula Sheet: Convolution Theorem</span>
              <ExternalLink className="w-3 h-3 opacity-70" />
            </a>
            <a
              href="https://youtube.com/watch?v=demo-math-laplace"
              target="_blank"
              rel="noreferrer"
              className="inline-flex items-center gap-2 px-4 py-2 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-xs font-semibold text-purple-300 border border-purple-500/30 transition cursor-pointer"
            >
              <Video className="w-3.5 h-3.5" />
              <span>18-Min Animated Walkthrough</span>
              <ExternalLink className="w-3 h-3 opacity-70" />
            </a>
          </div>
        </div>
      )}

      {/* Filter Tabs */}
      <div className="flex flex-wrap items-center gap-2 border-b border-white/[0.06] pb-4">
        <div className="flex items-center gap-1.5 text-xs text-slate-400 mr-2">
          <Filter className="w-3.5 h-3.5" />
          <span>Filter:</span>
        </div>
        <button
          onClick={() => setSelectedSubjectFilter('all')}
          className={`px-3.5 py-1.5 rounded-xl text-xs font-semibold transition cursor-pointer ${
            selectedSubjectFilter === 'all'
              ? 'bg-indigo-600 text-white shadow-md'
              : 'glass-panel text-slate-400 hover:text-white'
          }`}
        >
          All Subjects
        </button>
        {backlogs.map((b) => (
          <button
            key={b.id}
            onClick={() => setSelectedSubjectFilter(b.subjectCode)}
            className={`px-3.5 py-1.5 rounded-xl text-xs font-semibold transition cursor-pointer ${
              selectedSubjectFilter === b.subjectCode
                ? 'bg-indigo-600 text-white shadow-md'
                : 'glass-panel text-slate-400 hover:text-white'
            }`}
          >
            {b.subjectCode}
          </button>
        ))}

        <div className="h-4 w-px bg-slate-800 mx-2" />
        {['all', 'notes', 'video', 'formula'].map((t) => (
          <button
            key={t}
            onClick={() => setSelectedTypeFilter(t)}
            className={`px-3.5 py-1.5 rounded-xl text-xs font-semibold capitalize transition cursor-pointer ${
              selectedTypeFilter === t
                ? 'bg-emerald-600 text-white shadow-md'
                : 'glass-panel text-slate-400 hover:text-white'
            }`}
          >
            {t === 'all' ? 'All Formats' : t}
          </button>
        ))}
      </div>

      {/* Resources Cards Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
        {filteredResources.map((res) => (
          <div
            key={res.id}
            className="p-6 rounded-3xl glass-panel-interactive flex flex-col justify-between space-y-4 group"
          >
            <div className="space-y-3">
              <div className="flex items-center justify-between">
                <span className="text-[10px] font-bold uppercase tracking-wider text-indigo-400 bg-indigo-950/80 px-2.5 py-0.5 rounded-full border border-indigo-800">
                  {res.subjectCode} • {res.topicTag}
                </span>

                <div className="flex items-center gap-1 text-xs text-amber-400 font-bold">
                  <Star className="w-3.5 h-3.5 fill-amber-400" />
                  <span>{res.rating}</span>
                </div>
              </div>

              <h4 className="text-base font-bold text-white group-hover:text-indigo-300 transition leading-snug">
                {res.title}
              </h4>

              <p className="text-xs text-slate-400">By {res.author}</p>
            </div>

            <div className="pt-3 border-t border-white/[0.06] flex items-center justify-between">
              <div className="flex items-center gap-2 text-xs text-slate-400">
                {res.type === 'video' ? (
                  <Video className="w-4 h-4 text-purple-400" />
                ) : res.type === 'notes' ? (
                  <FileText className="w-4 h-4 text-emerald-400" />
                ) : (
                  <BookOpen className="w-4 h-4 text-amber-400" />
                )}
                <span>{res.meta}</span>
              </div>

              <a
                href={res.url}
                target="_blank"
                rel="noreferrer"
                className="inline-flex items-center gap-1 text-xs font-bold text-indigo-400 hover:text-indigo-300"
              >
                <span>Access</span>
                <ExternalLink className="w-3.5 h-3.5" />
              </a>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
