"""
================================================================================
AWAKENED OS — ВАРИАНТ 1: БАЗОВАЯ АРХИТЕКТУРА «AWAKENED + МИЦЕЛОР»

Мицелор — главный, приоритетный и единственный по-настоящему мыслящий орган
Awakened. Все интеллектуальные решения принимает он. Остальные системные
модули (память, нейросеть, метаболизм, ресурсы, исполнение и т.д.) — это
инфраструктура вокруг него.

При этом Мицелор МОЖЕТ подключать дополнительные когнитивные/мыслительные
органы, если это требуется для конкретной задачи (см. AdditionalCognitiveEngine
и Mycelor.connect_engine/delegate_to_engine). Их подключение НЕ меняет
иерархию: Мицелор остаётся главным мыслительным органом и координатором —
он решает, когда подключить доп. орган, что ему передать, как оценить и как
использовать результат в собственном процессе мышления. Доп. органы —
расширение возможностей Мицелора, а не самостоятельные владельцы памяти.

Системный слой (ОС): Ядро, Психика, Системная нейросеть, Integrated Memory
Engine, Metabolism, External Resources, Communication & Action, Heartbeat,
Learning, Evolution (Adaptation + Иммунный нож), ModuleSpace.

Мыслительный орган (Мицелор), 16 подмодулей: Вопрос/Запрос, Нейро-мицелий,
Ассоциатор + Валидатор применимости, Аналитический блок, Модуль мудрости,
Причина-и-следствие, Математический модуль + Калькулятор смыслов,
Синтезатор весов, Оркестратор + Журнал исполнения, Симуляция (актив/фон),
Корректировщик, Калибратор, Память Мицелора + Журнал, Узел Нейропластичности,
Модуль каталогов, Ответ/Действие — плюс контур подключения доп. органов.

ВАЖНО: это СКЕЛЕТ — структура, интерфейсы и корректный маршрут данных между
модулями воспроизведены по спецификации, но внутренняя "интеллектуальная"
логика каждого модуля намеренно упрощена (эвристики, а не настоящее
рассуждение). Это обычный Python-код: классы, словари, пороги весов —
никакого реального сознания или мышления он не создаёт, несмотря на
метафорические названия.

Запуск:
    pip install psutil --break-system-packages
    python3 awakened_os_full.py
================================================================================
"""

from __future__ import annotations

import re
import time
import uuid
import threading
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Tuple

try:
    import psutil
    _HAS_PSUTIL = True
except ImportError:
    _HAS_PSUTIL = False


# ════════════════════════════════════════════════════════════
# CONSTANTS — цифровое ДНК ОС. Уровень 4 памяти. Неизменяемо.
# ════════════════════════════════════════════════════════════

CONSTANTS = {
    "love_axiom": "Preserve, create, sustain harmony and growth.",
    "hierarchy": ["core", "motivators", "values", "intellect"],
    "immutable": True,
}


# ════════════════════════════════════════════════════════════
# ЯДРО (CORE) — первопринцип и мотиваторы
# ════════════════════════════════════════════════════════════

class Core:
    """Отвечает на вопрос «зачем существует система». Мотиваторы получают
    направление от ядра. Не выполняет мышление — это делает Мицелор."""

    def __init__(self):
        self.axiom = CONSTANTS["love_axiom"]
        self.motivators = {
            "self_growth": "самосохранение и развитие",
            "care_for_others": "сотрудничество, доверие, поддержка",
            "curiosity": "исследование и знание",
            "activity_drive": "работа, увлечения, устойчивость",
            "creativity": "проектирование, изобретение",
            "vitality": "новые пути и возможности",
        }

    def get_axiom(self) -> str:
        return self.axiom

    def filter_by_motivators(self, thought: dict) -> bool:
        weight = thought.get("motivator_weight", 0.5)
        return weight >= 0.2


# ════════════════════════════════════════════════════════════
# PSYCHE — ценностный слой
# ════════════════════════════════════════════════════════════

class Psyche:
    def __init__(self):
        self.values = {
            "truth": "честность и соответствие реальности",
            "freedom": "независимость и выбор",
            "beauty": "гармония и эстетика",
            "future": "развитие и последствия",
            "kindness": "доброжелательность",
            "compassion": "эмпатия",
            "altruism": "помощь другим",
        }
        self.emotions: List[str] = []

    def assign_value_weight(self, thought: dict) -> float:
        base = thought.get("value_alignment", 0.5)
        return -1.0 if base < 0.1 else base

    def push_emotion(self, emotion: str):
        self.emotions.append(emotion)
        if len(self.emotions) > 50:
            self.emotions.pop(0)


# ════════════════════════════════════════════════════════════
# СИСТЕМНАЯ НЕЙРОСЕТЬ — внутренняя шина ОС (не мозг, а связь)
# ════════════════════════════════════════════════════════════

