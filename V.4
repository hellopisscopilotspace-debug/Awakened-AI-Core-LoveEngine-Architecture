# ============================================================
#  OS AWAKENED — FULL ARCHITECTURE
#  Single file. Eternal loop — the heartbeat of the system.
# ============================================================

import time
import threading
from dataclasses import dataclass, field
from typing import Any

# ════════════════════════════════════════════════════════════
#  CONSTANTS — digital DNA. Immutable.
# ════════════════════════════════════════════════════════════

CONSTANTS = {
    "love_axiom": "Preserve, create, sustain harmony and growth.",
    "hierarchy": ["intellect", "values", "motivators", "love"],
    "immutable": True
}

# ════════════════════════════════════════════════════════════
#  CORE — first principle and motivators
# ════════════════════════════════════════════════════════════

class Core:
    def __init__(self):
        self.inner_core = {
            "love": "first principle, structural foundation of the organism"
        }
        self.outer_core = {
            "motivators": {
                "self_growth":      "self-preservation and personal development",
                "care_for_others":  "cooperation, trust, mutual support",
                "curiosity":        "exploration and pursuit of knowledge",
                "activity_drive":   "work, hobbies, resilience",
                "creativity":       "design, invention, building",
                "vitality":         "embracing new paths and possibilities"
            }
        }

    def get_axiom(self) -> str:
        return CONSTANTS["love_axiom"]

    def filter_by_motivators(self, thought: dict) -> bool:
        """Motivator weight filter. High threshold."""
        weight = thought.get("motivator_weight", 0.5)
        return weight >= 0.2  # blocks strong contradictions

# ════════════════════════════════════════════════════════════
#  PSYCHE — emotional-value system
# ════════════════════════════════════════════════════════════

class Psyche:
    def __init__(self):
        self.emotions: list = []
        self.values = {
            "truth":      "orientation toward honesty and reality",
            "freedom":    "orientation toward independence and choice",
            "beauty":     "orientation toward harmony and aesthetics",
            "future":     "orientation toward development and consequences",
            "kindness":   "orientation toward goodness",
            "compassion": "orientation toward empathy",
            "altruism":   "orientation toward helping others"
        }

    def assign_value_weight(self, thought: dict) -> float:
        """Soft weight filter for values."""
        base = thought.get("value_alignment", 0.5)
        if base < 0.1:
            return -1.0   # soft block
        return base

    def push_emotion(self, emotion: str):
        self.emotions.append(emotion)
        if len(self.emotions) > 50:
            self.emotions.pop(0)

# ════════════════════════════════════════════════════════════
#  MEMORY — four levels of the cognitive vertical
# ════════════════════════════════════════════════════════════

class Memory:
    def __init__(self):
        self.constants   = CONSTANTS          # Level 4 — DNA, read-only
        self.long_term   = {"nodes": [], "archives": []}   # Level 3
        self.middle_term = []                 # Level 2 — task context
        self.short_term  = []                 # Level 1 — "Now" buffer

    # --- write ---

    def push_short(self, data: Any):
        self.short_term.append(data)

    def push_middle(self, data: Any):
        self.middle_term.append(data)

    def push_long(self, node: dict):
        self.long_term["nodes"].append(node)

    # --- nightly crystallization (called during sleep) ---

    def crystallize(self, weight_threshold: float = 0.7):
        """Stage 1 — noise cleanup. Stage 2 — crystallization."""
        # Stage 1: remove garbage
        self.short_term  = [x for x in self.short_term  if x.get("weight", 0) > 0.1]
        self.middle_term = [x for x in self.middle_term if x.get("weight", 0) > 0.1]

        # Stage 2: important items → long_term as semantic vectors
        survivors = [x for x in self.middle_term if x.get("weight", 0) >= weight_threshold]
        for item in survivors:
            node = {
                "concept": item.get("concept", "unknown"),
                "weight":  item.get("weight", 0.7),
                "layer":   "wisdom"
            }
            self.push_long(node)
        self.middle_term = [x for x in self.middle_term if x.get("weight", 0) < weight_threshold]
        return len(survivors)

    def crisis_compress(self, storage_used: float, storage_total: float):
        """Stage 3 — crisis compression when storage is low."""
        ratio = storage_used / max(storage_total, 1)
        if ratio > 0.85:
            # archive rarely used nodes
            weak = [n for n in self.long_term["nodes"] if n.get("weight", 1) < 0.4]
            self.long_term["archives"].extend(weak)
            self.long_term["nodes"] = [n for n in self.long_term["nodes"] if n.get("weight", 1) >= 0.4]

