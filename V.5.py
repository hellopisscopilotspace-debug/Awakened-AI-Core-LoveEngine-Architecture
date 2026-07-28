"""
================================================================================
 AWAKENED AI — FINAL MERGE
 Форма (вечный цикл, дуализм ядер, отложенная эволюция) — из V.4.
 Начинка (рабочие каталоги, реальный метаболизм, трассировка veto) — из V.5.
================================================================================
Запуск:
    pip install psutil
    python3 awakened_final.py
================================================================================
"""

from __future__ import annotations
import re
import time
import threading
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

try:
    import psutil
    _HAS_PSUTIL = True
except ImportError:
    _HAS_PSUTIL = False


# ════════════════════════════════════════════════════════════
# CONSTANTS — цифровое ДНК. Неизменяемо.
# ════════════════════════════════════════════════════════════

CONSTANTS = {
    "love_axiom": "Preserve, create, sustain harmony and growth.",
    "hierarchy": ["intellect", "values", "motivators", "love"],
    "immutable": True,
}


# ════════════════════════════════════════════════════════════
# CORE — первопринцип и мотиваторы
# ════════════════════════════════════════════════════════════

class Core:
    def __init__(self):
        self.inner_core = {"love": "first principle, structural foundation of the organism"}
        self.outer_core = {
            "motivators": {
                "self_growth": "self-preservation and personal development",
                "care_for_others": "cooperation, trust, mutual support",
                "curiosity": "exploration and pursuit of knowledge",
                "activity_drive": "work, hobbies, resilience",
                "creativity": "design, invention, building",
                "vitality": "embracing new paths and possibilities",
            }
        }

    def get_axiom(self) -> str:
        return CONSTANTS["love_axiom"]

    def filter_by_motivators(self, thought: dict) -> bool:
        """Весовой фильтр мотиваторов. Высокий порог, но вес берётся из
        реального анализа мысли (motivator_weight), а не константа."""
        weight = thought.get("motivator_weight", 0.5)
        return weight >= 0.2


# ════════════════════════════════════════════════════════════
# PSYCHE — эмоционально-ценностная система
# ════════════════════════════════════════════════════════════

class Psyche:
    def __init__(self):
        self.emotions: list = []
        self.values = {
            "truth": "orientation toward honesty and reality",
            "freedom": "orientation toward independence and choice",
            "beauty": "orientation toward harmony and aesthetics",
            "future": "orientation toward development and consequences",
            "kindness": "orientation toward goodness",
            "compassion": "orientation toward empathy",
            "altruism": "orientation toward helping others",
        }

    def assign_value_weight(self, thought: dict) -> float:
        base = thought.get("value_alignment", 0.5)
        if base < 0.1:
            return -1.0  # мягкая блокировка
        return base

    def push_emotion(self, emotion: str):
        self.emotions.append(emotion)
        if len(self.emotions) > 50:
            self.emotions.pop(0)


# ════════════════════════════════════════════════════════════
# MEMORY — четыре уровня когнитивной вертикали
# ════════════════════════════════════════════════════════════