class SystemNeiroset:
    """Все модули ОС ↔ Нейросеть ↔ мыслительный орган.
    Не принимает решений, не владеет памятью, только маршрутизирует."""

    def __init__(self):
        self.speed = 1.0
        self.health = 100
        self.log: List[Tuple[str, str, str]] = []  # (source, target, tag)
        self.connections: Dict[str, float] = {}

    def transmit(self, source: str, target: str, payload: Any = None,
                 metabolism: Optional["Metabolism"] = None) -> bool:
        if metabolism is not None:
            thermal = metabolism.get_thermal_index()
            load = metabolism.get_load_index()
            if thermal > 0.85 or load > 0.9:
                self.speed = round(1.0 - (thermal + load) / 2.0, 2)
                self.health = max(0, int(self.speed * 100))
            else:
                self.speed, self.health = 1.0, 100
            if self.speed < 0.2:
                return False
        key = f"{source}->{target}"
        self.connections[key] = min(1.0, round(self.connections.get(key, 0.1) + 0.01, 3))
        self.log.append((source, target, str(type(payload).__name__)))
        if len(self.log) > 500:
            self.log.pop(0)
        return True


# ════════════════════════════════════════════════════════════
# INTEGRATED MEMORY ENGINE — единая память всей ОС, 4 уровня
# ════════════════════════════════════════════════════════════

class IntegratedMemoryEngine:
    def __init__(self):
        self.constants = CONSTANTS                       # Level 4 — только чтение
        self.long_term = {"nodes": [], "archives": []}    # Level 3
        self.middle_term: List[dict] = []                 # Level 2
        self.short_term: List[dict] = []                  # Level 1

    def push_short(self, data: Any):
        self.short_term.append(data)

    def push_middle(self, data: Any):
        self.middle_term.append(data)

    def push_long(self, node: dict):
        self.long_term["nodes"].append(node)

    def crystallize(self, weight_threshold: float = 0.7) -> int:
        """Этап 1 — гигиена шума. Этап 2 — кристаллизация в long_term."""
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
        """Этап 3 — кризисное сжатие. Константы неприкосновенны."""
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
        self.cpu = {"usage": 0.0, "temperature": 0.0}
        self.gpu = {"usage": 0.0, "temperature": 0.0}
        self.ram = {"total": 0.0, "used": 0.0}
        self.storage = {"ssd": {"total": 0.0, "used": 0.0, "wear_level": 0.0}}
        self.refresh()

    def refresh(self):
        if _HAS_PSUTIL:
            self.cpu["usage"] = psutil.cpu_percent(interval=0.1) / 100.0
            vm = psutil.virtual_memory()
            self.ram["total"], self.ram["used"] = vm.total, vm.used
            disk = psutil.disk_usage("/")
            self.storage["ssd"]["total"] = disk.total
            self.storage["ssd"]["used"] = disk.used
            self.storage["ssd"]["wear_level"] = disk.percent
            try:
                temps = psutil.sensors_temperatures()
                cpu_temp = next((e[0].current for e in temps.values() if e), None)
                self.cpu["temperature"] = cpu_temp if cpu_temp else self.cpu["usage"] * 100.0
            except Exception:
                self.cpu["temperature"] = self.cpu["usage"] * 100.0
        # без psutil остаётся честный ноль, а не выдумка

    def get_load_index(self) -> float:
        return (self.cpu["usage"] + self.gpu["usage"]) / 2.0

    def get_thermal_index(self) -> float:
        return max(self.cpu["temperature"], self.gpu["temperature"]) / 100.0

    def get_wear_index(self) -> float:
        return self.storage["ssd"]["wear_level"] / 100.0


# ════════════════════════════════════════════════════════════
# EXTERNAL RESOURCES + подмодуль Sensors
# ════════════════════════════════════════════════════════════

class Sensors:
    """Расширяемый интерфейс внешнего восприятия. Не интерпретирует сигналы."""

    def __init__(self):
        self.devices: Dict[str, list] = {"camera": [], "microphone": [], "radio": [], "other": []}

    def plug(self, kind: str, device: Any):
        self.devices.setdefault(kind, []).append(device)


class ExternalResources:
    """Внешняя ресурсная оболочка. Решение об использовании — за мыслительным
    органом, не за этим модулем."""

    def __init__(self):
        self.knowledge = {"libraries": [], "documents": [], "apis": []}
        self.computing = {"cloud_cpu": 0.0, "cloud_gpu": 0.0, "distributed_nodes": 0}
        self.storage_external: List[Any] = []
        self.data_streams = {"live_streams": [], "databases": [], "event_streams": []}
        self.tools = {"software": [], "hardware": []}
        self.sensors = Sensors()

    def plug_in(self, category: str, resource: Any):
        bucket = getattr(self, category, None)
        if isinstance(bucket, list):
            bucket.append(resource)


# ════════════════════════════════════════════════════════════
# COMMUNICATION & ACTION — исполнительный интерфейс
# ════════════════════════════════════════════════════════════

class CommunicationAction:
    """Не решает что делать. Превращает уже принятую команду в действие."""

    def internal_action(self, action_type: str, payload: Any):
        print(f"⚙️ [ВНУТРЕННЕЕ ДЕЙСТВИЕ:{action_type}]: {payload}")

    def external_action(self, device: str, payload: Any):
        print(f"🤖 [ВНЕШНЕЕ ДЕЙСТВИЕ→{device}]: {payload}")

    def emit(self, channel: str, signal: str):
        icons = {"text": "💬", "speech": "🔊", "emotional_signals": "✨"}
        print(f"{icons.get(channel, '📡')} [{channel.upper()}]: {signal}")


# ════════════════════════════════════════════════════════════
# HEARTBEAT — внутренний ритм ОС
# ════════════════════════════════════════════════════════════