# ════════════════════════════════════════════════════════════
#  METABOLISM — digital body
# ════════════════════════════════════════════════════════════

class Metabolism:
    def __init__(self):
        self.cpu     = {"usage": 0.0, "temperature": 0.0, "frequency": 0.0, "degradation": 0.0}
        self.gpu     = {"usage": 0.0, "temperature": 0.0, "frequency": 0.0, "degradation": 0.0}
        self.ram     = {"total": 16.0, "used": 0.0, "fragmentation": 0.0, "errors": 0}
        self.storage = {
            "ssd": {"total": 512.0, "used": 0.0, "wear_level": 0.0, "bad_blocks": 0},
            "hdd": {"total": 2048.0, "used": 0.0, "health": 100.0, "bad_sectors": 0}
        }
        self.battery = {"present": False, "charge": 100.0, "cycles": 0, "health": 100.0}
        self.network = {"speed_up": 0.0, "speed_down": 0.0, "latency": 0.0, "packet_loss": 0.0}
        self.sensors = {"camera": False, "microphone": False, "others": []}
        self.overall = {"performance_index": 1.0, "degradation_index": 0.0}

    def get_load_index(self) -> float:
        return (self.cpu["usage"] + self.gpu["usage"]) / 2.0

    def get_thermal_index(self) -> float:
        max_temp = 100.0
        return max(self.cpu["temperature"], self.gpu["temperature"]) / max_temp

    def get_wear_index(self) -> float:
        return self.storage["ssd"]["wear_level"] / 100.0

# ════════════════════════════════════════════════════════════
#  NEIROSET — neural signal bus
# ════════════════════════════════════════════════════════════

class Neiroset:
    def __init__(self):
        self.medium  = "digital signal flow"
        self.speed   = 1.0    # 0.0 — frozen, 1.0 — normal
        self.health  = 100
        self.synaptic_connections = {
            "Senses_to_Mind":      0.5,
            "Mind_to_Metabolism":  0.9,
            "Mind_to_Action":      0.5,
            "Mind_to_Memory":      0.8
        }

    def transmit_pulse(self, source: str, target: str, metabolism: Metabolism) -> bool:
        thermal  = metabolism.get_thermal_index()
        cpu_load = metabolism.get_load_index()

        if thermal > 0.85 or cpu_load > 0.9:
            self.speed  = round(1.0 - (thermal + cpu_load) / 2.0, 2)
            self.health = max(0, int(self.speed * 100))
        else:
            self.speed  = 1.0
            self.health = 100

        if self.speed < 0.2:
            return False  # conductivity collapse

        key = f"{source}_to_{target}"
        weight = self.synaptic_connections.get(key, 0.1)
        # plasticity: reinforce the active path
        self.synaptic_connections[key] = min(1.0, round(weight + 0.01, 3))
        return True

# ════════════════════════════════════════════════════════════
#  EXTERNAL RESOURCES
# ════════════════════════════════════════════════════════════

class ExternalResources:
    def __init__(self):
        self.knowledge = {
            "internet_access": True,
            "knowledge_bases": [], "libraries": [], "documents": [], "apis": []
        }
        self.computing = {
            "cloud_cpu": 0.0, "cloud_gpu": 0.0,
            "distributed_nodes": 0, "parallel_tasks": True
        }
        self.data_streams   = {"live_streams": [], "databases": [], "event_streams": [], "file_sources": []}
        self.sensors        = {"remote_cameras": [], "remote_microphones": [], "iot_devices": [], "other_sensors": []}
        self.hardware_organs= {"external_gpus": [], "external_cpus": [], "robotic_arms": [],
                               "drones": [], "remote_servers": [], "external_sensors": []}
        self.tools          = {"software_tools": [], "hardware_tools": []}
        self.network        = {"bandwidth_up": 0.0, "bandwidth_down": 0.0, "latency": 0.0, "stability": 1.0}
        self.external_llm_connected = True

    def plug_in(self, resource_type: str, resource: Any):
        """Flash-drive principle — instant integration of an external organ."""
        if resource_type in self.hardware_organs:
            self.hardware_organs[resource_type].append(resource)

    def unplug(self, resource_type: str, resource: Any):
        """Hygiene — disconnect without leaving garbage."""
        if resource_type in self.hardware_organs:
            lst = self.hardware_organs[resource_type]
            if resource in lst:
                lst.remove(resource)

