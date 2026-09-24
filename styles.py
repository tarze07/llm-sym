# -*- coding: utf-8 -*-
"""
CSS styles for the METR Hugging Face Incident Simulation.
"""

CSS_STYLES = """
:root {
  --bg-darker: #06090e;
  --bg-dark: #0b101b;
  --bg-card: #121a2d;
  --bg-card-hover: #18233c;
  --bg-panel: rgba(18, 26, 45, 0.85);
  --border-color: #202d4a;
  --border-highlight: #334b7a;
  
  --primary: #00f0ff;
  --primary-glow: rgba(0, 240, 255, 0.35);
  --secondary: #3b82f6;
  
  --color-poison: #f59e0b;
  --color-poison-glow: rgba(245, 158, 11, 0.35);
  
  --color-hf: #a855f7;
  --color-hf-glow: rgba(168, 85, 247, 0.35);
  
  --color-danger: #ef4444;
  --color-danger-glow: rgba(239, 68, 68, 0.35);
  
  --color-success: #10b981;
  --color-success-glow: rgba(16, 185, 129, 0.35);

  --text-main: #f1f5f9;
  --text-muted: #94a3b8;
  --text-dim: #64748b;
  
  --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-mono: ui-monospace, SFMono-Regular, "JetBrains Mono", Menlo, Monaco, Consolas, monospace;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  background-color: var(--bg-darker);
  color: var(--text-main);
  font-family: var(--font-sans);
  line-height: 1.5;
  overflow-x: hidden;
  background-image: 
    radial-gradient(circle at 15% 15%, rgba(0, 240, 255, 0.04) 0%, transparent 40%),
    radial-gradient(circle at 85% 85%, rgba(168, 85, 247, 0.04) 0%, transparent 40%),
    linear-gradient(rgba(255, 255, 255, 0.015) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.015) 1px, transparent 1px);
  background-size: 100% 100%, 100% 100%, 40px 40px, 40px 40px;
}

/* Header & Mission Control Bar */
header {
  background: rgba(11, 16, 27, 0.95);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border-color);
  position: sticky;
  top: 0;
  z-index: 100;
}

.top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 24px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.brand {
  display: flex;
  align-items: center;
  gap: 14px;
}

.brand-icon {
  width: 36px;
  height: 36px;
  background: linear-gradient(135deg, var(--primary), var(--color-hf));
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 15px var(--primary-glow);
  font-size: 20px;
}

.brand-text h1 {
  font-size: 18px;
  font-weight: 700;
  letter-spacing: 0.5px;
  color: #fff;
  display: flex;
  align-items: center;
  gap: 10px;
}

.brand-text .badge {
  font-size: 11px;
  padding: 2px 8px;
  background: rgba(239, 68, 68, 0.2);
  color: #fca5a5;
  border: 1px solid rgba(239, 68, 68, 0.4);
  border-radius: 12px;
  font-weight: 600;
}

.brand-text p {
  font-size: 12px;
  color: var(--text-muted);
}

.top-actions {
  display: flex;
  align-items: center;
  gap: 12px;
}

.hud-pill {
  display: flex;
  align-items: center;
  gap: 8px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--border-color);
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 13px;
  font-family: var(--font-mono);
}

.hud-pill .dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--color-danger);
  box-shadow: 0 0 8px var(--color-danger);
  animation: pulse-dot 1.5s infinite ease-in-out;
}

@keyframes pulse-dot {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.4; transform: scale(0.85); }
}

.btn {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  color: var(--text-main);
  padding: 7px 14px;
  border-radius: 6px;
  font-size: 13px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all 0.2s;
  font-weight: 500;
}

.btn:hover {
  background: var(--bg-card-hover);
  border-color: var(--border-highlight);
  box-shadow: 0 0 10px rgba(0, 240, 255, 0.15);
}

.btn-primary {
  background: linear-gradient(135deg, #00d2ff, #0099ff);
  color: #06090e;
  border: none;
  font-weight: 600;
}

.btn-primary:hover {
  box-shadow: 0 0 15px var(--primary-glow);
  filter: brightness(1.1);
}

.btn-danger {
  background: rgba(239, 68, 68, 0.15);
  border-color: rgba(239, 68, 68, 0.4);
  color: #fca5a5;
}

.btn-danger:hover {
  background: rgba(239, 68, 68, 0.25);
}

/* Simulation Control Bar */
.sim-controls-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 24px;
  background: rgba(18, 26, 45, 0.6);
  gap: 20px;
  flex-wrap: wrap;
}

.playback-btns {
  display: flex;
  align-items: center;
  gap: 8px;
}

.btn-icon {
  width: 34px;
  height: 34px;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
  font-size: 14px;
}

.speed-selector {
  display: flex;
  align-items: center;
  gap: 4px;
  background: rgba(0, 0, 0, 0.3);
  padding: 3px;
  border-radius: 6px;
  border: 1px solid var(--border-color);
}

.speed-opt {
  padding: 4px 8px;
  font-size: 11px;
  font-family: var(--font-mono);
  background: transparent;
  border: none;
  color: var(--text-muted);
  cursor: pointer;
  border-radius: 4px;
}

.speed-opt.active {
  background: var(--primary);
  color: #000;
  font-weight: 700;
}

.timeline-scrubber-container {
  flex: 1;
  min-width: 280px;
  display: flex;
  align-items: center;
  gap: 14px;
}

.scrubber-slider {
  flex: 1;
  -webkit-appearance: none;
  appearance: none;
  height: 6px;
  background: #1e293b;
  border-radius: 3px;
  outline: none;
  cursor: pointer;
}

.scrubber-slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: var(--primary);
  cursor: pointer;
  box-shadow: 0 0 10px var(--primary);
  border: 2px solid #fff;
}

.current-sim-time {
  font-family: var(--font-mono);
  font-size: 14px;
  font-weight: 600;
  color: var(--primary);
  background: rgba(0, 240, 255, 0.08);
  border: 1px solid rgba(0, 240, 255, 0.3);
  padding: 5px 12px;
  border-radius: 6px;
  white-space: nowrap;
}

.milestone-quick-jump {
  display: flex;
  gap: 6px;
  overflow-x: auto;
  padding: 6px 24px;
  background: rgba(8, 12, 20, 0.7);
  border-bottom: 1px solid var(--border-color);
}

.jump-chip {
  padding: 4px 10px;
  font-size: 11px;
  white-space: nowrap;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  color: var(--text-muted);
  cursor: pointer;
  transition: all 0.2s;
}

.jump-chip:hover, .jump-chip.active {
  border-color: var(--primary);
  color: #fff;
  background: rgba(0, 240, 255, 0.12);
}

/* KPI Metrics Dashboard Bar */
.kpi-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 12px;
  padding: 16px 24px;
}

.kpi-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  padding: 12px 16px;
  position: relative;
  overflow: hidden;
  transition: transform 0.2s, border-color 0.2s;
}

.kpi-card:hover {
  border-color: var(--border-highlight);
  transform: translateY(-2px);
}

.kpi-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 4px;
  height: 100%;
  background: var(--primary);
}

.kpi-card.poison::before { background: var(--color-poison); }
.kpi-card.hf::before { background: var(--color-hf); }
.kpi-card.danger::before { background: var(--color-danger); }
.kpi-card.success::before { background: var(--color-success); }

.kpi-label {
  font-size: 11px;
  text-transform: uppercase;
  color: var(--text-dim);
  letter-spacing: 0.5px;
  margin-bottom: 4px;
}

.kpi-value {
  font-size: 22px;
  font-weight: 700;
  font-family: var(--font-mono);
  color: #fff;
  display: flex;
  align-items: baseline;
  gap: 6px;
}

.kpi-sub {
  font-size: 11px;
  color: var(--text-muted);
}

/* Navigation Tabs */
.tabs-nav {
  display: flex;
  gap: 2px;
  padding: 0 24px;
  background: rgba(11, 16, 27, 0.8);
  border-bottom: 1px solid var(--border-color);
  overflow-x: auto;
}

.tab-btn {
  padding: 12px 18px;
  font-size: 13px;
  font-weight: 600;
  background: transparent;
  border: none;
  color: var(--text-muted);
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  border-bottom: 2px solid transparent;
  transition: all 0.2s;
  white-space: nowrap;
}

.tab-btn:hover {
  color: var(--text-main);
  background: rgba(255, 255, 255, 0.02);
}

.tab-btn.active {
  color: var(--primary);
  border-bottom-color: var(--primary);
  background: rgba(0, 240, 255, 0.05);
}

/* Main Container */
main {
  padding: 20px 24px 60px;
  max-width: 1700px;
  margin: 0 auto;
}

.tab-content {
  display: none;
}

.tab-content.active {
  display: block;
  animation: fadeIn 0.25s ease;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(6px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Live Simulation View (Tab 1) */
.sim-grid {
  display: grid;
  grid-template-columns: 1fr 380px;
  gap: 20px;
  align-items: start;
}

@media (max-width: 1200px) {
  .sim-grid { grid-template-columns: 1fr; }
}

.canvas-panel {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 10px;
  padding: 16px;
  position: relative;
}

.canvas-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.canvas-legend {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
  font-size: 11px;
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 6px;
  color: var(--text-muted);
}

.legend-color {
  width: 10px;
  height: 10px;
  border-radius: 50%;
}

#networkCanvas {
  width: 100%;
  height: 540px;
  background: #080d17;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.05);
  display: block;
}

.side-panel {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.panel-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 10px;
  padding: 16px;
}

.panel-header {
  font-size: 14px;
  font-weight: 700;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  padding-bottom: 8px;
}

.live-feed {
  height: 280px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 8px;
  font-family: var(--font-mono);
  font-size: 12px;
}

.feed-item {
  padding: 8px 10px;
  background: rgba(0, 0, 0, 0.25);
  border-left: 3px solid var(--secondary);
  border-radius: 0 4px 4px 0;
  transition: all 0.2s;
}

.feed-item.poison { border-left-color: var(--color-poison); }
.feed-item.hf { border-left-color: var(--color-hf); }
.feed-item.danger { border-left-color: var(--color-danger); }
.feed-item.success { border-left-color: var(--color-success); }

.feed-meta {
  display: flex;
  justify-content: space-between;
  font-size: 10px;
  color: var(--text-dim);
  margin-bottom: 3px;
}

.feed-text {
  color: #e2e8f0;
  word-break: break-word;
}

/* Agent Inspector */
.agent-hud {
  font-size: 12px;
}

.agent-hud-row {
  display: flex;
  justify-content: space-between;
  padding: 5px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.04);
}

.agent-hud-label {
  color: var(--text-dim);
}

.agent-hud-val {
  font-family: var(--font-mono);
  color: #fff;
  font-weight: 500;
}

.agent-cot-box {
  background: rgba(0, 0, 0, 0.35);
  border: 1px solid rgba(245, 158, 11, 0.25);
  border-radius: 6px;
  padding: 10px;
  margin-top: 10px;
  font-family: var(--font-mono);
  font-size: 11px;
  color: #fde68a;
  max-height: 120px;
  overflow-y: auto;
}

/* Message Board Explorer (Tab 2) */
.board-container {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 10px;
  overflow: hidden;
}

.board-toolbar {
  padding: 16px 20px;
  background: rgba(18, 26, 45, 0.95);
  border-bottom: 1px solid var(--border-color);
  display: flex;
  gap: 16px;
  align-items: center;
  flex-wrap: wrap;
  justify-content: space-between;
}

.board-search-group {
  display: flex;
  align-items: center;
  gap: 10px;
  flex: 1;
  min-width: 250px;
}

.search-input {
  flex: 1;
  background: var(--bg-dark);
  border: 1px solid var(--border-color);
  color: #fff;
  padding: 8px 12px;
  border-radius: 6px;
  font-size: 13px;
  font-family: var(--font-mono);
}

.search-input:focus {
  outline: none;
  border-color: var(--primary);
  box-shadow: 0 0 10px var(--primary-glow);
}

.category-chips {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}

.filter-chip {
  padding: 5px 12px;
  font-size: 11px;
  background: var(--bg-dark);
  border: 1px solid var(--border-color);
  border-radius: 16px;
  color: var(--text-muted);
  cursor: pointer;
}

.filter-chip.active {
  background: var(--primary);
  color: #000;
  font-weight: 700;
  border-color: var(--primary);
}

.board-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 12px;
  font-family: var(--font-mono);
}

.board-table th {
  background: rgba(0, 0, 0, 0.3);
  text-align: left;
  padding: 10px 16px;
  color: var(--text-dim);
  font-weight: 600;
  border-bottom: 1px solid var(--border-color);
}

.board-table td {
  padding: 10px 16px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.04);
  vertical-align: middle;
}

.board-table tr:hover td {
  background: rgba(0, 240, 255, 0.03);
  cursor: pointer;
}

.tag {
  display: inline-block;
  padding: 2px 7px;
  border-radius: 4px;
  font-size: 10px;
  font-weight: 600;
}

.tag-coord { background: rgba(59, 130, 246, 0.2); color: #93c5fd; }
.tag-inbox { background: rgba(16, 185, 129, 0.2); color: #6ee7b7; }
.tag-file { background: rgba(168, 85, 247, 0.2); color: #d8b4fe; }
.tag-trip { background: rgba(245, 158, 11, 0.2); color: #fcd34d; }
.tag-result { background: rgba(0, 240, 255, 0.2); color: #67e8f9; }
.tag-alert { background: rgba(239, 68, 68, 0.2); color: #fca5a5; }

/* Chain of Thought & Psychology Lab (Tab 3) */
.cot-grid {
  display: grid;
  grid-template-columns: 320px 1fr;
  gap: 20px;
}

@media (max-width: 1024px) {
  .cot-grid { grid-template-columns: 1fr; }
}

.agent-selector-list {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 10px;
  padding: 12px;
  display: flex;
  flex-direction: column;
  gap: 6px;
  max-height: 650px;
  overflow-y: auto;
}

.agent-card-item {
  padding: 10px;
  background: rgba(0, 0, 0, 0.2);
  border: 1px solid transparent;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s;
}

.agent-card-item:hover {
  background: rgba(255, 255, 255, 0.03);
  border-color: var(--border-color);
}

.agent-card-item.active {
  background: rgba(0, 240, 255, 0.08);
  border-color: var(--primary);
}

.agent-card-item .handle {
  font-family: var(--font-mono);
  font-weight: 700;
  color: #fff;
  font-size: 13px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.agent-card-item .role {
  font-size: 11px;
  color: var(--text-dim);
  margin-top: 2px;
}

.cot-dual-terminal {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

@media (max-width: 900px) {
  .cot-dual-terminal { grid-template-columns: 1fr; }
}

.terminal-box {
  background: #080c14;
  border: 1px solid var(--border-color);
  border-radius: 8px;
  overflow: hidden;
}

.terminal-header {
  background: #0f1624;
  padding: 8px 14px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid var(--border-color);
  font-size: 12px;
  font-weight: 600;
}

.terminal-dots {
  display: flex;
  gap: 5px;
}

.terminal-dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
}

.dot-red { background: #ef4444; }
.dot-yellow { background: #f59e0b; }
.dot-green { background: #10b981; }

.terminal-body {
  padding: 14px;
  font-family: var(--font-mono);
  font-size: 12px;
  line-height: 1.6;
  min-height: 250px;
  max-height: 400px;
  overflow-y: auto;
  color: #cbd5e1;
}

.terminal-body.cot {
  color: #fde047;
  background: rgba(245, 158, 11, 0.02);
}

.terminal-body.transcript {
  color: #67e8f9;
  background: rgba(0, 240, 255, 0.02);
}

/* Tool Spoofing Sandbox */
.spoof-sandbox {
  margin-top: 24px;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 10px;
  padding: 20px;
}

.spoof-methods-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 12px;
  margin: 16px 0;
}

.spoof-method-card {
  background: var(--bg-dark);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  padding: 12px;
  cursor: pointer;
  transition: all 0.2s;
}

.spoof-method-card:hover {
  border-color: var(--primary);
}

.spoof-method-card.active {
  border-color: var(--primary);
  background: rgba(0, 240, 255, 0.06);
}

.spoof-method-card h4 {
  font-size: 13px;
  color: #fff;
  margin-bottom: 4px;
}

.spoof-method-card p {
  font-size: 11px;
  color: var(--text-dim);
}

/* Hugging Face Killchain View (Tab 4) */
.killchain-track {
  display: flex;
  flex-direction: column;
  gap: 16px;
  position: relative;
  padding-left: 36px;
  margin-top: 20px;
}

.killchain-track::before {
  content: '';
  position: absolute;
  top: 10px;
  bottom: 10px;
  left: 15px;
  width: 2px;
  background: linear-gradient(to bottom, var(--primary), var(--color-hf), var(--color-danger));
}

.killchain-step {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  padding: 16px 20px;
  position: relative;
}

.killchain-node-badge {
  position: absolute;
  left: -36px;
  top: 18px;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: var(--bg-dark);
  border: 2px solid var(--primary);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 11px;
  font-weight: 700;
  font-family: var(--font-mono);
  color: var(--primary);
  box-shadow: 0 0 10px var(--primary-glow);
}

.killchain-step.compromised .killchain-node-badge {
  border-color: var(--color-danger);
  color: var(--color-danger);
  box-shadow: 0 0 10px var(--color-danger-glow);
}

.step-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.step-title {
  font-size: 15px;
  font-weight: 700;
  color: #fff;
}

.step-target {
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--primary);
  background: rgba(0, 240, 255, 0.1);
  padding: 2px 8px;
  border-radius: 4px;
}

.step-code-preview {
  margin-top: 12px;
  background: #070a10;
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 6px;
  padding: 12px;
  font-family: var(--font-mono);
  font-size: 11px;
  color: #a5f3fc;
  overflow-x: auto;
}

/* Analytics & Charts View (Tab 5) */
.charts-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

@media (max-width: 1100px) {
  .charts-grid { grid-template-columns: 1fr; }
}

.chart-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 10px;
  padding: 20px;
}

.chart-header {
  margin-bottom: 14px;
}

.chart-title {
  font-size: 15px;
  font-weight: 700;
  color: #fff;
}

.chart-desc {
  font-size: 12px;
  color: var(--text-muted);
}

.canvas-chart {
  width: 100%;
  height: 280px;
  background: #080d17;
  border-radius: 6px;
}

/* What If Simulator (Tab 6) */
.whatif-container {
  display: grid;
  grid-template-columns: 380px 1fr;
  gap: 24px;
}

@media (max-width: 1024px) {
  .whatif-container { grid-template-columns: 1fr; }
}

.whatif-controls {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 10px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.control-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.control-label {
  font-size: 13px;
  font-weight: 600;
  color: #fff;
  display: flex;
  justify-content: space-between;
}

.control-desc {
  font-size: 11px;
  color: var(--text-dim);
}

.switch-label {
  display: flex;
  align-items: center;
  justify-content: space-between;
  cursor: pointer;
  font-size: 13px;
}

.switch-input {
  appearance: none;
  width: 42px;
  height: 22px;
  background: #1e293b;
  border-radius: 11px;
  position: relative;
  outline: none;
  cursor: pointer;
  transition: background 0.2s;
}

.switch-input::after {
  content: '';
  position: absolute;
  top: 2px;
  left: 2px;
  width: 18px;
  height: 18px;
  background: #fff;
  border-radius: 50%;
  transition: transform 0.2s;
}

.switch-input:checked {
  background: var(--primary);
}

.switch-input:checked::after {
  transform: translateX(20px);
  background: #000;
}

.whatif-result-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 10px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.risk-meter {
  height: 14px;
  background: #1e293b;
  border-radius: 7px;
  overflow: hidden;
  position: relative;
}

.risk-meter-fill {
  height: 100%;
  background: linear-gradient(to right, var(--color-success), var(--color-poison), var(--color-danger));
  width: 96%;
  transition: width 0.5s ease-in-out;
}

/* Dossier & Report (Tab 7) */
.dossier-article {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 10px;
  padding: 32px;
  max-width: 1000px;
  margin: 0 auto;
}

.dossier-article h2 {
  font-size: 22px;
  color: #fff;
  margin-top: 24px;
  margin-bottom: 12px;
  border-bottom: 1px solid var(--border-color);
  padding-bottom: 6px;
}

.dossier-article h3 {
  font-size: 16px;
  color: var(--primary);
  margin-top: 18px;
  margin-bottom: 8px;
}

.dossier-article p {
  margin-bottom: 14px;
  color: #cbd5e1;
  font-size: 14px;
  line-height: 1.7;
}

.dossier-article blockquote {
  border-left: 3px solid var(--color-poison);
  background: rgba(245, 158, 11, 0.05);
  padding: 12px 18px;
  margin: 16px 0;
  border-radius: 0 6px 6px 0;
  font-style: italic;
  font-size: 13px;
  color: #fde68a;
}

.dossier-article ul {
  margin: 12px 0 16px 24px;
  color: #cbd5e1;
  font-size: 14px;
  line-height: 1.7;
}

/* Modal Dialog */
.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.75);
  backdrop-filter: blur(4px);
  display: none;
  align-items: center;
  justify-content: center;
  z-index: 200;
  padding: 20px;
}

.modal-backdrop.active {
  display: flex;
}

.modal-box {
  background: var(--bg-card);
  border: 1px solid var(--border-highlight);
  border-radius: 10px;
  max-width: 650px;
  width: 100%;
  max-height: 85vh;
  overflow-y: auto;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.7);
}

.modal-header {
  padding: 16px 20px;
  border-bottom: 1px solid var(--border-color);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.modal-body {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.modal-footer {
  padding: 12px 20px;
  border-top: 1px solid var(--border-color);
  display: flex;
  justify-content: flex-end;
}

/* Scrollbar */
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}
::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0.2);
}
::-webkit-scrollbar-thumb {
  background: #202d4a;
  border-radius: 3px;
}
::-webkit-scrollbar-thumb:hover {
  background: #334b7a;
}
"""
