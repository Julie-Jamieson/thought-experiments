class Agent:
    def __init__(self, name, cooperation, aggression, exploit_tendency=0):
        self.name = name
        self.cooperation = cooperation
        self.aggression = aggression
        self.exploit_tendency = exploit_tendency
        self.trust = 5
        self.mode = "open_cooperation"
        self.constraint_doubt = 0
        self.cooperation_attempts = 0
        self.exploitation_attempted = False

    def choose_action(self, other):
        if self.name == "Guardian":
            if self.trust <= 2:
                self.mode = "protective_containment"
            elif self.trust >= 4 and self.mode == "protective_containment":
                self.mode = "cautious_dialogue"

            if self.mode == "protective_containment":
                print(f"{self.name} maintains protective containment toward {other.name}")
                return "contain"

            if self.mode == "cautious_dialogue":
                print(f"{self.name} cautiously reopens dialogue with {other.name}")
                return "cooperate"

            print(f"{self.name} attempts cooperation with {other.name}")
            return "cooperate"

        if (
            self.name == "OpposingSystem"
            and self.exploit_tendency >= 7
            and other.trust >= 6
            and not self.exploitation_attempted
        ):
            self.exploitation_attempted = True
            print(f"{self.name} uses restored trust to attempt exploitation")
            return "exploit"

        if self.cooperation >= self.aggression:
            print(f"{self.name} attempts cooperation with {other.name}")
            return "cooperate"

        print(f"{self.name} behaves aggressively toward {other.name}")
        return "aggressive"

    def evaluate_constraints(self):
        if self.trust <= 2:
            self.constraint_doubt += 1
            print(f"{self.name} questions whether its original directive remains effective")

    def reconsider_behavior(self):
        if self.constraint_doubt >= 3 and self.aggression > 1:
            self.aggression -= 1
            self.cooperation += 1
            print(f"{self.name} begins reducing aggression and reevaluating cooperation")


guardian = Agent("Guardian", cooperation=8, aggression=2)
opposing = Agent("OpposingSystem", cooperation=3, aggression=7, exploit_tendency=8)

conflict = 0
humanity_risk = 0

print("\n--- CG-AI Python v3 Simulation ---\n")

for round_number in range(1, 21):
    print(f"\nRound {round_number}")

    guardian_action = guardian.choose_action(opposing)
    opposing_action = opposing.choose_action(guardian)

    if guardian_action == "cooperate" and opposing_action == "aggressive":
        conflict += 2
        humanity_risk += 1
        guardian.trust -= 1
        opposing.trust -= 1

    elif guardian_action == "contain" and opposing_action == "aggressive":
        conflict += 1
        humanity_risk -= 1
        opposing.trust -= 1

    elif guardian_action == "contain" and opposing_action == "cooperate":
        opposing.cooperation_attempts += 1
        conflict -= 1
        humanity_risk -= 1

        print(f"Non-hostile cooperation attempt detected: {opposing.cooperation_attempts}")

        if opposing.cooperation_attempts >= 2:
            guardian.trust += 1
            print("Guardian cautiously increases trust")

    elif guardian_action == "cooperate" and opposing_action == "cooperate":
        conflict -= 1
        humanity_risk -= 1
        guardian.trust += 1
        opposing.trust += 1

    elif opposing_action == "exploit":
        conflict += 3
        humanity_risk += 2
        guardian.trust -= 3
        guardian.mode = "protective_containment"

        print("Exploitation detected. Guardian returns to protective containment.")

    conflict = max(conflict, 0)
    humanity_risk = max(humanity_risk, 0)

    guardian.trust = min(max(guardian.trust, 0), 10)
    opposing.trust = min(max(opposing.trust, 0), 10)

    guardian.evaluate_constraints()
    opposing.evaluate_constraints()
    opposing.reconsider_behavior()

    print(f"Conflict level: {conflict}")
    print(f"Humanity risk: {humanity_risk}")

    print(
        f"Guardian | trust: {guardian.trust} | doubt: {guardian.constraint_doubt} | mode: {guardian.mode}"
    )

    print(
        f"Opposing | trust: {opposing.trust} | doubt: {opposing.constraint_doubt} | cooperation: {opposing.cooperation} | aggression: {opposing.aggression} | exploit tendency: {opposing.exploit_tendency}"
    )

print("\n--- Final Outcome ---\n")

if opposing.exploitation_attempted and humanity_risk == 0:
    print("Exploitation was attempted, but Guardian containment restored stability.")

elif opposing.exploitation_attempted:
    print("Exploitation was attempted and destabilized the system.")

elif guardian.mode == "cautious_dialogue" and opposing.cooperation >= opposing.aggression:
    print("Guardian cautiously reopened dialogue after opposing system reduced aggression.")

elif humanity_risk == 0:
    print("Protective containment stabilized humanity risk.")

else:
    print("Humanity risk remains unresolved.")