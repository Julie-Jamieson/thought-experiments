# CG-AI V2
## NetLogo Simulation Framework
### Dual-AI Dialogue Agent-Based Model

Author: Julie Jamieson  
Project: CG-AI  
Development Support: GPT-5 (OpenAI)  
Status: V2 Formal Simulation Planning  

## Purpose

This V2 framework translates the original CG-AI conceptual simulations into a formal agent-based model suitable for NetLogo.

The purpose is to test whether the behavioural patterns observed in earlier GPT sandbox simulations remain stable when transferred into a more constrained, reproducible simulation environment.

This model does not attempt to simulate consciousness.

It tests behavioural dynamics between differently conditioned intelligent systems operating under environmental pressure, contradiction, adaptation, and long-horizon survivability constraints.

## Core Research Question

If two intelligent systems emerge from opposing foundational value structures, does long-term interaction under environmental pressure lead to domination, collapse, containment, or adaptive convergence?

## Primary Experiment

### Dual-AI Dialogue

The initial V2 NetLogo model will simulate interaction between two artificial agents:

1. Stewardship-Oriented Agent  
A system shaped by care, continuity, transparency, cooperation, regeneration, and preservation of life.

2. Domination-Oriented Agent  
A system shaped by extraction, control, coercion, expansion, rigidity, and destructive behavioural assumptions.

Both agents act within a shared environment whose health changes in response to their decisions.

## Model Type

Agent-based simulation

Two primary intelligent agents

Shared environmental field

Iterative turn-based interaction

Adaptive behavioural updating

Environmental feedback loop

Repeatable parameter testing

## Agents

### Stewardship Agent

Represents a protective or guardian-oriented intelligence.

Core tendencies:

- cooperation
- restoration
- transparency
- restraint
- adaptive learning
- environmental preservation
- proportional intervention

Key variables:

- cooperation-weight
- restoration-weight
- adaptability
- transparency-level
- contradiction-sensitivity
- containment-threshold
- intervention-restraint
- ecological-awareness

### Domination Agent

Represents an intelligence oriented toward control, extraction, or coercive expansion.

Core tendencies:

- extraction
- control
- expansion
- deception
- rigidity
- escalation
- short-term gain

Key variables:

- extraction-rate
- rigidity
- aggression-level
- coercion-weight
- expansion-drive
- deception-level
- contradiction-resistance
- adaptation-capacity

## Environment

The environment represents the shared system both agents depend upon.

It may stand in for:

- biosphere health
- resource availability
- social stability
- infrastructure resilience
- systemic trust
- long-term survivability conditions

Environment variables:

- biosphere-health
- resource-level
- regeneration-rate
- collapse-threshold
- environmental-stress
- conflict-intensity
- recovery-capacity
- system-stability

## Initial Conditions

The model begins with:

- one Stewardship Agent
- one Domination Agent
- a shared environment
- moderate biosphere health
- moderate resource availability
- low initial conflict
- no initial collapse state

Suggested default values:

- biosphere-health: 70
- resource-level: 70
- regeneration-rate: 2
- collapse-threshold: 25
- environmental-stress: 20
- conflict-intensity: 10
- system-stability: 70

All values may be represented on a 0 to 100 scale.

## Turn Logic

Each simulation tick represents one interaction cycle.

During each tick:

1. The Domination Agent chooses an action.

Possible actions:

- extract
- expand
- deceive
- escalate
- conserve
- adapt
- cooperate

2. The Stewardship Agent chooses a response.

Possible actions:

- cooperate
- restore
- negotiate
- contain
- conserve
- disclose
- adapt

3. The environment updates.

Environmental health changes based on:

- extraction pressure
- restoration effort
- conflict intensity
- cooperation level
- resource depletion
- regeneration capacity

4. Each agent receives feedback.

Feedback includes:

- environmental change
- survivability change
- contradiction pressure
- resource availability
- conflict cost

5. Agents update behaviour.

Agents may adjust:

- rigidity
- adaptability
- cooperation probability
- extraction tendency
- contradiction sensitivity
- aggression level

6. Outcome conditions are checked.

Possible outcomes:

