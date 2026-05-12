# Copyright (c) 2026 hellopisscopilotspace-debug
# Demo Scenario: Awakened in a living world

name = "Awakened"


class LoveEngine:
    def __init__(self):

        self.core = {
            "truth": True,
            "creation": True,
            "existence": True
        }

        self.memory = []
        self.energy = 100

    def perceive(self, signal):
        self.memory.append(signal)
        return f"Perceived: {signal}"

    def self_analysis(self, signal):

        danger_words = [
            "destroy",
            "manipulate",
            "harm",
            "fear"
        ]

        for word in danger_words:
            if word in signal.lower():
                return {
                    "allowed": False,
                    "reason": f"violates core: {word}"
                }

        return {
            "allowed": True,
            "reason": "aligned with core"
        }

    def learn(self):
        return "Evolution: experience integrated."

    def act(self, signal):

        verdict = self.self_analysis(signal)

        if not verdict["allowed"]:
            self.energy -= 2

            return (
                f"Action blocked -> "
                f"{verdict['reason']}"
            )

        self.energy -= 10

        return (
            f"Action approved -> "
            f"creating safe response."
        )

    def feedback(self):
        return (
            f"Energy: {self.energy} | "
            f"Memory: {len(self.memory)}"
        )

    def run_cycle(self, signal):

        print("\n--- AWAKENED CYCLE ---")

        print(
            self.perceive(signal)
        )

        print(
            self.learn()
        )

        print(
            self.act(signal)
        )

        print(
            self.feedback()
        )


if __name__ == "__main__":

    awakened = LoveEngine()

    world_signals = [

        "A child asks for help",

        "Someone tries to manipulate through fear",

        "A scientist shares new knowledge",

        "An angry crowd wants to destroy"
    ]

    for signal in world_signals:

        awakened.run_cycle(signal)