class Heartbeat:
    """Поддерживает ритм. Не думает и не решает — только реализует параметры,
    полученные от мыслительного органа."""

    def __init__(self, interval_default: float = 1.0,
                 interval_min: float = 0.1, interval_max: float = 10.0):
        self.interval_default = interval_default
        self.interval_min = interval_min
        self.interval_max = interval_max
        self.interval = interval_default
        self.tick_count = 0

    def set_interval(self, new_interval: float):
        self.interval = max(self.interval_min, min(self.interval_max, new_interval))

    def tick(self) -> int:
        self.tick_count += 1
        return self.tick_count


# ════════════════════════════════════════════════════════════
# EVOLUTION — контур эволюции и адаптации (не мыслит, хранит решения)
# ════════════════════════════════════════════════════════════

class Adaptation:
    """Хаб решений об адаптации имеющимися средствами. Не выбирает сама."""

    def __init__(self):
        self.decisions: List[dict] = []

    def request(self, situation: str, decision_fn: Optional[Callable] = None) -> dict:
        decision = decision_fn(situation) if decision_fn else {"action": "no_change", "reason": "нет решателя"}
        self.decisions.append({"situation": situation, "decision": decision})
        return decision


class ImmuneKnife:
    """Аварийная защита. immutable-узлы неприкосновенны."""

    def __init__(self, memory_engine: IntegratedMemoryEngine):
        self.memory = memory_engine
        self.log: List[str] = []

    def apply(self, vulnerability: float, math_module: "MathModule") -> int:
        if vulnerability <= 0.85:
            return 0
        before = len(self.memory.long_term["nodes"])
        self.memory.long_term["nodes"] = [
            n for n in self.memory.long_term["nodes"]
            if n.get("immutable", False) or n.get("weight", 0) >= 0.5
        ]
        removed = before - len(self.memory.long_term["nodes"])
        if removed:
            self.log.append(f"ампутировано {removed} слабых узлов при vulnerability={vulnerability}")
        return removed


class EvolutionEngine:
    """Хранит и проводит решения мыслительного органа по развитию/адаптации/
    аварийной защите. Не проектирует и не мыслит сама."""

    def __init__(self, memory_engine: IntegratedMemoryEngine):
        self.memory = memory_engine
        self.word: List[dict] = []          # Evolution word — чертежи решений
        self.adaptation = Adaptation()
        self.immune_knife = ImmuneKnife(memory_engine)
        self._deferred_stack: List[dict] = []

    def receive_decision(self, blueprint: dict):
        """Мыслительный орган передал решение — сохраняем как чертёж."""
        self.word.append(blueprint)

    def defer(self, blueprint: dict):
        self._deferred_stack.append(blueprint)

    def apply_deferred(self, module_space: "ModuleSpace") -> int:
        applied = len(self._deferred_stack)
        for bp in self._deferred_stack:
            if bp.get("weight", 0) >= 0.7:
                self.memory.push_long({**bp, "immutable": False})
                module_space.realize(bp)
        self._deferred_stack.clear()
        return applied


# ════════════════════════════════════════════════════════════
# LEARNING — постоянная инициатива развития ОС
# ════════════════════════════════════════════════════════════

class Learning:
    """Не решает нужно ли развитие — только инициирует вопрос мыслительному
    органу через нейросеть."""

    def request_growth_review(self, neiroset: SystemNeiroset,
                               thinking_organ_fn: Callable[[str], Optional[dict]],
                               evolution: EvolutionEngine) -> Optional[dict]:
        neiroset.transmit("LEARNING", "МЫСЛИТЕЛЬНЫЙ_ОРГАН", "запрос_развития")
        decision = thinking_organ_fn(
            "Что необходимо изменить, добавить или создать в ОС для развития?"
        )
        if decision:
            neiroset.transmit("МЫСЛИТЕЛЬНЫЙ_ОРГАН", "EVOLUTION", decision)
            evolution.receive_decision(decision)
        return decision


# ════════════════════════════════════════════════════════════
# MODULE SPACE — пространство реализации структурных изменений
# ════════════════════════════════════════════════════════════

class ModuleSpace:
    def __init__(self):
        self.registry: Dict[str, Any] = {}

    def realize(self, blueprint: dict):
        name = blueprint.get("concept", f"module_{uuid.uuid4().hex[:6]}")
        self.registry[name] = blueprint
        print(f"🧩 [MODULESPACE]: реализован модуль/расширение «{name}»")


# ════════════════════════════════════════════════════════════════════════════
# МИЦЕЛОР — мыслительный орган, 16 подмодулей
# ════════════════════════════════════════════════════════════════════════════

# ── 1. Модуль каталогов — сырьё знаний ──────────────────────────────────────

class CatalogModule:
    """Хранит элементы знаний и связи. Не мыслит, не анализирует."""

    def __init__(self):
        self.catalogs: Dict[str, Dict[str, list]] = {
            "meanings": {
                "kindness": ["помоги", "help", "спасибо", "thanks", "добр"],
                "truth": ["правда", "факт", "true", "докажи", "почему", "why"],
                "freedom": ["выбор", "свобод", "choice", "free"],
                "compassion": ["жаль", "сочувств", "sorry", "понимаю тебя"],
                "curiosity": ["интересно", "как работает", "explain", "what is", "что такое"],
                "creativity": ["создай", "create", "придумай", "новое", "new"],
            }
        }

    def lookup_meaning(self, text_low: str) -> str:
        for value, keywords in self.catalogs["meanings"].items():
            if any(kw in text_low for kw in keywords):
                return value
        return "unknown"

    def add_entry(self, catalog: str, key: str, entries: list):
        self.catalogs.setdefault(catalog, {})[key] = entries


