# REQUIREMENTS.md

This document details the technical and functional requirements of the project, structured according to the PEGS methodology (Project, Environment, Goals, Systems).

---

## 1. PROJECT (P)

### P.1: Roles and Personnel

**P.1-01**: **Role Definition** : Each project member must have a primary role (e.g., Lead Developer, Product Owner) and a secondary role (e.g., QA Tester) to ensure redundancy.

**P.1-02**: **Project Manager Authority** One member is designated as Project Manager. They have the final authority on scope decisions and feature cuts to respect deadlines. 

**P.1-03**: **Communication Channels** The team must use a unified communication channel (e.g., Discord or Slack) with dedicated channels for `#dev`, `#art`, and `#general`. 

### P.2: Imposed Technical Choices

**P.2-01**: **English Only** All code variables, comments, commit messages, and documentation must be written in English. 

**P.2-02**: **Repository Hosting** The project source code and documentation must be hosted on GitHub (Public or Private repository). 

**P.2-03**: **Documentation Format** Requirements and specifications must be written in Markdown (.md) or AsciiDoc to ensure version control compatibility. 

**P.2-04**: **Name the files** The files shall have a way to name them

### P.3: Schedule and Milestones

**P.3-01**: **Sprint Duration** The development lifecycle adheres to a fixed 2-week Sprint cadence. Sprints cannot be extended.

**P.3-02**: **Meeting Rituals** The team must hold a Weekly Sync (max 30 mins) to track progress and update the risk register.

**P.3-03**: **Project Tracking** The project schedule (GitHub Projects or Jira) must be updated every 48 hours to reflect real-time progress. 

### P.4: Tasks and Deliverables

**P.4-01**: **Issue Granularity** Every task must be represented by a GitHub Issue. No task shall exceed 3 days of estimated work. 

**P.4-02**: **Traceability** Every Issue must be linked to a specific PEGS Requirement ID (e.g., "Implements [S-05]"). 

**P.4-03**: **Definition of Done (DoD)** A task is only "Done" when the code is committed, compiled without errors, and tested by a peer. 

**P.4-05**: **Gaming platforms** The game shall be on differents gaming platform like Steam, Epic Games ou GOG

### P.5: Required Technology Elements

**P.5-01**: **Development Hardware** All developers must possess a workstation capable of running Unreal Engine 5 at 30fps minimum to ensure local testing. 

**P.5-02**: **Software Licenses** The team must ensure valid licenses for all tools used (IDE, 3D Modeling software) or use free educational versions. 

### P.6: Risk and Mitigation Analysis

**P.6-01**: **Bus Factor Mitigation** No critical knowledge shall be held by a single person. Documentation or Pair Programming is mandatory for critical systems.

**P.6-02**: **Data Loss Prevention** A backup of the repository (or a fork) must be updated weekly to prevent total data loss. 

### P.7: Requirements Process and Report

**P.7-01**: **PEGS Framework** The project must strictly follow the PEGS structure for all specification documents.

**P.7-02**: **Validation Review**  Requirements must be reviewed and approved by the Project Manager before development begins on that section. 

## 2. ENVIRONMENT (E)

### E.1: Glossary

**E.1-01 LTS**: **Long Term Support** Refers to the version of the Game Engine (Unreal/Unity) that is guaranteed to be stable for the duration of the project.

**E.1-02**: **Vertical Slice** A portion of the software that demonstrates all layers of the architecture (UI, Logic, Data, Audio) functioning together in a final quality state.

### E.2: Components

**E.2-01**: **Development Engine** This is the core component providing the rendering, physics, and input subsystems.

**E.2-04**: **Audio API** The external component required to interface between the system logic and the user's audio hardware.

**E.2-05**: **Target Hardware** The end-user environment: A PC running Windows 10/11 x64 with a DirectX 12 compatible GPU (Min: GTX 1060).

### E.3: Constraints

**E.3-01**: **OS Compatibility** The system must be compiled exclusively for Windows 10/11 (64-bit). Linux and macOS environments are out of scope.

**E.3-04**: **Offline Operation** The system must function in an environment without internet access (Air-gapped), except for the initial installation.

### E.4: Assumptions

**E.4-01**: **User Privileges** We assume the system has Read/Write access to the user's `Documents/MyGames/` directory for storing configuration and save files.

**E.4-02**: **Driver Status** We assume the target environment has up-to-date GPU drivers (Vulkan/DX12 compliant). No legacy driver support is planned.

**E.4-03**: **Peripheral Availability** We assume the environment includes a standard Keyboard and Mouse or an XInput-compatible Controller.

