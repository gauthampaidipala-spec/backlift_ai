export interface Topic {
  id: string;
  title: string;
  unitNumber: number;
  historicalFrequency: number; // 0 to 100%
  isCompleted: boolean;
  completedAt?: string;
}

export interface Backlog {
  id: string;
  subjectName: string;
  subjectCode: string;
  semester: number;
  credits: number;
  attemptCount: number;
  targetExamDate: string; // YYYY-MM-DD
  difficulty: number; // 1 to 5
  prepPercentage: number; // 0 to 100
  topics: Topic[];
  priorityScore: number; // calculated 0 to 100
  status: 'critical' | 'high' | 'medium' | 'cleared';
  colorTag: string;
}

export interface StudyPlanItem {
  id: string;
  date: string; // YYYY-MM-DD
  timeSlot: string; // e.g. "09:00 AM - 10:30 AM"
  subjectId: string;
  subjectName: string;
  topicId: string;
  topicTitle: string;
  allocatedMinutes: number;
  isCompleted: boolean;
  isRescheduled?: boolean;
}

export interface StudentProfile {
  name: string;
  college: string;
  degree: string;
  semester: number;
  dailyStudyHours: number;
  preferredStudyTime: 'morning' | 'afternoon' | 'evening' | 'night';
  streakDays: number;
  lastStudyDate: string;
  totalHoursStudied: number;
  isProUser: boolean;
}

export interface ChatMessage {
  id: string;
  sender: 'user' | 'bot';
  text: string;
  timestamp: string;
  suggestions?: string[];
  actionType?: 'plan' | 'quiz' | 'explain' | 'priority';
}

export interface QuestionFrequencyItem {
  topic: string;
  unit: number;
  frequencyScore: number; // e.g. 85%
  recurrenceCount: number; // e.g. Appeared in 4 of 5 papers
  averageMarks: number;
  priorityCategory: 'high-yield' | 'moderate' | 'low';
}

export interface PastPaper {
  id: string;
  subjectCode: string;
  subjectName: string;
  sessionYear: string;
  totalMarks: number;
  durationHours: number;
  paperUrl?: string;
  keyTopics: QuestionFrequencyItem[];
  sampleQuestions: string[];
}

export interface StudyResource {
  id: string;
  subjectCode: string;
  subjectName: string;
  title: string;
  type: 'notes' | 'video' | 'paper' | 'formula';
  url: string;
  author: string;
  meta: string; // e.g. "18 pages PDF" or "14 mins Video"
  topicTag: string;
  rating: number;
  isVerifiedTopper: boolean;
}

export interface QuizQuestion {
  id: string;
  subjectCode: string;
  topic: string;
  question: string;
  options: string[];
  correctIndex: number;
  explanation: string;
  difficulty: 'easy' | 'medium' | 'hard';
}

export interface QuizAttempt {
  id: string;
  subjectCode: string;
  subjectName: string;
  topic: string;
  score: number;
  totalQuestions: number;
  weakConcepts: string[];
  attemptedAt: string;
}

export interface StudyBuddyGroup {
  id: string;
  name: string;
  subjectCode: string;
  subjectName: string;
  memberCount: number;
  activeOnline: number;
  targetExamDate: string;
  dailySprintGoal: string;
  recentMessage: string;
  avatarSeed: string;
}

export interface RecoveryFactorBreakdown {
  label: string;
  score: number;
  maxScore: number;
  status: 'positive' | 'warning' | 'critical';
  impactDescription: string;
}

export interface CampusBatchMetric {
  department: string;
  totalStudents: number;
  studentsWithBacklogs: number;
  averageRecoveryScore: number;
  bottleneckSubjects: {
    name: string;
    code: string;
    failureRate: number;
    enrolledBacklogs: number;
  }[];
}