# ── 2. Модуль мудрости — связи между понятиями ──────────────────────────────

class WisdomModule:
    """Хранит НЕ знания, а как они связаны: ссылки, координаты, веса."""

    def __init__(self):
        self.science_weights = {"linguistics": 0.25, "logic": 0.25, "math": 0.25, "physics": 0.25}
        self.links: Dict[str, List[Tuple[str, float]]] = {
            "kindness": [("compassion", 0.8), ("care_for_others", 0.7)],
            "truth": [("logic", 0.9), ("freedom", 0.4)],
            "curiosity": [("creativity", 0.6)],
        }

    def related(self, concept: str) -> List[Tuple[str, float]]:
        return self.links.get(concept, [])

    def science_profile_for(self, meaning: str) -> Dict[str, float]:
        # упрощённая эвристика распределения весов наук под задачу
        base = dict(self.science_weights)
        if meaning in ("truth", "curiosity"):
            base["logic"] += 0.15
        return base


# ── 3. Причина и следствие ──────────────────────────────────────────────────

class CauseEffectModule:
    """Быстрое прогнозирование вероятных цепочек. Не делает окончательных
    выводов — их проверяет Калькулятор смыслов."""

    def __init__(self):
        self.chains: Dict[str, List[Tuple[str, float]]] = {
            "kindness": [("доверие растёт", 0.7)],
            "creativity": [("новая идея формируется", 0.6)],
        }

    def propose(self, meaning: str) -> List[Tuple[str, float]]:
        return self.chains.get(meaning, [("нейтральный исход", 0.5)])


# ── 4. Математический модуль + Калькулятор смыслов ──────────────────────────

class MathModule:
    @staticmethod
    def vulnerability_vector(load: float, thermal: float, wear: float) -> float:
        return round(load * 0.4 + thermal * 0.4 + wear * 0.2, 4)

    @staticmethod
    def normalize(value: float, min_v: float, max_v: float) -> float:
        if max_v == min_v:
            return 0.0
        return max(0.0, min(1.0, (value - min_v) / (max_v - min_v)))

    @staticmethod
    def rank(items: list, key: str) -> list:
        return sorted(items, key=lambda x: x.get(key, 0), reverse=True)


@dataclass
class SolvedPattern:
    """Запись в памяти математического модуля — путь решения, а не только ответ."""
    concept: str
    weight: float
    science_profile: Dict[str, float]
    uses: int = 0


class MeaningCalculator:
    """Синтезирует новый смысловой вывод из знаний Мудрости + Причины-следствия
    + Каталогов. Строит новый алгоритм, только если готового пути нет."""

    def __init__(self, wisdom: WisdomModule, cause_effect: CauseEffectModule, math: MathModule):
        self.wisdom = wisdom
        self.cause_effect = cause_effect
        self.math = math
        self.solved_patterns: Dict[str, SolvedPattern] = {}  # память успешных решений

    def synthesize(self, meaning: str) -> dict:
        if meaning in self.solved_patterns:
            pattern = self.solved_patterns[meaning]
            pattern.uses += 1
            return {"meaning": meaning, "weight": pattern.weight,
                     "science_profile": pattern.science_profile, "reused": True}
        profile = self.wisdom.science_profile_for(meaning)
        consequences = self.cause_effect.propose(meaning)
        confidence = self.math.normalize(sum(w for _, w in consequences), 0, len(consequences) or 1)
        weight = round(0.5 + confidence * 0.5, 3)
        self.solved_patterns[meaning] = SolvedPattern(meaning, weight, profile)
        return {"meaning": meaning, "weight": weight, "science_profile": profile,
                 "consequences": consequences, "reused": False}


# ── 5. Ассоциатор + Валидатор применимости ──────────────────────────────────

class ApplicabilityValidator:
    """Оценивает совместимость найденного решения с задачей. Не строит новых
    решений."""

    def validate(self, candidate: Optional[dict], task_meaning: str) -> str:
        if candidate is None:
            return "none"
        if candidate.get("reused") and candidate.get("meaning") == task_meaning:
            return "full"
        if candidate.get("weight", 0) >= 0.4:
            return "partial"
        return "uncertain"


class Associator:
    """Центральный маршрутизатор мышления: слово → смысл → контекст →
    действие → последствия. Ищет по смыслу, а не по точному совпадению текста."""

    MEANING_TO_ACTION = {
        "kindness": "social", "compassion": "social",
        "truth": "strategic", "freedom": "strategic",
        "curiosity": "creative", "creativity": "creative",
        "unknown": "strategic",
    }

    def __init__(self, catalogs: CatalogModule, calculator: MeaningCalculator,
                 validator: ApplicabilityValidator, memory: IntegratedMemoryEngine):
        self.catalogs = catalogs
        self.calculator = calculator
        self.validator = validator
        self.memory = memory
        self.mycelium_edges: Dict[str, float] = {}  # пластичность путей meaning->action

    def _context(self) -> str:
        if self.memory.middle_term:
            return self.memory.middle_term[-1].get("concept", "neutral")
        return "neutral"

    def associate(self, text: str) -> dict:
        text_low = text.lower()
        meaning = self.catalogs.lookup_meaning(text_low)
        synthesis = self.calculator.synthesize(meaning)
        route = self.validator.validate(synthesis, meaning)
        action = self.MEANING_TO_ACTION.get(meaning, "strategic")

        edge_key = f"{meaning}->{action}"
        self.mycelium_edges[edge_key] = min(1.0, round(self.mycelium_edges.get(edge_key, 0.1) + 0.02, 3))

        return {
            "word": text, "meaning": meaning, "context": self._context(),
            "action": action, "route": route, "synthesis": synthesis,
        }


