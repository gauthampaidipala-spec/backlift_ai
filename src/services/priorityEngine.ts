import { Backlog, RecoveryFactorBreakdown, StudyPlanItem, QuizAttempt } from '../types';

/**
 * Calculates priority score (0-100) for a backlog subject.
 * Higher score = needs more immediate urgent attention.
 */
export function calculateBacklogPriority(backlog: Omit<Backlog, 'priorityScore' | 'status'>): {
  score: number;
  status: 'critical' | 'high' | 'medium' | 'cleared';
} {
  if (backlog.prepPercentage >= 95) {
    return { score: 15, status: 'cleared' };
  }

  const today = new Date();
  const examDate = new Date(backlog.targetExamDate);
  const diffTime = examDate.getTime() - today.getTime();
  const daysUntilExam = Math.max(1, Math.ceil(diffTime / (1000 * 60 * 60 * 24)));

  // 1. Exam Urgency Component (40%)
  // <= 7 days: 100, 14 days: 80, 30 days: 50, >60 days: 20
  let urgencyScore = 0;
  if (daysUntilExam <= 7) urgencyScore = 100;
  else if (daysUntilExam <= 14) urgencyScore = 85;
  else if (daysUntilExam <= 30) urgencyScore = 65;
  else if (daysUntilExam <= 60) urgencyScore = 40;
  else urgencyScore = 20;

  // 2. Credits Weightage (20%)
  // Standard university course is 1 to 4 credits
  const creditScore = Math.min(100, (backlog.credits / 4) * 100);

  // 3. Preparation Deficit Gap (25%)
  const prepGap = 100 - backlog.prepPercentage;

  // 4. Perceived Difficulty (15%)
  // 1-5 scale -> 20, 40, 60, 80, 100
  const difficultyScore = (backlog.difficulty / 5) * 100;

  // Attempt penalty boost: if attemptCount > 1, add multiplier to avoid repeated failure
  const attemptMultiplier = backlog.attemptCount > 1 ? 1.12 : 1.0;

  const rawScore =
    (urgencyScore * 0.4 +
      creditScore * 0.2 +
      prepGap * 0.25 +
      difficultyScore * 0.15) *
    attemptMultiplier;

  const finalScore = Math.min(100, Math.max(0, Math.round(rawScore)));

  let status: 'critical' | 'high' | 'medium' | 'cleared' = 'medium';
  if (finalScore >= 75) status = 'critical';
  else if (finalScore >= 50) status = 'high';

  return { score: finalScore, status };
}

/**
 * Calculates the internal Academic Recovery Score (0-100) and factor breakdowns.
 * Note: Clearly framed as an internal diagnostic planning indicator.
 */
export function calculateAcademicRecoveryScore(
  backlogs: Backlog[],
  streakDays: number,
  quizAttempts: QuizAttempt[]
): {
  overallScore: number;
  gradeBadge: string;
  factors: RecoveryFactorBreakdown[];
  statusMessage: string;
} {
  if (backlogs.length === 0) {
    return {
      overallScore: 100,
      gradeBadge: 'All Cleared',
      factors: [],
      statusMessage: 'Congratulations! No active backlogs recorded.',
    };
  }

  // 1. Preparation Coverage Factor (35% weight)
  const avgPrep =
    backlogs.reduce((acc, b) => acc + b.prepPercentage, 0) / backlogs.length;
  const prepScore = Math.round(avgPrep);

  // 2. Quiz Performance Factor (25% weight)
  let quizScore = 50; // default baseline if no quizzes yet
  if (quizAttempts.length > 0) {
    const totalQuizPct = quizAttempts.reduce(
      (acc, q) => acc + (q.score / q.totalQuestions) * 100,
      0
    );
    quizScore = Math.round(totalQuizPct / quizAttempts.length);
  }

  // 3. Study Consistency / Streak Factor (20% weight)
  // 7+ days = 100, 3 days = 60, 1 day = 30
  const streakScore = Math.min(100, Math.round((streakDays / 7) * 100));

  // 4. Exam Proximity Cushion Factor (20% weight)
  const today = new Date();
  const closestExamDays = Math.min(
    ...backlogs.map((b) => {
      const diff = new Date(b.targetExamDate).getTime() - today.getTime();
      return Math.max(1, Math.ceil(diff / (1000 * 60 * 60 * 24)));
    })
  );

  let cushionScore = 50;
  if (closestExamDays > 30) cushionScore = 90;
  else if (closestExamDays > 14) cushionScore = 75;
  else if (closestExamDays > 7) cushionScore = 50;
  else cushionScore = 30;

  // Composite calculation
  const composite = Math.round(
    prepScore * 0.35 +
      quizScore * 0.25 +
      streakScore * 0.2 +
      cushionScore * 0.2
  );

  const overallScore = Math.min(100, Math.max(5, composite));

  const factors: RecoveryFactorBreakdown[] = [
    {
      label: 'Syllabus Preparation',
      score: prepScore,
      maxScore: 100,
      status: prepScore >= 70 ? 'positive' : prepScore >= 40 ? 'warning' : 'critical',
      impactDescription: `Average topic completion across ${backlogs.length} backlogs is ${prepScore}%.`,
    },
    {
      label: 'Quiz Diagnostics & Recall',
      score: quizScore,
      maxScore: 100,
      status: quizScore >= 70 ? 'positive' : quizScore >= 50 ? 'warning' : 'critical',
      impactDescription:
        quizAttempts.length > 0
          ? `Average diagnostic quiz accuracy is ${quizScore}%.`
          : 'Based on baseline syllabus estimation (Take a quiz to calibrate).',
    },
    {
      label: 'Study Consistency Streak',
      score: streakScore,
      maxScore: 100,
      status: streakDays >= 5 ? 'positive' : streakDays >= 2 ? 'warning' : 'critical',
      impactDescription: `Active study streak is ${streakDays} consecutive day${streakDays === 1 ? '' : 's'}.`,
    },
    {
      label: 'Exam Timeline Cushion',
      score: cushionScore,
      maxScore: 100,
      status: closestExamDays > 14 ? 'positive' : closestExamDays > 7 ? 'warning' : 'critical',
      impactDescription: `Nearest exam is in ${closestExamDays} days.`,
    },
  ];

  let gradeBadge = 'Moderate Pace';
  let statusMessage =
    'Steady recovery progress. Focus on critical topics to reach safe zone.';

  if (overallScore >= 80) {
    gradeBadge = 'High Readiness';
    statusMessage = 'Strong recovery momentum! Maintain consistency until exam day.';
  } else if (overallScore < 50) {
    gradeBadge = 'Urgent Turnaround Needed';
    statusMessage =
      'Immediate intervention required. Prioritize the highest-priority paper first.';
  }

  return {
    overallScore,
    gradeBadge,
    factors,
    statusMessage,
  };
}