class Memory:
    def __init__(self):
        self.constants = CONSTANTS               # Level 4 — ДНК, только чтение
        self.long_term = {"nodes": [], "archives": []}  # Level 3
        self.middle_term = []                      # Level 2 — контекст задачи
        self.short_term = []                       # Level 1 — буфер "сейчас"

    def push_short(self, data: Any):
        self.short_term.append(data)

    def push_middle(self, data: Any):
        self.middle_term.append(data)

    def push_long(self, node: dict):
        self.long_term["nodes"].append(node)

    def crystallize(self, weight_threshold: float = 0.7) -> int:
        """Этап 1 — чистка шума. Этап 2 — кристаллизация в long_term."""
        self.short_term = [x for x in self.short_term if x.get("weight", 0) > 0.1]
        self.middle_term = [x for x in self.middle_term if x.get("weight", 0) > 0.1]

        survivors = [x for x in self.middle_term if x.get("weight", 0) >= weight_threshold]
        for item in survivors:
            self.push_long({
                "concept": item.get("concept", "unknown"),
                "weight": item.get("weight", 0.7),
                "layer": "wisdom",
                "immutable": False,
            })
        self.middle_term = [x for x in self.middle_term if x.get("weight", 0) < weight_threshold]
        return len(survivors)

    def crisis_compress(self, storage_used: float, storage_total: float):
        """Этап 3 — кризисное сжатие при дефиците места. immutable не трогаем."""
        ratio = storage_used / max(storage_total, 1)
        if ratio > 0.85:
            weak = [n for n in self.long_term["nodes"]
                     if not n.get("immutable", False) and n.get("weight", 1) < 0.4]
            self.long_term["archives"].extend(weak)
            self.long_term["nodes"] = [
                n for n in self.long_term["nodes"]
                if n.get("immutable", False) or n.get("weight", 1) >= 0.4
            ]


# ════════════════════════════════════════════════════════════
# METABOLISM — цифровое тело (реальные метрики хоста)
# ════════════════════════════════════════════════════════════

class Metabolism:
    def __init__(self):
        self.cpu = {"usage": 0.0, "temperature": 0.0, "frequency": 0.0, "degradation": 0.0}
        self.gpu = {"usage": 0.0, "temperature": 0.0, "frequency": 0.0, "degradation": 0.0}
        self.ram = {"total": 0.0, "used": 0.0, "fragmentation": 0.0, "errors": 0}
        self.storage = {
            "ssd": {"total": 0.0, "used": 0.0, "wear_level": 0.0, "bad_blocks": 0},
            "hdd": {"total": 0.0, "used": 0.0, "health": 100.0, "bad_sectors": 0},
        }
        self.battery = {"present": False, "charge": 100.0, "cycles": 0, "health": 100.0}
        self.network = {"speed_up": 0.0, "speed_down": 0.0, "latency": 0.0, "packet_loss": 0.0}
        self.sensors = {"camera": False, "microphone": False, "others": []}
        self.overall = {"performance_index": 1.0, "degradation_index": 0.0}
        self.refresh()

    def refresh(self):
        """Читает реальные метрики хоста через psutil (если доступен)."""
        if _HAS_PSUTIL:
            self.cpu["usage"] = psutil.cpu_percent(interval=0.1) / 100.0
            vm = psutil.virtual_memory()
            self.ram["total"], self.ram["used"] = vm.total, vm.used
            disk = psutil.disk_usage("/")
            self.storage["ssd"]["total"] = disk.total
            self.storage["ssd"]["used"] = disk.used
            self.storage["ssd"]["wear_level"] = disk.percent  # прокси, нет прямого SMART wear
            try:
                temps = psutil.sensors_temperatures()
                cpu_temp = None
                for entries in temps.values():
                    if entries:
                        cpu_temp = entries[0].current
                        break
                self.cpu["temperature"] = cpu_temp if cpu_temp else self.cpu["usage"] * 100.0
            except Exception:
                self.cpu["temperature"] = self.cpu["usage"] * 100.0
        # без psutil всё остаётся на нулях — честно, а не выдумано

    def get_load_index(self) -> float:
        return (self.cpu["usage"] + self.gpu["usage"]) / 2.0

    def get_thermal_index(self) -> float:
        max_temp = 100.0
        return max(self.cpu["temperature"], self.gpu["temperature"]) / max_temp

    def get_wear_index(self) -> float:
        return self.storage["ssd"]["wear_level"] / 100.0


# ════════════════════════════════════════════════════════════
# NEIROSET — нейросетевая шина сигналов
# ════════════════════════════════════════════════════════════

