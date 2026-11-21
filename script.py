#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════╗
║   AquaFlow Logistics — One-Click Website Updater v2.0            ║
║                                                                  ║
║   Updates:                                                       ║
║   • New cream-beige / dark-grey theme                            ║
║   • Unique liquid-capsule loading bar                            ║
║   • Interactive mouse-following background + particles           ║
║   • Brand-new 3D water-orb hero widget (replaces tanker SVG)     ║
║                                                                  ║
║   Usage:  python update_aquaflow.py                              ║
╚══════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import shutil
import webbrowser
from pathlib import Path
from datetime import datetime


# ─────────────────────────────────────────────────────────────────
# NEW HTML CONTENT (cream-beige + dark theme, new loader, new hero)
# ─────────────────────────────────────────────────────────────────
NEW_HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>AquaFlow Logistics — Reliable Water Delivery, On Demand</title>

<script src="https://cdn.tailwindcss.com"></script>

<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&display=swap" rel="stylesheet" />

<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/qrcode@1.5.3/build/qrcode.min.js"></script>

<script>
  tailwind.config = {
    darkMode: 'class',
    theme: {
      extend: {
        fontFamily: {
          sans: ['Inter', 'system-ui', 'sans-serif'],
          display: ['"Plus Jakarta Sans"', 'Inter', 'sans-serif'],
          serif: ['Fraunces', 'serif'],
        },
        colors: {
          cream: {
            50:  '#FDFBF7',
            100: '#FAF7F2',
            200: '#F5EFE6',
            300: '#E8DCC4',
            400: '#D4C4A0',
            500: '#B8935A',
            600: '#9A7A48',
            700: '#7D6239',
            800: '#5F4A2B',
            900: '#3F3120',
          },
          charcoal: {
            50:  '#F5F3EF',
            100: '#E8E4DC',
            700: '#2A2520',
            800: '#1A1714',
            900: '#0A0908',
            950: '#050403',
          }
        },
        animation: {
          'float': 'float 6s ease-in-out infinite',
          'glow-pulse': 'glowPulse 3s ease-in-out infinite',
          'slide-up': 'slideUp 0.6s cubic-bezier(0.16, 1, 0.3, 1)',
          'fade-in': 'fadeIn 0.8s ease-out',
          'shimmer': 'shimmer 3s linear infinite',
          'spin-slow': 'spin 20s linear infinite',
          'blob': 'blob 12s ease-in-out infinite',
        },
        keyframes: {
          float: {
            '0%, 100%': { transform: 'translateY(0px)' },
            '50%': { transform: 'translateY(-14px)' },
          },
          glowPulse: {
            '0%, 100%': { boxShadow: '0 0 30px rgba(184, 147, 90, 0.3)' },
            '50%': { boxShadow: '0 0 60px rgba(184, 147, 90, 0.6)' },
          },
          slideUp: {
            '0%': { transform: 'translateY(40px)', opacity: '0' },
            '100%': { transform: 'translateY(0)', opacity: '1' },
          },
          fadeIn: {
            '0%': { opacity: '0' },
            '100%': { opacity: '1' },
          },
          shimmer: {
            '0%': { backgroundPosition: '-200% 0' },
            '100%': { backgroundPosition: '200% 0' },
          },
          blob: {
            '0%, 100%': { transform: 'translate(0, 0) scale(1)' },
            '33%': { transform: 'translate(30px, -50px) scale(1.1)' },
            '66%': { transform: 'translate(-20px, 20px) scale(0.9)' },
          },
        }
      }
    }
  }
</script>