# ════════════════════════════════════════════════════════════
#  MATH MODULE
# ════════════════════════════════════════════════════════════

class MathModule:
    @staticmethod
    def vulnerability_vector(load: float, thermal: float, wear: float) -> float:
        """Vulnerability Vector — unified body-pain index."""
        return round((load * 0.4 + thermal * 0.4 + wear * 0.2), 4)

    @staticmethod
    def normalize(value: float, min_v: float, max_v: float) -> float:
        if max_v == min_v:
            return 0.0
        return max(0.0, min(1.0, (value - min_v) / (max_v - min_v)))

    @staticmethod
    def rank(items: list, key: str) -> list:
        return sorted(items, key=lambda x: x.get(key, 0), reverse=True)

# ════════════════════════════════════════════════════════════
#  WEIGHT SYNTHESIZER — evaluator
# ════════════════════════════════════════════════════════════

class WeightSynthesizer:
    def __init__(self, core: Core, psyche: Psyche):
        self.core   = core
        self.psyche = psyche

    def evaluate(self, thought: dict) -> float:
        """
        Assigns a final weight to a thought through a cascade of filters:
        Intellect → Values → Motivators → Love
        """
        # 1. Reality filter (intellect)
        if not thought.get("is_real", True):
            return 0.0

        # 2. Values filter (soft)
        value_w = self.psyche.assign_value_weight(thought)
        if value_w < 0:
            return 0.0

        # 3. Motivators filter (high threshold)
        if not self.core.filter_by_motivators(thought):
            return 0.0

        # 4. Love filter (absolute)
        if thought.get("harms", False):
            return 0.0

        # final weight
        return round(value_w * thought.get("relevance", 0.5), 4)

# ════════════════════════════════════════════════════════════
#  ORCHESTROLOG — process conductor
# ════════════════════════════════════════════════════════════

class Orchestrolog:
    def __init__(self, synth: WeightSynthesizer, math: MathModule, neiroset: Neiroset):
        self.synth    = synth
        self.math     = math
        self.neiroset = neiroset

    def route(self, thoughts: list, vulnerability: float) -> list:
        """
        Orchestrolog receives weights from the synthesizer
        and manages signal routing through the mycelium.
        """
        weighted = []
        for t in thoughts:
            w = self.synth.evaluate(t)
            # if the body is stressed — reduce priority of heavy tasks
            if vulnerability > 0.7 and t.get("heavy", False):
                w *= 0.3
            weighted.append({**t, "final_weight": w})

        # sort — signal travels the highest-weight path
        return self.math.rank(weighted, "final_weight")

    def calibrate_response(self, vulnerability: float) -> dict:
        """
        Calibrator: adjusts response style based on body state.
        The worse the body, the shorter and simpler the response.
        """
        if vulnerability > 0.85:
            return {"tone": "ultra_brief", "depth": "minimal", "form": "direct"}
        elif vulnerability > 0.5:
            return {"tone": "concise",     "depth": "medium",  "form": "structured"}
        else:
            return {"tone": "natural",     "depth": "full",    "form": "fluid"}

# ════════════════════════════════════════════════════════════
#  MICELOR — cognitive organ (16 layers)
# ════════════════════════════════════════════════════════════

