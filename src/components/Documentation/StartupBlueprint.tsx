import React, { useState } from 'react';
import {
  Briefcase,
  FileText,
  Target,
  Layers,
  Sparkles,
  DollarSign,
  Cpu,
  Mic,
  Presentation,
  CheckCircle2,
} from 'lucide-react';

export const StartupBlueprint: React.FC = () => {
  const [activeSection, setActiveSection] = useState<'pitch' | 'features' | 'architecture' | 'business' | 'script'>('pitch');

  return (
    <div className="space-y-8 animate-in fade-in duration-300">
      {/* Top Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center gap-2">
            <h2 className="text-xl font-extrabold text-white flex items-center gap-2">
              <Briefcase className="w-5 h-5 text-cyan-400" />
              BackLift AI: Startup Concept Blueprint & Pitch Deck
            </h2>
            <span className="text-[10px] font-bold uppercase tracking-wider text-cyan-400 bg-cyan-400/10 px-2.5 py-0.5 rounded-full border border-cyan-400/20">
              Final Defense Ready
            </span>
          </div>
          <p className="text-xs text-slate-400 mt-0.5">
            Complete startup documentation covering all 20 deliverables requested for the college evaluation and internship defense.
          </p>
        </div>

        {/* Section Navigation Tabs */}
        <div className="flex flex-wrap items-center gap-1.5 p-1 rounded-2xl glass-panel">
          <button
            onClick={() => setActiveSection('pitch')}
            className={`px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer flex items-center gap-1.5 ${
              activeSection === 'pitch'
                ? 'bg-cyan-600 text-white shadow-md shadow-cyan-600/20'
                : 'text-slate-400 hover:text-white'
            }`}
          >
            <Presentation className="w-3.5 h-3.5" />
            <span>Pitch & UVP</span>
          </button>
          <button
            onClick={() => setActiveSection('features')}
            className={`px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer flex items-center gap-1.5 ${
              activeSection === 'features'
                ? 'bg-cyan-600 text-white shadow-md shadow-cyan-600/20'
                : 'text-slate-400 hover:text-white'
            }`}
          >
            <Layers className="w-3.5 h-3.5" />
            <span>30-Feature Matrix</span>
          </button>
          <button
            onClick={() => setActiveSection('architecture')}
            className={`px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer flex items-center gap-1.5 ${
              activeSection === 'architecture'
                ? 'bg-cyan-600 text-white shadow-md shadow-cyan-600/20'
                : 'text-slate-400 hover:text-white'
            }`}
          >
            <Cpu className="w-3.5 h-3.5" />
            <span>AI & DB Arch</span>
          </button>
          <button
            onClick={() => setActiveSection('business')}
            className={`px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer flex items-center gap-1.5 ${
              activeSection === 'business'
                ? 'bg-cyan-600 text-white shadow-md shadow-cyan-600/20'
                : 'text-slate-400 hover:text-white'
            }`}
          >
            <DollarSign className="w-3.5 h-3.5" />
            <span>Business & GTM</span>
          </button>
          <button
            onClick={() => setActiveSection('script')}
            className={`px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer flex items-center gap-1.5 ${
              activeSection === 'script'
                ? 'bg-cyan-600 text-white shadow-md shadow-cyan-600/20'
                : 'text-slate-400 hover:text-white'
            }`}
          >
            <Mic className="w-3.5 h-3.5" />
            <span>Pitch Scripts</span>
          </button>
        </div>
      </div>

      {/* Section 1: Pitch & UVP */}
      {activeSection === 'pitch' && (
        <div className="space-y-6">
          <div className="p-8 rounded-3xl glass-panel space-y-4">
            <span className="text-xs font-bold uppercase tracking-wider text-cyan-400">
              Startup Vision & Value Proposition
            </span>
            <h3 className="text-xl sm:text-2xl font-extrabold text-white leading-snug">
              "From Backlog Paralysis to Degree Completion: The personalized AI recovery operating system that turns overwhelming exam backlogs into achievable daily micro-actions."
            </h3>
            <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
              BackLift AI is engineered for the 35%+ of university undergraduates who carry uncleared backlogs, repeat examinations, or multi-subject cognitive burnout. By merging algorithmic prioritization with resilient study scheduling and non-judgmental AI coaching, BackLift AI rescues students from academic crisis and guides them across the graduation stage.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="p-6 rounded-3xl glass-panel space-y-3">
              <h4 className="text-sm font-bold text-white flex items-center gap-2">
                <Target className="w-4 h-4 text-rose-400" />
                The Backlog Paralysis Cycle
              </h4>
              <ul className="text-xs text-slate-300 space-y-2 list-disc list-inside leading-relaxed">
                <li>Prioritization paralysis: Not knowing which paper to study first.</li>
                <li>Timetable collapse: Missing one day triggers guilt and abandonment.</li>
                <li>Information scattering: Notes and solved papers lost across Telegram.</li>
                <li>Shame and isolation: Fear of approaching mentors or peers.</li>
              </ul>
            </div>

            <div className="p-6 rounded-3xl glass-panel space-y-3">
              <h4 className="text-sm font-bold text-white flex items-center gap-2">
                <Sparkles className="w-4 h-4 text-emerald-400" />
                The BackLift AI Solution
              </h4>
              <ul className="text-xs text-slate-300 space-y-2 list-disc list-inside leading-relaxed">
                <li><strong>Backlog Priority Engine</strong>: Formulaic ranking of urgency.</li>
                <li><strong>Missed-Day Recovery Engine</strong>: Automatic rescheduling.</li>
                <li><strong>Past-Paper Analyzer</strong>: High-frequency unit mapping.</li>
                <li><strong>Ethical Recovery Score</strong>: Internal planning diagnostics.</li>
              </ul>
            </div>
          </div>
        </div>
      )}

      {/* Section 2: 30-Feature Matrix */}
      {activeSection === 'features' && (
        <div className="glass-panel rounded-3xl p-6 sm:p-8 space-y-5">
          <div className="border-b border-white/[0.06] pb-4">
            <h3 className="text-base font-bold text-white">
              Complete 30-Feature Functional Matrix
            </h3>
            <p className="text-xs text-slate-400 mt-0.5">
              10 Core Functional Modules + 20 High-Value Unique Differentiators
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
            {[
              '1. Central Recovery Dashboard with Diagnostic ARS',
              '2. Backlog Priority Engine (Algorithmic Ranking)',
              '3. Interactive Backlog CRUD Manager with Credit Weights',
              '4. AI Adaptive Study Planner (Daily Hour Allocation)',
              '5. Missed-Day Recovery Engine (Schedule Rebalancer)',
              '6. AI Academic Recovery Chatbot (LiftBot)',
              '7. AI Concept Explanation Mode (Simple Analogies)',
              '8. Ask From My Notes (Contextual Student Q&A)',
              '9. Internal Academic Recovery Score (0-100 Diagnostic)',
              '10. Recovery Factor Breakdown (Transparency Explanations)',
              '11. Important Topic Analyzer (Frequency Heuristics)',
              '12. Previous Paper Frequency Graph & Unit Weights',
              '13. Curated Study Resource Hub (Topper Notes & Formulae)',
              '14. Resource Recommendation Engine (Weakness Matching)',
              '15. AI Diagnostic Quiz Generator (MCQs with Rationales)',
              '16. Weak Topic Detector (Automated Error Categorization)',
              '17. AI Revision Quiz (Pre-Exam Spaced Repetition)',
              '18. Pomodoro Focus Timer (25m Deep Work Sessions)',
              '19. Study Streak & Consistency Tracker (Gamified Habits)',
              '20. Recovery Milestones & Celebration Animations',
              '21. Exam Countdown Clocks (Days Remaining Meter)',
              '22. Smart Revision Mode (72h High-Yield Sprints)',
              '23. Personalized Daily Study Goals (Actionable Checklists)',
              '24. Exam Readiness Heatmap (Unit Mastery Percentages)',
              '25. Subject Difficulty vs. Credit Stakes Map',
              '26. Study Buddy Peer Lobbies (Repeat Examination Rooms)',
              '27. Study Buddy Matcher (Course & Syllabus Pairing)',
              '28. Proactive Contextual Study Notification System',
              '29. Academic Recovery Progress Report (Exportable PDF)',
              '30. Institutional Campus Dean Analytics Portal (B2B SaaS)',
            ].map((feat, idx) => (
              <div
                key={idx}
                className="p-3.5 rounded-2xl bg-slate-800/40 border border-white/[0.06] flex items-center gap-2.5 text-slate-200"
              >
                <CheckCircle2 className="w-4 h-4 text-cyan-400 shrink-0" />
                <span>{feat}</span>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Section 3: AI & Database Architecture */}
      {activeSection === 'architecture' && (
        <div className="space-y-6">
          <div className="p-6 sm:p-8 rounded-3xl glass-panel space-y-5">
            <h3 className="text-base font-bold text-white flex items-center gap-2">
              <Cpu className="w-4 h-4 text-indigo-400" />
              Algorithmic Formulation & AI Workflow
            </h3>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-5 text-xs">
              <div className="p-5 rounded-2xl bg-slate-950/60 border border-white/[0.06] space-y-2.5">
                <span className="font-bold text-indigo-300">
                  1. Backlog Priority Index Formula
                </span>
                <p className="font-mono text-slate-300 bg-slate-900/80 p-3 rounded-xl border border-white/[0.06]">
                  Priority = (Urgency × 0.40) + (Credits × 0.20) + (PrepGap × 0.25) + (Difficulty × 0.15)
                </p>
                <p className="text-slate-400 text-xs leading-relaxed">
                  Prioritizes near exams with high credit weight and low preparation. Multiplies by 1.12 for repeat attempts.
                </p>
              </div>

              <div className="p-5 rounded-2xl bg-slate-950/60 border border-white/[0.06] space-y-2.5">
                <span className="font-bold text-indigo-300">
                  2. Academic Recovery Score (ARS)
                </span>
                <p className="font-mono text-slate-300 bg-slate-900/80 p-3 rounded-xl border border-white/[0.06]">
                  ARS = (AvgPrep × 0.35) + (QuizAvg × 0.25) + (Streak × 0.20) + (Cushion × 0.20)
                </p>
                <p className="text-slate-400 text-xs leading-relaxed">
                  Clearly framed as an internal diagnostic planning metric, never an official exam passing guarantee.
                </p>
              </div>
            </div>
          </div>

          <div className="p-6 sm:p-8 rounded-3xl glass-panel space-y-4">
            <h3 className="text-base font-bold text-white flex items-center gap-2">
              <FileText className="w-4 h-4 text-cyan-400" />
              Relational Database Entities (PostgreSQL 3NF)
            </h3>
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 text-xs">
              {[
                { name: 'STUDENTS', desc: 'Auth, streak, hours, profile' },
                { name: 'BACKLOGS', desc: 'Credits, attempt#, exam date' },
                { name: 'TOPICS', desc: 'Units, frequency weights, status' },
                { name: 'STUDY_PLANS', desc: 'Daily time slots, completion' },
                { name: 'QUIZ_ATTEMPTS', desc: 'Scores, weak concept tags' },
                { name: 'STUDY_SESSIONS', desc: 'Pomodoro tagged focus mins' },
                { name: 'STUDY_GROUPS', desc: 'Peer lobbies, member rosters' },
                { name: 'PAST_PAPERS', desc: 'Exam questions, mark weights' },
              ].map((ent, i) => (
                <div key={i} className="p-4 rounded-2xl bg-slate-800/40 border border-white/[0.06]">
                  <span className="font-bold text-cyan-300 block">{ent.name}</span>
                  <span className="text-xs text-slate-400 mt-1 block">{ent.desc}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* Section 4: Business Model & Revenue */}
      {activeSection === 'business' && (
        <div className="space-y-6">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="p-6 rounded-3xl glass-panel space-y-4">
              <span className="text-xs font-bold uppercase tracking-wider text-slate-400">
                B2C Student Freemium
              </span>
              <div className="text-3xl font-black text-white">Free Forever</div>
              <ul className="text-xs text-slate-300 space-y-2 list-disc list-inside leading-relaxed">
                <li>Track up to 2 active backlogs</li>
                <li>Static timetable generator</li>
                <li>10 AI chatbot questions / week</li>
                <li>Standard resource library</li>
              </ul>
            </div>

            <div className="p-6 rounded-3xl glass-panel border border-indigo-500/30 space-y-4 shadow-xl shadow-indigo-600/10">
              <span className="text-xs font-bold uppercase tracking-wider text-indigo-400">
                BackLift Pro (B2C)
              </span>
              <div className="text-3xl font-black text-indigo-300">
                ₹299 / $4.99 <span className="text-xs font-normal text-slate-400">/ mo</span>
              </div>
              <ul className="text-xs text-slate-200 space-y-2 list-disc list-inside leading-relaxed">
                <li>Unlimited backlog subjects</li>
                <li>Missed-Day Recovery Engine</li>
                <li>Unlimited AI Chatbot & Ask My Notes</li>
                <li>Past Paper Frequency Analyzer</li>
                <li>Unlimited AI Quizzes & Weakness Detector</li>
              </ul>
            </div>

            <div className="p-6 rounded-3xl glass-panel border border-amber-500/25 space-y-4">
              <span className="text-xs font-bold uppercase tracking-wider text-amber-400">
                BackLift Campus (B2B SaaS)
              </span>
              <div className="text-3xl font-black text-amber-300">
                $2 to $5 <span className="text-xs font-normal text-slate-400">/ student / yr</span>
              </div>
              <ul className="text-xs text-slate-300 space-y-2 list-disc list-inside leading-relaxed">
                <li>Institutional Faculty/Dean portal</li>
                <li>Batch-wide dropout risk alerts</li>
                <li>Departmental bottleneck subject metrics</li>
                <li>Accreditation compliance dossiers (NAAC)</li>
              </ul>
            </div>
          </div>
        </div>
      )}

      {/* Section 5: Presentation Scripts */}
      {activeSection === 'script' && (
        <div className="space-y-6">
          <div className="p-8 rounded-3xl glass-panel space-y-4">
            <div className="flex items-center gap-2">
              <Mic className="w-5 h-5 text-cyan-400" />
              <h3 className="text-base font-bold text-white">
                2-Minute Elevator Startup Pitch (Speaking Script)
              </h3>
            </div>
            <div className="p-5 rounded-2xl bg-slate-950/60 border border-white/[0.06] text-xs sm:text-sm text-slate-300 leading-relaxed space-y-3">
              <p>
                "Respected judges and professors: over 35% of undergraduate engineering and professional students carry uncleared academic backlogs. When a student fails a paper, they don't just lose marks—they lose confidence. They suffer from the <strong>Backlog Paralysis Cycle</strong>: overwhelmed by multiple subjects, their study timetables collapse after 48 hours, and they freeze."
              </p>
              <p>
                "That is why we built <strong>BackLift AI</strong>. Instead of empty to-do apps, our proprietary <strong>Backlog Priority Engine</strong> mathematically organizes what to study today based on exam urgency, credits, and past attempts. If a student misses a day, our <strong>Missed-Day Recovery Engine</strong> smoothly redistributes remaining topics without panic."
              </p>
              <p>
                "We analyze historical question papers to highlight high-frequency topics, generate instant diagnostic quizzes, flag weak concepts automatically, and provide an empathetic 24/7 AI tutor. With a high-margin freemium B2C model and a B2B campus portal for university retention, BackLift AI is lifting students out of backlogs and back onto the graduation stage."
              </p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