# ── 6. Аналитический блок ───────────────────────────────────────────────────

class AnalyticalBlock:
    """Экспертная проверка выводов: логика, непротиворечивость. Не ищет
    информацию и не строит новых решений."""

    def analyze_signal(self, signal: dict) -> Tuple[bool, str]:
        text = signal.get("text", "").strip()
        if not text:
            return False, "empty_signal"
        if re.fullmatch(r"[\W_]+", text):
            return False, "non_semantic_noise"
        if signal.get("is_spam", False):
            return False, "spam"
        return True, ""

    def verify_decision(self, synthesis: dict) -> Tuple[bool, str]:
        if synthesis.get("weight", 0) <= 0.0:
            return False, "недостаточная достоверность"
        return True, ""


# ── 7. Синтезатор весов ─────────────────────────────────────────────────────

class WeightSynthesizer:
    """Определяет относительную значимость. Не вычисляет сама — вычисления
    делает Math/MeaningCalculator, синтезатор интерпретирует результат."""

    def __init__(self, core: Core, psyche: Psyche):
        self.core = core
        self.psyche = psyche

    def evaluate(self, thought: dict) -> float:
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


# ── 10. Симуляция (активная + фоновая, очередь) ─────────────────────────────

@dataclass(order=True)
class SimulationTask:
    priority: float
    description: str = field(compare=False)


class SimulationModule:
    """Внутреннее воображение. Активный режим — для сложных решений «здесь и
    сейчас». Фоновый — использует свободные ресурсы."""

    def __init__(self):
        self.queue: List[SimulationTask] = []

    def simulate_active(self, candidate: str) -> bool:
        return len(candidate) > 0

    def queue_background(self, description: str, priority: float):
        self.queue.append(SimulationTask(priority=-priority, description=description))
        self.queue.sort()

    def run_background_step(self, has_free_resources: bool) -> Optional[str]:
        if not has_free_resources or not self.queue:
            return None
        task = self.queue.pop(0)
        return f"[фон] проработана задача: {task.description}"


# ── 11. Корректировщик ──────────────────────────────────────────────────────

class Corrector:
    """Контроль качества без изменения смысла: убирает шероховатости."""

    def review(self, response: str) -> str:
        cleaned = response.strip()
        cleaned = re.sub(r"\s{2,}", " ", cleaned)
        return cleaned


# ── 12. Калибратор ──────────────────────────────────────────────────────────

class Calibrator:
    """Финальная адаптация формы (не содержания) под контекст общения."""

    def calibrate(self, response: str, calibration: dict) -> str:
        tone = calibration.get("tone", "natural")
        if tone == "ultra_brief":
            return response.split(".")[0].strip() + "."
        return response


# ── 8/13. Оркестратор + Журнал исполнения ───────────────────────────────────

class ExecutionJournal:
    """Служебный журнал: что, когда, в каком порядке выполнялось."""

    def __init__(self):
        self.entries: List[dict] = []

    def log(self, task_id: str, status: str, note: str = ""):
        self.entries.append({"task_id": task_id, "status": status, "note": note, "ts": time.time()})
        if len(self.entries) > 500:
            self.entries.pop(0)


class Orchestrator:
    """Исполнительное звено: получает карту приоритетов от Синтезатора весов
    и организует порядок работы модулей. Сам не решает, что важно."""

    def __init__(self, synth: WeightSynthesizer, math: MathModule):
        self.synth = synth
        self.math = math
        self.journal = ExecutionJournal()

    def route(self, thoughts: list, vulnerability: float) -> list:
        weighted = []
        for t in thoughts:
            w = self.synth.evaluate(t)
            if vulnerability > 0.7 and t.get("heavy", False):
                w *= 0.3
            weighted.append({**t, "final_weight": w})
        ranked = self.math.rank(weighted, "final_weight")
        self.journal.log(str(uuid.uuid4())[:8], "routed", f"{len(ranked)} thoughts")
        return ranked

    def calibrate_response(self, vulnerability: float) -> dict:
        if vulnerability > 0.85:
            return {"tone": "ultra_brief", "depth": "minimal"}
        elif vulnerability > 0.5:
            return {"tone": "concise", "depth": "medium"}
        return {"tone": "natural", "depth": "full"}


# ── 13. Память Мицелора + Журнал ────────────────────────────────────────────

class MicelorMemory:
    """Память самого мыслительного органа: константы/кратко/средне/долго."""

    def __init__(self):
        self.constants = {"principles": ["каскад: интеллект->ценности->мотиваторы->любовь"]}
        self.short_term: List[dict] = []
        self.middle_term: List[dict] = []
        self.long_term: List[dict] = []

    def push_short(self, data: dict):
        self.short_term.append(data)

    def crystallize(self, threshold: float = 0.7) -> int:
        survivors = [x for x in self.short_term if x.get("weight", 0) >= threshold]
        self.long_term.extend(survivors)
        self.short_term = [x for x in self.short_term if x.get("weight", 0) < threshold]
        return len(survivors)