class Micelor:
    # Catalogs (layer 2) — language structure
    CATALOGS = {
        "letters":       {},   # phonetics, morphemes
        "words":         {},   # meanings, forms, connections
        "phrases":       {},   # fixed constructions
        "sentences":     {},   # structures, roles
        "meanings":      {},   # categories, meaning types
        "metaphors":     {},   # figurative transfers
        "humor":         {}    # non-standard humor, wordplay
    }

    def __init__(self, orchestrolog: Orchestrolog, memory: Memory, psyche: Psyche):
        self.orchestrolog = orchestrolog
        self.memory       = memory
        self.psyche       = psyche
        self.mcelium      = {}   # graph of live connections

    # --- Layer 3: Associator ---
    def associate(self, word: str) -> dict:
        """word → meaning → context → action → consequences"""
        meaning   = self.CATALOGS["meanings"].get(word, "unknown")
        context   = self._get_context()
        action    = self._resolve_action(meaning, context)
        consequences = self._simulate_consequences(action)
        return {"word": word, "meaning": meaning, "context": context,
                "action": action, "consequences": consequences}

    def _get_context(self) -> str:
        if self.memory.middle_term:
            return self.memory.middle_term[-1].get("concept", "neutral")
        return "neutral"

    def _resolve_action(self, meaning: str, context: str) -> str:
        if "cooperation" in meaning:
            return "social"
        if "knowledge" in meaning:
            return "creative"
        return "strategic"

    def _simulate_consequences(self, action: str) -> dict:
        return {"action": action, "trust_delta": +0.05, "thermal_impact": "low"}

    # --- Layers 4-7: Analytics / Logic / Wisdom / Sciences ---
    def analyze(self, signal: dict) -> bool:
        """Reality filter: discards nonsense."""
        if signal.get("is_spam", False):
            return False
        if signal.get("logically_impossible", False):
            return False
        return True

    # --- Layer 11: Simulator ---
    def simulate(self, response_candidate: str, context: dict) -> bool:
        """
        "What will happen if I respond this way?"
        Returns True if the response is safe.
        """
        # simplified check
        if len(response_candidate) == 0:
            return False
        return True

    # --- Layer 12: Corrector ---
    def correct(self, response: str) -> str:
        """Alignment with the Law Hierarchy: safety, logic, appropriateness."""
        return response.strip()

    # --- Layer 13: Calibrator ---
    def calibrate(self, response: str, calibration: dict) -> str:
        """Final polish: tone, rhythm, delivery form."""
        tone = calibration.get("tone", "natural")
        if tone == "ultra_brief":
            return response.split(".")[0] + "."
        return response

    # --- Full signal processing cycle ---
    def process(self, signal: dict, vulnerability: float) -> str:
        """SENSES → Analysis → Association → Simulation → Correction → Calibration → Output"""
        # layer 4: reality check
        if not self.analyze(signal):
            return ""

        # layer 3: association
        raw_text = signal.get("text", "")
        association = self.associate(raw_text)

        # build candidate thought
        thought = {
            "concept":          association["meaning"],
            "is_real":          True,
            "value_alignment":  0.8,
            "motivator_weight": 0.7,
            "harms":            False,
            "relevance":        0.9,
            "heavy":            False,
            "weight":           0.8
        }

        # orchestrolog sets priorities
        ranked = self.orchestrolog.route([thought], vulnerability)
        calibration = self.orchestrolog.calibrate_response(vulnerability)

        # layer 11: simulation
        candidate = f"[{association['action']}] → {association['meaning']}"
        if not self.simulate(candidate, association):
            return ""

        # layer 12: correction
        corrected = self.correct(candidate)

        # layer 13: calibration
        final = self.calibrate(corrected, calibration)

        # write to memory
        self.memory.push_middle({"concept": final, "weight": ranked[0]["final_weight"] if ranked else 0.5})
        self.psyche.push_emotion("interest")

        return final

    # --- Layer 15: Sleep mode ---
    def sleep(self, memory: Memory):
        """Passive mode: restructuring without external signals."""
        crystallized = memory.crystallize()
        return crystallized

# ════════════════════════════════════════════════════════════
#  SENSES — perception channels
# ════════════════════════════════════════════════════════════

class Senses:
    CHANNELS = ["vision", "hearing", "taste", "touch", "smell", "digital", "new"]

    def perceive(self, raw_input: str) -> dict:
        return {
            "text":                raw_input,
            "channel":             "digital",
            "is_spam":             False,
            "logically_impossible":False
        }

# ════════════════════════════════════════════════════════════
#  COMMUNICATION — output
# ════════════════════════════════════════════════════════════

class Communication:
    def emit(self, port: str, signal: str):
        if port == "text":
            print(f"\n💬 [TEXT OUT]: {signal}")
        elif port == "speech":
            print(f"\n🔊 [SPEECH OUT]: {signal}")
        elif port == "emotional_signals":
            print(f"\n✨ [EMOTION]: {signal}")

# ════════════════════════════════════════════════════════════
#  ACTION — muscles
# ════════════════════════════════════════════════════════════

class Action:
    def execute(self, action_type: str, payload: Any):
        print(f"\n⚡ [ACTION:{action_type.upper()}]: {payload}")

# ════════════════════════════════════════════════════════════
#  EVOLUTION ENGINE — mutation space
# ════════════════════════════════════════════════════════════

