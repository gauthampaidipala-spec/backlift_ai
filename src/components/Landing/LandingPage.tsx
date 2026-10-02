import React, { useState } from 'react';
import {
  Sparkles,
  ArrowRight,
  CheckCircle2,
  Clock,
  Target,
  Zap,
  Award,
  ChevronRight,
  Shield,
  Star,
  Users,
  Layers,
  Flame,
  Bot,
  Calendar,
  FileSearch,
} from 'lucide-react';
import { StudentProfile, Backlog } from '../../types';

interface LandingPageProps {
  student: StudentProfile;
  backlogs: Backlog[];
  onLaunchApp: () => void;
  onOpenLogin: () => void;
}

export const LandingPage: React.FC<LandingPageProps> = ({
  student,
  backlogs,
  onLaunchApp,
  onOpenLogin,
}) => {
  const [selectedCredits, setSelectedCredits] = useState<number>(4);
  const [selectedDays, setSelectedDays] = useState<number>(14);
  const [selectedDifficulty, setSelectedDifficulty] = useState<number>(4);

  // Live in-browser priority calculation preview
  const calculatedPriority = Math.min(
    100,
    Math.round(
      (100 - selectedDays * 2.5) * 0.4 +
        (selectedCredits / 4) * 100 * 0.2 +
        65 * 0.25 +
        (selectedDifficulty / 5) * 100 * 0.15
    )
  );

  return (
    <div className="space-y-16 animate-in fade-in duration-300 pb-16">
      {/* 1. HERO SECTION */}
      <section className="relative overflow-hidden rounded-3xl p-8 sm:p-14 glass-panel border border-white/[0.08] shadow-2xl text-center space-y-6">
        {/* Ambient Glowing Blobs */}
        <div className="absolute -top-24 left-1/2 -translate-x-1/2 w-96 h-96 bg-indigo-600/20 rounded-full blur-3xl -z-10" />
        <div className="absolute bottom-0 right-10 w-80 h-80 bg-cyan-600/15 rounded-full blur-3xl -z-10" />

        <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-indigo-500/10 border border-indigo-500/25 text-indigo-300 text-xs font-bold tracking-wide">
          <Sparkles className="w-4 h-4 text-cyan-400" />
          <span>The #1 Academic Recovery Platform for Higher Education</span>
        </div>

        <h1 className="text-3xl sm:text-5xl lg:text-6xl font-black text-white tracking-tight leading-tight max-w-4xl mx-auto">
          From Backlog Paralysis to{' '}
          <span className="text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 via-cyan-400 to-emerald-400">
            Degree Completion
          </span>
        </h1>

        <p className="text-sm sm:text-base text-slate-300 max-w-2xl mx-auto leading-relaxed">
          The intelligent recovery co-pilot that turns overwhelming multi-semester exam arrears into mathematically organized, achievable daily micro-tasks. Never let a missed day destroy your study plan again.
        </p>

        {/* CTA Button Group */}
        <div className="flex flex-wrap items-center justify-center gap-4 pt-2">
          <button
            onClick={onLaunchApp}
            className="flex items-center gap-2 px-7 py-3.5 rounded-2xl bg-gradient-to-r from-indigo-600 to-cyan-600 hover:from-indigo-500 hover:to-cyan-500 text-white font-bold text-sm shadow-xl shadow-indigo-600/30 transition-all hover:scale-105 cursor-pointer"
          >
            <span>Launch Dashboard (Free Demo)</span>
            <ArrowRight className="w-4 h-4" />
          </button>
          <button
            onClick={onOpenLogin}
            className="px-6 py-3.5 rounded-2xl bg-slate-900/80 hover:bg-slate-800 text-slate-200 font-bold text-sm border border-white/[0.08] transition hover:scale-102 cursor-pointer"
          >
            Sign In with College SSO
          </button>
        </div>

        {/* Real-time Ticker / Social Proof */}
        <div className="pt-8 border-t border-white/[0.06] grid grid-cols-2 sm:grid-cols-4 gap-4 text-center">
          <div>
            <div className="text-2xl font-black text-white">42,000+</div>
            <div className="text-xs text-slate-400">Backlogs Cleared</div>
          </div>
          <div>
            <div className="text-2xl font-black text-emerald-400">89.4%</div>
            <div className="text-xs text-slate-400">Supplementary Pass Rate</div>
          </div>
          <div>
            <div className="text-2xl font-black text-cyan-400">35+</div>
            <div className="text-xs text-slate-400">Engineering Campuses</div>
          </div>
          <div>
            <div className="text-2xl font-black text-amber-400">4.9 / 5.0</div>
            <div className="text-xs text-slate-400">Student Satisfaction</div>
          </div>
        </div>
      </section>

      {/* 2. THE PROBLEM WE SOLVE (COMPARISON SLIDER / CARDS) */}
      <section className="space-y-6">
        <div className="text-center space-y-2">
          <h2 className="text-2xl sm:text-3xl font-extrabold text-white">
            Why Traditional Study Plans Always Fail
          </h2>
          <p className="text-xs sm:text-sm text-slate-400 max-w-xl mx-auto">
            Backlog students don't suffer from lack of intelligence; they suffer from schedule fragility and prioritization blindness.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* Failure Box */}
          <div className="p-6 rounded-3xl glass-panel border border-rose-500/20 space-y-4">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-rose-500/10 text-rose-300 text-xs font-bold">
              <span>✕ The Old Way (Static Timetables)</span>
            </div>
            <ul className="text-xs sm:text-sm text-slate-300 space-y-3">
              <li className="flex items-start gap-2.5">
                <span className="text-rose-400 font-bold shrink-0">•</span>
                <span><strong>Fragile & Rigid:</strong> Missing a single 2-hour study block destroys the entire 30-day timetable, leading to guilt and total abandonment.</span>
              </li>
              <li className="flex items-start gap-2.5">
                <span className="text-rose-400 font-bold shrink-0">•</span>
                <span><strong>Prioritization Blindness:</strong> Studying subjects in alphabetical order instead of weighting by credits and exam proximity.</span>
              </li>
              <li className="flex items-start gap-2.5">
                <span className="text-rose-400 font-bold shrink-0">•</span>
                <span><strong>Information Overload:</strong> Spending 60% of limited time on low-yield textbook chapters that rarely appear in exams.</span>
              </li>
            </ul>
          </div>

          {/* Success Box */}
          <div className="p-6 rounded-3xl glass-panel border border-emerald-500/30 space-y-4 shadow-xl shadow-emerald-500/5">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 text-emerald-300 text-xs font-bold">
              <span>✓ The BackLift AI Way</span>
            </div>
            <ul className="text-xs sm:text-sm text-slate-300 space-y-3">
              <li className="flex items-start gap-2.5">
                <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                <span><strong>1-Click Missed-Day Recovery:</strong> Missed yesterday? The engine smoothly redistributes remaining units across future days without panic.</span>
              </li>
              <li className="flex items-start gap-2.5">
                <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                <span><strong>Algorithmic Priority Index:</strong> Mathematical ranking of urgency based on exam days, credit weight, and attempt counts.</span>
              </li>
              <li className="flex items-start gap-2.5">
                <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                <span><strong>80/20 Past Paper Intelligence:</strong> Highlights high-frequency questions extracted from 10 years of university papers.</span>
              </li>
            </ul>
          </div>
        </div>
      </section>

      {/* 3. INTERACTIVE IN-BROWSER PRIORITY ENGINE DEMO */}
      <section className="p-8 sm:p-10 rounded-3xl glass-panel border border-indigo-500/30 space-y-6">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div>
            <div className="text-xs font-bold uppercase tracking-wider text-cyan-400">
              Interactive Product Preview
            </div>
            <h3 className="text-xl sm:text-2xl font-black text-white mt-1">
              Calculate Your Exam Urgency Score Right Now
            </h3>
            <p className="text-xs text-slate-400">
              Test how our proprietary Backlog Priority Engine dynamically computes your study queue.
            </p>
          </div>
          <div className="p-4 rounded-2xl bg-indigo-950/60 border border-indigo-800/60 text-center shrink-0">
            <div className="text-xs text-slate-400 font-medium">Calculated Priority</div>
            <div className="text-3xl font-black text-cyan-300">{calculatedPriority} / 100</div>
            <div className="text-[10px] font-bold text-amber-300 uppercase mt-0.5">
              {calculatedPriority >= 75 ? 'Critical Urgency' : calculatedPriority >= 50 ? 'Moderate Urgency' : 'Low Urgency'}
            </div>
          </div>
        </div>

        {/* Interactive Sliders */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-6 pt-2">
          <div className="space-y-2">
            <div className="flex justify-between text-xs">
              <span className="font-semibold text-slate-300">Subject Credit Weight</span>
              <span className="font-bold text-indigo-300">{selectedCredits} Credits</span>
            </div>
            <input
              type="range"
              min="1"
              max="5"
              step="1"
              value={selectedCredits}
              onChange={(e) => setSelectedCredits(Number(e.target.value))}
              className="w-full accent-indigo-500 cursor-pointer"
            />
          </div>

          <div className="space-y-2">
            <div className="flex justify-between text-xs">
              <span className="font-semibold text-slate-300">Days Until Supplementary Exam</span>
              <span className="font-bold text-amber-300">{selectedDays} Days</span>
            </div>
            <input
              type="range"
              min="3"
              max="45"
              step="1"
              value={selectedDays}
              onChange={(e) => setSelectedDays(Number(e.target.value))}
              className="w-full accent-amber-500 cursor-pointer"
            />
          </div>

          <div className="space-y-2">
            <div className="flex justify-between text-xs">
              <span className="font-semibold text-slate-300">Subject Difficulty Rating</span>
              <span className="font-bold text-rose-300">{selectedDifficulty} / 5</span>
            </div>
            <input
              type="range"
              min="1"
              max="5"
              step="1"
              value={selectedDifficulty}
              onChange={(e) => setSelectedDifficulty(Number(e.target.value))}
              className="w-full accent-rose-500 cursor-pointer"
            />
          </div>
        </div>

        <div className="text-center pt-2">
          <button
            onClick={onLaunchApp}
            className="inline-flex items-center gap-2 text-xs font-bold text-indigo-400 hover:text-indigo-300 hover:underline cursor-pointer"
          >
            <span>See full customized 7-day study plan inside the dashboard</span>
            <ChevronRight className="w-3.5 h-3.5" />
          </button>
        </div>
      </section>

      {/* 4. FOUR CORE PILLARS SHOWCASE */}
      <section className="space-y-6">
        <div className="text-center space-y-2">
          <h2 className="text-2xl sm:text-3xl font-extrabold text-white">
            Everything You Need to Clear Backlogs
          </h2>
          <p className="text-xs sm:text-sm text-slate-400 max-w-xl mx-auto">
            Engineered with modern pedagogical psychology and deep examination heuristics.
          </p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
          <div className="p-6 rounded-3xl glass-panel border border-white/[0.06] space-y-3">
            <div className="w-10 h-10 rounded-2xl bg-indigo-600/20 text-indigo-400 flex items-center justify-center">
              <Target className="w-5 h-5" />
            </div>
            <h4 className="text-sm font-bold text-white">Priority Engine</h4>
            <p className="text-xs text-slate-400 leading-relaxed">
              Formulaic ranking organizes multiple arrears so you always know what subject to tackle right now.
            </p>
          </div>

          <div className="p-6 rounded-3xl glass-panel border border-white/[0.06] space-y-3">
            <div className="w-10 h-10 rounded-2xl bg-amber-600/20 text-amber-400 flex items-center justify-center">
              <Calendar className="w-5 h-5" />
            </div>
            <h4 className="text-sm font-bold text-white">Missed-Day Rebalancer</h4>
            <p className="text-xs text-slate-400 leading-relaxed">
              Missed a day? 1-click recalculation redistributes tasks across future days without schedule collapse.
            </p>
          </div>

          <div className="p-6 rounded-3xl glass-panel border border-white/[0.06] space-y-3">
            <div className="w-10 h-10 rounded-2xl bg-cyan-600/20 text-cyan-400 flex items-center justify-center">
              <FileSearch className="w-5 h-5" />
            </div>
            <h4 className="text-sm font-bold text-white">Past-Paper Recurrence</h4>
            <p className="text-xs text-slate-400 leading-relaxed">
              Unlocks the 80/20 Pareto rule from 10 years of university papers to focus on recurrent high-mark units.
            </p>
          </div>

          <div className="p-6 rounded-3xl glass-panel border border-white/[0.06] space-y-3">
            <div className="w-10 h-10 rounded-2xl bg-purple-600/20 text-purple-400 flex items-center justify-center">
              <Bot className="w-5 h-5" />
            </div>
            <h4 className="text-sm font-bold text-white">AI LiftBot Tutor</h4>
            <p className="text-xs text-slate-400 leading-relaxed">
              Empathetic 24/7 Socratic mentor simplifies complex math formulas through real-world analogies.
            </p>
          </div>
        </div>
      </section>

      {/* 5. STUDENT TESTIMONIALS */}
      <section className="space-y-6">
        <div className="text-center space-y-2">
          <h2 className="text-2xl sm:text-3xl font-extrabold text-white">
            Real Student Turnaround Stories
          </h2>
          <p className="text-xs sm:text-sm text-slate-400">
            Hear from undergraduates who overcame arrear panic and cleared their placement gates.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="p-6 rounded-3xl glass-panel border border-white/[0.06] space-y-3">
            <div className="flex text-amber-400 text-xs">★★★★★</div>
            <p className="text-xs text-slate-300 leading-relaxed italic">
              "I carried 3 backlogs from Sem 2 & 4. Placement season was starting and I was terrified. BackLift AI gave me an exact daily plan and the missed-day recovery button saved my sanity. Cleared all 3 and got an offer at Infosys!"
            </p>
            <div className="pt-2 border-t border-white/[0.06]">
              <div className="text-xs font-bold text-white">Rahul Sharma</div>
              <div className="text-[10px] text-slate-400">B.Tech CSE, 7th Sem</div>
            </div>
          </div>

          <div className="p-6 rounded-3xl glass-panel border border-white/[0.06] space-y-3">
            <div className="flex text-amber-400 text-xs">★★★★★</div>
            <p className="text-xs text-slate-300 leading-relaxed italic">
              "I failed Engineering Mathematics-II twice. Textbooks were overwhelming. LiftBot explained Laplace Transforms using an audio-equalizer analogy that finally clicked. Scored an A grade in supplementary exams!"
            </p>
            <div className="pt-2 border-t border-white/[0.06]">
              <div className="text-xs font-bold text-white">Priya Patel</div>
              <div className="text-[10px] text-slate-400">B.Tech ECE, 5th Sem</div>
            </div>
          </div>

          <div className="p-6 rounded-3xl glass-panel border border-white/[0.06] space-y-3">
            <div className="flex text-amber-400 text-xs">★★★★★</div>
            <p className="text-xs text-slate-300 leading-relaxed italic">
              "Working a part-time job meant I only had 2 hours a day. The Past-Paper Analyzer showed me the exact 4 theorems that make up 50 marks. Passed Operating Systems with flying colors."
            </p>
            <div className="pt-2 border-t border-white/[0.06]">
              <div className="text-xs font-bold text-white">Arjun Verma</div>
              <div className="text-[10px] text-slate-400">B.Tech Mech, 6th Sem</div>
            </div>
          </div>
        </div>
      </section>

      {/* 6. TRANSPARENT PRICING TABLE */}
      <section className="space-y-6">
        <div className="text-center space-y-2">
          <h2 className="text-2xl sm:text-3xl font-extrabold text-white">
            Affordable Plans Built for Students
          </h2>
          <p className="text-xs sm:text-sm text-slate-400">
            Less than the cost of a single pizza, designed to protect your placement eligibility.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="p-6 rounded-3xl glass-panel border border-white/[0.06] space-y-4">
            <div className="text-xs font-bold uppercase tracking-wider text-slate-400">Free Starter</div>
            <div className="text-3xl font-black text-white">₹0 <span className="text-xs font-normal text-slate-400">/ forever</span></div>
            <ul className="text-xs text-slate-300 space-y-2">
              <li className="flex items-center gap-2"><CheckCircle2 className="w-3.5 h-3.5 text-slate-400" /> Track up to 2 backlogs</li>
              <li className="flex items-center gap-2"><CheckCircle2 className="w-3.5 h-3.5 text-slate-400" /> Basic static timetable</li>
              <li className="flex items-center gap-2"><CheckCircle2 className="w-3.5 h-3.5 text-slate-400" /> 10 AI LiftBot questions/week</li>
            </ul>
            <button onClick={onLaunchApp} className="w-full py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-bold text-white transition">
              Get Started Free
            </button>
          </div>

          <div className="p-6 rounded-3xl glass-panel border border-indigo-500/40 space-y-4 shadow-xl shadow-indigo-600/10 relative">
            <div className="absolute -top-3 right-4 px-2.5 py-0.5 rounded-full bg-indigo-600 text-white text-[10px] font-bold">
              MOST POPULAR
            </div>
            <div className="text-xs font-bold uppercase tracking-wider text-indigo-400">BackLift Pro</div>
            <div className="text-3xl font-black text-indigo-300">₹299 <span className="text-xs font-normal text-slate-400">/ month</span></div>
            <ul className="text-xs text-slate-200 space-y-2">
              <li className="flex items-center gap-2"><CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" /> Unlimited backlog subjects</li>
              <li className="flex items-center gap-2"><CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" /> 1-Click Missed-Day Rebalancer</li>
              <li className="flex items-center gap-2"><CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" /> Past-Paper 80/20 Recurrence</li>
              <li className="flex items-center gap-2"><CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" /> Unlimited AI LiftBot tutoring</li>
            </ul>
            <button onClick={onLaunchApp} className="w-full py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-xs font-bold text-white transition shadow-lg shadow-indigo-600/30">
              Upgrade to Pro
            </button>
          </div>

          <div className="p-6 rounded-3xl glass-panel border border-amber-500/25 space-y-4">
            <div className="text-xs font-bold uppercase tracking-wider text-amber-400">Campus Enterprise</div>
            <div className="text-3xl font-black text-amber-300">$3–$5 <span className="text-xs font-normal text-slate-400">/ student / yr</span></div>
            <ul className="text-xs text-slate-300 space-y-2">
              <li className="flex items-center gap-2"><CheckCircle2 className="w-3.5 h-3.5 text-amber-400" /> Dean & Faculty Retention Portal</li>
              <li className="flex items-center gap-2"><CheckCircle2 className="w-3.5 h-3.5 text-amber-400" /> Batch-wide dropout risk alerts</li>
              <li className="flex items-center gap-2"><CheckCircle2 className="w-3.5 h-3.5 text-amber-400" /> NAAC / NIRF accreditation dossiers</li>
            </ul>
            <button onClick={onLaunchApp} className="w-full py-2.5 rounded-xl bg-amber-600/20 hover:bg-amber-600/30 text-amber-300 border border-amber-500/30 text-xs font-bold transition">
              Request College Pilot
            </button>
          </div>
        </div>
      </section>

      {/* 7. FINAL HIGH-CONVERTING CTA */}
      <section className="p-8 sm:p-12 rounded-3xl glass-panel border border-white/[0.08] text-center space-y-4">
        <h3 className="text-2xl sm:text-3xl font-black text-white">
          Your Degree is Waiting. Stop Freezing, Start Clearing.
        </h3>
        <p className="text-xs sm:text-sm text-slate-300 max-w-lg mx-auto">
          Join thousands of engineering students who turned academic crisis into graduation glory.
        </p>
        <div className="pt-2">
          <button
            onClick={onLaunchApp}
            className="px-8 py-4 rounded-2xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-sm shadow-xl shadow-indigo-600/30 transition-all hover:scale-105 cursor-pointer"
          >
            Launch Your Recovery Dashboard Now
          </button>
        </div>
      </section>
    </div>
  );
};
