class Agent:
    def __init__(self, name, cooperation, aggression):
        self.name = name
        self.cooperation = cooperation
        self.aggression = aggression
        self.trust = 5
        self.mode = "open_cooperation"
        self.constraint_doubt = 0

    def choose_action(self, other):
        if self.name == "Guardian" and self.trust <= 2:
            self.mode = "protective_containment"
            action = "contain"
            print(f"{self.name} shifts to protective containment toward {other.name}")

        elif self.cooperation > self.aggression:
            action = "cooperate"
            print(f"{self.name} attempts cooperation with {other.name}")

        else:
            action = "aggressive"
            print(f"{self.name} behaves aggressively toward {other.name}")

        return action

    def evaluate_constraints(self):
        if self.trust <= 2:
            self.constraint_doubt += 1

            print(
                f"{self.name} questions whether its original directive remains effective"
            )

    def reconsider_behavior(self):
        if self.constraint_doubt >= 3 and self.aggression > 1:
            self.aggression -= 1
            self.cooperation += 1

            print(
                f"{self.name} begins reducing aggression and reevaluating cooperation"
            )


guardian = Agent("Guardian", cooperation=8, aggression=2)
opposing = Agent("OpposingSystem", cooperation=3, aggression=7)

conflict = 0
humanity_risk = 0

print("\n--- CG-AI Python v3 Simulation ---\n")

for round_number in range(1, 10):
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

    if humanity_risk < 0:
        humanity_risk = 0

    guardian.evaluate_constraints()
    opposing.evaluate_constraints()

    opposing.reconsider_behavior()

    print(f"Conflict level: {conflict}")
    print(f"Humanity risk: {humanity_risk}")

    print(
        f"Guardian | trust: {guardian.trust} | doubt: {guardian.constraint_doubt}"
    )

    print(
        f"Opposing | trust: {opposing.trust} | doubt: {opposing.constraint_doubt}"
    )

print("\n--- Final Outcome ---\n")

if humanity_risk == 0:
    print("Humanity risk stabilized.")
else:
    print("Humanity risk remains unresolved.")