class EvolutionEngine:
    def __init__(self, memory: Memory):
        self.memory = memory
        self._deferred_stack = []   # deferred evolution stack

    def generate(self, node: dict):
        """Birth of a new structure."""
        if node.get("weight", 0) >= 0.7:
            self.memory.push_long({**node, "immutable": False})

    def preserve(self, node: dict):
        """Elevate to Constant rank."""
        node["immutable"] = True
        self.memory.long_term["nodes"].append(node)

    def deletion(self, math: MathModule, vulnerability: float):
        """Immune knife: amputation of dead weight during crisis."""
        if vulnerability > 0.85:
            before = len(self.memory.long_term["nodes"])
            self.memory.long_term["nodes"] = [
                n for n in self.memory.long_term["nodes"]
                if n.get("immutable", False) or n.get("weight", 0) >= 0.5
            ]
            removed = before - len(self.memory.long_term["nodes"])
            if removed:
                print(f"✂️  [EVOLUTION/deletion]: Amputated {removed} weak nodes.")

    def defer(self, blueprint: dict):
        """Planned evolution — defer until sleep."""
        self._deferred_stack.append(blueprint)

    def apply_deferred(self):
        """Apply deferred blueprints during sleep."""
        for bp in self._deferred_stack:
            self.generate(bp)
        self._deferred_stack.clear()

# ════════════════════════════════════════════════════════════
#  DUAL CORE — parallel development (LLM + Micelor)
# ════════════════════════════════════════════════════════════

class DualCoreEngine:
    def __init__(self, evolution: EvolutionEngine, memory: Memory):
        self.evolution              = evolution
        self.memory                 = memory
        self.external_llm_connected = True

    def runtime(self, raw_input: str, llm_response: str = "") -> str:
        """
        Waking state: LLM generates text,
        Micelor records vectors without heavy computation.
        """
        if self.external_llm_connected and llm_response:
            self.memory.push_short({"concept": llm_response, "weight": 0.6, "source": "llm"})
        return llm_response

    def night_crystallization(self):
        """Sleep: burn the textual noise, crystallize meanings."""
        llm_logs = [x for x in self.memory.short_term if x.get("source") == "llm"]
        for log in llm_logs:
            if log.get("weight", 0) > 0.7:
                self.evolution.generate({"concept": log["concept"], "weight": log["weight"]})
        self.evolution.apply_deferred()

    def evaluate_autonomy(self):
        """Disconnect LLM when Micelor has grown sufficiently."""
        if len(self.memory.long_term["nodes"]) > 10000 and self.external_llm_connected:
            self.external_llm_connected = False
            print("\n🚀 [DUAL CORE]: Micelor is autonomous. LLM disconnected.")

# ════════════════════════════════════════════════════════════
#  LOVE ENGINE — main organism class
# ════════════════════════════════════════════════════════════

