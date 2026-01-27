# REQUIREMENTS.md

This document details the technical and functional requirements of the project, structured according to the PEGS methodology (Project, Environment, Goals, Systems).

---

## 1. PROJECT (Process & Organization)

| ID | Title | Description |
| :--- | :--- | :--- |
| **P-01** | **Methodology** | Adoption of the Scrum*method: 2-week Sprints, Daily Stand-up, and Sprint Review. |
| **P-02** | **Code Quality** | Mandatory Code Reviews. No branch is merged into `main` without validation by a peer. |
| **P-03** | **Git Flow** | Strict branch usage: `feature/`, `fix/`, `docs/`. Atomic commits with explicit messages. |
| **P-04** | **Documentation** | The GDD (Game Design Document) must be updated before coding any major new feature. |
| **P-05** | **Assets & Licenses** | Strict inventory of third-party assets. Only Royalty-Free (CC0) or paid commercial license assets are allowed. |

---

## 2. ENVIRONMENT (Tools & Tech)

| ID | Title | Description |
| :--- | :--- | :--- |
| **E-01** | **Game Engine** | Project developed using Unreal Engine 5.3+ (or Unity LTS) to leverage volumetric lighting. |
| **E-02** | **Version Control** | Mandatory use of Git LFS (Large File Storage) for binary versioning (`.uasset`, `.wav`, `.psd`). |
| **E-03** | **IDE & Linter** | Visual Studio / Rider. Shared Linter configuration to standardize code style. |
| **E-04** | **CI/CD** | Automated pipeline (GitHub Actions) to verify compilation on every Push. |
| **E-05** | **Target Hardware** | The game must be tested on mid-range hardware (equivalent to RTX 3060) to ensure accessibility. |

---

## 3. GOALS (Objectives)

### 3.1 Project Goals (KPIs & Delivery)
| ID | Title | Description |
| :--- | :--- | :--- |
| **G-PROJ-01** | **Vertical Slice** | Delivery of a functional 15-minute demo (including all core mechanics) at T+3 months. |
| **G-PROJ-02** | **Performance** | Maintain constant 60 FPS at 1080p. Loading times < 15s on SSD. |
| **G-PROJ-03** | **Stability** | Zero critical crashes (Class A bugs) during the Beta release. |

### 3.2 Player Goals (Gameplay Loop)
| ID | Title | Description |
| :--- | :--- | :--- |
| **G-GAME-01** | **Investigation (Debunk)** | The player must identify the rational cause of phenomena (e.g., find the whistling pipe) to reduce stress levels. |
| **G-GAME-02** | **Survival** | The player must escape the human antagonist without direct confrontation (hiding, diversion). |
| **G-GAME-03** | **Resource Management** | The player must manage batteries (Tools/Flashlight) to avoid being blind or unable to detect threats. |

---

## 4. SYSTEM (Functionality & Rules)

### 4.1 Perception & Health System (Bio-Feedback)
* **S-01 (Toxicity Logic)**: A hidden `ToxicityLevel` variable increases if the player remains in gas or infrasound zones.
    * *If Level > 30%*: Slight visual blur.
    * *If Level > 70%*: Appearance of visual hallucinations (fake enemies).
    * *If Level = 100%*: Panic state (inverted controls or death).
* **S-02 (Recovery)**: Toxicity level decreases only if the player leaves the zone or resolves the physical issue (e.g., closing a valve).

### 4.2 AI System (The Antagonist)
* **S-03 (Physical Movement)**: The AI never teleports. It must physically traverse the path (NavMesh) to reach the player.
* **S-04 (Sound Reaction)**: The AI possesses "hearing." Running or hitting an object generates a `NoiseEvent` at a specific location, attracting the AI.
* **S-05 (Sabotage)**: If the AI loses the player, it enters "Sabotage" mode: cutting lights or reactivating gas sources to force the player to move.

### 4.3 Physics & Tools System
* **S-06 (Diegetic Interaction)**: No on-screen HUD. Values (Radiation, dB, Temperature) are displayed physically on the 3D models of the tools.
* **S-07 (Environmental Chaos)**: Lightweight objects are not static. They are subject to variable wind forces (Force Vector System) to simulate natural "Poltergeists."
* **S-08 (Hand Constraints)**: The player has two hand slots.
    * *Left Hand:* Flashlight or Detection Tool.
    * *Right Hand:* World Interaction (open door).
    * *Rule:* Impossible to aim with a tool and open a complex door simultaneously.