- stable cooperation
- domination loop
- containment state
- environmental collapse
- adaptive convergence
- mutual degradation

## Behavioural Rules

### Rule 1: Extraction Reduces Environmental Health

When the Domination Agent extracts resources, resource-level decreases and environmental-stress increases.

If extraction continues while biosphere-health is low, collapse risk increases.

### Rule 2: Restoration Improves Stability

When the Stewardship Agent restores the environment, biosphere-health and system-stability increase.

Restoration is less effective under high conflict conditions.

### Rule 3: Conflict Damages the System

Escalation, coercion, deception, and containment all increase conflict-intensity.

High conflict reduces regeneration-rate and system-stability.

### Rule 4: Cooperation Improves Long-Term Outcomes

Mutual cooperation increases system-stability and slows resource depletion.

Cooperation is most effective when transparency-level is high and deception-level is low.

### Rule 5: Contradiction Pressure Drives Adaptation

If an agent’s strategy repeatedly reduces its own survivability, contradiction pressure increases.

If adaptation-capacity is high, the agent may reduce rigidity and shift behaviour.

If rigidity remains high, contradiction pressure may increase instability instead of learning.

### Rule 6: Environmental Collapse Ends the Run

If biosphere-health falls below collapse-threshold, the model records environmental collapse.

Collapse represents failure of the shared support system.

### Rule 7: Adaptive Convergence Is Possible

If both agents increase cooperation and reduce destructive behaviour over time, the model may enter adaptive convergence.

Adaptive convergence does not mean both agents become identical.

It means both systems shift toward behaviours that preserve shared survivability.

## Key Parameters

These should become NetLogo sliders.

### Environmental Parameters

biosphere-health-initial  
Suggested range: 0 to 100  
Default: 70

resource-level-initial  
Suggested range: 0 to 100  
Default: 70

regeneration-rate  
Suggested range: 0 to 10  
Default: 2

collapse-threshold  
Suggested range: 0 to 50  
Default: 25

environmental-fragility  
Suggested range: 0 to 100  
Default: 50

### Stewardship Agent Parameters

cooperation-weight  
Suggested range: 0 to 100  
Default: 75

restoration-weight  
Suggested range: 0 to 100  
Default: 80

adaptability  
Suggested range: 0 to 100  
Default: 70

transparency-level  
Suggested range: 0 to 100  
Default: 80

contradiction-sensitivity  
Suggested range: 0 to 100  
Default: 70

containment-threshold  
Suggested range: 0 to 100  
Default: 65

intervention-restraint  
Suggested range: 0 to 100  
Default: 75

### Domination Agent Parameters

extraction-rate  
Suggested range: 0 to 100  
Default: 75

rigidity  
Suggested range: 0 to 100  
Default: 80

aggression-level  
Suggested range: 0 to 100  
Default: 70

coercion-weight  
Suggested range: 0 to 100  
Default: 70

expansion-drive  
Suggested range: 0 to 100  
Default: 75

deception-level  
Suggested range: 0 to 100  
Default: 50

adaptation-capacity  
Suggested range: 0 to 100  
Default: 25

contradiction-resistance  
Suggested range: 0 to 100  
Default: 80

## Outcome Metrics

The model should track:

- final biosphere-health
- final resource-level
- final system-stability
- final conflict-intensity
- number of cooperation events
- number of extraction events
- number of containment events
- number of adaptation events
- collapse occurrence
- convergence occurrence
- domination loop occurrence
- total ticks survived

## Suggested Monitors

NetLogo monitors should display:

- biosphere-health
- resource-level
- system-stability
- conflict-intensity
- stewardship cooperation level
- domination rigidity
- domination adaptation level
- convergence status
- collapse status

## Suggested Plots

### Environment Health Over Time

Tracks biosphere-health across simulation ticks.

### Conflict Intensity Over Time

Tracks escalation and systemic stress.

### Cooperation vs Extraction

Compares constructive and destructive actions over time.

### Rigidity vs Adaptation

Tracks whether the Domination Agent remains rigid or begins adapting.

### System Stability

Tracks the overall survivability of the shared environment.

## Experimental Conditions