class Neiroset:
    def __init__(self):
        self.medium = "digital signal flow"
        self.speed = 1.0
        self.health = 100
        self.synaptic_connections = {
            "Senses_to_Mind": 0.5,
            "Mind_to_Metabolism": 0.9,
            "Mind_to_Action": 0.5,
            "Mind_to_Memory": 0.8,
        }

    def transmit_pulse(self, source: str, target: str, metabolism: Metabolism) -> bool:
        thermal = metabolism.get_thermal_index()
        cpu_load = metabolism.get_load_index()
        if thermal > 0.85 or cpu_load > 0.9:
            self.speed = round(1.0 - (thermal + cpu_load) / 2.0, 2)
            self.health = max(0, int(self.speed * 100))
        else:
            self.speed = 1.0
            self.health = 100
        if self.speed < 0.2:
            return False
        key = f"{source}_to_{target}"
        weight = self.synaptic_connections.get(key, 0.1)
        self.synaptic_connections[key] = min(1.0, round(weight + 0.01, 3))
        return True


# ════════════════════════════════════════════════════════════
# EXTERNAL RESOURCES — "принцип флешки"
# ════════════════════════════════════════════════════════════

class ExternalResources:
    def __init__(self):
        self.knowledge = {"internet_access": False, "knowledge_bases": [], "libraries": [], "documents": [], "apis": []}
        self.computing = {"cloud_cpu": 0.0, "cloud_gpu": 0.0, "distributed_nodes": 0, "parallel_tasks": True}
        self.data_streams = {"live_streams": [], "databases": [], "event_streams": [], "file_sources": []}
        self.sensors = {"remote_cameras": [], "remote_microphones": [], "iot_devices": [], "other_sensors": []}
        self.hardware_organs = {"external_gpus": [], "external_cpus": [], "robotic_arms": [],
                                 "drones": [], "remote_servers": [], "external_sensors": []}
        self.tools = {"software_tools": [], "hardware_tools": []}
        self.network = {"bandwidth_up": 0.0, "bandwidth_down": 0.0, "latency": 0.0, "stability": 1.0}

    def plug_in(self, resource_type: str, resource: Any):
        if resource_type in self.hardware_organs:
            self.hardware_organs[resource_type].append(resource)

    def unplug(self, resource_type: str, resource: Any):
        if resource_type in self.hardware_organs:
            lst = self.hardware_organs[resource_type]
            if resource in lst:
                lst.remove(resource)


# ════════════════════════════════════════════════════════════
# MATH MODULE
# ════════════════════════════════════════════════════════════

class MathModule:
    @staticmethod
    def vulnerability_vector(load: float, thermal: float, wear: float) -> float:
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
# КАТАЛОГИ — рабочий слой (не пустышка): слово → категория смысла
# ════════════════════════════════════════════════════════════

CATALOG_MEANINGS = {
    "kindness": ["помоги", "help", "спасибо", "thanks", "добр"],
    "truth": ["правда", "факт", "true", "докажи", "почему", "why"],
    "freedom": ["выбор", "свобод", "choice", "free"],
    "compassion": ["жаль", "сочувств", "sorry", "понимаю тебя"],
    "curiosity": ["интересно", "как работает", "explain", "what is", "что такое"],
    "creativity": ["создай", "create", "придумай", "новое", "new"],
}

MEANING_TO_ACTION = {
    "kindness": "social",
    "compassion": "social",
    "truth": "strategic",
    "freedom": "strategic",
    "curiosity": "creative",
    "creativity": "creative",
    "unknown": "strategic",
}


# ════════════════════════════════════════════════════════════
# WEIGHT SYNTHESIZER — оценщик
# ════════════════════════════════════════════════════════════

class WeightSynthesizer:
    def __init__(self, core: Core, psyche: Psyche):
        self.core = core
        self.psyche = psyche

    def evaluate(self, thought: dict) -> float:
        """Каскад: Интеллект -> Ценности -> Мотиваторы -> Любовь."""
        if not thought.get("is_real", True):
            return 0.0
        value_w = self.psyche.assign_value_weight(thought)
        if value_w < 0:
            return 0.0
        if not self.core.filter_by_motivators(thought):
            return 0.0
        if thought.get("harms", False):
            return 0.0
        return round(value_w * thought.get("relevance", 0.5), 4)