/**
 * Generates an initial multi-day study schedule based on subject priorities.
 */
export function generateAdaptiveStudyPlan(
  backlogs: Backlog[],
  dailyHours: number,
  startDateStr?: string
): StudyPlanItem[] {
  const plan: StudyPlanItem[] = [];
  const baseDate = startDateStr ? new Date(startDateStr) : new Date();

  // Sort backlogs by priority (descending)
  const sortedBacklogs = [...backlogs].sort((a, b) => b.priorityScore - a.priorityScore);

  // Generate 7 days sprint
  for (let dayOffset = 0; dayOffset < 7; dayOffset++) {
    const currentDate = new Date(baseDate);
    currentDate.setDate(baseDate.getDate() + dayOffset);
    const dateStr = currentDate.toISOString().split('T')[0];

    // Distribute hours into 1.5 hour study blocks
    const sessionCount = Math.max(1, Math.floor(dailyHours / 1.5));

    for (let s = 0; s < sessionCount; s++) {
      // Pick subject: top priority subject gets 60% of sessions
      const subjectIndex = s === 0 ? 0 : s % sortedBacklogs.length;
      const targetSubject = sortedBacklogs[subjectIndex] || sortedBacklogs[0];

      if (!targetSubject) continue;

      // Find an incomplete topic or first topic
      const pendingTopics = targetSubject.topics.filter((t) => !t.isCompleted);
      const chosenTopic =
        pendingTopics[s % (pendingTopics.length || 1)] ||
        targetSubject.topics[0] || {
          id: `top-gen-${s}`,
          title: `Unit ${s + 1} Core Concepts Revision`,
          unitNumber: s + 1,
          historicalFrequency: 85,
          isCompleted: false,
        };

      const timeSlots = [
        '09:00 AM - 10:30 AM',
        '11:00 AM - 12:30 PM',
        '03:00 PM - 04:30 PM',
        '07:00 PM - 08:30 PM',
      ];

      plan.push({
        id: `plan-${dayOffset}-${s}-${Date.now() % 10000}`,
        date: dateStr,
        timeSlot: timeSlots[s % timeSlots.length],
        subjectId: targetSubject.id,
        subjectName: targetSubject.subjectName,
        topicId: chosenTopic.id,
        topicTitle: chosenTopic.title,
        allocatedMinutes: 90,
        isCompleted: dayOffset === 0 && s === 0 ? true : false, // first one done demo
      });
    }
  }

  return plan;
}

/**
 * Unique Differentiator: Missed-Day Recovery Engine.
 * Takes uncompleted tasks from a missed date and seamlessly redistributes them
 * across the remaining days without causing overwhelming hours.
 */
export function rebalanceMissedDayPlan(
  currentPlan: StudyPlanItem[],
  missedDateStr: string
): { updatedPlan: StudyPlanItem[]; rescheduledCount: number } {
  const missedItems = currentPlan.filter(
    (item) => item.date === missedDateStr && !item.isCompleted
  );

  if (missedItems.length === 0) {
    return { updatedPlan: currentPlan, rescheduledCount: 0 };
  }

  // Future dates in current plan
  const futureDates = Array.from(
    new Set(
      currentPlan
        .filter((item) => item.date > missedDateStr)
        .map((item) => item.date)
    )
  ).sort();

  if (futureDates.length === 0) {
    return { updatedPlan: currentPlan, rescheduledCount: 0 };
  }

  const updatedPlan = currentPlan.filter(
    (item) => !(item.date === missedDateStr && !item.isCompleted)
  );

  let targetDateIdx = 0;
  missedItems.forEach((missedItem) => {
    const targetDate = futureDates[targetDateIdx % futureDates.length];
    targetDateIdx++;

    updatedPlan.push({
      ...missedItem,
      id: `rebalanced-${missedItem.id}`,
      date: targetDate,
      timeSlot: '05:30 PM - 06:30 PM (Recovery)',
      allocatedMinutes: 60, // compressed revision sprint
      isRescheduled: true,
    });
  });

  return {
    updatedPlan: updatedPlan.sort((a, b) => a.date.localeCompare(b.date)),
    rescheduledCount: missedItems.length,
  };
}