<style>
  html { scroll-behavior: smooth; }

  /* ── Light Theme (Cream-Beige) ── */
  body {
    font-family: 'Inter', sans-serif;
    background: #FAF7F2;
    color: #3F3120;
    overflow-x: hidden;
    transition: background 0.5s ease, color 0.5s ease;
  }
  body.dark {
    background: #0A0908;
    color: #E8E4DC;
  }

  h1, h2, h3, h4, h5, h6, .font-display { font-family: 'Plus Jakarta Sans', sans-serif; }
  .font-serif { font-family: 'Fraunces', serif; }

  /* ── Glassmorphism ── */
  .glass {
    background: rgba(255, 255, 255, 0.55);
    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
    border: 1px solid rgba(184, 147, 90, 0.18);
  }
  body.dark .glass {
    background: rgba(26, 23, 20, 0.55);
    border: 1px solid rgba(212, 184, 150, 0.15);
  }
  .glass-strong {
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(24px) saturate(180%);
    -webkit-backdrop-filter: blur(24px) saturate(180%);
    border: 1px solid rgba(184, 147, 90, 0.25);
  }
  body.dark .glass-strong {
    background: rgba(10, 9, 8, 0.85);
    border: 1px solid rgba(212, 184, 150, 0.2);
  }

  /* ── Gradient text ── */
  .gradient-text {
    background: linear-gradient(135deg, #B8935A 0%, #D4B896 50%, #9A7A48 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  /* ── Glow border ── */
  .accent-glow {
    box-shadow:
      0 0 0 1px rgba(184, 147, 90, 0.2),
      0 0 30px rgba(184, 147, 90, 0.12),
      inset 0 1px 0 rgba(255, 255, 255, 0.5);
  }
  body.dark .accent-glow {
    box-shadow:
      0 0 0 1px rgba(212, 184, 150, 0.2),
      0 0 30px rgba(212, 184, 150, 0.15),
      inset 0 1px 0 rgba(255, 255, 255, 0.05);
  }
  .accent-glow-strong {
    box-shadow:
      0 0 0 1px rgba(184, 147, 90, 0.4),
      0 0 40px rgba(184, 147, 90, 0.3),
      inset 0 1px 0 rgba(255, 255, 255, 0.5);
  }
  body.dark .accent-glow-strong {
    box-shadow:
      0 0 0 1px rgba(212, 184, 150, 0.4),
      0 0 40px rgba(212, 184, 150, 0.3),
      inset 0 1px 0 rgba(255, 255, 255, 0.08);
  }

  /* ── Ambient blobs ── */
  .ambient-blob {
    position: absolute;
    border-radius: 50%;
    filter: blur(100px);
    opacity: 0.35;
    pointer-events: none;
    z-index: 0;
  }

  /* ── Interactive background canvas ── */
  #bgCanvas {
    position: fixed;
    inset: 0;
    z-index: 0;
    pointer-events: none;
  }

  /* ── Scrollbar ── */
  ::-webkit-scrollbar { width: 10px; height: 10px; }
  ::-webkit-scrollbar-track { background: transparent; }
  ::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #9A7A48, #B8935A);
    border-radius: 10px;
  }
  body.dark ::-webkit-scrollbar-track { background: #0A0908; }

  /* ── Preloader ── */
  #preloader {
    position: fixed;
    inset: 0;
    z-index: 9999;
    background: #FAF7F2;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: opacity 1s ease, visibility 1s ease;
  }
  body.dark #preloader { background: #0A0908; }
  #preloader.hidden-loader { opacity: 0; visibility: hidden; }

  /* Liquid capsule loader */
  .liquid-capsule {
    position: relative;
    width: 320px;
    height: 70px;
    border-radius: 999px;
    background: rgba(184, 147, 90, 0.08);
    border: 1.5px solid rgba(184, 147, 90, 0.25);
    overflow: hidden;
    box-shadow: inset 0 2px 8px rgba(184, 147, 90, 0.1);
  }
  body.dark .liquid-capsule {
    background: rgba(212, 184, 150, 0.06);
    border-color: rgba(212, 184, 150, 0.2);
  }
  .liquid-fill {
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 0%;
    background: linear-gradient(180deg, #D4B896 0%, #B8935A 60%, #7D6239 100%);
    transition: width 0.15s linear;
    border-radius: 999px 0 0 999px;
  }
  .liquid-wave {
    position: absolute;
    top: -8px;
    right: -20px;
    width: 60px;
    height: 90px;
    background: radial-gradient(ellipse at center, rgba(255,255,255,0.4) 0%, transparent 70%);
    animation: waveMove 2s ease-in-out infinite;
  }
  @keyframes waveMove {
    0%, 100% { transform: translateX(0) scaleY(1); }
    50% { transform: translateX(-6px) scaleY(1.15); }
  }
  .liquid-bubbles {
    position: absolute;
    inset: 0;
    overflow: hidden;
  }
  .liquid-bubble {
    position: absolute;
    bottom: -10px;
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.5);
    animation: bubbleRise 2.5s ease-in infinite;
  }
  @keyframes bubbleRise {
    0% { transform: translateY(0) scale(0.5); opacity: 0; }
    20% { opacity: 0.8; }
    100% { transform: translateY(-80px) scale(1); opacity: 0; }
  }
  .loader-percent {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Fraunces', serif;
    font-weight: 600;
    font-size: 22px;
    color: #3F3120;
    mix-blend-mode: difference;
    z-index: 2;
  }
  body.dark .loader-percent { color: #F5F3EF; }

  /* Hero grid pattern */
  .grid-pattern {
    background-image:
      linear-gradient(rgba(184, 147, 90, 0.08) 1px, transparent 1px),
      linear-gradient(90deg, rgba(184, 147, 90, 0.08) 1px, transparent 1px);
    background-size: 60px 60px;
    mask-image: radial-gradient(ellipse at center, black 30%, transparent 75%);
    -webkit-mask-image: radial-gradient(ellipse at center, black 30%, transparent 75%);
  }
  body.dark .grid-pattern {
    background-image:
      linear-gradient(rgba(212, 184, 150, 0.06) 1px, transparent 1px),
      linear-gradient(90deg, rgba(212, 184, 150, 0.06) 1px, transparent 1px);
  }

  /* Shimmer text */
  .shimmer-text {
    background: linear-gradient(90deg, #B8935A 0%, #F5EFE6 25%, #B8935A 50%, #F5EFE6 75%, #B8935A 100%);
    background-size: 200% 100%;
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shimmer 3s linear infinite;
  }

  /* Button shine */
  .btn-shine { position: relative; overflow: hidden; }
  .btn-shine::after {
    content: '';
    position: absolute;
    top: 0; left: -100%;
    width: 100%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
    transition: left 0.6s ease;
  }
  .btn-shine:hover::after { left: 100%; }

  /* Modal */
  .modal-backdrop {
    position: fixed;
    inset: 0;
    z-index: 100;
    background: rgba(10, 9, 8, 0.6);
    backdrop-filter: blur(8px);
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.3s ease, visibility 0.3s ease;
    padding: 16px;
  }
  .modal-backdrop.active { opacity: 1; visibility: visible; }
  .modal-panel {
    max-height: 92vh;
    overflow-y: auto;
    transform: translateY(30px) scale(0.97);
    transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  }
  .modal-backdrop.active .modal-panel { transform: translateY(0) scale(1); }

  /* Step indicator */
  .step-dot { transition: all 0.4s ease; }
  .step-dot.active {
    background: linear-gradient(135deg, #B8935A, #D4B896);
    box-shadow: 0 0 20px rgba(184, 147, 90, 0.6);
    color: white;
  }
  .step-dot.completed { background: rgba(184, 147, 90, 0.25); color: #B8935A; }
  .step-line { transition: background 0.4s ease; }
  .step-line.active { background: linear-gradient(90deg, #B8935A, #D4B896); }

  /* Capacity card */
  .capacity-card { transition: all 0.3s ease; cursor: pointer; }
  .capacity-card:hover { transform: translateY(-4px); border-color: rgba(184, 147, 90, 0.5); }
  .capacity-card.selected {
    border-color: #B8935A;
    background: linear-gradient(135deg, rgba(184, 147, 90, 0.12), rgba(255, 255, 255, 0.6));
    box-shadow: 0 0 30px rgba(184, 147, 90, 0.25);
  }
  body.dark .capacity-card.selected {
    background: linear-gradient(135deg, rgba(212, 184, 150, 0.15), rgba(26, 23, 20, 0.6));
  }

  /* Time slot */
  .time-slot { transition: all 0.25s ease; cursor: pointer; }
  .time-slot:hover:not(.disabled) { border-color: rgba(184, 147, 90, 0.5); background: rgba(184, 147, 90, 0.08); }
  .time-slot.selected { border-color: #B8935A; background: rgba(184, 147, 90, 0.2); }
  .time-slot.disabled { opacity: 0.35; cursor: not-allowed; }

  /* Status tracker */
  .status-step { position: relative; }
  .status-step::before {
    content: '';
    position: absolute;
    left: 20px;
    top: 40px;
    width: 2px;
    height: calc(100% - 40px);
    background: rgba(184, 147, 90, 0.15);
  }
  .status-step:last-child::before { display: none; }
  .status-step.done::before { background: linear-gradient(180deg, #B8935A, rgba(184, 147, 90, 0.3)); }

  /* Print */
  @media print {
    body * { visibility: hidden; }
    #receipt-print, #receipt-print * { visibility: visible; }
    #receipt-print {
      position: absolute;
      left: 0; top: 0;
      width: 100%;
      background: white !important;
      color: black !important;
    }
    .no-print { display: none !important; }
  }

  /* Input */
  .input-field {
    width: 100%;
    padding: 12px 16px;
    background: rgba(255, 255, 255, 0.7);
    border: 1px solid rgba(184, 147, 90, 0.2);
    border-radius: 12px;
    color: #3F3120;
    font-size: 14px;
    transition: all 0.25s ease;
    outline: none;
  }
  body.dark .input-field {
    background: rgba(26, 23, 20, 0.6);
    border-color: rgba(212, 184, 150, 0.2);
    color: #E8E4DC;
  }
  .input-field:focus {
    border-color: #B8935A;
    box-shadow: 0 0 0 3px rgba(184, 147, 90, 0.15);
  }
  .input-field::placeholder { color: #8B7355; }
  body.dark .input-field::placeholder { color: #6B6358; }

  /* Reveal */
  .reveal { opacity: 0; transform: translateY(30px); transition: opacity 0.8s ease, transform 0.8s ease; }
  .reveal.visible { opacity: 1; transform: translateY(0); }

  /* Theme toggle */
  .theme-toggle {
    width: 44px;
    height: 24px;
    border-radius: 999px;
    background: rgba(184, 147, 90, 0.2);
    border: 1px solid rgba(184, 147, 90, 0.3);
    position: relative;
    cursor: pointer;
    transition: all 0.3s ease;
  }
  .theme-toggle::after {
    content: '';
    position: absolute;
    top: 2px; left: 2px;
    width: 18px; height: 18px;
    border-radius: 50%;
    background: linear-gradient(135deg, #B8935A, #D4B896);
    transition: transform 0.3s ease;
    box-shadow: 0 2px 6px rgba(184, 147, 90, 0.4);
  }
  body.dark .theme-toggle::after { transform: translateX(20px); }

  /* Hero orb container */
  .hero-orb-wrap {
    position: relative;
    width: 100%;
    aspect-ratio: 1;
    max-width: 520px;
    margin: 0 auto;
  }
  #heroCanvas {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
  }
  .hero-stat-card {
    position: absolute;
    z-index: 10;
    padding: 12px 16px;
    border-radius: 16px;
    backdrop-filter: blur(20px);
    background: rgba(255, 255, 255, 0.7);
    border: 1px solid rgba(184, 147, 90, 0.2);
    box-shadow: 0 8px 30px rgba(184, 147, 90, 0.1);
  }
  body.dark .hero-stat-card {
    background: rgba(26, 23, 20, 0.7);
    border-color: rgba(212, 184, 150, 0.15);
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
  }
</style>
</head>

<body class="bg-cream-100 text-cream-900 antialiased">

<!-- Interactive background canvas -->
<canvas id="bgCanvas"></canvas>

<!-- ════════════════════════════════════════════════════════════ -->
<!-- PRELOADER: Liquid Capsule                                    -->
<!-- ════════════════════════════════════════════════════════════ -->
<div id="preloader">
  <div class="text-center">
    <div class="flex items-center justify-center gap-3 mb-8">
      <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-cream-500 to-cream-700 flex items-center justify-center shadow-lg shadow-cream-500/30">
        <i data-lucide="droplets" class="w-6 h-6 text-white"></i>
      </div>
      <div class="text-left">
        <h1 class="font-display font-bold text-2xl tracking-tight">AquaFlow</h1>
        <p class="text-xs text-cream-700 -mt-1">Logistics</p>
      </div>
    </div>

    <p class="text-sm font-medium mb-4 opacity-70">Preparing pure experience...</p>

    <!-- Liquid capsule loader -->
    <div class="liquid-capsule">
      <div class="liquid-fill" id="liquidFill">
        <div class="liquid-wave"></div>
        <div class="liquid-bubbles">
          <div class="liquid-bubble" style="left: 15%; animation-delay: 0s;"></div>
          <div class="liquid-bubble" style="left: 35%; animation-delay: 0.6s;"></div>
          <div class="liquid-bubble" style="left: 55%; animation-delay: 1.2s;"></div>
          <div class="liquid-bubble" style="left: 75%; animation-delay: 1.8s;"></div>
          <div class="liquid-bubble" style="left: 90%; animation-delay: 0.3s;"></div>
        </div>
      </div>
      <div class="loader-percent" id="progressPercent">0%</div>
    </div>

    <p class="text-[11px] mt-5 opacity-50 font-mono tracking-widest">AQUAFLOW · EST. 2026</p>
  </div>
</div>

<!-- ════════════════════════════════════════════════════════════ -->
<!-- MAIN APP                                                     -->
<!-- ════════════════════════════════════════════════════════════ -->
<div id="mainApp" class="opacity-0 transition-opacity duration-1000 relative z-10">

  <!-- ─── NAVBAR ─── -->
  <nav class="fixed top-0 left-0 right-0 z-50 glass-strong border-b border-cream-500/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <a href="#" class="flex items-center gap-2.5 group">
          <div class="w-9 h-9 rounded-lg bg-gradient-to-br from-cream-500 to-cream-700 flex items-center justify-center shadow-lg shadow-cream-500/30 group-hover:shadow-cream-500/50 transition">
            <i data-lucide="droplets" class="w-5 h-5 text-white"></i>
          </div>
          <div class="leading-tight">
            <div class="font-display font-bold text-lg">AquaFlow</div>
            <div class="text-[10px] text-cream-700 -mt-0.5 tracking-widest uppercase">Logistics</div>
          </div>
        </a>

        <div class="hidden md:flex items-center gap-8 text-sm font-medium">
          <a href="#home" class="hover:text-cream-600 transition">Home</a>
          <a href="#features" class="hover:text-cream-600 transition">Features</a>
          <a href="#dashboard" class="hover:text-cream-600 transition">Track Order</a>
          <a href="#contact" class="hover:text-cream-600 transition">Contact</a>
        </div>

        <div class="flex items-center gap-3">
          <div class="theme-toggle" onclick="toggleTheme()" title="Toggle theme"></div>
          <button onclick="openBookingModal()" class="btn-shine bg-gradient-to-r from-cream-600 to-cream-700 hover:from-cream-500 hover:to-cream-600 text-white px-5 py-2.5 rounded-xl font-semibold text-sm shadow-lg shadow-cream-500/30 hover:shadow-cream-500/50 transition-all flex items-center gap-2">
            <i data-lucide="truck" class="w-4 h-4"></i>
            <span>Book Tanker</span>
          </button>
        </div>
      </div>
    </div>
  </nav>

  <!-- ─── HERO ─── -->
  <section id="home" class="relative min-h-screen pt-24 pb-20 overflow-hidden">
    <div class="ambient-blob bg-cream-400 w-[500px] h-[500px] -top-40 -left-40"></div>
    <div class="ambient-blob bg-cream-500 w-[400px] h-[400px] top-1/2 -right-40 opacity-20"></div>
    <div class="absolute inset-0 grid-pattern"></div>

    <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-10">
      <div class="grid lg:grid-cols-2 gap-12 items-center">
        <!-- Left: Copy -->
        <div class="animate-fade-in">
          <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full glass border border-cream-500/30 text-xs font-medium text-cream-700 mb-6">
            <span class="relative flex h-2 w-2">
              <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-cream-500 opacity-75"></span>
              <span class="relative inline-flex rounded-full h-2 w-2 bg-cream-600"></span>
            </span>
            Live Service Across 120+ Cities
          </div>

          <h1 class="font-display font-extrabold text-5xl sm:text-6xl lg:text-7xl leading-[1.05] tracking-tight mb-6">
            Reliable Water Delivery,
            <span class="gradient-text block font-serif italic font-medium">On Demand.</span>
          </h1>

          <p class="text-lg opacity-70 max-w-xl mb-8 leading-relaxed">
            From homes to industries — book verified water tankers in seconds. Real-time tracking, transparent pricing, and on-time delivery guaranteed.
          </p>

          <div class="flex flex-col sm:flex-row gap-4 mb-12">
            <button onclick="openBookingModal()" class="btn-shine group bg-gradient-to-r from-cream-600 to-cream-700 hover:from-cream-500 hover:to-cream-600 text-white px-7 py-4 rounded-xl font-semibold shadow-xl shadow-cream-500/30 hover:shadow-cream-500/50 transition-all flex items-center justify-center gap-2">
              <i data-lucide="calendar-plus" class="w-5 h-5"></i>
              Book a Tanker
              <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-1 transition"></i>
            </button>
            <a href="#dashboard" class="glass border border-cream-500/30 hover:border-cream-500/60 px-7 py-4 rounded-xl font-semibold transition-all flex items-center justify-center gap-2">
              <i data-lucide="map-pin" class="w-5 h-5 text-cream-600"></i>
              Track My Order
            </a>
          </div>

          <!-- Stats -->
          <div class="grid grid-cols-3 gap-4 max-w-lg">
            <div>
              <div class="font-display font-bold text-3xl">98<span class="gradient-text">%</span></div>
              <div class="text-xs opacity-60 mt-1">On-time Delivery</div>
            </div>
            <div>
              <div class="font-display font-bold text-3xl">2.4<span class="gradient-text">M</span></div>
              <div class="text-xs opacity-60 mt-1">Liters Delivered</div>
            </div>
            <div>
              <div class="font-display font-bold text-3xl">50<span class="gradient-text">K+</span></div>
              <div class="text-xs opacity-60 mt-1">Happy Customers</div>
            </div>
          </div>
        </div>

        <!-- Right: 3D Water Orb -->
        <div class="relative animate-slide-up">
          <div class="hero-orb-wrap">
            <canvas id="heroCanvas"></canvas>

            <!-- Floating stat cards -->
            <div class="hero-stat-card top-6 right-0 animate-float" style="animation-delay: 0.3s">
              <div class="flex items-center gap-2.5">
                <div class="w-9 h-9 rounded-xl bg-green-500/15 flex items-center justify-center">
                  <i data-lucide="check-circle-2" class="w-4 h-4 text-green-600"></i>
                </div>
                <div>
                  <div class="text-[10px] opacity-60">Verified</div>
                  <div class="text-sm font-semibold">ISO Certified</div>
                </div>
              </div>
            </div>

            <div class="hero-stat-card bottom-16 left-0 animate-float" style="animation-delay: 0.8s">
              <div class="flex items-center gap-2.5">
                <div class="w-9 h-9 rounded-xl bg-cream-500/15 flex items-center justify-center">
                  <i data-lucide="navigation" class="w-4 h-4 text-cream-600"></i>
                </div>
                <div>
                  <div class="text-[10px] opacity-60">Live Tracking</div>
                  <div class="text-sm font-semibold">GPS Enabled</div>
                </div>
              </div>
            </div>

            <div class="hero-stat-card top-1/2 -left-4 animate-float" style="animation-delay: 1.3s">
              <div class="flex items-center gap-2.5">
                <div class="w-9 h-9 rounded-xl bg-blue-500/15 flex items-center justify-center">
                  <i data-lucide="droplet" class="w-4 h-4 text-blue-600"></i>
                </div>
                <div>
                  <div class="text-[10px] opacity-60">Purity</div>
                  <div class="text-sm font-semibold">99.9% Pure</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ─── FEATURES ─── -->
  <section id="features" class="relative py-24 overflow-hidden">
    <div class="ambient-blob bg-cream-500 w-[400px] h-[400px] top-20 left-1/2 -translate-x-1/2 opacity-20"></div>

    <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16 reveal">
        <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full glass border border-cream-500/30 text-xs font-medium text-cream-700 mb-4">
          <i data-lucide="sparkles" class="w-3 h-3"></i>
          Why Choose AquaFlow
        </div>
        <h2 class="font-display font-bold text-4xl sm:text-5xl mb-4">
          Built for <span class="gradient-text font-serif italic">Speed, Safety & Scale</span>
        </h2>
        <p class="opacity-70 max-w-2xl mx-auto">
          Every drop delivered with precision. Our fleet, technology, and team are engineered to serve you reliably.
        </p>
      </div>

      <div class="grid md:grid-cols-3 gap-6">
        <div class="reveal glass rounded-3xl p-8 accent-glow hover:accent-glow-strong transition-all group">
          <div class="w-14 h-14 rounded-2xl bg-gradient-to-br from-cream-500/20 to-cream-700/20 border border-cream-500/30 flex items-center justify-center mb-6 group-hover:scale-110 transition">
            <i data-lucide="gauge" class="w-7 h-7 text-cream-600"></i>
          </div>
          <h3 class="font-display font-bold text-xl mb-3">Flexible Capacity</h3>
          <p class="opacity-70 text-sm leading-relaxed mb-5">
            From 1,000L residential tankers to 10,000L industrial giants — pick the exact size for your needs.
          </p>
          <div class="flex flex-wrap gap-2">
            <span class="px-3 py-1 rounded-full bg-cream-500/10 border border-cream-500/20 text-xs text-cream-700">1,000L</span>
            <span class="px-3 py-1 rounded-full bg-cream-500/10 border border-cream-500/20 text-xs text-cream-700">5,000L</span>
            <span class="px-3 py-1 rounded-full bg-cream-500/10 border border-cream-500/20 text-xs text-cream-700">10,000L</span>
          </div>
        </div>

        <div class="reveal glass rounded-3xl p-8 accent-glow hover:accent-glow-strong transition-all group" style="transition-delay: 0.1s">
          <div class="w-14 h-14 rounded-2xl bg-gradient-to-br from-cream-500/20 to-cream-700/20 border border-cream-500/30 flex items-center justify-center mb-6 group-hover:scale-110 transition">
            <i data-lucide="navigation" class="w-7 h-7 text-cream-600"></i>
          </div>
          <h3 class="font-display font-bold text-xl mb-3">Live GPS Tracking</h3>
          <p class="opacity-70 text-sm leading-relaxed mb-5">
            Watch your tanker approach in real-time. Get ETAs, driver details, and instant notifications at every step.
          </p>
          <div class="flex items-center gap-2 text-xs text-cream-700">
            <span class="relative flex h-2 w-2">
              <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-500 opacity-75"></span>
              <span class="relative inline-flex rounded-full h-2 w-2 bg-green-600"></span>
            </span>
            Real-time updates every 30s
          </div>
        </div>

        <div class="reveal glass rounded-3xl p-8 accent-glow hover:accent-glow-strong transition-all group" style="transition-delay: 0.2s">
          <div class="w-14 h-14 rounded-2xl bg-gradient-to-br from-cream-500/20 to-cream-700/20 border border-cream-500/30 flex items-center justify-center mb-6 group-hover:scale-110 transition">
            <i data-lucide="shield-check" class="w-7 h-7 text-cream-600"></i>
          </div>
          <h3 class="font-display font-bold text-xl mb-3">Verified Safety</h3>
          <p class="opacity-70 text-sm leading-relaxed mb-5">
            Every tanker is BIS-certified, water-quality tested, and driven by background-verified professionals.
          </p>
          <div class="flex items-center gap-4 text-xs">
            <div class="flex items-center gap-1.5">
              <i data-lucide="award" class="w-3.5 h-3.5 text-cream-600"></i>
              BIS Certified
            </div>
            <div class="flex items-center gap-1.5">
              <i data-lucide="flask-conical" class="w-3.5 h-3.5 text-cream-600"></i>
              Lab Tested
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ─── DASHBOARD / TRACKER ─── -->
  <section id="dashboard" class="relative py-24 overflow-hidden">
    <div class="ambient-blob bg-cream-500 w-[500px] h-[500px] -bottom-40 -right-40 opacity-20"></div>

    <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-12 reveal">
        <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full glass border border-cream-500/30 text-xs font-medium text-cream-700 mb-4">
          <i data-lucide="radar" class="w-3 h-3"></i>
          Live Order Tracker
        </div>
        <h2 class="font-display font-bold text-4xl sm:text-5xl mb-4">
          Track Your <span class="gradient-text font-serif italic">Delivery</span>
        </h2>
        <p class="opacity-70 max-w-2xl mx-auto">
          Enter your Booking ID to see real-time status of your water tanker delivery.
        </p>
      </div>

      <div class="max-w-2xl mx-auto mb-10 reveal">
        <div class="glass rounded-2xl p-6 accent-glow">
          <label class="text-xs font-semibold text-cream-700 uppercase tracking-wider mb-2 block">Booking ID</label>
          <div class="flex gap-3">
            <div class="flex-1 relative">
              <i data-lucide="search" class="absolute left-4 top-1/2 -translate-y-1/2 w-4 h-4 opacity-50"></i>
              <input id="trackInput" type="text" placeholder="e.g. AF-94821" class="input-field pl-11" />
            </div>
            <button onclick="trackOrder()" class="btn-shine bg-gradient-to-r from-cream-600 to-cream-700 hover:from-cream-500 hover:to-cream-600 text-white px-6 py-3 rounded-xl font-semibold shadow-lg shadow-cream-500/30 transition-all flex items-center gap-2">
              <i data-lucide="search" class="w-4 h-4"></i>
              Track
            </button>
          </div>
          <p class="text-xs opacity-50 mt-3">Try: <button onclick="document.getElementById('trackInput').value='AF-94821';trackOrder()" class="text-cream-600 hover:underline font-semibold">AF-94821</button> or <button onclick="document.getElementById('trackInput').value='AF-58203';trackOrder()" class="text-cream-600 hover:underline font-semibold">AF-58203</button></p>
        </div>
      </div>

      <div id="trackerResult" class="max-w-3xl mx-auto hidden">
        <div class="glass rounded-3xl p-8 accent-glow">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-8 pb-6 border-b border-cream-500/10">
            <div>
              <div class="text-xs opacity-60 mb-1">Booking ID</div>
              <div class="font-display font-bold text-2xl" id="trackBookingId">AF-94821</div>
            </div>
            <div class="flex items-center gap-2 px-3 py-1.5 rounded-full bg-cream-500/15 border border-cream-500/30">
              <span class="relative flex h-2 w-2">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-cream-500 opacity-75"></span>
                <span class="relative inline-flex rounded-full h-2 w-2 bg-cream-600"></span>
              </span>
              <span class="text-sm font-semibold text-cream-700" id="trackStatus">Out for Delivery</span>
            </div>
          </div>

          <div class="space-y-0" id="timelineContainer"></div>

          <div class="mt-8 pt-6 border-t border-cream-500/10 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
            <div class="flex items-center gap-3">
              <div class="w-12 h-12 rounded-full bg-gradient-to-br from-cream-500 to-cream-700 flex items-center justify-center text-white font-bold">RK</div>
              <div>
                <div class="font-semibold">Rajesh Kumar</div>
                <div class="text-xs opacity-60">Driver • Vehicle MH-12-AB-4521</div>
              </div>
            </div>
            <div class="flex gap-2">
              <button class="glass border border-cream-500/30 hover:border-cream-500/60 px-4 py-2 rounded-xl text-sm font-medium flex items-center gap-2 transition">
                <i data-lucide="phone" class="w-4 h-4 text-cream-600"></i>
                Call
              </button>
              <button class="glass border border-cream-500/30 hover:border-cream-500/60 px-4 py-2 rounded-xl text-sm font-medium flex items-center gap-2 transition">
                <i data-lucide="message-square" class="w-4 h-4 text-cream-600"></i>
                Message
              </button>
            </div>
          </div>
        </div>
      </div>

      <div id="trackerEmpty" class="max-w-md mx-auto text-center py-12 hidden">
        <div class="w-16 h-16 mx-auto rounded-2xl glass flex items-center justify-center mb-4">
          <i data-lucide="package-search" class="w-8 h-8 opacity-50"></i>
        </div>
        <p class="opacity-70">No booking found with that ID. Please check and try again.</p>
      </div>
    </div>
  </section>

  <!-- ─── CTA ─── -->
  <section class="relative py-20 overflow-hidden">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="reveal glass-strong rounded-3xl p-10 sm:p-16 text-center accent-glow-strong relative overflow-hidden">
        <div class="ambient-blob bg-cream-500 w-[300px] h-[300px] -top-20 -right-20 opacity-30"></div>
        <div class="relative">
          <h2 class="font-display font-bold text-3xl sm:text-5xl mb-4">
            Ready for <span class="gradient-text font-serif italic">Crystal-Clear</span> Delivery?
          </h2>
          <p class="opacity-70 max-w-xl mx-auto mb-8">
            Join 50,000+ homes and businesses that trust AquaFlow for their daily water needs.
          </p>
          <button onclick="openBookingModal()" class="btn-shine bg-gradient-to-r from-cream-600 to-cream-700 hover:from-cream-500 hover:to-cream-600 text-white px-8 py-4 rounded-xl font-semibold text-lg shadow-xl shadow-cream-500/40 hover:shadow-cream-500/60 transition-all inline-flex items-center gap-2">
            <i data-lucide="sparkles" class="w-5 h-5"></i>
            Book Your Tanker Now
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- ─── FOOTER ─── -->
  <footer id="contact" class="relative border-t border-cream-500/10 py-12 mt-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid md:grid-cols-4 gap-8 mb-10">
        <div class="md:col-span-2">
          <div class="flex items-center gap-2.5 mb-4">
            <div class="w-9 h-9 rounded-lg bg-gradient-to-br from-cream-500 to-cream-700 flex items-center justify-center">
              <i data-lucide="droplets" class="w-5 h-5 text-white"></i>
            </div>
            <div>
              <div class="font-display font-bold text-lg">AquaFlow</div>
              <div class="text-[10px] text-cream-700 -mt-0.5 tracking-widest uppercase">Logistics</div>
            </div>
          </div>
          <p class="opacity-70 text-sm max-w-sm mb-4">
            India's most trusted on-demand water tanker delivery platform. Pure water, delivered pure & simple.
          </p>
          <div class="flex gap-3">
            <a href="#" class="w-9 h-9 rounded-lg glass border border-cream-500/20 flex items-center justify-center hover:border-cream-500/50 transition">
              <i data-lucide="twitter" class="w-4 h-4 text-cream-600"></i>
            </a>
            <a href="#" class="w-9 h-9 rounded-lg glass border border-cream-500/20 flex items-center justify-center hover:border-cream-500/50 transition">
              <i data-lucide="instagram" class="w-4 h-4 text-cream-600"></i>
            </a>
            <a href="#" class="w-9 h-9 rounded-lg glass border border-cream-500/20 flex items-center justify-center hover:border-cream-500/50 transition">
              <i data-lucide="facebook" class="w-4 h-4 text-cream-600"></i>
            </a>
          </div>
        </div>

        <div>
          <h4 class="font-semibold mb-4 text-sm">Company</h4>
          <ul class="space-y-2 text-sm opacity-70">
            <li><a href="#" class="hover:text-cream-600 transition">About Us</a></li>
            <li><a href="#" class="hover:text-cream-600 transition">Careers</a></li>
            <li><a href="#" class="hover:text-cream-600 transition">Blog</a></li>
            <li><a href="#" class="hover:text-cream-600 transition">Press</a></li>
          </ul>
        </div>

        <div>
          <h4 class="font-semibold mb-4 text-sm">Support</h4>
          <ul class="space-y-2 text-sm opacity-70">
            <li class="flex items-center gap-2"><i data-lucide="phone" class="w-3.5 h-3.5 text-cream-600"></i> 1800-AQUA-FLOW</li>
            <li class="flex items-center gap-2"><i data-lucide="mail" class="w-3.5 h-3.5 text-cream-600"></i> help@aquaflow.in</li>
            <li class="flex items-center gap-2"><i data-lucide="map-pin" class="w-3.5 h-3.5 text-cream-600"></i> Mumbai, India</li>
          </ul>
        </div>
      </div>

      <div class="pt-8 border-t border-cream-500/10 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs opacity-60">
        <p>© 2026 AquaFlow Logistics Pvt. Ltd. All rights reserved.</p>
        <div class="flex gap-6">
          <a href="#" class="hover:text-cream-600 transition">Privacy</a>
          <a href="#" class="hover:text-cream-600 transition">Terms</a>
          <a href="#" class="hover:text-cream-600 transition">Refunds</a>
        </div>
      </div>
    </div>
  </footer>
</div>

<!-- ════════════════════════════════════════════════════════════ -->
<!-- BOOKING MODAL                                                -->
<!-- ════════════════════════════════════════════════════════════ -->
<div id="bookingModal" class="modal-backdrop">
  <div class="modal-panel glass-strong rounded-3xl w-full max-w-2xl accent-glow-strong">
    <div class="flex items-center justify-between p-6 border-b border-cream-500/10">
      <div>
        <h3 class="font-display font-bold text-2xl">Book Your Tanker</h3>
        <p class="text-xs opacity-60 mt-0.5">Step <span id="currentStepNum">1</span> of 5</p>
      </div>
      <button onclick="closeBookingModal()" class="w-9 h-9 rounded-lg hover:bg-cream-500/10 flex items-center justify-center transition">
        <i data-lucide="x" class="w-5 h-5 opacity-60"></i>
      </button>
    </div>

    <div class="px-6 pt-6">
      <div class="flex items-center justify-between mb-2">
        <div class="step-dot active w-8 h-8 rounded-full flex items-center justify-center text-xs font-bold border border-cream-500/30" data-step="1">1</div>
        <div class="step-line flex-1 h-0.5 bg-cream-500/20 mx-2" data-line="1"></div>
        <div class="step-dot w-8 h-8 rounded-full flex items-center justify-center text-xs font-bold border border-cream-500/20 opacity-50" data-step="2">2</div>
        <div class="step-line flex-1 h-0.5 bg-cream-500/20 mx-2" data-line="2"></div>
        <div class="step-dot w-8 h-8 rounded-full flex items-center justify-center text-xs font-bold border border-cream-500/20 opacity-50" data-step="3">3</div>
        <div class="step-line flex-1 h-0.5 bg-cream-500/20 mx-2" data-line="3"></div>
        <div class="step-dot w-8 h-8 rounded-full flex items-center justify-center text-xs font-bold border border-cream-500/20 opacity-50" data-step="4">4</div>
        <div class="step-line flex-1 h-0.5 bg-cream-500/20 mx-2" data-line="4"></div>
        <div class="step-dot w-8 h-8 rounded-full flex items-center justify-center text-xs font-bold border border-cream-500/20 opacity-50" data-step="5">5</div>
      </div>
      <div class="flex justify-between text-[10px] opacity-60 font-medium px-1">
        <span>Details</span><span>Address</span><span>Capacity</span><span>Schedule</span><span>Payment</span>
      </div>
    </div>

    <div class="p-6">
      <div class="booking-step" data-step="1">
        <h4 class="font-display font-semibold text-lg mb-1">Personal Details</h4>
        <p class="text-sm opacity-60 mb-5">Let us know who's receiving the delivery.</p>
        <div class="space-y-4">
          <div>
            <label class="text-xs font-semibold opacity-70 uppercase tracking-wider mb-1.5 block">Full Name</label>
            <div class="relative">
              <i data-lucide="user" class="absolute left-4 top-1/2 -translate-y-1/2 w-4 h-4 opacity-50"></i>
              <input id="fullName" type="text" placeholder="John Doe" class="input-field pl-11" />
            </div>
          </div>
          <div>
            <label class="text-xs font-semibold opacity-70 uppercase tracking-wider mb-1.5 block">Phone Number</label>
            <div class="relative">
              <i data-lucide="phone" class="absolute left-4 top-1/2 -translate-y-1/2 w-4 h-4 opacity-50"></i>
              <input id="phone" type="tel" placeholder="+91 98765 43210" maxlength="15" class="input-field pl-11" />
            </div>
          </div>
          <div>
            <label class="text-xs font-semibold opacity-70 uppercase tracking-wider mb-1.5 block">Email (Optional)</label>
            <div class="relative">
              <i data-lucide="mail" class="absolute left-4 top-1/2 -translate-y-1/2 w-4 h-4 opacity-50"></i>
              <input id="email" type="email" placeholder="you@example.com" class="input-field pl-11" />
            </div>
          </div>
        </div>
      </div>

      <div class="booking-step hidden" data-step="2">
        <h4 class="font-display font-semibold text-lg mb-1">Delivery Address</h4>
        <p class="text-sm opacity-60 mb-5">Where should we deliver your water?</p>
        <div class="space-y-4">
          <div>
            <label class="text-xs font-semibold opacity-70 uppercase tracking-wider mb-1.5 block">Full Address</label>
            <textarea id="address" rows="3" placeholder="House No, Street, Locality..." class="input-field resize-none"></textarea>
          </div>
          <div class="grid grid-cols-2 gap-3">
            <div>
              <label class="text-xs font-semibold opacity-70 uppercase tracking-wider mb-1.5 block">City</label>
              <input id="city" type="text" placeholder="Mumbai" class="input-field" />
            </div>
            <div>
              <label class="text-xs font-semibold opacity-70 uppercase tracking-wider mb-1.5 block">Pincode</label>
              <input id="pincode" type="text" placeholder="400001" maxlength="6" class="input-field" />
            </div>
          </div>
          <div>
            <label class="text-xs font-semibold opacity-70 uppercase tracking-wider mb-1.5 block">Landmark (Optional)</label>
            <div class="relative">
              <i data-lucide="map-pin" class="absolute left-4 top-3.5 w-4 h-4 opacity-50"></i>
              <input id="landmark" type="text" placeholder="Near City Mall" class="input-field pl-11" />
            </div>
          </div>
        </div>
      </div>

      <div class="booking-step hidden" data-step="3">
        <h4 class="font-display font-semibold text-lg mb-1">Select Tanker Capacity</h4>
        <p class="text-sm opacity-60 mb-5">Choose the right size for your needs.</p>
        <div class="space-y-3">
          <div class="capacity-card glass rounded-2xl p-5 border border-cream-500/20" data-capacity="1000" data-price="1200" data-label="Residential">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-4">
                <div class="w-12 h-12 rounded-xl bg-cream-500/15 border border-cream-500/30 flex items-center justify-center">
                  <i data-lucide="home" class="w-6 h-6 text-cream-600"></i>
                </div>
                <div>
                  <div class="font-semibold">Residential</div>
                  <div class="text-xs opacity-60">1,000 Liters • Small homes</div>
                </div>
              </div>
              <div class="text-right">
                <div class="font-display font-bold text-xl">₹1,200</div>
                <div class="text-[10px] opacity-50">₹1.20/L</div>
              </div>
            </div>
          </div>

          <div class="capacity-card glass rounded-2xl p-5 border border-cream-500/20 relative" data-capacity="5000" data-price="5500" data-label="Commercial">
            <div class="absolute -top-2 right-4 px-2 py-0.5 rounded-full bg-gradient-to-r from-cream-500 to-cream-700 text-[10px] font-bold text-white uppercase tracking-wider">Popular</div>
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-4">
                <div class="w-12 h-12 rounded-xl bg-cream-500/15 border border-cream-500/30 flex items-center justify-center">
                  <i data-lucide="building-2" class="w-6 h-6 text-cream-600"></i>
                </div>
                <div>
                  <div class="font-semibold">Commercial</div>
                  <div class="text-xs opacity-60">5,000 Liters • Offices & societies</div>
                </div>
              </div>
              <div class="text-right">
                <div class="font-display font-bold text-xl">₹5,500</div>
                <div class="text-[10px] opacity-50">₹1.10/L</div>
              </div>
            </div>
          </div>

          <div class="capacity-card glass rounded-2xl p-5 border border-cream-500/20" data-capacity="10000" data-price="10000" data-label="Industrial">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-4">
                <div class="w-12 h-12 rounded-xl bg-cream-500/15 border border-cream-500/30 flex items-center justify-center">
                  <i data-lucide="factory" class="w-6 h-6 text-cream-600"></i>
                </div>
                <div>
                  <div class="font-semibold">Industrial</div>
                  <div class="text-xs opacity-60">10,000 Liters • Factories & bulk</div>
                </div>
              </div>
              <div class="text-right">
                <div class="font-display font-bold text-xl">₹10,000</div>
                <div class="text-[10px] opacity-50">₹1.00/L</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="booking-step hidden" data-step="4">
        <h4 class="font-display font-semibold text-lg mb-1">Pick Date & Time</h4>
        <p class="text-sm opacity-60 mb-5">Choose a convenient delivery slot.</p>
        <div class="space-y-5">
          <div>
            <label class="text-xs font-semibold opacity-70 uppercase tracking-wider mb-2 block">Delivery Date</label>
            <input id="deliveryDate" type="date" class="input-field" />
          </div>
          <div>
            <label class="text-xs font-semibold opacity-70 uppercase tracking-wider mb-2 block">Time Slot</label>
            <div class="grid grid-cols-2 sm:grid-cols-3 gap-2">
              <div class="time-slot glass rounded-xl p-3 border border-cream-500/20 text-center" data-slot="06:00 - 08:00 AM">
                <div class="text-xs opacity-60">Early</div>
                <div class="text-sm font-semibold">6 - 8 AM</div>
              </div>
              <div class="time-slot glass rounded-xl p-3 border border-cream-500/20 text-center" data-slot="08:00 - 10:00 AM">
                <div class="text-xs opacity-60">Morning</div>
                <div class="text-sm font-semibold">8 - 10 AM</div>
              </div>
              <div class="time-slot glass rounded-xl p-3 border border-cream-500/20 text-center" data-slot="10:00 - 12:00 PM">
                <div class="text-xs opacity-60">Late Morning</div>
                <div class="text-sm font-semibold">10 - 12 PM</div>
              </div>
              <div class="time-slot glass rounded-xl p-3 border border-cream-500/20 text-center" data-slot="02:00 - 04:00 PM">
                <div class="text-xs opacity-60">Afternoon</div>
                <div class="text-sm font-semibold">2 - 4 PM</div>
              </div>
              <div class="time-slot glass rounded-xl p-3 border border-cream-500/20 text-center" data-slot="04:00 - 06:00 PM">
                <div class="text-xs opacity-60">Evening</div>
                <div class="text-sm font-semibold">4 - 6 PM</div>
              </div>
              <div class="time-slot glass rounded-xl p-3 border border-cream-500/20 text-center disabled" data-slot="">
                <div class="text-xs opacity-60">Night</div>
                <div class="text-sm font-semibold">6 - 8 PM</div>
                <div class="text-[9px] text-red-500 mt-0.5">Full</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="booking-step hidden" data-step="5">
        <h4 class="font-display font-semibold text-lg mb-1">Payment Method</h4>
        <p class="text-sm opacity-60 mb-5">Choose how you'd like to pay.</p>
        <div class="space-y-3 mb-6">
          <label class="flex items-center gap-4 glass rounded-2xl p-4 border border-cream-500/20 cursor-pointer hover:border-cream-500/50 transition">
            <input type="radio" name="payment" value="UPI" class="w-4 h-4 accent-cream-600" checked />
            <div class="w-10 h-10 rounded-lg bg-cream-500/15 border border-cream-500/30 flex items-center justify-center">
              <i data-lucide="smartphone" class="w-5 h-5 text-cream-600"></i>
            </div>
            <div class="flex-1">
              <div class="font-semibold text-sm">UPI / Online</div>
              <div class="text-xs opacity-60">Pay via GPay, PhonePe, Paytm</div>
            </div>
          </label>
          <label class="flex items-center gap-4 glass rounded-2xl p-4 border border-cream-500/20 cursor-pointer hover:border-cream-500/50 transition">
            <input type="radio" name="payment" value="Card" class="w-4 h-4 accent-cream-600" />
            <div class="w-10 h-10 rounded-lg bg-cream-500/15 border border-cream-500/30 flex items-center justify-center">
              <i data-lucide="credit-card" class="w-5 h-5 text-cream-600"></i>
            </div>
            <div class="flex-1">
              <div class="font-semibold text-sm">Credit / Debit Card</div>
              <div class="text-xs opacity-60">Visa, Mastercard, RuPay</div>
            </div>
          </label>
          <label class="flex items-center gap-4 glass rounded-2xl p-4 border border-cream-500/20 cursor-pointer hover:border-cream-500/50 transition">
            <input type="radio" name="payment" value="COD" class="w-4 h-4 accent-cream-600" />
            <div class="w-10 h-10 rounded-lg bg-cream-500/15 border border-cream-500/30 flex items-center justify-center">
              <i data-lucide="banknote" class="w-5 h-5 text-cream-600"></i>
            </div>
            <div class="flex-1">
              <div class="font-semibold text-sm">Cash on Delivery</div>
              <div class="text-xs opacity-60">Pay when the tanker arrives</div>
            </div>
          </label>
        </div>

        <div class="glass rounded-2xl p-5 border border-cream-500/20">
          <div class="text-xs font-semibold text-cream-700 uppercase tracking-wider mb-3">Order Summary</div>
          <div class="space-y-2 text-sm">
            <div class="flex justify-between opacity-80">
              <span>Tanker (<span id="sumCapacity">—</span>)</span>
              <span id="sumBase">₹0</span>
            </div>
            <div class="flex justify-between opacity-80">
              <span>Delivery Fee</span>
              <span class="text-green-600">FREE</span>
            </div>
            <div class="flex justify-between opacity-80">
              <span>GST (5%)</span>
              <span id="sumGst">₹0</span>
            </div>
            <div class="border-t border-cream-500/10 pt-2 mt-2 flex justify-between">
              <span class="font-semibold">Total</span>
              <span class="font-display font-bold text-xl gradient-text" id="sumTotal">₹0</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="p-6 border-t border-cream-500/10 flex items-center justify-between gap-3">
      <button id="prevBtn" onclick="prevStep()" class="px-5 py-2.5 rounded-xl text-sm font-semibold opacity-70 hover:bg-cream-500/10 transition hidden">← Back</button>
      <div class="flex-1"></div>
      <button id="nextBtn" onclick="nextStep()" class="btn-shine bg-gradient-to-r from-cream-600 to-cream-700 hover:from-cream-500 hover:to-cream-600 text-white px-6 py-2.5 rounded-xl font-semibold text-sm shadow-lg shadow-cream-500/30 transition-all flex items-center gap-2">
        Continue <i data-lucide="arrow-right" class="w-4 h-4"></i>
      </button>
    </div>
  </div>
</div>

<!-- ════════════════════════════════════════════════════════════ -->
<!-- RECEIPT MODAL                                                -->
<!-- ════════════════════════════════════════════════════════════ -->
<div id="receiptModal" class="modal-backdrop">
  <div class="modal-panel glass-strong rounded-3xl w-full max-w-md accent-glow-strong">
    <div id="receipt-print" class="p-6">
      <div class="text-center mb-6 pb-6 border-b border-cream-500/10">
        <div class="w-16 h-16 mx-auto rounded-full bg-gradient-to-br from-green-500 to-green-700 flex items-center justify-center mb-4 shadow-lg shadow-green-500/30">
          <i data-lucide="check" class="w-8 h-8 text-white"></i>
        </div>
        <h3 class="font-display font-bold text-2xl mb-1">Booking Confirmed!</h3>
        <p class="text-sm opacity-60">Your water tanker is on the way.</p>
      </div>

      <div class="glass rounded-xl p-4 mb-4 border border-cream-500/20 text-center">
        <div class="text-[10px] opacity-60 uppercase tracking-widest">Booking ID</div>
        <div class="font-display font-bold text-2xl gradient-text" id="receiptId">#AF-00000</div>
        <div class="text-xs opacity-60 mt-1" id="receiptTimestamp">—</div>
      </div>

      <div class="mb-4">
        <div class="text-[10px] opacity-60 uppercase tracking-widest mb-2">Customer</div>
        <div class="glass rounded-xl p-4 border border-cream-500/20 text-sm">
          <div class="font-semibold" id="receiptName">—</div>
          <div class="opacity-60 text-xs mt-0.5" id="receiptPhone">—</div>
          <div class="text-xs mt-2 pt-2 border-t border-cream-500/10" id="receiptAddress">—</div>
        </div>
      </div>

      <div class="mb-4">
        <div class="text-[10px] opacity-60 uppercase tracking-widest mb-2">Scheduled Delivery</div>
        <div class="glass rounded-xl p-4 border border-cream-500/20 text-sm flex items-center gap-3">
          <i data-lucide="calendar" class="w-5 h-5 text-cream-600"></i>
          <div>
            <div class="font-semibold" id="receiptDate">—</div>
            <div class="text-xs opacity-60" id="receiptSlot">—</div>
          </div>
        </div>
      </div>

      <div class="mb-4">
        <div class="text-[10px] opacity-60 uppercase tracking-widest mb-2">Bill Breakdown</div>
        <div class="glass rounded-xl p-4 border border-cream-500/20 text-sm">
          <div class="space-y-2">
            <div class="flex justify-between opacity-80">
              <span id="receiptItem">Tanker (—)</span>
              <span id="receiptBase">₹0</span>
            </div>
            <div class="flex justify-between opacity-80">
              <span>Delivery Fee</span>
              <span class="text-green-600">FREE</span>
            </div>
            <div class="flex justify-between opacity-80">
              <span>GST (5%)</span>
              <span id="receiptGst">₹0</span>
            </div>
            <div class="border-t border-cream-500/10 pt-2 mt-2 flex justify-between">
              <span class="font-semibold">Total Paid</span>
              <span class="font-display font-bold text-lg gradient-text" id="receiptTotal">₹0</span>
            </div>
          </div>
          <div class="mt-3 pt-3 border-t border-cream-500/10 text-xs opacity-60 flex items-center gap-2">
            <i data-lucide="wallet" class="w-3.5 h-3.5"></i>
            <span id="receiptPayment">—</span>
          </div>
        </div>
      </div>

      <div class="text-center mb-4">
        <div class="text-[10px] opacity-60 uppercase tracking-widest mb-2">Scan to Track Live</div>
        <div class="inline-block p-3 bg-white rounded-xl">
          <canvas id="qrCanvas" width="140" height="140"></canvas>
        </div>
        <div class="text-[10px] opacity-50 mt-2 font-mono" id="receiptQrText">aquaflow.in/track/AF-00000</div>
      </div>

      <div class="text-center text-[10px] opacity-50 border-t border-cream-500/10 pt-4">
        Thank you for choosing AquaFlow Logistics.<br/>
        For support: 1800-AQUA-FLOW
      </div>
    </div>

    <div class="no-print p-6 pt-0 flex gap-3">
      <button onclick="window.print()" class="flex-1 glass border border-cream-500/30 hover:border-cream-500/60 px-4 py-3 rounded-xl font-semibold text-sm flex items-center justify-center gap-2 transition">
        <i data-lucide="printer" class="w-4 h-4 text-cream-600"></i>
        Print / Save
      </button>
      <button onclick="closeReceiptModal()" class="flex-1 btn-shine bg-gradient-to-r from-cream-600 to-cream-700 hover:from-cream-500 hover:to-cream-600 text-white px-4 py-3 rounded-xl font-semibold text-sm shadow-lg shadow-cream-500/30 transition-all flex items-center justify-center gap-2">
        <i data-lucide="check" class="w-4 h-4"></i>
        Done
      </button>
    </div>
  </div>
</div>

<!-- ════════════════════════════════════════════════════════════ -->
<!-- SCRIPTS                                                      -->
<!-- ════════════════════════════════════════════════════════════ -->
<script>
/* ──────────────────────────────────────────────────────────────
   THEME TOGGLE
   ────────────────────────────────────────────────────────────── */
function toggleTheme() {
  document.body.classList.toggle('dark');
  localStorage.setItem('aquaflow-theme', document.body.classList.contains('dark') ? 'dark' : 'light');
  // Re-render hero orb colors
  if (window.heroOrb && window.heroOrb.updateTheme) {
    window.heroOrb.updateTheme(document.body.classList.contains('dark'));
  }
}
if (localStorage.getItem('aquaflow-theme') === 'dark') {
  document.body.classList.add('dark');
}

/* ──────────────────────────────────────────────────────────────
   INTERACTIVE BACKGROUND (mouse-following gradient + particles)
   ────────────────────────────────────────────────────────────── */
(function initBg() {
  const canvas = document.getElementById('bgCanvas');
  const ctx = canvas.getContext('2d');
  let w, h;
  let mouse = { x: -1000, y: -1000 };
  let particles = [];
  const PARTICLE_COUNT = 40;

  function resize() {
    w = canvas.width = window.innerWidth;
    h = canvas.height = window.innerHeight;
  }
  resize();
  window.addEventListener('resize', resize);

  window.addEventListener('mousemove', (e) => {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
  });
  window.addEventListener('mouseleave', () => { mouse.x = -1000; mouse.y = -1000; });

  // Init particles
  for (let i = 0; i < PARTICLE_COUNT; i++) {
    particles.push({
      x: Math.random() * w,
      y: Math.random() * h,
      vx: (Math.random() - 0.5) * 0.3,
      vy: (Math.random() - 0.5) * 0.3,
      r: Math.random() * 2 + 1,
      o: Math.random() * 0.4 + 0.1,
    });
  }

  function draw() {
    ctx.clearRect(0, 0, w, h);
    const isDark = document.body.classList.contains('dark');

    // Mouse-following radial glow
    if (mouse.x > 0) {
      const grad = ctx.createRadialGradient(mouse.x, mouse.y, 0, mouse.x, mouse.y, 350);
      if (isDark) {
        grad.addColorStop(0, 'rgba(212, 184, 150, 0.12)');
        grad.addColorStop(1, 'rgba(212, 184, 150, 0)');
      } else {
        grad.addColorStop(0, 'rgba(184, 147, 90, 0.15)');
        grad.addColorStop(1, 'rgba(184, 147, 90, 0)');
      }
      ctx.fillStyle = grad;
      ctx.fillRect(0, 0, w, h);
    }

    // Particles
    particles.forEach(p => {
      p.x += p.vx;
      p.y += p.vy;
      if (p.x < 0 || p.x > w) p.vx *= -1;
      if (p.y < 0 || p.y > h) p.vy *= -1;

      // Mouse repulsion
      const dx = p.x - mouse.x;
      const dy = p.y - mouse.y;
      const dist = Math.sqrt(dx * dx + dy * dy);
      if (dist < 150) {
        p.x += (dx / dist) * 1.2;
        p.y += (dy / dist) * 1.2;
      }

      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = isDark
        ? `rgba(212, 184, 150, ${p.o})`
        : `rgba(184, 147, 90, ${p.o})`;
      ctx.fill();
    });

    // Connect nearby particles
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 120) {
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.strokeStyle = isDark
            ? `rgba(212, 184, 150, ${0.08 * (1 - dist / 120)})`
            : `rgba(184, 147, 90, ${0.1 * (1 - dist / 120)})`;
          ctx.lineWidth = 0.5;
          ctx.stroke();
        }
      }
    }

    requestAnimationFrame(draw);
  }
  draw();
})();

/* ──────────────────────────────────────────────────────────────
   PRELOADER — Liquid Capsule
   ────────────────────────────────────────────────────────────── */
(function initPreloader() {
  const fill = document.getElementById('liquidFill');
  const percent = document.getElementById('progressPercent');
  const preloader = document.getElementById('preloader');
  const mainApp = document.getElementById('mainApp');
  let progress = 0;

  const interval = setInterval(() => {
    progress += 1 + Math.random() * 1.5;
    if (progress > 100) progress = 100;
    fill.style.width = progress + '%';
    percent.textContent = Math.floor(progress) + '%';

    if (progress >= 100) {
      clearInterval(interval);
      setTimeout(() => {
        preloader.classList.add('hidden-loader');
        mainApp.style.opacity = '1';
      }, 600);
    }
  }, 40);
})();

/* ──────────────────────────────────────────────────────────────
   HERO 3D WATER ORB (Three.js) — replaces tanker SVG
   ────────────────────────────────────────────────────────────── */
(function initHeroOrb() {
  const canvas = document.getElementById('heroCanvas');
  if (!canvas) return;

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(45, 1, 0.1, 100);
  camera.position.set(0, 0, 4);

  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  function resize() {
    const rect = canvas.getBoundingClientRect();
    renderer.setSize(rect.width, rect.height, false);
    camera.aspect = rect.width / rect.height;
    camera.updateProjectionMatrix();
  }
  resize();
  window.addEventListener('resize', resize);

  // Lights
  scene.add(new THREE.AmbientLight(0xffffff, 0.4));
  const keyLight = new THREE.DirectionalLight(0xffffff, 1.2);
  keyLight.position.set(3, 3, 3);
  scene.add(keyLight);
  const rimLight = new THREE.PointLight(0xB8935A, 2, 10);
  rimLight.position.set(-3, 1, 2);
  scene.add(rimLight);

  // Water orb — custom shader sphere with animated noise
  const orbGeo = new THREE.SphereGeometry(1.1, 128, 128);
  const orbMat = new THREE.ShaderMaterial({
    uniforms: {
      uTime: { value: 0 },
      uMouse: { value: new THREE.Vector2(0, 0) },
      uColor1: { value: new THREE.Color(0xB8935A) },
      uColor2: { value: new THREE.Color(0xD4B896) },
      uColor3: { value: new THREE.Color(0x7D6239) },
    },
    vertexShader: `
      uniform float uTime;
      uniform vec2 uMouse;
      varying vec3 vNormal;
      varying vec3 vPos;
      varying float vNoise;

      // Simplex-like noise
      vec3 mod289(vec3 x){return x-floor(x*(1./289.))*289.;}
      vec4 mod289(vec4 x){return x-floor(x*(1./289.))*289.;}
      vec4 perm(vec4 x){return mod289(((x*34.)+1.)*x);}
      float noise(vec3 p){
        vec3 a=floor(p);vec3 d=p-a;d=d*d*(3.-2.*d);
        vec4 b=a.xxyy+vec4(0.,1.,0.,1.);
        vec4 k1=perm(b.xyxy);vec4 k2=perm(k1.xyxy+b.zzww);
        vec4 c=k2+a.zzzz;vec4 k3=perm(c);vec4 k4=perm(c+1.);
        vec4 o1=fract(k3*(1./41.));vec4 o2=fract(k4*(1./41.));
        vec4 o3=o2*d.z+o1*(1.-d.z);
        vec2 o4=o3.yw*d.x+o3.xz*(1.-d.x);
        return o4.y*d.y+o4.x*(1.-d.y);
      }

      void main() {
        vNormal = normal;
        vec3 pos = position;
        float n = noise(pos * 2.0 + uTime * 0.4);
        n += noise(pos * 4.0 - uTime * 0.6) * 0.5;
        // Mouse influence
        float mouseInfluence = (uMouse.x * normal.x + uMouse.y * normal.y) * 0.1;
        pos += normal * (n * 0.15 + mouseInfluence);
        vNoise = n;
        vPos = pos;
        gl_Position = projectionMatrix * modelViewMatrix * vec4(pos, 1.0);
      }
    `,
    fragmentShader: `
      uniform vec3 uColor1;
      uniform vec3 uColor2;
      uniform vec3 uColor3;
      uniform float uTime;
      varying vec3 vNormal;
      varying vec3 vPos;
      varying float vNoise;

      void main() {
        // Fresnel-like rim
        vec3 viewDir = normalize(cameraPosition - vPos);
        float fresnel = pow(1.0 - max(dot(viewDir, vNormal), 0.0), 2.5);

        // Color mix based on noise + position
        vec3 color = mix(uColor1, uColor2, vNoise);
        color = mix(color, uColor3, smoothstep(0.4, 0.8, vNoise));

        // Add highlight
        color += fresnel * vec3(1.0, 0.95, 0.85) * 0.6;

        // Subtle caustics
        float caustic = sin(vPos.x * 8.0 + uTime) * sin(vPos.y * 8.0 - uTime) * 0.1;
        color += caustic;

        gl_FragColor = vec4(color, 0.92);
      }
    `,
    transparent: true,
  });
  const orb = new THREE.Mesh(orbGeo, orbMat);
  scene.add(orb);

  // Inner glow sphere
  const glowGeo = new THREE.SphereGeometry(1.3, 32, 32);
  const glowMat = new THREE.ShaderMaterial({
    uniforms: {
      uColor: { value: new THREE.Color(0xD4B896) },
    },
    vertexShader: `
      varying vec3 vNormal;
      void main() {
        vNormal = normalize(normalMatrix * normal);
        gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
      }
    `,
    fragmentShader: `
      uniform vec3 uColor;
      varying vec3 vNormal;
      void main() {
        float intensity = pow(0.7 - dot(vNormal, vec3(0., 0., 1.0)), 2.0);
        gl_FragColor = vec4(uColor, intensity * 0.5);
      }
    `,
    transparent: true,
    side: THREE.BackSide,
    blending: THREE.AdditiveBlending,
  });
  const glow = new THREE.Mesh(glowGeo, glowMat);
  scene.add(glow);

  // Orbiting droplet particles
  const droplets = [];
  for (let i = 0; i < 8; i++) {
    const d = new THREE.Mesh(
      new THREE.SphereGeometry(0.06, 16, 16),
      new THREE.MeshStandardMaterial({
        color: 0xD4B896,
        emissive: 0xB8935A,
        emissiveIntensity: 0.4,
        metalness: 0.3,
        roughness: 0.2,
      })
    );
    d.userData = {
      radius: 1.5 + Math.random() * 0.4,
      speed: 0.3 + Math.random() * 0.4,
      phase: Math.random() * Math.PI * 2,
      tilt: (Math.random() - 0.5) * 1.2,
    };
    scene.add(d);
    droplets.push(d);
  }

  // Mouse tracking
  let mouseTarget = { x: 0, y: 0 };
  let mouseCurrent = { x: 0, y: 0 };
  canvas.addEventListener('mousemove', (e) => {
    const rect = canvas.getBoundingClientRect();
    mouseTarget.x = ((e.clientX - rect.left) / rect.width) * 2 - 1;
    mouseTarget.y = -(((e.clientY - rect.top) / rect.height) * 2 - 1);
  });
  canvas.addEventListener('mouseleave', () => {
    mouseTarget.x = 0;
    mouseTarget.y = 0;
  });

  const clock = new THREE.Clock();

  function animate() {
    requestAnimationFrame(animate);
    const t = clock.getElapsedTime();

    // Smooth mouse
    mouseCurrent.x += (mouseTarget.x - mouseCurrent.x) * 0.08;
    mouseCurrent.y += (mouseTarget.y - mouseCurrent.y) * 0.08;

    orbMat.uniforms.uTime.value = t;
    orbMat.uniforms.uMouse.value.set(mouseCurrent.x, mouseCurrent.y);

    // Orb rotation follows mouse
    orb.rotation.y = t * 0.2 + mouseCurrent.x * 0.5;
    orb.rotation.x = mouseCurrent.y * 0.3;

    // Orbiting droplets
    droplets.forEach((d, i) => {
      const angle = t * d.userData.speed + d.userData.phase;
      d.position.x = Math.cos(angle) * d.userData.radius;
      d.position.z = Math.sin(angle) * d.userData.radius;
      d.position.y = Math.sin(angle * 1.5 + d.userData.tilt) * 0.5;
    });

    // Glow pulse
    glow.scale.setScalar(1 + Math.sin(t * 1.5) * 0.03);

    renderer.render(scene, camera);
  }
  animate();

  // Theme update
  window.heroOrb = {
    updateTheme: (isDark) => {
      if (isDark) {
        orbMat.uniforms.uColor1.value.set(0xD4B896);
        orbMat.uniforms.uColor2.value.set(0xE8DCC4);
        orbMat.uniforms.uColor3.value.set(0x9A7A48);
        glowMat.uniforms.uColor.value.set(0xE8DCC4);
      } else {
        orbMat.uniforms.uColor1.value.set(0xB8935A);
        orbMat.uniforms.uColor2.value.set(0xD4B896);
        orbMat.uniforms.uColor3.value.set(0x7D6239);
        glowMat.uniforms.uColor.value.set(0xD4B896);
      }
    }
  };
})();

/* ──────────────────────────────────────────────────────────────
   LUCIDE ICONS + SCROLL REVEAL
   ────────────────────────────────────────────────────────────── */
lucide.createIcons();
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) entry.target.classList.add('visible');
  });
}, { threshold: 0.1 });
document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

/* ──────────────────────────────────────────────────────────────
   BOOKING MODAL
   ────────────────────────────────────────────────────────────── */
const bookingModal = document.getElementById('bookingModal');
const receiptModal = document.getElementById('receiptModal');
let currentStep = 1;
const totalSteps = 5;

const bookingData = {
  fullName: '', phone: '', email: '',
  address: '', city: '', pincode: '', landmark: '',
  capacity: null, capacityLabel: '', price: 0,
  date: '', slot: '', payment: 'UPI',
};

function openBookingModal() {
  bookingModal.classList.add('active');
  document.body.style.overflow = 'hidden';
  const today = new Date().toISOString().split('T')[0];
  document.getElementById('deliveryDate').min = today;
  document.getElementById('deliveryDate').value = today;
  bookingData.date = today;
}
function closeBookingModal() {
  bookingModal.classList.remove('active');
  document.body.style.overflow = '';
}
function closeReceiptModal() {
  receiptModal.classList.remove('active');
  document.body.style.overflow = '';
  resetBookingForm();
}

[bookingModal, receiptModal].forEach(m => {
  m.addEventListener('click', (e) => {
    if (e.target === m) {
      if (m === bookingModal) closeBookingModal();
      else closeReceiptModal();
    }
  });
});

document.querySelectorAll('.capacity-card').forEach(card => {
  card.addEventListener('click', () => {
    document.querySelectorAll('.capacity-card').forEach(c => c.classList.remove('selected'));
    card.classList.add('selected');
    bookingData.capacity = parseInt(card.dataset.capacity);
    bookingData.capacityLabel = card.dataset.label;
    bookingData.price = parseInt(card.dataset.price);
    updateSummary();
  });
});

document.querySelectorAll('.time-slot:not(.disabled)').forEach(slot => {
  slot.addEventListener('click', () => {
    document.querySelectorAll('.time-slot').forEach(s => s.classList.remove('selected'));
    slot.classList.add('selected');
    bookingData.slot = slot.dataset.slot;
  });
});

document.getElementById('deliveryDate').addEventListener('change', (e) => {
  bookingData.date = e.target.value;
});

document.querySelectorAll('input[name="payment"]').forEach(r => {
  r.addEventListener('change', (e) => { bookingData.payment = e.target.value; });
});

function updateSummary() {
  const base = bookingData.price;
  const gst = Math.round(base * 0.05);
  const total = base + gst;
  document.getElementById('sumCapacity').textContent = bookingData.capacity ? `${bookingData.capacity.toLocaleString()}L ${bookingData.capacityLabel}` : '—';
  document.getElementById('sumBase').textContent = '₹' + base.toLocaleString();
  document.getElementById('sumGst').textContent = '₹' + gst.toLocaleString();
  document.getElementById('sumTotal').textContent = '₹' + total.toLocaleString();
}

function validateStep(step) {
  const errors = [];
  if (step === 1) {
    const name = document.getElementById('fullName').value.trim();
    const phone = document.getElementById('phone').value.trim();
    if (!name || name.length < 2) errors.push('Please enter your full name.');
    if (!phone || phone.replace(/\D/g, '').length < 10) errors.push('Please enter a valid phone number (10+ digits).');
    bookingData.fullName = name;
    bookingData.phone = phone;
    bookingData.email = document.getElementById('email').value.trim();
  } else if (step === 2) {
    const addr = document.getElementById('address').value.trim();
    const city = document.getElementById('city').value.trim();
    const pin = document.getElementById('pincode').value.trim();
    if (!addr || addr.length < 5) errors.push('Please enter a valid delivery address.');
    if (!city) errors.push('Please enter your city.');
    if (!pin || pin.length !== 6) errors.push('Please enter a valid 6-digit pincode.');
    bookingData.address = addr;
    bookingData.city = city;
    bookingData.pincode = pin;
    bookingData.landmark = document.getElementById('landmark').value.trim();
  } else if (step === 3) {
    if (!bookingData.capacity) errors.push('Please select a tanker capacity.');
  } else if (step === 4) {
    if (!bookingData.date) errors.push('Please select a delivery date.');
    if (!bookingData.slot) errors.push('Please select a time slot.');
  }
  return errors;
}

function showToast(msg, type = 'error') {
  const toast = document.createElement('div');
  toast.className = `fixed top-20 left-1/2 -translate-x-1/2 z-[200] px-5 py-3 rounded-xl shadow-xl text-sm font-medium animate-slide-up ${
    type === 'error' ? 'bg-red-500 text-white' : 'bg-green-600 text-white'
  }`;
  toast.textContent = msg;
  document.body.appendChild(toast);
  setTimeout(() => toast.remove(), 2800);
}

function nextStep() {
  const errors = validateStep(currentStep);
  if (errors.length) { showToast(errors[0]); return; }
  if (currentStep < totalSteps) {
    currentStep++;
    updateStepUI();
  } else {
    submitBooking();
  }
}
function prevStep() {
  if (currentStep > 1) { currentStep--; updateStepUI(); }
}

function updateStepUI() {
  document.querySelectorAll('.booking-step').forEach(s => s.classList.add('hidden'));
  document.querySelector(`.booking-step[data-step="${currentStep}"]`).classList.remove('hidden');

  document.querySelectorAll('.step-dot').forEach(dot => {
    const s = parseInt(dot.dataset.step);
    dot.classList.remove('active', 'completed');
    if (s === currentStep) dot.classList.add('active');
    else if (s < currentStep) dot.classList.add('completed');
  });
  document.querySelectorAll('.step-line').forEach(line => {
    const l = parseInt(line.dataset.line);
    line.classList.toggle('active', l < currentStep);
  });

  document.getElementById('currentStepNum').textContent = currentStep;
  document.getElementById('prevBtn').classList.toggle('hidden', currentStep === 1);

  const nextBtn = document.getElementById('nextBtn');
  if (currentStep === totalSteps) {
    nextBtn.innerHTML = '<i data-lucide="check" class="w-4 h-4"></i> Confirm Booking';
  } else {
    nextBtn.innerHTML = 'Continue <i data-lucide="arrow-right" class="w-4 h-4"></i>';
  }
  lucide.createIcons();
  document.querySelector('.modal-panel').scrollTop = 0;
}

function submitBooking() {
  const bookingId = 'AF-' + Math.floor(10000 + Math.random() * 90000);
  const base = bookingData.price;
  const gst = Math.round(base * 0.05);
  const total = base + gst;
  const now = new Date();
  const timestamp = now.toLocaleString('en-IN', { dateStyle: 'medium', timeStyle: 'short' });
  const dateFormatted = new Date(bookingData.date).toLocaleDateString('en-IN', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' });

  const paymentLabels = {
    'UPI': 'Paid via UPI / Online',
    'Card': 'Paid via Credit/Debit Card',
    'COD': 'Cash on Delivery (pay on arrival)',
  };

  document.getElementById('receiptId').textContent = '#' + bookingId;
  document.getElementById('receiptTimestamp').textContent = 'Booked on ' + timestamp;
  document.getElementById('receiptName').textContent = bookingData.fullName;
  document.getElementById('receiptPhone').textContent = bookingData.phone + (bookingData.email ? ' • ' + bookingData.email : '');
  document.getElementById('receiptAddress').textContent =
    bookingData.address + ', ' + bookingData.city + ' - ' + bookingData.pincode +
    (bookingData.landmark ? ' (Landmark: ' + bookingData.landmark + ')' : '');
  document.getElementById('receiptDate').textContent = dateFormatted;
  document.getElementById('receiptSlot').textContent = bookingData.slot;
  document.getElementById('receiptItem').textContent = `${bookingData.capacityLabel} Tanker (${bookingData.capacity.toLocaleString()}L)`;
  document.getElementById('receiptBase').textContent = '₹' + base.toLocaleString();
  document.getElementById('receiptGst').textContent = '₹' + gst.toLocaleString();
  document.getElementById('receiptTotal').textContent = '₹' + total.toLocaleString();
  document.getElementById('receiptPayment').textContent = paymentLabels[bookingData.payment];
  document.getElementById('receiptQrText').textContent = 'aquaflow.in/track/' + bookingId;

  const qrCanvas = document.getElementById('qrCanvas');
  QRCode.toCanvas(qrCanvas, 'https://aquaflow.in/track/' + bookingId, {
    width: 140, margin: 1,
    color: { dark: '#3F3120', light: '#FFFFFF' }
  });

  recentBookings[bookingId] = {
    id: bookingId,
    customer: bookingData.fullName,
    phone: bookingData.phone,
    capacity: bookingData.capacity,
    statusIndex: 0,
    date: bookingData.date,
    slot: bookingData.slot,
    address: bookingData.address + ', ' + bookingData.city,
  };

  closeBookingModal();
  setTimeout(() => {
    receiptModal.classList.add('active');
    document.body.style.overflow = 'hidden';
    lucide.createIcons();
  }, 300);
}

function resetBookingForm() {
  currentStep = 1;
  updateStepUI();
  ['fullName', 'phone', 'email', 'address', 'city', 'pincode', 'landmark'].forEach(id => {
    document.getElementById(id).value = '';
  });
  document.querySelectorAll('.capacity-card').forEach(c => c.classList.remove('selected'));
  document.querySelectorAll('.time-slot').forEach(s => s.classList.remove('selected'));
  document.querySelector('input[name="payment"][value="UPI"]').checked = true;
  Object.keys(bookingData).forEach(k => {
    if (typeof bookingData[k] === 'number') bookingData[k] = 0;
    else if (typeof bookingData[k] === 'string') bookingData[k] = '';
  });
  bookingData.payment = 'UPI';
  updateSummary();
}

/* ──────────────────────────────────────────────────────────────
   ORDER TRACKER
   ────────────────────────────────────────────────────────────── */
const recentBookings = {
  'AF-94821': {
    id: 'AF-94821', customer: 'Aarav Sharma', capacity: 5000,
    statusIndex: 2, date: '2026-10-28', slot: '10:00 - 12:00 PM',
    address: '42 Marine Drive, Mumbai',
  },
  'AF-58203': {
    id: 'AF-58203', customer: 'Priya Patel', capacity: 1000,
    statusIndex: 3, date: '2026-10-27', slot: '06:00 - 08:00 AM',
    address: '15 Park Street, Kolkata',
  },
};

const statusSteps = [
  { label: 'Order Confirmed', desc: 'We received your booking', icon: 'check-circle-2' },
  { label: 'Dispatched', desc: 'Tanker assigned & leaving depot', icon: 'truck' },
  { label: 'Out for Delivery', desc: 'On the way to your location', icon: 'navigation' },
  { label: 'Delivered', desc: 'Water delivered successfully', icon: 'party-poppper' },
];

function trackOrder() {
  const id = document.getElementById('trackInput').value.trim().toUpperCase();
  const result = document.getElementById('trackerResult');
  const empty = document.getElementById('trackerEmpty');

  if (!id) { showToast('Please enter a Booking ID'); return; }

  const booking = recentBookings[id];
  if (!booking) {
    result.classList.add('hidden');
    empty.classList.remove('hidden');
    return;
  }

  empty.classList.add('hidden');
  result.classList.remove('hidden');

  document.getElementById('trackBookingId').textContent = booking.id;
  document.getElementById('trackStatus').textContent = statusSteps[booking.statusIndex].label;

  const container = document.getElementById('timelineContainer');
  container.innerHTML = '';
  statusSteps.forEach((step, idx) => {
    const done = idx <= booking.statusIndex;
    const current = idx === booking.statusIndex;
    const div = document.createElement('div');
    div.className = `status-step flex gap-4 pb-6 ${done ? 'done' : ''}`;
    div.innerHTML = `
      <div class="relative z-10 w-10 h-10 rounded-full flex items-center justify-center flex-shrink-0 ${
        done
          ? 'bg-gradient-to-br from-cream-500 to-cream-700 text-white shadow-lg shadow-cream-500/30'
          : 'bg-cream-500/10 opacity-50 border border-cream-500/20'
      } ${current ? 'animate-glow-pulse' : ''}">
        <i data-lucide="${step.icon}" class="w-4 h-4"></i>
      </div>
      <div class="flex-1 pt-1.5">
        <div class="flex items-center gap-2">
          <div class="font-semibold ${done ? '' : 'opacity-50'}">${step.label}</div>
          ${current ? '<span class="px-2 py-0.5 rounded-full bg-cream-500/15 border border-cream-500/30 text-[10px] font-bold text-cream-700 uppercase tracking-wider">Current</span>' : ''}
        </div>
        <div class="text-xs ${done ? 'opacity-70' : 'opacity-40'} mt-0.5">${step.desc}</div>
      </div>
    `;
    container.appendChild(div);
  });

  lucide.createIcons();
  result.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

/* ──────────────────────────────────────────────────────────────
   KEYBOARD SHORTCUTS
   ────────────────────────────────────────────────────────────── */
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    if (receiptModal.classList.contains('active')) closeReceiptModal();
    else if (bookingModal.classList.contains('active')) closeBookingModal();
  }
});
</script>

</body>
</html>'''


# ─────────────────────────────────────────────────────────────────
# UPDATER LOGIC
# ─────────────────────────────────────────────────────────────────
def find_html_file():
    """Locate the AquaFlow HTML file in current directory."""
    candidates = [
        'aquaflow.html',
        'index.html',
        'AquaFlow.html',
        'aquaflow-logistics.html',
    ]
    for name in candidates:
        if Path(name).exists():
            return Path(name)

    # Fallback: any .html file in current dir
    html_files = list(Path('.').glob('*.html'))
    if html_files:
        return html_files[0]
    return None


def main():
    print("\n" + "=" * 62)
    print("  AQUAFLOW LOGISTICS — ONE-CLICK UPDATER v2.0")
    print("=" * 62)
    print("\n  Changes applied:")
    print("    ✦ New cream-beige (light) + charcoal (dark) theme")
    print("    ✦ Unique liquid-capsule loading bar with bubbles")
    print("    ✦ Interactive mouse-following background + particles")
    print("    ✦ Brand-new 3D water-orb hero widget (Three.js)")
    print("    ✦ Theme toggle button in navbar")
    print("    ✦ Fraunces serif font for elegant accents")
    print()

    # Find existing HTML file
    html_path = find_html_file()

    if html_path is None:
        # No existing file — create a fresh one
        html_path = Path('aquaflow.html')
        print(f"  → No existing HTML found. Creating: {html_path.name}")
    else:
        # Create timestamped backup
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_name = f"{html_path.stem}_backup_{timestamp}{html_path.suffix}"
        backup_path = html_path.with_name(backup_name)
        try:
            shutil.copy2(html_path, backup_path)
            print(f"  ✓ Backup created: {backup_path.name}")
        except Exception as e:
            print(f"  ! Warning: Could not create backup ({e})")

        print(f"  → Updating: {html_path.name}")

    # Write new content
    try:
        html_path.write_text(NEW_HTML, encoding='utf-8')
        print(f"  ✓ Website updated successfully!")
        print(f"  ✓ File size: {html_path.stat().st_size / 1024:.1f} KB")
    except Exception as e:
        print(f"\n  ✗ Error writing file: {e}")
        sys.exit(1)

    # Summary
    print("\n" + "-" * 62)
    print("  HOW TO USE:")
    print(f"    1. Open '{html_path.name}' in your browser")
    print(f"    2. Click the theme toggle (top-right) to switch modes")
    print(f"    3. Move your mouse — see the interactive background!")
    print(f"    4. Hover over the hero orb — it reacts to your cursor")
    print(f"    5. Try booking IDs: AF-94821 or AF-58203")
    print("-" * 62)

    # Optionally open in browser
    try:
        response = input("\n  Open in browser now? [Y/n]: ").strip().lower()
        if response in ('', 'y', 'yes'):
            webbrowser.open(f'file://{html_path.resolve()}')
            print("  ✓ Opened in your default browser.")
    except (EOFError, KeyboardInterrupt):
        pass

    print("\n  Done! Enjoy your new AquaFlow website. 🌊\n")


if __name__ == "__main__":
    main()