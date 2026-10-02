import React, { useState } from 'react';
import {
  HelpCircle,
  CheckCircle2,
  XCircle,
  Sparkles,
  RotateCcw,
  AlertTriangle,
  Award,
  ArrowRight,
} from 'lucide-react';
import { QuizQuestion, QuizAttempt, Backlog } from '../../types';
import { sampleQuizQuestions } from '../../data/mockData';
import confetti from 'canvas-confetti';

interface QuizGeneratorProps {
  backlogs: Backlog[];
  weakTopics: string[];
  onSaveAttempt: (attempt: QuizAttempt) => void;
  onAddWeakTopic: (topic: string) => void;
  onNavigateTab: (tab: any) => void;
}

export const QuizGenerator: React.FC<QuizGeneratorProps> = ({
  backlogs,
  weakTopics,
  onSaveAttempt,
  onAddWeakTopic,
  onNavigateTab,
}) => {
  const [selectedSubject, setSelectedSubject] = useState<string>('MATH201');
  const [selectedDifficulty, setSelectedDifficulty] = useState<'easy' | 'medium' | 'hard'>('medium');
  const [isQuizActive, setIsQuizActive] = useState<boolean>(false);
  const [currentQuestionIdx, setCurrentQuestionIdx] = useState<number>(0);
  const [selectedAnswers, setSelectedAnswers] = useState<number[]>([]);
  const [isFinished, setIsFinished] = useState<boolean>(false);

  const questions: QuizQuestion[] = sampleQuizQuestions.filter(
    (q) => q.subjectCode === selectedSubject
  ).length > 0
    ? sampleQuizQuestions.filter((q) => q.subjectCode === selectedSubject)
    : sampleQuizQuestions;

  const handleStartQuiz = () => {
    setIsQuizActive(true);
    setCurrentQuestionIdx(0);
    setSelectedAnswers([]);
    setIsFinished(false);
  };

  const handleSelectOption = (optionIdx: number) => {
    if (selectedAnswers[currentQuestionIdx] !== undefined) return;
    const updated = [...selectedAnswers];
    updated[currentQuestionIdx] = optionIdx;
    setSelectedAnswers(updated);
  };

  const handleNextQuestion = () => {
    if (currentQuestionIdx < questions.length - 1) {
      setCurrentQuestionIdx(currentQuestionIdx + 1);
    } else {
      handleFinishQuiz();
    }
  };

  const handleFinishQuiz = () => {
    setIsFinished(true);

    let correctCount = 0;
    const identifiedWeak: string[] = [];

    questions.forEach((q, idx) => {
      if (selectedAnswers[idx] === q.correctIndex) {
        correctCount++;
      } else {
        const weakLabel = `${q.topic} (${q.subjectCode})`;
        identifiedWeak.push(weakLabel);
        onAddWeakTopic(weakLabel);
      }
    });

    const attempt: QuizAttempt = {
      id: `attempt-${Date.now()}`,
      subjectCode: selectedSubject,
      subjectName: backlogs.find((b) => b.subjectCode === selectedSubject)?.subjectName || selectedSubject,
      topic: questions[0]?.topic || 'Core Units Revision',
      score: correctCount,
      totalQuestions: questions.length,
      weakConcepts: identifiedWeak,
      attemptedAt: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    };

    onSaveAttempt(attempt);

    if (correctCount / questions.length >= 0.7) {
      confetti({ particleCount: 70, spread: 80 });
    }
  };

  const currentQ = questions[currentQuestionIdx];
  const hasAnsweredCurrent = selectedAnswers[currentQuestionIdx] !== undefined;
  const currentSelection = selectedAnswers[currentQuestionIdx];

  return (
    <div className="space-y-8 animate-in fade-in duration-300">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-extrabold text-white flex items-center gap-2">
            <HelpCircle className="w-5 h-5 text-indigo-400" />
            AI Diagnostic Quiz & Weak Topic Detector
          </h2>
          <p className="text-xs text-slate-400 mt-0.5">
            Targeted active recall testing with automated cognitive weakness calibration.
          </p>
        </div>

        <div className="flex items-center gap-2 px-4 py-2 rounded-2xl bg-amber-500/10 border border-amber-500/25 text-xs font-semibold text-amber-300">
          <AlertTriangle className="w-4 h-4" />
          <span>{weakTopics.length} Weak Concepts Flagged</span>
        </div>
      </div>

      {!isQuizActive ? (
        /* Configuration Screen */
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
          <div className="lg:col-span-7 glass-panel rounded-3xl p-6 sm:p-8 space-y-6">
            <div>
              <h3 className="text-base font-bold text-white flex items-center gap-2">
                <Sparkles className="w-4 h-4 text-purple-400" />
                Configure Diagnostic Session
              </h3>
              <p className="text-xs text-slate-400 mt-0.5">
                Questions are synthesized based on historical university exam question styles.
              </p>
            </div>

            <div className="space-y-5">
              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-2">
                  Select Backlog Subject
                </label>
                <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                  {backlogs.map((b) => (
                    <button
                      key={b.id}
                      type="button"
                      onClick={() => setSelectedSubject(b.subjectCode)}
                      className={`p-4 rounded-2xl border text-left transition cursor-pointer ${
                        selectedSubject === b.subjectCode
                          ? 'bg-indigo-600/20 border-indigo-500 text-white shadow-md shadow-indigo-600/20'
                          : 'bg-slate-900/60 border-white/[0.06] text-slate-400 hover:border-slate-600'
                      }`}
                    >
                      <div className="text-[10px] font-bold uppercase tracking-wider text-indigo-400">
                        {b.subjectCode}
                      </div>
                      <div className="text-xs font-bold text-slate-200 mt-1 truncate">
                        {b.subjectName}
                      </div>
                    </button>
                  ))}
                </div>
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-2">
                  Target Difficulty
                </label>
                <div className="grid grid-cols-3 gap-3">
                  {(['easy', 'medium', 'hard'] as const).map((diff) => (
                    <button
                      key={diff}
                      type="button"
                      onClick={() => setSelectedDifficulty(diff)}
                      className={`py-2.5 rounded-xl text-xs font-bold capitalize border transition cursor-pointer ${
                        selectedDifficulty === diff
                          ? 'bg-indigo-600 text-white border-indigo-500 shadow-md'
                          : 'bg-slate-900/60 border-white/[0.06] text-slate-400 hover:text-white'
                      }`}
                    >
                      {diff}
                    </button>
                  ))}
                </div>
              </div>

              <div className="p-4 rounded-2xl bg-indigo-950/40 border border-indigo-800/40 text-xs text-slate-300 flex items-start gap-3">
                <Sparkles className="w-5 h-5 text-indigo-400 shrink-0 mt-0.5" />
                <div>
                  <strong className="text-white">Active Weak Topic Calibration:</strong>
                  <p className="text-slate-400 mt-0.5">
                    Any incorrect question answers automatically update your <strong>Weak Topic Detector</strong> and recommend corresponding video/notes in the Resource Hub.
                  </p>
                </div>
              </div>
            </div>

            <button
              onClick={handleStartQuiz}
              className="w-full py-4 rounded-2xl bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-500 hover:to-purple-500 text-white text-xs font-bold shadow-xl shadow-indigo-600/30 transition hover:scale-102 flex items-center justify-center gap-2 cursor-pointer"
            >
              <span>Launch Diagnostic Quiz ({questions.length} Questions)</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          </div>

          {/* Right Column: Detected Weak Topics */}
          <div className="lg:col-span-5 glass-panel rounded-3xl p-6 sm:p-8 space-y-4">
            <div className="flex items-center justify-between border-b border-white/[0.06] pb-4">
              <h3 className="text-base font-bold text-white flex items-center gap-2">
                <AlertTriangle className="w-4 h-4 text-amber-400" />
                Detected Weak Areas
              </h3>
              <span className="text-xs text-slate-400">Needs Practice</span>
            </div>

            {weakTopics.length === 0 ? (
              <div className="p-8 text-center text-xs text-slate-400">
                No weak concepts flagged yet! Take a diagnostic quiz to calibrate.
              </div>
            ) : (
              <div className="space-y-3">
                {weakTopics.map((topic, idx) => (
                  <div
                    key={idx}
                    className="p-3.5 rounded-2xl bg-slate-800/40 border border-amber-500/20 flex items-center justify-between gap-3 text-xs"
                  >
                    <span className="text-amber-200 font-medium">⚠️ {topic}</span>
                    <button
                      onClick={() => onNavigateTab('chatbot')}
                      className="text-xs text-indigo-400 hover:text-indigo-300 font-bold whitespace-nowrap cursor-pointer"
                    >
                      Explain →
                    </button>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      ) : !isFinished && currentQ ? (
        /* Quiz Active Runner Screen */
        <div className="max-w-2xl mx-auto glass-panel rounded-3xl p-6 sm:p-10 space-y-6 shadow-2xl">
          <div className="flex items-center justify-between text-xs">
            <span className="font-bold text-indigo-400">
              Question {currentQuestionIdx + 1} of {questions.length}
            </span>
            <span className="text-slate-400 uppercase tracking-wider text-[10px] bg-slate-800/80 px-2.5 py-0.5 rounded-full">
              {currentQ.topic}
            </span>
          </div>

          <div className="w-full bg-slate-800 rounded-full h-1.5 overflow-hidden">
            <div
              className="h-full bg-indigo-500 rounded-full transition-all duration-300"
              style={{
                width: `${((currentQuestionIdx + 1) / questions.length) * 100}%`,
              }}
            />
          </div>

          <h3 className="text-base sm:text-lg font-bold text-white leading-relaxed">
            {currentQ.question}
          </h3>

          <div className="space-y-3">
            {currentQ.options.map((option, optIdx) => {
              const isSelected = currentSelection === optIdx;
              const isCorrect = currentQ.correctIndex === optIdx;

              let optionStyle = 'bg-slate-800/40 border-white/[0.06] text-slate-200 hover:border-slate-500';
              if (hasAnsweredCurrent) {
                if (isCorrect) {
                  optionStyle = 'bg-emerald-950/40 border-emerald-500 text-emerald-200 font-semibold';
                } else if (isSelected) {
                  optionStyle = 'bg-rose-950/40 border-rose-500 text-rose-200 font-semibold';
                } else {
                  optionStyle = 'bg-slate-900/40 border-transparent text-slate-500';
                }
              }

              return (
                <button
                  key={optIdx}
                  type="button"
                  onClick={() => handleSelectOption(optIdx)}
                  className={`w-full p-4 rounded-2xl border text-left text-xs sm:text-sm transition-all flex items-center justify-between gap-3 cursor-pointer ${optionStyle}`}
                >
                  <span>{option}</span>
                  {hasAnsweredCurrent && (
                    <span>
                      {isCorrect ? (
                        <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
                      ) : isSelected ? (
                        <XCircle className="w-4 h-4 text-rose-400 shrink-0" />
                      ) : null}
                    </span>
                  )}
                </button>
              );
            })}
          </div>

          {hasAnsweredCurrent && (
            <div className="p-4 rounded-2xl bg-indigo-950/40 border border-indigo-800/40 text-xs text-indigo-200 space-y-1 animate-in fade-in">
              <strong className="text-white flex items-center gap-1.5">
                <Sparkles className="w-3.5 h-3.5 text-indigo-400" />
                Examiner Rationale:
              </strong>
              <p className="text-slate-300 leading-relaxed">{currentQ.explanation}</p>
            </div>
          )}

          {hasAnsweredCurrent && (
            <div className="flex justify-end pt-2">
              <button
                onClick={handleNextQuestion}
                className="px-6 py-3 rounded-2xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold transition shadow-lg shadow-indigo-600/20 flex items-center gap-2 cursor-pointer"
              >
                <span>
                  {currentQuestionIdx < questions.length - 1 ? 'Next Question' : 'Complete Diagnostic'}
                </span>
                <ArrowRight className="w-4 h-4" />
              </button>
            </div>
          )}
        </div>
      ) : (
        /* Results Screen */
        <div className="max-w-xl mx-auto glass-panel rounded-3xl p-8 sm:p-12 space-y-6 text-center shadow-2xl animate-in zoom-in-95 duration-200">
          <div className="w-20 h-20 rounded-3xl bg-indigo-600/20 border border-indigo-500/30 flex items-center justify-center mx-auto text-indigo-400 shadow-xl">
            <Award className="w-10 h-10" />
          </div>

          <div>
            <span className="text-xs font-bold uppercase tracking-wider text-slate-400">
              Diagnostic Assessment Finished
            </span>
            <h3 className="text-3xl font-black text-white mt-1">
              {selectedAnswers.filter((a, i) => a === questions[i].correctIndex).length} / {questions.length} Correct
            </h3>
            <p className="text-xs text-slate-400 mt-2 max-w-sm mx-auto leading-relaxed">
              Your Academic Recovery Score and Weak Topic Detector have been automatically updated.
            </p>
          </div>

          <div className="flex justify-center gap-3 pt-3">
            <button
              onClick={handleStartQuiz}
              className="flex items-center gap-1.5 px-5 py-2.5 rounded-2xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold transition cursor-pointer"
            >
              <RotateCcw className="w-3.5 h-3.5" />
              <span>Retry Quiz</span>
            </button>
            <button
              onClick={() => setIsQuizActive(false)}
              className="px-6 py-2.5 rounded-2xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold transition shadow-lg shadow-indigo-600/20 cursor-pointer"
            >
              <span>Return to Quizzes</span>
            </button>
          </div>
        </div>
      )}
    </div>
  );
};