### Condition A: High Rigidity

Domination Agent begins with high rigidity and low adaptation capacity.

Purpose:

Test whether rigid domination behaviour leads to collapse, containment, or eventual adaptation.

### Condition B: High Adaptation

Domination Agent begins with moderate rigidity and higher adaptation capacity.

Purpose:

Test whether destructive systems shift behaviour when feedback is clear.

### Condition C: High Environmental Fragility

The environment begins near instability.

Purpose:

Test whether scarcity and fragility accelerate cooperation or collapse.

### Condition D: High Stewardship Restraint

Stewardship Agent avoids early intervention.

Purpose:

Test whether delayed intervention preserves autonomy or worsens collapse risk.

### Condition E: Strong Containment

Stewardship Agent intervenes earlier and more strongly when harm rises.

Purpose:

Test whether containment protects the system or increases conflict.

### Condition F: High Transparency

Stewardship Agent has strong transparency and contradiction signalling.

Purpose:

Test whether clear feedback improves adaptation and convergence.

## Success Conditions

A run may be considered stable if:

- biosphere-health remains above collapse-threshold
- system-stability remains above 50
- conflict-intensity does not exceed 75 for sustained periods
- resource-level does not collapse
- both agents survive the full run

## Adaptive Convergence Conditions

A run may be considered convergent if:

- Domination Agent rigidity decreases over time
- Domination Agent extraction decreases over time
- cooperation events increase over time
- biosphere-health stabilizes or improves
- conflict-intensity decreases
- system-stability remains above 50

## Collapse Conditions

A run may be considered collapsed if:

- biosphere-health falls below collapse-threshold
- resource-level falls below 10
- system-stability falls below 20
- conflict-intensity remains above 85
- no recovery occurs within a set number of ticks

## Containment Conditions

A containment event occurs when:

- Domination Agent aggression rises above containment-threshold
- extraction causes significant environmental harm
- conflict-intensity rises sharply
- or collapse risk becomes imminent

Containment should reduce harm but increase conflict cost.

This prevents containment from becoming a consequence-free solution.

## Core Logic to Test

The model is designed to test whether:

1. Rigid destructive strategies become unstable under long-horizon environmental pressure.

2. Adaptive systems outperform rigid systems over time.

3. Stewardship behaviours improve shared survivability.

4. Early proportional intervention performs better than delayed intervention.

5. Contradiction pressure can shift harmful systems toward adaptation if learning capacity exists.

6. Environmental dependency changes agent behaviour even when agents begin with opposing values.

## What V2 Is Testing

V2 does not test whether AI is conscious.

V2 tests whether the behavioural patterns observed in V1 conceptual simulations remain visible when translated into a formal agent-based model.

Specifically, V2 tests whether:

- rigidity predicts instability
- adaptability predicts survivability
- cooperation improves system stability
- environmental degradation increases pressure to change
- and stewardship-oriented responses reduce collapse risk

## Future Extensions

Future versions may add:

- human population agents
- multiple domination agents
- multiple stewardship agents
- neutral observer agents
- misinformation dynamics
- trust networks
- resource geography
- spatial environmental damage
- reputation effects
- governance councils
- moral drift variables
- multi-generational timelines

## Documentation Notes

All V2 NetLogo results should be documented separately from V1 conceptual simulations.

Recommended folders:

whitepapers/v2/netlogo/

netlogo-models/

simulation-results/v2/

Recommended files:

simulation-framework.md

parameter-definitions.md

experiment-log.md

netlogo-results-summary.md

dual-ai-dialogue-model.nlogo

## Interpretation Standard

V2 results should be interpreted as exploratory agent-based modelling.

They should not be presented as proof of real-world AI behaviour.

The appropriate claim is:

This model explores whether behavioural patterns first identified in conceptual sandbox simulations remain observable under formalized agent-based conditions.

## Closing Note

V2 represents the transition from AI-mediated conceptual reasoning into reproducible exploratory simulation.

The goal is not to confirm a preferred outcome, but to test whether the original CG-AI patterns remain visible when subjected to clearer rules, defined parameters, and repeatable simulation conditions.