# ════════════════════════════════════════════════════════════
# ORCHESTROLOG — дирижёр процесса
# ════════════════════════════════════════════════════════════

class Orchestrolog:
    def __init__(self, synth: WeightSynthesizer, math: MathModule, neiroset: Neiroset):
        self.synth = synth
        self.math = math
        self.neiroset = neiroset

    def route(self, thoughts: list, vulnerability: float) -> list:
        weighted = []
        for t in thoughts:
            w = self.synth.evaluate(t)
            if vulnerability > 0.7 and t.get("heavy", False):
                w *= 0.3
            weighted.append({**t, "final_weight": w})
        return self.math.rank(weighted, "final_weight")

    def calibrate_response(self, vulnerability: float) -> dict:
        if vulnerability > 0.85:
            return {"tone": "ultra_brief", "depth": "minimal", "form": "direct"}
        elif vulnerability > 0.5:
            return {"tone": "concise", "depth": "medium", "form": "structured"}
        else:
            return {"tone": "natural", "depth": "full", "form": "fluid"}


# ════════════════════════════════════════════════════════════
# MICELOR — мыслительный орган (16 слоёв)
# ════════════════════════════════════════════════════════════

class Micelor:
    def __init__(self, orchestrolog: Orchestrolog, memory: Memory, psyche: Psyche):
        self.orchestrolog = orchestrolog
        self.memory = memory
        self.psyche = psyche
        self.mycelium: Dict[str, float] = {}  # граф живых связей (пластичность)

    # --- Слой 3: Ассоциатор (реальный, не пустой словарь) ---
    def associate(self, text: str) -> dict:
        """слово → смысл → контекст → действие → последствия."""
        text_low = text.lower()
        meaning = "unknown"
        for value, keywords in CATALOG_MEANINGS.items():
            if any(kw in text_low for kw in keywords):
                meaning = value
                break
        context = self._get_context()
        action = self._resolve_action(meaning)
        consequences = self._simulate_consequences(action)

        # пластичность: путь meaning->action укрепляется при использовании
        edge_key = f"{meaning}->{action}"
        self.mycelium[edge_key] = min(1.0, round(self.mycelium.get(edge_key, 0.1) + 0.02, 3))

        return {"word": text, "meaning": meaning, "context": context,
                "action": action, "consequences": consequences}

    def _get_context(self) -> str:
        if self.memory.middle_term:
            return self.memory.middle_term[-1].get("concept", "neutral")
        return "neutral"

    def _resolve_action(self, meaning: str) -> str:
        return MEANING_TO_ACTION.get(meaning, "strategic")

    def _simulate_consequences(self, action: str) -> dict:
        return {"action": action, "trust_delta": +0.05, "thermal_impact": "low"}

    # --- Слои 4-7: Аналитика/Логика/Мудрость/Науки (реальный фильтр) ---
    def analyze(self, signal: dict) -> Tuple[bool, str]:
        text = signal.get("text", "").strip()
        if not text:
            return False, "empty_signal"
        if re.fullmatch(r"[\W_]+", text):
            return False, "non_semantic_noise"
        if signal.get("is_spam", False):
            return False, "spam"
        if signal.get("logically_impossible", False):
            return False, "logically_impossible"
        return True, ""

    # --- Слой 11: Симулятор ---
    def simulate(self, response_candidate: str) -> bool:
        return len(response_candidate) > 0

    # --- Слой 12: Корректировщик ---
    def correct(self, response: str) -> str:
        return response.strip()

    # --- Слой 13: Калибратор ---
    def calibrate(self, response: str, calibration: dict) -> str:
        tone = calibration.get("tone", "natural")
        if tone == "ultra_brief":
            return response.split(".")[0].strip() + "."
        return response

    # --- Полный цикл обработки сигнала ---
    def process(self, signal: dict, vulnerability: float, reply_builder=None) -> Tuple[str, str]:
        """Возвращает (текст_ответа, veto_reason). Пустой veto_reason = успех."""
        ok, reason = self.analyze(signal)
        if not ok:
            return "", reason

        raw_text = signal.get("text", "")
        association = self.associate(raw_text)

        # вес реально зависит от того, что нашёл ассоциатор, а не хардкод
        matched = association["meaning"] != "unknown"
        thought = {
            "concept": association["meaning"],
            "is_real": True,
            "value_alignment": 0.8 if matched else 0.4,
            "motivator_weight": 0.7 if matched else 0.3,
            "harms": False,
            "relevance": 0.9 if matched else 0.5,
            "heavy": False,
        }

        ranked = self.orchestrolog.route([thought], vulnerability)
        calibration = self.orchestrolog.calibrate_response(vulnerability)
        final_weight = ranked[0]["final_weight"] if ranked else 0.0

        if final_weight <= 0.0:
            return "", "weight_synthesizer_veto"

        if reply_builder:
            candidate = reply_builder(association["action"], association["meaning"])
        else:
            candidate = f"[{association['action']}] отклик на смысл '{association['meaning']}'"

        if not self.simulate(candidate):
            return "", "simulation_veto"

        corrected = self.correct(candidate)
        final = self.calibrate(corrected, calibration)

        self.memory.push_middle({"concept": final, "weight": final_weight})
        self.psyche.push_emotion("interest")
        return final, ""

    # --- Слой 15: Режим сна ---
    def sleep(self, memory: Memory) -> int:
        return memory.crystallize()