### E.5: Effects

**E.5-01**: **Disk Footprint**:The system installation will consume approximately 10 GB of storage space on the host environment's drive.

**E.5-04**: **Peripheral Control** The system takes exclusive control of the controller's vibration motors (Haptics) and mouse cursor locking during execution.

### E.6: Invariants

**E.6-01**: **Engine Version** The Unreal Engine version (e.g., 5.3) is locked. The environment will not be upgraded to 5.4+ mid-project to avoid breaking changes.

**E.6-02**: **Repository URL** The remote origin URL of the Git repository is invariant and serves as the single source of truth.

**E.6-03**: **Language Standard** The C++ standard used (e.g., C++17 or C++20) or the blueprint remains constant throughout the codebase lifecycle.

## 3. GOALS (G)

### G.1: Context and Overall Objective

**G.1-01**: **Context** The current horror game market is saturated with supernatural "ghost hunting" simulators and "walking simulators" that rely on jump scares and mystical tropes. Players are becoming desensitized to scripted supernatural events.

**G.1-02**: **Core Concept** The project introduces "Rational Horror": a sub-genre where every perceived paranormal event is generated by a rare but explainable physical phenomenon (Infrasound, Gas leaks, Magnetism).

**G.1-04**: **Innovation** To create a gameplay loop based on Cognitive Dissonance, forcing the player to choose between trusting their senses (which are hallucinating) or their tools (which show the truth).

### G.2: Current Situation

**G.2-01**: **Existing Solutions** Most competitors handle sanity as a simple health bar. When it drops, the game spawns random monsters. There is rarely a mechanic to "cure" the fear through logic.

**G.2-02**: **Technological Gap** Few games utilize Binaural Audio and Volumetric Physics as core gameplay mechanics; they are usually just cosmetic layers.

**G.2-04**: **Opportunity** Unreal Engine 5 now allows for real-time simulation of gas fluids and dynamic lighting (Lumen) necessary to create realistic optical illusions (Pareidolia) without pre-rendered scripts.

### G.3: Expected Benefits

**G.3-01**: **Player Immersion** By removing the HUD and relying on diegetic tools, the player achieves a state of "Flow" and deeper immersion.

**G.3-03**: **Replayability** The systemic nature of the physics engine and the AI means that "scares" are not scripted events but dynamic interactions, making each playthrough unique.

**G.3-04**: **Market Positioning** The studio establishes itself as a pioneer in "Hard Science Horror," differentiating its IP from the mass of supernatural games.

### G.4: Functionality Overview

**G.4-01**: **Investigation System** The ability to equip and use handheld tools (Geiger Counter, Thermal Cam, dB Meter) to scan the environment and identify anomaly sources.

**G.4-02**: **Bio-Feedback Engine** A background system that tracks toxicity, temperature, and noise exposure to trigger procedural audio-visual hallucinations.

**G.4-03**: **Antagonist AI** A non-supernatural enemy agent capable of patrolling, listening for player noise, and sabotaging environmental systems (lights, vents).

**G.4-04**: **Physics Interaction** The ability for the player to manipulate objects (pick up, throw, block doors) to alter the environment or create distractions.

**G.4-05**: **Spatial Audio Navigation** The rendering of 3D audio cues allowing the player to locate invisible hazards or the enemy purely by ear.

### G.5: High-Level Usage Scenario

**G.5-01**: **Step 1 - The Event** The player enters a basement and hears a "demonic scream" and sees a shadow moving on the wall. The vision starts to blur.

**G.5-02**: **Step 2 - Analysis** The player equips the Spectrum Analyzer. The screen shows a spike at 19Hz (Infrasound) coming from an HVAC pipe, not a ghost.

**G.5-03**: **Step 3 - Debunking** The player interacts with the loose pipe to fix it. The vibration stops. The "scream" ceases, and the vision clears (Sanity restores).

**G.5-04**: **Step 4 - The Real Threat** With the noise gone, the player now hears faint footsteps behind them. It wasn't a ghost; the human killer was using the noise to hide his approach.
**G.5-05**: **Step 5 - Survival** The player throws a wrench to create a distraction and hides in a locker to evade the killer.

### G.6: Limitations and Exclusions

**G.6-01**: **No Multiplayer** The game is strictly a narrative Single-Player experience. No Co-op or PvP modes are planned for the initial release.

**G.6-02**: **No Combat Weapons** The player cannot use guns or knives to kill the antagonist. The gameplay focuses on evasion and gadgetry, not lethal combat.

