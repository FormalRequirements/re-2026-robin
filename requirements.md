# REQUIREMENTS.md

This document details the technical and functional requirements of the project, structured according to the PEGS methodology (Project, Environment, Goals, Systems).

---

## 1. PROJECT

### P.1: Roles and Personnel

**P.1-01**: **Role Definition** : Each project member must have a primary role (e.g., Lead Developer, Product Owner) and a secondary role (e.g., QA Tester) to ensure redundancy. 
**P.1-02**: **Project Manager Authority** One member is designated as Project Manager. They have the final authority on scope decisions and feature cuts to respect deadlines. 
**P.1-03**: **Communication Channels** The team must use a unified communication channel (e.g., Discord or Slack) with dedicated channels for `#dev`, `#art`, and `#general`. 

### P.2: Imposed Technical Choices

**P.2-01**: **English Only** All code variables, comments, commit messages, and documentation must be written in English. 
**P.2-02**: **Repository Hosting** The project source code and documentation must be hosted on GitHub (Public or Private repository). 
**P.2-03**: **Documentation Format** Requirements and specifications must be written in Markdown (.md) or AsciiDoc to ensure version control compatibility. 

### P.3: Schedule and Milestones

**P.3-01**: **Sprint Duration** The development lifecycle adheres to a fixed 2-week Sprint cadence. Sprints cannot be extended.  
**P.3-02**: **Meeting Rituals** The team must hold a Weekly Sync (max 30 mins) to track progress and update the risk register. 
**P.3-03**: **Project Tracking** The project schedule (GitHub Projects or Jira) must be updated every 48 hours to reflect real-time progress. 

### P.4: Tasks and Deliverables

**P.4-01**: **Issue Granularity** Every task must be represented by a GitHub Issue. No task should exceed 3 days of estimated work. 
**P.4-02**: **Traceability** Every Issue must be linked to a specific PEGS Requirement ID (e.g., "Implements [S-05]"). 
**P.4-03**: **Definition of Done (DoD)** | A task is only "Done" when the code is committed, compiled without errors, and tested by a peer. 

### P.5: Required Technology Elements

**P.5-01**: **Development Hardware**  All developers must possess a workstation capable of running Unreal Engine 5 at 30fps minimum to ensure local testing. 
**P.5-02**: **Software Licenses** The team must ensure valid licenses for all tools used (IDE, 3D Modeling software) or use free educational versions. 

### P.6: Risk and Mitigation Analysis

**P.6-01**: **Bus Factor Mitigation** No critical knowledge should be held by a single person. Documentation or Pair Programming is mandatory for critical systems.
**P.6-02**: **Data Loss Prevention** A backup of the repository (or a fork) must be updated weekly to prevent total data loss. 

### P.7: Requirements Process and Report

**P.7-01**: **PEGS Framework** The project must strictly follow the PEGS structure for all specification documents. 
**P.7-02**: **Validation Review**  Requirements must be reviewed and approved by the Project Manager before development begins on that section. 

## 2. ENVIRONMENT (E)

### E.1: Glossary

**E.1-01 LTS**: **Long Term Support**. Refers to the version of the Game Engine (Unreal/Unity) that is guaranteed to be stable for the duration of the project.
**E.1-02**: **Vertical Slice**: A portion of the software that demonstrates all layers of the architecture (UI, Logic, Data, Audio) functioning together in a final quality state.

### E.2: Components

**E.2-01 Development Engine**: **Unreal Engine 5.3+**. This is the core component providing the rendering, physics, and input subsystems.
**E.2-04 Audio API**: **Wwise SDK**. The external component required to interface between the system logic and the user's audio hardware.
**E.2-05 Target Hardware**: The end-user environment: A PC running Windows 10/11 x64 with a DirectX 12 compatible GPU (Min: GTX 1060).

### E.3: Constraints

**E.3-01 OS Compatibility**: The system must be compiled exclusively for Windows 10/11 (64-bit). Linux and macOS environments are out of scope.
**E.3-04 Offline Operation**: The system must function in an environment without internet access (Air-gapped), except for the initial installation.

### E.4: Assumptions

**E.4-01 User Privileges**: We assume the system has Read/Write access to the user's `Documents/MyGames/` directory for storing configuration and save files.
**E.4-02 Driver Status**: We assume the target environment has up-to-date GPU drivers (Vulkan/DX12 compliant). No legacy driver support is planned.
**E.4-03 Peripheral Availability**: We assume the environment includes a standard Keyboard and Mouse or an XInput-compatible **Controller**.

### E.5: Effects

**E.5-01 Disk Footprint**: The system installation will consume approximately 10 GB of storage space on the host environment's drive.
* **E.5-04 Peripheral Control**: The system takes exclusive control of the controller's vibration motors (Haptics) and mouse cursor locking during execution.

### E.6: Invariants

**E.6-01 Engine Version**: The Unreal Engine version (e.g., 5.3) is locked. The environment will not be upgraded to 5.4+ mid-project to avoid breaking changes.
**E.6-02 Repository URL**: The remote origin URL of the Git repository is invariant and serves as the single source of truth.
**E.6-03 Language Standard**: The C++ standard used (e.g., C++17 or C++20) remains constant throughout the codebase lifecycle.

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