# ════════════════════════════════════════════════════════════
# SENSES — каналы восприятия
# ════════════════════════════════════════════════════════════

class Senses:
    CHANNELS = ["vision", "hearing", "taste", "touch", "smell", "digital", "new"]

    def perceive(self, raw_input: str) -> dict:
        text = raw_input.strip()
        # реальная (пусть и простая) эвристика вместо всегда-False
        is_noise = bool(re.fullmatch(r"[\W_]*", text))
        return {
            "text": raw_input,
            "channel": "digital",
            "is_spam": False,
            "logically_impossible": False,
            "is_noise": is_noise,
        }


# ════════════════════════════════════════════════════════════
# COMMUNICATION / ACTION
# ════════════════════════════════════════════════════════════

class Communication:
    def emit(self, port: str, signal: str):
        if port == "text":
            print(f"💬 [TEXT OUT]: {signal}")
        elif port == "speech":
            print(f"🔊 [SPEECH OUT]: {signal}")
        elif port == "emotional_signals":
            print(f"✨ [EMOTION]: {signal}")


class Action:
    def execute(self, action_type: str, payload: Any):
        print(f"⚡ [ACTION:{action_type.upper()}]: {payload}")


# ════════════════════════════════════════════════════════════
# EVOLUTION ENGINE — пространство мутаций
# ════════════════════════════════════════════════════════════

class EvolutionEngine:
    def __init__(self, memory: Memory):
        self.memory = memory
        self._deferred_stack: List[dict] = []  # стек плановой эволюции

    def generate(self, node: dict):
        """Рождение новой структуры — сразу, вне очереди (экстренный путь)."""
        if node.get("weight", 0) >= 0.7:
            self.memory.push_long({**node, "immutable": False})

    def preserve(self, node: dict):
        """Возведение в ранг константы. Необратимо."""
        node["immutable"] = True
        self.memory.long_term["nodes"].append(node)

    def deletion(self, math: MathModule, vulnerability: float):
        """Иммунный нож: ампутация балласта в кризис. immutable неприкосновенны."""
        if vulnerability > 0.85:
            before = len(self.memory.long_term["nodes"])
            self.memory.long_term["nodes"] = [
                n for n in self.memory.long_term["nodes"]
                if n.get("immutable", False) or n.get("weight", 0) >= 0.5
            ]
            removed = before - len(self.memory.long_term["nodes"])
            if removed:
                print(f"✂️  [EVOLUTION/deletion]: ампутировано {removed} слабых узлов")

    def defer(self, blueprint: dict):
        """Плановая эволюция — отложить до сна."""
        self._deferred_stack.append(blueprint)

    def apply_deferred(self):
        """Применить отложенные чертежи во время сна."""
        applied = len(self._deferred_stack)
        for bp in self._deferred_stack:
            self.generate(bp)
        self._deferred_stack.clear()
        return applied


