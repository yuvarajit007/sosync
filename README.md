# ⚡ SOSync — AI-Assisted Rapid Emergency Response System

> **Autonomous Incident Evidence Capture, AI Scene Classification & Multi-Agency Dispatch System**

A fast, reliable emergency-reporting platform that addresses communication delays during critical accidents. With a single touch, it automatically captures 5 incident photos, acquires precision GPS location, analyzes the scene with AI vision, verifies with human-in-the-loop failsafes, and routes structured reports to police, medical, and fire responders.

---

## 🚀 Quick Start Instructions

You can run the application directly in your browser:

### Option 1: Run via Python Local Server (Recommended)
Open a terminal in this directory and run:
```bash
python server.py
```
Then open your browser at:
👉 **`http://localhost:8080`**

### Option 2: Direct Browser Launch
Double-click `index.html` or open it directly in Google Chrome, Microsoft Edge, or Mozilla Firefox.

---

## 🌟 Key Features & Views

### 1. 📱 Citizen / Victim Mobile SOS App
- **One-Touch Emergency Trigger:** Concentric pulsing SOS button with tactile response.
- **5-Photo Rapid Burst Capture:** Captures 5 evidence frames over ~5 seconds with telemetry watermark (timestamp, GPS coordinates).
- **WebRTC & Synthetic Engine:** Supports both your device's live webcam and built-in emergency scenario simulations (Highway Collision, Structure Fire, Cardiac Collapse, Crime/Assault).
- **AI Scene Diagnostics:** Real-time multi-modal detection of vehicles, fire/smoke, injuries, and fluid hazards.
- **10-Second Fail-Safe Countdown:** Auto-forwards report if the victim is unconscious or unable to confirm.
- **AI First-Aid Guidance:** Context-aware medical advice while responders are en route.

### 2. 🚨 Command & Dispatch Center (HQ)
- **Live Interactive Tactical Map:** Canvas-based GIS vector map with emergency pins, live responder vehicle tracking (Ambulance, Police, Fire), and distance vectors.
- **5-Photo Evidence Dossier:** Full inspection gallery with AI bounding boxes and timestamp offsets.
- **Multi-Agency Dispatch Coordination:** Simultaneous routing to 108 Emergency Medical, 100 Highway Police, and 101 Fire & Rescue.
- **Standardized Export:** Export incident docket as JSON-LD / EDXL-DE compatible file with 1 click.

### 3. 🚑 Responder Vehicle Interface (In-Cab HUD)
- **Turn-by-Turn GPS Navigation HUD:** High-contrast night-vision driver screen with simulated 3D road perspective and live ETA countdown.
- **Pre-Arrival Trauma Kit Briefing:** AI-recommended medical equipment checklist (e.g. spine board, extrication shears, oxygen).
- **Hands-Free Audio Readout:** Web Speech API voice synthesis for audio situation updates.
- **1-Tap Mission Status:** Quick updates for *En Route*, *Arrived on Scene*, and *Patient Secured*.

### 4. 🔄 3D Workflow & Judge Presentation Deck
- **Interactive 9-Step 3D Cards:** Visual isometric cards matching the project workflow.
- **Auto-Play Workflow:** Step-by-step playback with progress tracker.
- **ASCII Architecture Block Diagram:** Ready for copying into presentation slides.
- **Judge Defense Cheat-Sheet:** Slide notes, response time benchmarks, and anticipated Q&A answers.1

---

## 📂 Project Structure

```text
├── index.html            # Main Single-Page Web Application
├── styles.css            # Dark tactical emergency design system
├── app.js                # Core controller, audio synth, map engine, & burst pipeline
├── server.py             # Lightweight local HTTP server runner
├── PRESENTATION_DECK.md  # Complete PPT slide deck, architecture diagrams & Q&A
└── README.md             # Project documentation
```

---

## 🛠️ Technology Stack
- **Frontend:** HTML5, Modern CSS3 (Vanilla Tactical Theme), ES6+ JavaScript.
- **Audio:** Web Audio API (Synthesized sirens, alarms, and camera shutters) + Web Speech API (TTS).
- **Graphics & GIS:** HTML5 Canvas 2D Vector Mapping & Real-time Driving Simulator.
- **Sensors:** Geolocation API, WebRTC MediaStream Camera API.
- **Architecture Standard:** EDXL-DE (Emergency Data Exchange Language) and Schema.org JSON-LD.
