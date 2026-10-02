import React from 'react';

interface BackLiftLogoProps {
  size?: 'sm' | 'md' | 'lg' | 'xl';
  showText?: boolean;
  showTagline?: boolean;
  className?: string;
}

export const BackLiftLogo: React.FC<BackLiftLogoProps> = ({
  size = 'md',
  showText = true,
  showTagline = false,
  className = '',
}) => {
  const dimensions = {
    sm: { icon: 28, text: 'text-sm', badge: 'text-[9px]', tag: 'text-[10px]' },
    md: { icon: 40, text: 'text-lg', badge: 'text-[10px]', tag: 'text-[11px]' },
    lg: { icon: 56, text: 'text-2xl', badge: 'text-xs', tag: 'text-xs' },
    xl: { icon: 72, text: 'text-3xl', badge: 'text-sm', tag: 'text-sm' },
  }[size];

  return (
    <div className={`inline-flex items-center gap-3 select-none ${className}`}>
      {/* Visual Vector Icon */}
      <div
        className="relative shrink-0 flex items-center justify-center rounded-2xl bg-gradient-to-br from-slate-900 to-[#0d1424] border border-indigo-500/30 shadow-lg shadow-indigo-500/20 group hover:border-cyan-400/50 transition-all duration-300"
        style={{ width: dimensions.icon, height: dimensions.icon }}
      >
        {/* Glowing ambient light behind icon */}
        <div className="absolute inset-0 bg-gradient-to-tr from-indigo-600/40 via-cyan-500/30 to-purple-600/40 rounded-2xl blur-sm -z-10 opacity-70 group-hover:opacity-100 transition-opacity" />

        <svg
          viewBox="0 0 48 48"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          className="w-4/5 h-4/5 transform group-hover:scale-105 transition-transform"
        >
          <defs>
            <linearGradient id="blGradPrimary" x1="4" y1="44" x2="44" y2="4" gradientUnits="userSpaceOnUse">
              <stop offset="0%" stopColor="#6366F1" />
              <stop offset="50%" stopColor="#06B6D4" />
              <stop offset="100%" stopColor="#10B981" />
            </linearGradient>
            <linearGradient id="blGradAccent" x1="12" y1="36" x2="36" y2="12" gradientUnits="userSpaceOnUse">
              <stop offset="0%" stopColor="#A855F7" />
              <stop offset="100%" stopColor="#38BDF8" />
            </linearGradient>
            <filter id="blGlow" x="-20%" y="-20%" width="140%" height="140%">
              <feGaussianBlur stdDeviation="2" result="blur" />
              <feComposite in="SourceGraphic" in2="blur" operator="over" />
            </filter>
          </defs>

          {/* Upward Ascending Chevron Wings (The "Lift") */}
          <path
            d="M8 32L24 16L40 32L34 37L24 27L14 37L8 32Z"
            fill="url(#blGradPrimary)"
            filter="url(#blGlow)"
          />

          {/* Academic Graduation / Turnaround Diamond Node */}
          <path
            d="M24 6L30 13L24 20L18 13L24 6Z"
            fill="url(#blGradAccent)"
          />

          {/* Inner Light Flare Core */}
          <circle cx="24" cy="13" r="2.5" fill="#FFFFFF" />

          {/* Base Trajectory Ground Line */}
          <rect x="16" y="40" width="16" height="2.5" rx="1.25" fill="#6366F1" opacity="0.6" />
        </svg>

        {/* Live Status Pip */}
        <span className="absolute -top-1 -right-1 w-2.5 h-2.5 bg-emerald-400 rounded-full border-2 border-[#0b0f19] animate-pulse" />
      </div>

      {/* Brand Typography */}
      {showText && (
        <div className="flex flex-col text-left">
          <div className="flex items-center gap-2">
            <span className={`font-black tracking-tight text-white ${dimensions.text}`}>
              BackLift<span className="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-indigo-400">.AI</span>
            </span>
            <span className={`px-2 py-0.5 rounded-full bg-indigo-500/15 border border-indigo-500/30 text-indigo-300 font-extrabold uppercase tracking-wider ${dimensions.badge}`}>
              Turnaround
            </span>
          </div>
          {showTagline && (
            <p className={`text-slate-400 font-medium tracking-normal ${dimensions.tag}`}>
              Intelligent Academic Recovery & Degree Completion
            </p>
          )}
        </div>
      )}
    </div>
  );
};