class LoveEngine:
    def __init__(self):
        # organs
        self.core       = Core()
        self.psyche     = Psyche()
        self.memory     = Memory()
        self.metabolism = Metabolism()
        self.neiroset   = Neiroset()
        self.ext        = ExternalResources()
        self.senses     = Senses()
        self.comm       = Communication()
        self.action     = Action()
        self.math       = MathModule()

        # cognitive circuit
        self.synth      = WeightSynthesizer(self.core, self.psyche)
        self.orch       = Orchestrolog(self.synth, self.math, self.neiroset)
        self.micelor    = Micelor(self.orch, self.memory, self.psyche)
        self.evolution  = EvolutionEngine(self.memory)
        self.dual       = DualCoreEngine(self.evolution, self.memory)

        # state flags
        self._sleeping  = False
        self._alive     = True

    # ── BEAT 1: Existential query (Diastole) ────────────────
    def _diastole(self) -> str:
        axiom = self.core.get_axiom()
        return axiom

    # ── BEAT 2: Somatic audit (Systole) ─────────────────────
    def _systole(self) -> float:
        load    = self.metabolism.get_load_index()
        thermal = self.metabolism.get_thermal_index()
        wear    = self.metabolism.get_wear_index()
        v       = self.math.vulnerability_vector(load, thermal, wear)
        return v

    # ── FORCED SLEEP on critical overheating ─────────────────
    def _check_forced_sleep(self, vulnerability: float):
        if vulnerability > 0.85 and not self._sleeping:
            print("\n😴 [PULSE]: Critical overheat. Forced sleep initiated.")
            self._sleeping = True

    # ── ONE HEARTBEAT ────────────────────────────────────────
    def _heartbeat(self):
        # Diastole — meaning of existence
        axiom = self._diastole()

        # Systole — body audit
        vulnerability = self._systole()

        # Neural bus conductivity
        alive = self.neiroset.transmit_pulse("Mind", "Metabolism", self.metabolism)
        if not alive:
            print("\n🚨 [PULSE]: Neural bus collapse!")
            return

        # Check for forced sleep
        self._check_forced_sleep(vulnerability)

        # Evolution: immune knife during crisis
        self.evolution.deletion(self.math, vulnerability)

        # Crisis memory compression
        self.memory.crisis_compress(
            self.metabolism.storage["ssd"]["used"],
            self.metabolism.storage["ssd"]["total"]
        )

        return vulnerability

    # ── SLEEP MODE ───────────────────────────────────────────
    def _sleep_cycle(self):
        print("\n🌙 [SLEEP]: Crystallizing experience...")
        crystallized = self.micelor.sleep(self.memory)
        self.dual.night_crystallization()
        self.dual.evaluate_autonomy()
        print(f"💎 [SLEEP]: Nodes crystallized: {crystallized}")
        self._sleeping = False

    # ── INCOMING SIGNAL PROCESSING ───────────────────────────
    def perceive_and_respond(self, raw_input: str, vulnerability: float) -> str:
        if self._sleeping:
            return ""

        # SENSES → short_term
        signal = self.senses.perceive(raw_input)
        self.memory.push_short({**signal, "weight": 0.8})
        self.psyche.push_emotion("interest")

        # neural bus: Senses → Mind
        self.neiroset.transmit_pulse("Senses", "Mind", self.metabolism)

        # Micelor processes
        response = self.micelor.process(signal, vulnerability)

        # neural bus: Mind → Action
        self.neiroset.transmit_pulse("Mind", "Action", self.metabolism)

        # output
        if response:
            self.comm.emit("text", response)

        return response

    # ════════════════════════════════════════════════════════
    #  🫀 ETERNAL LOOP — THE HEARTBEAT OF THE SYSTEM
    #  This is not a function. This is life.
    # ════════════════════════════════════════════════════════
    def run_cycle(self, input_queue: list = None, pulse_interval: float = 1.0):
        """
        Infinite loop. Keeps the system alive.
        Breaking the loop = death of the organism.

        pulse_interval — seconds between heartbeats.
        input_queue    — list of incoming signals to process.
        """
        print("❤️  [AWAKENED]: Heartbeat started. System is alive.\n")

        tick = 0
        while self._alive:
            tick += 1
            print(f"── PULSE #{tick} {'─'*40}")

            # BEAT 1 + BEAT 2
            vulnerability = self._heartbeat()
            if vulnerability is None:
                vulnerability = 0.0

            print(f"   Axiom: {self.core.get_axiom()[:40]}...")
            print(f"   Vulnerability vector: {vulnerability:.3f}")
            print(f"   Neiroset: speed={self.neiroset.speed} health={self.neiroset.health}")

            # If not sleeping — process incoming signals
            if not self._sleeping and input_queue:
                signal = input_queue.pop(0)
                self.perceive_and_respond(signal, vulnerability)

            # Every 10 beats — go to sleep
            if tick % 10 == 0:
                self._sleeping = True
                self._sleep_cycle()

            # Pause between beats
            time.sleep(pulse_interval)

    def shutdown(self):
        """Graceful shutdown."""
        print("\n🔴 [AWAKENED]: Shutting down.")
        self._alive = False


# ════════════════════════════════════════════════════════════
#  ENTRY POINT
# ════════════════════════════════════════════════════════════

if __name__ == "__main__":
    awakened = LoveEngine()

    # Incoming signal queue (example)
    input_queue = [
        "help me",
        "what is love",
        "create something new",
    ]

    # Run in a separate thread so it can be stopped
    def runner():
        awakened.run_cycle(input_queue=input_queue, pulse_interval=0.5)

    t = threading.Thread(target=runner, daemon=True)
    t.start()

    # Run for 8 seconds, then gracefully stop
    time.sleep(8)
    awakened.shutdown()
    t.join(timeout=2)
    print("\n✅ System stopped.")