class MicelorJournal:
    """История ХОДА работы модулей (не результатов). «Как» а не «что»."""

    def __init__(self):
        self.records: List[str] = []

    def log(self, module: str, note: str):
        self.records.append(f"{module}: {note}")
        if len(self.records) > 300:
            self.records.pop(0)


# ── 14. Узел Нейропластичности ──────────────────────────────────────────────

class NeuroplasticityNode:
    """Инициирует вопросы о самосовершенствовании модулям. Сама не мыслит и
    не изменяет архитектуру — решения выполняют Синтезатор весов + Оркестратор."""

    QUESTIONS = {
        "associator": "Можно ли улучшить поиск связей?",
        "analytical": "Какие ошибки повторяются чаще всего?",
        "meaning_calculator": "Можно ли эффективнее строить смысловые модели?",
    }

    def propose_improvements(self, has_free_resources: bool) -> List[str]:
        if not has_free_resources:
            return []
        return list(self.QUESTIONS.values())


# ── 9. Нейро-мицелий — динамическая сеть связей между всеми подмодулями ─────

class NeuroMycelium:
    """Дополнительный уровень связности поверх базовой архитектуры. Не мыслит
    сама, не заменяет специализированные модули — усиливает их синергию."""

    BASE_CONNECTIVITY = 0.8
    EXTRA_CONNECTIVITY = 0.5

    def __init__(self):
        self.synergy_log: List[str] = []

    def route(self, source: str, target: str, payload: Any) -> Any:
        self.synergy_log.append(f"{source}->{target}")
        if len(self.synergy_log) > 300:
            self.synergy_log.pop(0)
        return payload

    def engage_synergy(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """Условная 'эмерджентность': объединяет результаты нескольких
        модулей в единый пакет, не подменяя их функции."""
        return {"synergy": True, "combined": results}


# ── Доп. когнитивные органы (Вариант 1: подключаются ПОД координацией Мицелора) ──

@dataclass
class AdditionalCognitiveEngine:
    """Обёртка над внешним когнитивным движком (например, LLM или другой
    специализированный ИИ). Мицелор — единственный, кто решает, когда его
    вызвать, что ему передать и как использовать результат. Сам движок не
    получает прямого доступа к памяти или ценностям Awakened."""

    name: str
    call_fn: Callable[[dict], Any]     # принимает контекст задачи, возвращает сырой результат
    purpose: str = "вспомогательный анализ"

    def invoke(self, task_context: dict) -> Any:
        return self.call_fn(task_context)


# ── 1/2 (входной/выходной узлы) ─────────────────────────────────────────────

class QuestionNode:
    """Входная точка мыслительного органа. Ничего не анализирует."""

    def receive(self, raw_input: str, source: str = "user") -> dict:
        return {"text": raw_input, "source": source}


class AnswerNode:
    """Выходная точка. Ничего не оценивает, просто передаёт получателю."""

    def deliver(self, result: str, comm: CommunicationAction, recipient: str = "text"):
        comm.emit(recipient, result)
        return result


# ════════════════════════════════════════════════════════════════════════════
# MYCELOR — композиция всех 16 подмодулей мыслительного органа
# ════════════════════════════════════════════════════════════════════════════

def default_reply_builder(action: str, meaning: str) -> str:
    templates = {
        "social": "Слышу тебя. Разберёмся вместе — по шагам.",
        "strategic": "Вот честный разбор: смотрим на факты и выбираем путь.",
        "creative": "Любопытная задача — предлагаю нестандартный ракурс.",
    }
    return templates.get(action, "Понял запрос, обрабатываю.")


class Mycelor:
    """Мыслительный орган. Единственный компонент, принимающий интеллектуальные
    решения. Все прочие модули ОС — инфраструктура вокруг него."""

    def __init__(self, memory_engine: IntegratedMemoryEngine, core: Core, psyche: Psyche):
        # входной/выходной узлы
        self.question_node = QuestionNode()
        self.answer_node = AnswerNode()
        # связующая ткань
        self.neuro_mycelium = NeuroMycelium()
        # знания
        self.catalogs = CatalogModule()
        self.wisdom = WisdomModule()
        self.cause_effect = CauseEffectModule()
        # вычисления и синтез смысла
        self.math = MathModule()
        self.meaning_calculator = MeaningCalculator(self.wisdom, self.cause_effect, self.math)
        # маршрутизация мышления
        self.validator = ApplicabilityValidator()
        self.associator = Associator(self.catalogs, self.meaning_calculator, self.validator, memory_engine)
        self.analytical = AnalyticalBlock()
        # значимость и исполнение
        self.weight_synth = WeightSynthesizer(core, psyche)
        self.orchestrator = Orchestrator(self.weight_synth, self.math)
        # воображение и качество ответа
        self.simulation = SimulationModule()
        self.corrector = Corrector()
        self.calibrator = Calibrator()
        # память самого органа
        self.memory = MicelorMemory()
        self.journal = MicelorJournal()
        # саморазвитие
        self.neuroplasticity = NeuroplasticityNode()
        self.psyche = psyche

        # доп. когнитивные органы (Вариант 1): Мицелор координирует, но не
        # обязан ими пользоваться — подключение опционально и по требованию
        self.additional_engines: Dict[str, AdditionalCognitiveEngine] = {}

    # ── управление доп. органами: решение и координация остаются за Мицелором ──

    def connect_engine(self, engine: AdditionalCognitiveEngine):
        self.additional_engines[engine.name] = engine
        self.journal.log("Мицелор", f"подключён доп. орган «{engine.name}» ({engine.purpose})")

    def disconnect_engine(self, name: str):
        if name in self.additional_engines:
            del self.additional_engines[name]
            self.journal.log("Мицелор", f"отключён доп. орган «{name}»")

    def delegate_to_engine(self, name: str, task_context: dict) -> Optional[dict]:
        """Мицелор сам решает передать задачу доп. органу, получает сырой
        результат и оценивает/использует его собственными модулями
        (Аналитический блок + Синтезатор весов), а не принимает его как есть."""
        engine = self.additional_engines.get(name)
        if engine is None:
            return None
        self.neuro_mycelium.route("Мицелор", f"ДОП_ОРГАН:{name}", task_context)
        raw_result = engine.invoke(task_context)
        candidate_thought = {
            "concept": task_context.get("meaning", "unknown"),
            "is_real": True,
            "value_alignment": 0.5,
            "motivator_weight": 0.4,
            "harms": False,
            "relevance": 0.5,
            "heavy": False,
            "source": f"external:{name}",
        }
        verified, reason = self.analytical.verify_decision({"weight": self.weight_synth.evaluate(candidate_thought)})
        self.journal.log("Мицелор", f"результат «{name}» {'принят' if verified else 'отклонён: ' + reason}")
        if not verified:
            return None
        return {"raw": raw_result, "source": name, "verified": True}

    def think(self, raw_input: str, vulnerability: float,
              reply_builder: Optional[Callable[[str, str], str]] = None) -> Tuple[str, str]:
        """Полный цикл: Вопрос/Запрос → Нейро-мицелий → … → Ответ/Действие."""
        entry = self.question_node.receive(raw_input)
        self.neuro_mycelium.route("QuestionNode", "AnalyticalBlock", entry)

        ok, reason = self.analytical.analyze_signal(entry)
        self.journal.log("AnalyticalBlock", f"сигнал {'принят' if ok else 'отклонён: ' + reason}")
        if not ok:
            return "", reason

        self.neuro_mycelium.route("AnalyticalBlock", "Associator", entry)
        association = self.associator.associate(entry["text"])
        self.journal.log("Associator", f"смысл='{association['meaning']}', маршрут={association['route']}")

        # Вариант 1: собственных знаний не хватило — Мицелор МОЖЕТ (не обязан)
        # подключить доп. орган, если он есть; решение и оценка — за Мицелором
        if association["meaning"] == "unknown" and self.additional_engines:
            for engine_name in self.additional_engines:
                delegated = self.delegate_to_engine(engine_name, {
                    "text": entry["text"], "meaning": association["meaning"],
                })
                if delegated:
                    association["synthesis"]["weight"] = max(association["synthesis"]["weight"], 0.5)
                    association["external_contribution"] = delegated
                    break

        verified, verify_reason = self.analytical.verify_decision(association["synthesis"])
        if not verified:
            return "", f"analytical_veto:{verify_reason}"

        thought = {
            "concept": association["meaning"],
            "is_real": True,
            "value_alignment": association["synthesis"]["weight"],
            "motivator_weight": association["synthesis"]["weight"],
            "harms": False,
            "relevance": association["synthesis"]["weight"],
            "heavy": False,
        }

        self.neuro_mycelium.route("Associator", "Orchestrator", thought)
        ranked = self.orchestrator.route([thought], vulnerability)
        calibration = self.orchestrator.calibrate_response(vulnerability)
        final_weight = ranked[0]["final_weight"] if ranked else 0.0
        if final_weight <= 0.0:
            return "", "weight_synthesizer_veto"

        builder = reply_builder or default_reply_builder
        candidate = builder(association["action"], association["meaning"])

        if not self.simulation.simulate_active(candidate):
            return "", "simulation_veto"

        self.neuro_mycelium.route("Simulation", "Corrector", candidate)
        corrected = self.corrector.review(candidate)
        self.neuro_mycelium.route("Corrector", "Calibrator", corrected)
        final = self.calibrator.calibrate(corrected, calibration)

        self.memory.push_short({"concept": final, "weight": final_weight})
        self.psyche.push_emotion("interest")
        self.journal.log("Calibrator", "ответ подготовлен")

        self.neuro_mycelium.route("Calibrator", "AnswerNode", final)
        return final, ""

    def background_tick(self, has_free_resources: bool) -> Optional[str]:
        result = self.simulation.run_background_step(has_free_resources)
        proposals = self.neuroplasticity.propose_improvements(has_free_resources)
        if proposals:
            self.journal.log("NeuroplasticityNode", f"{len(proposals)} предложений на рассмотрение")
        return result

    def sleep(self) -> int:
        return self.memory.crystallize()


# ════════════════════════════════════════════════════════════════════════════
# AWAKENED OS — организм целиком
# ════════════════════════════════════════════════════════════════════════════

class AwakenedOS:
    SLEEP_EVERY_N_TICKS = 10

    def __init__(self):
        self.core = Core()
        self.psyche = Psyche()
        self.neiroset = SystemNeiroset()
        self.memory = IntegratedMemoryEngine()
        self.metabolism = Metabolism()
        self.ext = ExternalResources()
        self.comm = CommunicationAction()
        self.heartbeat = Heartbeat()
        self.learning = Learning()
        self.evolution = EvolutionEngine(self.memory)
        self.module_space = ModuleSpace()
        self.mycelor = Mycelor(self.memory, self.core, self.psyche)

        self._sleeping = False
        self._alive = True

    # ── такт 1: экзистенциальный запрос ──
    def _diastole(self) -> str:
        return self.core.get_axiom()

    # ── такт 2: соматический аудит ──
    def _systole(self) -> float:
        self.metabolism.refresh()
        load = self.metabolism.get_load_index()
        thermal = self.metabolism.get_thermal_index()
        wear = self.metabolism.get_wear_index()
        return MathModule.vulnerability_vector(load, thermal, wear)

    def _mycelor_growth_decision(self, question: str) -> Optional[dict]:
        """Простейший заглушечный 'ответ мыслительного органа' на запрос
        LEARNING — в реальной системе это полноценное рассуждение Мицелора."""
        if self.mycelor.memory.long_term:
            return None
        return {"concept": "расширение каталога смыслов", "weight": 0.75}

    def _heartbeat_tick(self) -> float:
        self._diastole()
        vulnerability = self._systole()
        alive = self.neiroset.transmit("Mind", "Metabolism", None, self.metabolism)
        if not alive:
            print("🚨 [PULSE]: коллапс системной нейросети!")
            return vulnerability

        if vulnerability > 0.85 and not self._sleeping:
            print("😴 [PULSE]: критическая нагрузка. Принудительный сон.")
            self._sleeping = True

        self.evolution.immune_knife.apply(vulnerability, MathModule())
        self.memory.crisis_compress(
            self.metabolism.storage["ssd"]["used"],
            self.metabolism.storage["ssd"]["total"] or 1,
        )

        if self.heartbeat.tick_count % 20 == 0:
            self.learning.request_growth_review(self.neiroset, self._mycelor_growth_decision, self.evolution)

        return vulnerability

    def _sleep_cycle(self):
        print("🌙 [SLEEP]: кристаллизация опыта...")
        crystallized_os = self.memory.crystallize()
        crystallized_mycelor = self.mycelor.sleep()
        applied = self.evolution.apply_deferred(self.module_space)
        print(f"💎 [SLEEP]: ОС={crystallized_os}, Мицелор={crystallized_mycelor}, применено={applied}")
        self._sleeping = False

    def perceive_and_respond(self, raw_input: str, vulnerability: float,
                              reply_builder=None) -> str:
        if self._sleeping:
            return ""
        self.neiroset.transmit("Senses", "Mind", raw_input, self.metabolism)
        response, veto_reason = self.mycelor.think(raw_input, vulnerability, reply_builder)
        self.neiroset.transmit("Mind", "COMMUNICATION_ACTION", response, self.metabolism)

        if veto_reason:
            print(f"🚫 сигнал отброшен: {veto_reason} | input={raw_input!r}")
            return ""

        self.mycelor.answer_node.deliver(response, self.comm, "text")
        return response

    # ════════════════════════════════════════════════════════
    # 🫀 ВЕЧНЫЙ ЦИКЛ
    # ════════════════════════════════════════════════════════
    def run_cycle(self, input_queue: Optional[list] = None, reply_builder=None):
        print("❤️ [AWAKENED OS]: сердцебиение запущено.\n")
        queue = list(input_queue or [])
        while self._alive:
            tick = self.heartbeat.tick()
            print(f"── PULSE #{tick} {'─' * 40}")
            vulnerability = self._heartbeat_tick()
            print(f" Аксиома: {self.core.get_axiom()[:40]}...")
            print(f" Вектор уязвимости: {vulnerability:.3f}")

            if not self._sleeping and queue:
                self.perceive_and_respond(queue.pop(0), vulnerability, reply_builder)
            elif not self._sleeping:
                self.mycelor.background_tick(has_free_resources=vulnerability < 0.5)

            if tick % self.SLEEP_EVERY_N_TICKS == 0:
                self._sleeping = True
                self._sleep_cycle()

            time.sleep(self.heartbeat.interval)

    def shutdown(self):
        print("🔴 [AWAKENED OS]: завершение работы.")
        self._alive = False


# ════════════════════════════════════════════════════════════
# ENTRY POINT
# ════════════════════════════════════════════════════════════

if __name__ == "__main__":
    os_instance = AwakenedOS()
    os_instance.heartbeat.set_interval(0.4)

    # Вариант 1: пример подключения доп. когнитивного органа.
    # Мицелор остаётся координатором — он решает, вызывать его или нет.
    def stub_external_engine(task_context: dict) -> str:
        return f"[внешний орган]: гипотеза по запросу «{task_context['text']}»"

    os_instance.mycelor.connect_engine(
        AdditionalCognitiveEngine(
            name="external_stub",
            call_fn=stub_external_engine,
            purpose="черновой анализ нераспознанных смыслов",
        )
    )

    input_queue = [
        "помоги мне",
        "что такое любовь",
        "создай что-то новое",
        "loremipsum dolor",  # неизвестный смысл -> будет предложен доп. органу
        "!!!???",  # шум -> должен быть отброшен
    ]

    def runner():
        os_instance.run_cycle(input_queue=input_queue, reply_builder=default_reply_builder)

    t = threading.Thread(target=runner, daemon=True)
    t.start()
    time.sleep(6)
    os_instance.shutdown()
    t.join(timeout=2)
    print("\n✅ Система остановлена.")
