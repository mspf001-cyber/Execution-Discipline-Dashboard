# Execution Discipline Dashboard

Behavioral analytics dashboard built with Streamlit to track deep work consistency, distraction patterns, impulse control, and study intensity across a structured 30-day execution cycle.

This project focuses on measurable behavior instead of motivational abstraction.

---

## Purpose

The goal of this dashboard is to create a measurable execution framework using quantifiable daily inputs.

It tracks:

- Deep Work Blocks
- Escapes (distraction events)
- Urges Resisted
- Study Hours
- 7-day rolling behavioral trends
- Execution Level classification (1–8)
- Structured 30-day discipline plan

This tool is designed for local usage and personal performance tracking.

---

## Core Metrics

### Deep Work Blocks
Number of uninterrupted focused work sessions (typically 60–90 minutes).

Measures cognitive intensity.

### Escapes
Number of distraction events (YouTube, phone checks, task switching).

Measures avoidance behavior.

### Urges Resisted
Number of times distraction impulse was consciously ignored.

Measures impulse control growth.

### Study Hours
Total focused study duration per day.

Measures execution volume.

---

## Execution Level Model

Execution level is computed using rolling 7-day behavioral analytics.

- **Level 1 – Chaos:** No structure, no consistency  
- **Level 2 – Reactive:** High escape frequency  
- **Level 3 – Inconsistent:** Some effort, unstable output  
- **Level 4 – Structured but Fragile:** Routine exists, relapse risk present  
- **Level 5 – Stable Execution:** Consistent 3+ deep work blocks  
- **Level 6 – Self-Correcting:** Urges resisted > escapes consistently  
- **Level 7 – High Performer:** Strong upward execution trend  
- **Level 8 – Elite Discipline:** Low variance, high consistency  

---

## 30-Day Execution Structure

The dashboard follows a 4-phase discipline model:

### Phase 1 (Days 1–7) – Stabilization
- Minimum 2 deep work blocks daily
- Log every day
- Observe escape triggers

Avoid:
- System redesign
- Productivity binge
- Extreme restriction

Learn:
- Discomfort tolerance

---

### Phase 2 (Days 8–15) – Structure
- 3 deep work blocks average
- Define task before starting
- Reduce escape frequency

Avoid:
- Random browsing
- Undefined sessions

Learn:
- Clarity reduces drift

---

### Phase 3 (Days 16–23) – Control
- Urges resisted > escapes
- Maintain positive trend slope
- Analyze weak days calmly

Avoid:
- Emotional collapse
- Overcorrection

Learn:
- Recovery without relapse

---

### Phase 4 (Days 24–30) – Execution Upgrade
- 4 deep work blocks on peak days
- Maintain low variance
- Increase measurable output

Avoid:
- Tool upgrades
- Structural changes

Learn:
- Boredom tolerance mastery

---

## Features

- Integer Day Index Graphs (1–30)
- 30-Day rolling visualization
- Deep Work / Escape comparison
- Urge control tracking
- Study hour tracking
- Level classification engine
- Diagnosis system
- CSV-based lightweight storage
- Defensive schema handling

## Install dependencies:

```bash
pip install streamlit pandas matplotlib numpy
```

## Run the Dashboard
```bash
python -m streamlit run dashboard.py
```

## Scope
Single-user, localhost behavioral tracking tool.

Not designed for:

Multi-user systems

Cloud persistence

SaaS deployment

## License
Open-source for educational and personal development use.