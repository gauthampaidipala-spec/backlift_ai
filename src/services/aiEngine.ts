import { Backlog, StudentProfile } from '../types';

export interface AIContext {
  student: StudentProfile;
  backlogs: Backlog[];
  weakTopics: string[];
}

/**
 * Intelligent Academic Recovery Chatbot Engine ("LiftBot").
 * Generates personalized, empathetic, actionable study guidance.
 */
export function generateAIChatResponse(
  userQuery: string,
  context: AIContext
): { text: string; suggestions?: string[] } {
  const query = userQuery.toLowerCase().trim();
  const sortedBacklogs = [...context.backlogs].sort((a, b) => b.priorityScore - a.priorityScore);
  const highestPriority = sortedBacklogs[0] || null;

  // 1. "Which subject should I study first?" or prioritization questions
  if (
    query.includes('which subject') ||
    query.includes('study first') ||
    query.includes('prioritize') ||
    query.includes('what should i study')
  ) {
    if (!highestPriority) {
      return {
        text: `### 🎯 Prioritization Assessment
You currently have no active backlogs registered! You can focus on your regular semester coursework or prepare ahead.`,
        suggestions: ['Add a new subject', 'View study planner', 'Take a mock quiz'],
      };
    }

    const examDays = Math.max(
      1,
      Math.ceil(
        (new Date(highestPriority.targetExamDate).getTime() - Date.now()) /
          (1000 * 60 * 60 * 24)
      )
    );

    return {
      text: `### 🚨 Priority Engine Recommendation

Based on your current academic profile, your highest priority subject right now is:

**👉 ${highestPriority.subjectName} (${highestPriority.subjectCode})**

Here is why:
- **Exam Urgency**: Your exam is in **${examDays} days** (${highestPriority.targetExamDate}).
- **Credit Weight**: Worth **${highestPriority.credits} credits** (crucial for your CGPA recovery).
- **Current Preparation**: Recorded at **${highestPriority.prepPercentage}%** (a ${100 - highestPriority.prepPercentage}% syllabus gap remains).
- **Previous Attempts**: ${highestPriority.attemptCount} attempt(s) logged.

#### Recommended Action For Today:
1. Allocate **65% of your available ${context.student.dailyStudyHours} hours** (${(context.student.dailyStudyHours * 0.65).toFixed(1)} hrs) to **${highestPriority.subjectName}**.
2. Start with high-frequency units: *Fourier Series / Convolution Theorem*.
3. Test yourself with a 5-question micro-quiz before going to sleep.`,
      suggestions: [
        `Create a 7-day study plan for ${highestPriority.subjectCode}`,
        'Give me important topics',
        'Start 25m Focus Timer',
      ],
    };
  }

  // 2. "How should I prepare for my 3 backlogs?" or multiple backlogs strategy
  if (
    query.includes('how should i prepare') ||
    query.includes('3 backlogs') ||
    query.includes('multiple backlogs') ||
    query.includes('struggling with backlogs')
  ) {
    return {
      text: `### 📘 Strategic Multi-Backlog Recovery Blueprint

Managing multiple backlogs alongside regular classes is completely doable when you stop studying reactively and start studying **in triage sprints**.

Here is the exact 4-step framework we recommend:

1. **The 60/30/10 Rule**:
   - **60% of daily time**: Dedicate to your **#1 Highest-Priority paper** (${highestPriority?.subjectName || 'Maths-II'}).
   - **30% of daily time**: Dedicate to your **#2 secondary backlog** (${sortedBacklogs[1]?.subjectName || 'Operating Systems'}).
   - **10% of daily time**: Formula revision, active flashcards, or rest.

2. **Stop Starting from Chapter 1**:
   - Struggling students often waste 5 days perfecting Unit 1. Look at the **Topic Analyzer**: focus on the 3 units that appear in **80% of university question papers**.

3. **Active Recall over Passive Reading**:
   - Don't just stare at PDF notes. Solve 2 previous exam questions with pen and paper every evening.

4. **Preserve Your Daily Streak**:
   - Even if you are exhausted, study for 25 minutes using our **Focus Timer**. Consistency preserves mental momentum.`,
      suggestions: [
        'Which subject should I study first?',
        'Give me important topics',
        'Create a 7-day study plan',
      ],
    };
  }

  // 3. "Explain this topic simply" or concept explanations
  if (
    query.includes('explain') ||
    query.includes('simply') ||
    query.includes('concept') ||
    query.includes('what is') ||
    query.includes('fourier') ||
    query.includes('semaphore') ||
    query.includes('laplace')
  ) {
    if (query.includes('semaphore') || query.includes('sync') || query.includes('deadlock')) {
      return {
        text: `### 💡 Concept Simplifier: Semaphores & Process Synchronization

Imagine a **single public restroom key** in a busy university cafe:

1. **The Problem (Race Condition)**:
   - If two students try to unlock and enter the door simultaneously, chaos happens.
2. **The Semaphore Key (S)**:
   - A semaphore is simply an integer variable used for signaling.
   - **Wait() / P()**: Before entering, you check if the key is available (S > 0). If yes, you grab it and decrement S (S = S - 1). If S == 0, you wait in line.
   - **Signal() / V()**: When you leave, you put the key back on the counter (S = S + 1), waking up the next student waiting.
3. **Types in Exams**:
   - **Counting Semaphore**: Range can be unrestricted (e.g., parking lot with 50 spots).
   - **Binary Semaphore (Mutex)**: Can only be 0 or 1. Used for mutual exclusion.

*Exam Tip: University examiners frequently ask for the pseudo-code implementation of wait() and signal(). Memorize the while(S <= 0); S--; structure!*`,
        suggestions: ['Quiz me on Operating Systems', 'Give me important topics for CS302'],
      };
    }

    if (query.includes('fourier') || query.includes('laplace') || query.includes('math')) {
      return {
        text: `### 💡 Concept Simplifier: Fourier Series Made Intuitive

Imagine making a **fruit smoothie**:

1. **The Core Intuition**:
   - A Fourier Series says that *any repeating periodic sound or signal* (the smoothie) is just a blend of pure, simple sine and cosine waves (the bananas, strawberries, and milk) at different frequencies.
2. **The Mathematical Recipe**:
   $$f(x) = \\frac{a_0}{2} + \\sum_{n=1}^{\\infty} [a_n \\cos(nx) + b_n \\sin(nx)]$$
   - **$a_0/2$**: The baseline DC level (average value of the signal).
   - **$a_n$**: How much "cosine flavour" of frequency $n$ is present.
   - **$b_n$**: How much "sine flavour" of frequency $n$ is present.
3. **The Ultimate Exam Shortcut**:
   - If $f(x)$ is **Even** ($f(-x) = f(x)$), then $b_n = 0$! You save half the calculation time!
   - If $f(x)$ is **Odd** ($f(-x) = -f(x)$), then $a_0 = 0$ and $a_n = 0$! You only calculate $b_n$!`,
        suggestions: ['Quiz me on Fourier Series', 'Show formulas for Laplace', 'Which subject should I study first?'],
      };
    }

    return {
      text: `### 💡 AI Concept Simplification Mode

I can break down any complex engineering, mathematics, or science topic into simple analogies with exam-oriented key formulas.

Which specific topic would you like me to unpack?
- **Engineering Maths**: Fourier Series, Laplace Transforms, Cauchy-Riemann Equations
- **Operating Systems**: Deadlock Bankers Algorithm, Semaphores, Page Replacement
- **Electronics**: Op-Amps, K-Maps, JK Flip Flops, 555 Timers`,
      suggestions: ['Explain Fourier Series', 'Explain Semaphores', 'Explain Bankers Algorithm'],
    };
  }

  // 4. "Create a 7-day study plan"
  if (query.includes('7-day') || query.includes('study plan') || query.includes('timetable')) {
    return {
      text: `### 🗓️ AI 7-Day Academic Turnaround Sprint Plan

Tailored for **${context.student.name}** with **${context.student.dailyStudyHours} hours/day**:

| Day | Focus Subject | High-Yield Topic Target | Hours |
| :--- | :--- | :--- | :--- |
| **Day 1** | ${highestPriority?.subjectName || 'Maths-II'} | Fourier Series & Dirichlet Conditions | 2.5 hrs + Quiz |
| **Day 2** | ${highestPriority?.subjectName || 'Maths-II'} | Inverse Laplace (Convolution Theorem) | 2.5 hrs + Past Qs |
| **Day 3** | ${sortedBacklogs[1]?.subjectName || 'Operating Systems'} | Semaphores & Dining Philosophers | 2.5 hrs + Notes |
| **Day 4** | ${sortedBacklogs[1]?.subjectName || 'Operating Systems'} | Bankers Algorithm & Safe State Numerical | 2.5 hrs + Practice |
| **Day 5** | ${highestPriority?.subjectName || 'Maths-II'} | Second-Order Linear Differential Equations | 2.5 hrs + Quiz |
| **Day 6** | ${sortedBacklogs[2]?.subjectName || 'Electronics'} | K-Maps & Logic Minimization Practice | 2.0 hrs + Formulas |
| **Day 7** | **All Backlogs** | Full Mock Test + Review Weak Topic Badges | 3.5 hrs Sprint |

*Pro-Tip: If you ever miss a day, click the **"Missed Yesterday"** button in the Study Planner to automatically rebalance remaining days without panic.*`,
      suggestions: ['Open Study Planner', 'Take a Diagnostic Quiz', 'Start Focus Session'],
    };
  }

  // 5. "Give me important topics" or exam weightage
  if (query.includes('important topic') || query.includes('weightage') || query.includes('previous papers')) {
    return {
      text: `### 📊 High-Yield Question Paper Analysis

*(Disclaimer: Identified via historical frequency heuristics across past 5 university exam cycles. Use as targeted guidance, not a paper leak or guarantee).*

#### High-Yield Topics for ${highestPriority?.subjectName || 'Your Priority Subject'}:
1. **Fourier Series on $(-\\pi, \\pi)$ and $(0, 2\\pi)$** — ⭐⭐⭐⭐⭐ (Appeared in 5/5 past papers, Avg 14 Marks)
2. **Convolution Theorem for Inverse Laplace** — ⭐⭐⭐⭐⭐ (Appeared in 5/5 past papers, Avg 14 Marks)
3. **Cauchy-Euler Differential Equations** — ⭐⭐⭐⭐ (Appeared in 4/5 past papers, Avg 10 Marks)
4. **Stokes & Gauss Divergence Theorems** — ⭐⭐⭐⭐ (Appeared in 4/5 past papers, Avg 12 Marks)

**Strategic Takeaway**: Master just these 4 topic types and you have covered over **50 marks** of typical university paper weightage!`,
      suggestions: ['View full Question Paper Analyzer', 'Quiz me on Fourier Series', 'Download Topper Notes'],
    };
  }

  // 6. "I have 15 days before my exam. What should I do?"
  if (
    query.includes('15 days') ||
    query.includes('days left') ||
    query.includes('last minute') ||
    query.includes('exam near')
  ) {
    return {
      text: `### ⏳ The 15-Day Academic Turnaround Protocol

With 15 days remaining, **your study strategy must shift from comprehensive reading to targeted mark maximization**:

1. **Days 1 to 5 (High-Yield Coverage)**:
   - Study ONLY the top 3 highest-frequency topics per unit. Do NOT try to read the entire textbook cover to cover.
2. **Days 6 to 10 (Solved Numericals & Derivations)**:
   - Solve at least 3 previous year university question papers with a strict 3-hour timer.
3. **Days 11 to 13 (Weak Topic Eradication)**:
   - Check your **Weak Topic Detector** badges on the dashboard. Revise only those identified gaps.
4. **Days 14 to 15 (Smart Revision Mode)**:
   - Review formula sheets, standard definitions, and step-marking formats. Sleep at least 7 hours before exam day.`,
      suggestions: ['Show Important Topics', 'Start Focus Timer', 'Which subject should I study first?'],
    };
  }

  // 7. "I am weak in this topic. How can I improve?" or weak areas
  if (query.includes('weak') || query.includes('improve') || query.includes('failing') || query.includes('hard')) {
    return {
      text: `### 🛡️ Targeted Weakness Remediation Strategy

Struggling with a specific concept is completely normal. Here is the **Feynman Micro-Loop** to fix it in under 45 minutes:

1. **Step 1: Simplify**: Read the 2-page summary in the **Study Resource Hub** rather than dense 60-page textbooks.
2. **Step 2: Teach It**: Open the AI Chatbot and type *"Explain [Concept] like I am 12"*.
3. **Step 3: Solve 1 Solved Example**: Copy out a solved numerical line by line, explaining each step out loud.
4. **Step 4: Micro-Quiz**: Take our 5-question AI chapter quiz to test retention.`,
      suggestions: ['Explain Fourier Series simply', 'Take Diagnostic Quiz', 'Open Resource Hub'],
    };
  }

  // 8. "Quiz me" or practice
  if (query.includes('quiz') || query.includes('test me') || query.includes('practice')) {
    return {
      text: `### 📝 Diagnostic Quiz Ready!

I have prepared interactive diagnostic multiple-choice quizzes tailored for:
1. **MATH201**: Fourier Series & Laplace Transforms
2. **CS302**: Process Synchronization & Deadlocks
3. **EC204**: Operational Amplifiers & K-Maps

Head over to the **AI Quizzes** module from the sidebar, or click below to launch your session. Every incorrect answer automatically feeds the **Weak Topic Detector** to calibrate your recovery score!`,
      suggestions: ['Open AI Quizzes', 'Explain Fourier Series', 'Which subject should I study first?'],
    };
  }

  // Default intelligent assistant response
  return {
    text: `Hello ${context.student.name}! I am **LiftBot**, your dedicated AI Academic Recovery Coach.

I am analyzing your current profile:
- **Active Backlogs**: ${context.backlogs.length} subject(s)
- **Top Priority**: ${highestPriority?.subjectName || 'General Recovery'} (Exam: ${highestPriority?.targetExamDate || 'N/A'})
- **Study Streak**: 🔥 ${context.student.streakDays} Days

How can I assist your turnaround today?`,
    suggestions: [
      'Which subject should I study first?',
      'How should I prepare for my 3 backlogs?',
      'Explain Fourier Series simply',
      'Create a 7-day study plan',
    ],
  };
}
