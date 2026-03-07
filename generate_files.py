files = {
    'src/lib/supabase/client.ts': '''import { createClient as createSupabaseClient } from "@supabase/supabase-js"

export const createClient = () =>
  createSupabaseClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
  )
''',
    'src/components/ui/Button.tsx': '''"use client"
import { cn } from "@/lib/utils"
import { Loader2 } from "lucide-react"
import type { ButtonHTMLAttributes } from "react"

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "secondary" | "ghost" | "danger" | "success" | "outline"
  size?: "sm" | "md" | "lg"
  loading?: boolean
  fullWidth?: boolean
}

export function Button({ variant = "primary", size = "md", loading, fullWidth, className, children, disabled, ...props }: ButtonProps) {
  const base = "inline-flex items-center justify-center gap-2 rounded-lg font-medium transition-all focus:outline-none disabled:opacity-50 disabled:cursor-not-allowed"
  const variants = {
    primary:   "bg-sky-500 text-white hover:bg-sky-400 shadow-sm",
    secondary: "bg-slate-700 text-slate-200 hover:bg-slate-600",
    ghost:     "text-slate-400 hover:text-slate-200 hover:bg-slate-800",
    danger:    "bg-red-500 text-white hover:bg-red-400",
    success:   "bg-emerald-500 text-white hover:bg-emerald-400",
    outline:   "border border-slate-600 text-slate-300 hover:border-sky-500 hover:text-sky-400",
  }
  const sizes = { sm: "px-3 py-1.5 text-xs", md: "px-4 py-2 text-sm", lg: "px-5 py-2.5 text-base" }
  return (
    <button
      className={cn(base, variants[variant], sizes[size], fullWidth && "w-full", className)}
      disabled={disabled || loading}
      {...props}
    >
      {loading && <Loader2 size={14} className="animate-spin" />}
      {children}
    </button>
  )
}
''',
    'src/components/ui/Input.tsx': '''"use client"
import { cn } from "@/lib/utils"
import { forwardRef } from "react"
import type { InputHTMLAttributes, TextareaHTMLAttributes } from "react"

interface InputProps extends InputHTMLAttributes<HTMLInputElement> {
  label?: string
  error?: string
  hint?: string
}

export const Input = forwardRef<HTMLInputElement, InputProps>(
  ({ label, error, hint, className, ...props }, ref) => (
    <div className="flex flex-col gap-1.5">
      {label && <label className="text-xs font-medium text-slate-300">{label}</label>}
      <input
        ref={ref}
        className={cn(
          "w-full rounded-lg border bg-slate-800 px-3 py-2 text-sm text-slate-200 placeholder-slate-500 outline-none transition-all",
          error ? "border-red-500 focus:ring-1 focus:ring-red-500" : "border-slate-700 focus:border-sky-500 focus:ring-1 focus:ring-sky-500",
          className
        )}
        {...props}
      />
      {error && <p className="text-xs text-red-400">{error}</p>}
      {hint && !error && <p className="text-xs text-slate-500">{hint}</p>}
    </div>
  )
)
Input.displayName = "Input"
''',
    'src/components/ui/Toast.tsx': '''"use client"
import { Toaster, toast } from "react-hot-toast"

export function ToastProvider() {
  return (
    <Toaster
      position="top-right"
      toastOptions={{
        duration: 4000,
        style: {
          background: "#1e293b",
          color: "#e2e8f0",
          border: "1px solid #334155",
          borderRadius: "12px",
          fontSize: "13px",
        },
      }}
    />
  )
}

export const notify = {
  success: (msg: string) => toast.success(msg),
  error:   (msg: string) => toast.error(msg),
  info:    (msg: string) => toast(msg),
  warning: (msg: string) => toast(msg),
}
'''
}

import os

for path, content in files.items():
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Written: {path}')