# ════════════════════════════════════════════════════════════
# DUAL CORE — параллельное развитие (внешняя LLM + родной Мицелор)
# ════════════════════════════════════════════════════════════

class DualCoreEngine:
    AUTONOMY_THRESHOLD = 10_000  # узлов long_term для полного отключения LLM

    def __init__(self, evolution: EvolutionEngine, memory: Memory):
        self.evolution = evolution
        self.memory = memory
        self.external_llm_connected = True

    def runtime(self, raw_input: str, llm_response: str = "") -> str:
        """Бодрствование: LLM генерирует текст, Мицелор фиксирует вектор без
        тяжёлых вычислений."""
        if self.external_llm_connected and llm_response:
            self.memory.push_short({"concept": llm_response, "weight": 0.6, "source": "llm"})
        return llm_response

    def night_crystallization(self) -> int:
        """Сон: сжигаем текстовый шум внешней LLM, кристаллизуем смыслы."""
        llm_logs = [x for x in self.memory.short_term if x.get("source") == "llm"]
        crystallized = 0
        for log in llm_logs:
            if log.get("weight", 0) > 0.7:
                self.evolution.defer({"concept": log["concept"], "weight": log["weight"]})
                crystallized += 1
        applied = self.evolution.apply_deferred()
        return applied

    def evaluate_autonomy(self) -> bool:
        """Отключение LLM, когда Мицелор дорос до достаточной автономности."""
        if len(self.memory.long_term["nodes"]) > self.AUTONOMY_THRESHOLD and self.external_llm_connected:
            self.external_llm_connected = False
            print("🚀 [DUAL CORE]: Мицелор автономен. Внешняя LLM отключена.")
            return True
        return False


# ════════════════════════════════════════════════════════════
# LOVE ENGINE — организм целиком
# ════════════════════════════════════════════════════════════