**G.6-03**: **No VR Support** While the concept suits VR, the initial "Vertical Slice" targets Desktop PC only to ensure graphical fidelity.

### G.7: Stakeholders and Requirements Sources

**G.7-01**: **Lead Designer** Source of the core gameplay mechanics, narrative structure, and the "Rational Horror" manifesto.

**G.7-02**: **Target Audience** Hardcore Horror fans and Immersive Sim players (identified via market research and competitive analysis).

**G.7-03**: **Investors/Publishers** Stakeholders defining the budget, the timeline (Milestones), and the rating targets (PEGI 18).

## 4. SYSTEM (S)

### S.1: Components

**S.1-01**: **Chaos Physics Handler** A subsystem leveraging Unreal's Chaos engine to manage deterministic "poltergeist" events. It applies force vectors to specific rigid bodies (books, chairs) to simulate wind drafts or vibration.

**S.1-02**: **AI Sensory Cortex**: The AI sub-component that processes environmental stimuli. It contains a NoiseListener (detects sound events) and a VisionCone (detects light/movement), feeding data to the Behavior Tree.

**S.1-03**: **Tool Logic Controller** The state machine managing the player's active equipment. It handles battery consumption, data visualization (updating textures on tool screens), and state switching (On/Off/Recharge).

### S.2: Functionality

**S.2-03**: **Propagate Sound** The system must calculate audio occlusion in real-time. If a wall exists between the Source and Listener, apply a Low-Pass Filter and volume attenuation curve defined in the Unreal project.

**S.2-04**: **Debunking Logic** The system must validate interactions. If the player uses the "Wrench" tool on a "Loose Pipe" actor, the system must: Stop the Hissing Sound, Disable the Gas Volume, and Reset the player's Stress recovery rate.

**S.2-05**: **AI Pathfinding** The system must update the Antagonist's path dynamically. If the player blocks a door with a physics object, the AI must recalculate a path via the NavMesh or trigger a "Breach" animation to destroy the obstacle.

### S.3: Interfaces

**S.3-01**: **Diegetic User Interface (UI)** The system shall not render 2D HUD elements (Health bars, Ammo). All feedback interfaces must be rendered to "Render Targets" (textures) mapped onto the 3D models of the tools (Watch, Geiger Counter screen).

**S.3-04**: **Input Interface** The system accepts inputs via the Enhanced Input System, mapping logical actions (e.g., Action_Inspect) to physical hardware (e.g., Keyboard_E or Gamepad_FaceButton_Left).

### S.4: Detailed Usage Scenarios

**S.4-02**: **Scenario: Audio Evasion**
1. **System Input** Player sprints across a wooden floor surface.

2. **System Process** AnimNotify on footstep generates a NoiseEvent with Tag Wood and Radius 1500 units.

3. **AI Response** AI Agent within radius receives the event. Switches state from Patrol to Investigate.

4. **AI Action** AI calculates path to the noise location.

5. **Player Response** Player hears AI footsteps approaching via HRTF audio and throws a GlassBottle object into the next room.

6. **System Resolution** Bottle breaks. New NoiseEvent generated. AI updates target to the new noise source, allowing player to slip away.

### S.5: Prioritization

**S.5-01**: **Must Have (Critical)**
Player Movement & Interaction.
Antagonist AI (Pathfinding & Sensing).
Sanity/Toxicity calculation system.
Basic Diegetic Tools (Flashlight, Meter).

**S.5-02**: **sahll Have (Important)**
Advanced Volumetric Fog reacting to light.
Complex physics interactions (blocking doors).
Full Controller Haptics support.

**S.5-03**: **Could Have (Desirable)**
Voice Recognition (AI hears player microphone).
Dynamic destruction of environment walls.

**S.5-04**: **Won't Have (Out of Scope)**
Multiplayer Networking.
Combat weapons (Guns/Melee damage).
VR Support (deferred to post-launch).

### S.6: Verification and Acceptance

**S.6-02**: **Performance Profiling** The system is verified using "Unreal Insights" to ensure the AI logic thread does not exceed 2ms per frame and Total Frame Time remains under 16.6ms (60 FPS).

**S.6-03**: **Playtest Acceptance** A "Vertical Slice" build is played by a focus group (N=10). Acceptance criterion: 80% of players must successfully identify a specific "Ghost" as a physical anomaly without external hints.

**S.6-04**: **Audio Verification** Validation that audio occlusion is functioning by measuring dB levels of a sound source while moving the listener behind geometry (Must show >10dB drop).