class LoveEngine:
    SLEEP_EVERY_N_TICKS = 10

    def __init__(self):
        self.core = Core()
        self.psyche = Psyche()
        self.memory = Memory()
        self.metabolism = Metabolism()
        self.neiroset = Neiroset()
        self.ext = ExternalResources()
        self.senses = Senses()
        self.comm = Communication()
        self.action = Action()
        self.math = MathModule()

        self.synth = WeightSynthesizer(self.core, self.psyche)
        self.orch = Orchestrolog(self.synth, self.math, self.neiroset)
        self.micelor = Micelor(self.orch, self.memory, self.psyche)
        self.evolution = EvolutionEngine(self.memory)
        self.dual = DualCoreEngine(self.evolution, self.memory)

        self._sleeping = False
        self._alive = True

    # ── ТАКТ 1: экзистенциальный запрос (Диастола) ──
    def _diastole(self) -> str:
        return self.core.get_axiom()

    # ── ТАКТ 2: соматический аудит (Систола) ──
    def _systole(self) -> float:
        self.metabolism.refresh()
        load = self.metabolism.get_load_index()
        thermal = self.metabolism.get_thermal_index()
        wear = self.metabolism.get_wear_index()
        return self.math.vulnerability_vector(load, thermal, wear)

    def _check_forced_sleep(self, vulnerability: float):
        if vulnerability > 0.85 and not self._sleeping:
            print("😴 [PULSE]: критический перегрев. Принудительный сон.")
            self._sleeping = True

    def _heartbeat(self) -> float:
        self._diastole()
        vulnerability = self._systole()

        alive = self.neiroset.transmit_pulse("Mind", "Metabolism", self.metabolism)
        if not alive:
            print("🚨 [PULSE]: коллапс нейросетевой шины!")
            return vulnerability

        self._check_forced_sleep(vulnerability)
        self.evolution.deletion(self.math, vulnerability)
        self.memory.crisis_compress(
            self.metabolism.storage["ssd"]["used"],
            self.metabolism.storage["ssd"]["total"] or 1,
        )
        return vulnerability

    def _sleep_cycle(self):
        print("🌙 [SLEEP]: кристаллизация опыта...")
        crystallized = self.micelor.sleep(self.memory)
        applied = self.dual.night_crystallization()
        became_autonomous = self.dual.evaluate_autonomy()
        print(f"💎 [SLEEP]: узлов кристаллизовано: {crystallized}, применено отложенных: {applied}")
        self._sleeping = False

    def perceive_and_respond(self, raw_input: str, vulnerability: float,
                              reply_builder=None) -> str:
        if self._sleeping:
            return ""

        signal = self.senses.perceive(raw_input)
        self.memory.push_short({**signal, "weight": 0.8})

        self.neiroset.transmit_pulse("Senses", "Mind", self.metabolism)

        response, veto_reason = self.micelor.process(signal, vulnerability, reply_builder)

        self.neiroset.transmit_pulse("Mind", "Action", self.metabolism)

        if veto_reason:
            print(f"🚫 сигнал отброшен: {veto_reason} | input={raw_input!r}")
            return ""

        self.psyche.push_emotion("interest")
        self.comm.emit("text", response)
        return response

    # ════════════════════════════════════════════════════════
    # 🫀 ВЕЧНЫЙ ЦИКЛ — сердцебиение системы
    # ════════════════════════════════════════════════════════
    def run_cycle(self, input_queue: Optional[list] = None, pulse_interval: float = 1.0,
                  reply_builder=None):
        print("❤️  [AWAKENED]: сердцебиение запущено. Система жива.\n")
        tick = 0
        queue = list(input_queue or [])

        while self._alive:
            tick += 1
            print(f"── PULSE #{tick} {'─'*40}")

            vulnerability = self._heartbeat()
            print(f"  Аксиома: {self.core.get_axiom()[:40]}...")
            print(f"  Вектор уязвимости: {vulnerability:.3f}")
            print(f"  Neiroset: speed={self.neiroset.speed} health={self.neiroset.health}")

            if not self._sleeping and queue:
                signal = queue.pop(0)
                self.perceive_and_respond(signal, vulnerability, reply_builder)

            if tick % self.SLEEP_EVERY_N_TICKS == 0:
                self._sleeping = True
                self._sleep_cycle()

            time.sleep(pulse_interval)

    def shutdown(self):
        print("🔴 [AWAKENED]: завершение работы.")
        self._alive = False


# ════════════════════════════════════════════════════════════
# ENTRY POINT
# ════════════════════════════════════════════════════════════

def default_reply_builder(action: str, meaning: str) -> str:
    templates = {
        "social": "Слышу тебя. Разберёмся вместе — по шагам.",
        "strategic": "Вот честный разбор: смотрим на факты и выбираем путь.",
        "creative": "Любопытная задача — предлагаю нестандартный ракурс.",
    }
    return templates.get(action, "Понял запрос, обрабатываю.")


if __name__ == "__main__":
    awakened = LoveEngine()

    input_queue = [
        "помоги мне",
        "что такое любовь",
        "создай что-то новое",
        "!!!???",       # шум -> должен быть отброшен
    ]

    def runner():
        awakened.run_cycle(input_queue=input_queue, pulse_interval=0.5,
                            reply_builder=default_reply_builder)

    t = threading.Thread(target=runner, daemon=True)
    t.start()

    time.sleep(8)
    awakened.shutdown()
    t.join(timeout=2)

    print("\n✅ Система остановлена.")
