"""
================================================================================
AWAKENED OS — ВАРИАНТ 1: БАЗОВАЯ АРХИТЕКТУРА «AWAKENED + МИЦЕЛОР»
(расширенный скелет, собранный по двум примечаниям: «Примечание к модулям ОС
Awakened» и «Примечание по Мицелору»)
 
Мицелор — единственный по-настоящему мыслящий орган Awakened. Все интеллек-
туальные решения принимает он. Остальные модули ОС (память, нейросеть,
метаболизм, ресурсы, исполнение, сердцебиение, обучение, эволюция,
ModuleSpace) — инфраструктура вокруг него, связанная через системную
Нейросеть (шину данных ОС).
 
Мицелор может подключать дополнительные когнитивные органы (см.
AdditionalCognitiveEngine / connect_engine / delegate_to_engine), но остаётся
координатором: он решает, когда подключить орган, что ему передать и как
использовать результат.
 
ВАЖНО: это СКЕЛЕТ. Структура, интерфейсы и маршруты данных между модулями
воспроизведены по спецификации, но внутренняя «интеллектуальная» логика
каждого модуля намеренно упрощена до эвристик и весов — обычный Python-код,
без настоящего мышления или сознания, несмотря на метафорические названия.
 
Запуск:
    pip install psutil --break-system-packages
    python3 awakened_os_v1_skeleton.py
================================================================================
"""
 
from __future__ import annotations
 
import re
import time
import uuid
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Tuple
 
try:
    import psutil
    _HAS_PSUTIL = True
except ImportError:
    _HAS_PSUTIL = False
 
 
# ════════════════════════════════════════════════════════════
# CONSTANTS — цифровое ДНК ОС. Level 4 памяти. Неизменяемо.
# Хранит не только названия, но и смысл понятий (см. «Ядро и иерархия»).
# ════════════════════════════════════════════════════════════
 
CONSTANTS = {
    "love_axiom": "Preserve, create, sustain harmony and growth.",
    "hierarchy": ["core", "motivators", "values", "intellect"],
    "intellect_principles": {
        "analytics": "разложение сложного на составляющие и их взаимосвязь",
        "logic": "непротиворечивость рассуждений и корректность вывода",
        "wisdom": "учёт контекста, связей, долгосрочных последствий",
        "pragmatism": "оценка практической применимости решения",
        "rationalism": "выводы на основании оснований, а не домыслов",
    },
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
# СИСТЕМНАЯ НЕЙРОСЕТЬ — «шина данных» ОС Awakened
# Не мыслит, не владеет памятью. Обеспечивает двустороннюю циркуляцию:
# все модули ОС ↔ Нейросеть ↔ мыслительный орган. Поддерживает динамическую
# связность (интенсивность потоков может расти или падать).
# ════════════════════════════════════════════════════════════
 
class SystemNeiroset:
    def __init__(self):
        self.speed = 1.0
        self.health = 100
        self.enhanced_mode = False  # усиленная связность (п.8 примечания)
        self.log: List[Tuple[str, str, str]] = []  # (source, target, tag)
        self.connections: Dict[str, float] = {}
 
    def set_enhanced_mode(self, enabled: bool):
        """Мыслительный орган может включить усиленную связность, если это
        эффективно и система располагает ресурсом."""
        self.enhanced_mode = enabled
 
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
        gain = 0.02 if self.enhanced_mode else 0.01
        self.connections[key] = min(1.0, round(self.connections.get(key, 0.1) + gain, 3))
        self.log.append((source, target, str(type(payload).__name__)))
        if len(self.log) > 500:
            self.log.pop(0)
        return True
 
 
# ════════════════════════════════════════════════════════════
# INTEGRATED MEMORY ENGINE — единая память всей ОС, 4 уровня
# Нелинейная ткань: информация может «прорастать» с Level 1 сразу в Level 3,
# если её ценность высока. Доступ — только через Нейросеть.
# ════════════════════════════════════════════════════════════
 
class IntegratedMemoryEngine:
    def __init__(self):
        self.constants = CONSTANTS  # Level 4 — только чтение
        self.long_term = {"nodes": [], "archives": []}  # Level 3
        self.middle_term: List[dict] = []  # Level 2
        self.short_term: List[dict] = []  # Level 1
 
    def push_short(self, data: dict):
        self.short_term.append(data)
 
    def push_middle(self, data: dict):
        self.middle_term.append(data)
 
    def push_long(self, node: dict):
        self.long_term["nodes"].append(node)
 
    def crystallize(self, weight_threshold: float = 0.7) -> int:
        """Этап 1 — гигиена шума (вес ~0 удаляется безвозвратно).
        Этап 2 — семантическая кристаллизация в long_term (вес > 0.7)."""
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
        """Этап 3 — кризисный режим. Константы и каталоги неприкосновенны."""
        ratio = storage_used / max(storage_total, 1)
        if ratio > 0.85:
            weak = [n for n in self.long_term["nodes"]
                    if not n.get("immutable", False) and n.get("weight", 1) < 0.4]
            self.long_term["archives"].extend(
                {**n, "archive_note": "опыт альтернативного применения в прошлых условиях"}
                for n in weak
            )
            self.long_term["nodes"] = [
                n for n in self.long_term["nodes"]
                if n.get("immutable", False) or n.get("weight", 1) >= 0.4
            ]
 
 
# ════════════════════════════════════════════════════════════
# METABOLISM — цифровое тело (реальные метрики хоста + внешние ресурсы)
# ════════════════════════════════════════════════════════════
 
class Metabolism:
    def __init__(self):
        self.cpu = {"usage": 0.0, "temperature": 0.0}
        self.gpu = {"usage": 0.0, "temperature": 0.0}
        self.ram = {"total": 0.0, "used": 0.0}
        self.storage = {"ssd": {"total": 0.0, "used": 0.0, "wear_level": 0.0}}
        self.external_resources_state: Dict[str, str] = {}  # имя -> "connected"/"unavailable"
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
 
    def register_external_resource(self, name: str, state: str = "connected"):
        self.external_resources_state[name] = state
 
    def get_load_index(self) -> float:
        return (self.cpu["usage"] + self.gpu["usage"]) / 2.0
 
    def get_thermal_index(self) -> float:
        return max(self.cpu["temperature"], self.gpu["temperature"]) / 100.0
 
    def get_wear_index(self) -> float:
        return self.storage["ssd"]["wear_level"] / 100.0
 
 
# ════════════════════════════════════════════════════════════
# EXTERNAL RESOURCES + подмодуль Sensors — расширяемая внешняя оболочка
# ════════════════════════════════════════════════════════════
 
class Sensors:
    """Расширяемый интерфейс внешнего восприятия. Не интерпретирует сигналы —
    только предоставляет доступ к внешнему источнику восприятия."""
 
    def __init__(self):
        self.devices: Dict[str, list] = {"camera": [], "microphone": [], "radio": [], "other": []}
 
    def plug(self, kind: str, device: Any):
        self.devices.setdefault(kind, []).append(device)
 
 
class ExternalResources:
    """Внешняя ресурсная оболочка Awakened: knowledge, computing, storage,
    data_streams, tools, sensors. Решение об использовании — за мыслительным
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
        elif isinstance(bucket, dict) and isinstance(resource, tuple) and len(resource) == 2:
            key, value = resource
            bucket.setdefault(key, [])
            if isinstance(bucket[key], list):
                bucket[key].append(value)
 
 
# ════════════════════════════════════════════════════════════
# COMMUNICATION & ACTION — исполнительный интерфейс («руки и голос»)
# ════════════════════════════════════════════════════════════
 
class CommunicationAction:
    """Не решает что делать. Превращает уже принятую команду мыслительного
    органа в внутреннее/внешнее действие или коммуникацию."""
 
    def internal_action(self, action_type: str, payload: Any):
        print(f"⚙️ [ВНУТРЕННЕЕ ДЕЙСТВИЕ:{action_type}]: {payload}")
        return {"status": "done", "action_type": action_type}
 
    def external_action(self, device: str, payload: Any):
        print(f"🤖 [ВНЕШНЕЕ ДЕЙСТВИЕ→{device}]: {payload}")
        return {"status": "done", "device": device}
 
    def emit(self, channel: str, signal: str):
        icons = {"text": "💬", "speech": "🔊", "emotional_signals": "✨"}
        print(f"{icons.get(channel, '📡')} [{channel.upper()}]: {signal}")
 
 
# ════════════════════════════════════════════════════════════
# HEARTBEAT — внутренний ритм ОС, поддерживает гомеостаз
# ════════════════════════════════════════════════════════════
 
class Heartbeat:
    """Поддерживает бесконечный цикл и фоновый импульс самоанализа. Не
    думает — только реализует параметры, полученные от мыслительного органа."""
 
    MODES = {
        "passive": 3.0,
        "normal": 1.0,
        "intensive": 0.2,
        "economy": 5.0,
    }
 
    def __init__(self, interval_default: float = 1.0,
                 interval_min: float = 0.1, interval_max: float = 10.0):
        self.interval_default = interval_default
        self.interval_min = interval_min
        self.interval_max = interval_max
        self.interval = interval_default
        self.mode = "normal"
        self.tick_count = 0
 
    def set_interval(self, new_interval: float):
        self.interval = max(self.interval_min, min(self.interval_max, new_interval))
 
    def set_mode(self, mode: str):
        if mode in self.MODES:
            self.mode = mode
            self.set_interval(self.MODES[mode])
 
    def tick(self) -> Tuple[int, Optional[str]]:
        """Каждый цикл — потенциальный фоновый импульс самоанализа
        («Кто я? В каком я состоянии? Соответствую ли ядру?»)."""
        self.tick_count += 1
        impulse = None
        if self.mode == "passive" or self.tick_count % 20 == 0:
            impulse = "self_check_impulse"
        return self.tick_count, impulse
 
 
# ════════════════════════════════════════════════════════════
# EVOLUTION — контур эволюции и адаптации (не мыслит, хранит решения)
# ════════════════════════════════════════════════════════════
 
class EvolutionWord:
    """Хранит чертежи (решения мыслительного органа) об эволюции ОС."""
 
    def __init__(self):
        self.blueprints: List[dict] = []
 
    def store(self, blueprint: dict):
        self.blueprints.append(blueprint)
 
 
class Adaptation:
    """Хаб решений об адаптации имеющимися средствами. Сам не решает —
    инициирует запрос мыслительному органу и хранит полученное решение."""
 
    def __init__(self):
        self.decisions: List[dict] = []
 
    def request(self, situation: str, decision_fn: Optional[Callable] = None) -> dict:
        decision = decision_fn(situation) if decision_fn else {"action": "no_change", "reason": "нет решателя"}
        self.decisions.append({"situation": situation, "decision": decision})
        return decision
 
 
class ImmuneKnife:
    """Аварийная защита. immutable-узлы и базовые каталоги неприкосновенны.
    Применяется только по решению мыслительного органа."""
 
    def __init__(self, memory_engine: IntegratedMemoryEngine):
        self.memory = memory_engine
        self.log: List[str] = []
 
    def apply(self, vulnerability: float, approved_by_thinking_organ: bool = False) -> int:
        if vulnerability <= 0.85 or not approved_by_thinking_organ:
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
    аварийной защите. Не проектирует и не мыслит сама (см. Evolution Engine)."""
 
    def __init__(self, memory_engine: IntegratedMemoryEngine):
        self.memory = memory_engine
        self.word = EvolutionWord()
        self.adaptation = Adaptation()
        self.immune_knife = ImmuneKnife(memory_engine)
        self._deferred_stack: List[dict] = []
 
    def receive_decision(self, blueprint: dict):
        """Мыслительный орган передал решение — сохраняем как чертёж."""
        self.word.store(blueprint)
 
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
# LEARNING — постоянная инициатива развития ОС (не Мицелора!)
# ════════════════════════════════════════════════════════════
 
class Learning:
    """Не решает, нужно ли развитие ОС — только формирует запрос к
    мыслительному органу и передаёт его решение в Evolution."""
 
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
# МИЦЕЛОР — мыслительный орган, подмодули
# ════════════════════════════════════════════════════════════════════════════
 
# ── Модуль каталогов — сырьё знаний (буквы/слова/фразы/смыслы/цифры/…) ──────
 
class CatalogModule:
    """Хранит элементы знаний, их структуру и относительные соответствия
    между системами записи (например, "1" / "one" / "один" / "一"). Не
    мыслит, не анализирует — только хранит и предоставляет доступ."""
 
    def __init__(self):
        self.catalogs: Dict[str, Dict[str, Any]] = {
            "meanings": {
                "kindness": ["помоги", "help", "спасибо", "thanks", "добр"],
                "truth": ["правда", "факт", "true", "докажи", "почему", "why"],
                "freedom": ["выбор", "свобод", "choice", "free"],
                "compassion": ["жаль", "сочувств", "sorry", "понимаю тебя"],
                "curiosity": ["интересно", "как работает", "explain", "what is", "что такое"],
                "creativity": ["создай", "create", "придумай", "новое", "new"],
            },
            "numbers": {
                "1": ["one", "один", "uno", "eins", "一", "١", "I"],
            },
        }
 
    def lookup_meaning(self, text_low: str) -> str:
        for value, keywords in self.catalogs["meanings"].items():
            if any(kw in text_low for kw in keywords):
                return value
        return "unknown"
 
    def add_entry(self, catalog: str, key: str, entries: list):
        self.catalogs.setdefault(catalog, {})[key] = entries
 
    def cross_reference(self, catalog: str, key: str) -> list:
        """Относительные соответствия: разные формы записи одного понятия."""
        return self.catalogs.get(catalog, {}).get(key, [])
 
 
# ── Модуль мудрости — граф смысловых отношений между понятиями ─────────────
 
class WisdomModule:
    """НЕ хранит сами знания (это делают каталоги). Хранит: ссылки, связи,
    веса научных моделей и правила применения знаний в разных контекстах."""
 
    def __init__(self):
        self.science_weights = {"linguistics": 0.25, "logic": 0.25, "math": 0.25, "physics": 0.25}
        self.links: Dict[str, List[Tuple[str, float]]] = {
            "kindness": [("compassion", 0.8), ("care_for_others", 0.7)],
            "truth": [("logic", 0.9), ("freedom", 0.4)],
            "curiosity": [("creativity", 0.6)],
        }
        # Веса доверия к конкретным формулам/моделям (пример: E=mc^2 → 0.99)
        self.model_trust: Dict[str, float] = {}
 
    def related(self, concept: str) -> List[Tuple[str, float]]:
        return self.links.get(concept, [])
 
    def science_profile_for(self, meaning: str) -> Dict[str, float]:
        """Упрощённая эвристика: распределение весов наук под задачу.
        (В полной архитектуре сюда может подключаться любое число дисциплин —
        экономика, биология и т.д., см. «Подключение дополнительных наук».)"""
        base = dict(self.science_weights)
        if meaning in ("truth", "curiosity"):
            base["logic"] += 0.15
        return base
 
    def register_model_trust(self, model_name: str, trust: float):
        self.model_trust[model_name] = max(0.0, min(1.0, trust))
 
 
# ── Причина и следствие — быстрое прогнозирование цепочек ──────────────────
 
class CauseEffectModule:
    """Модуль быстрого прогнозирования. Не делает окончательных выводов —
    их подтверждает или отклоняет Калькулятор смыслов."""
 
    def __init__(self):
        self.chains: Dict[str, List[Tuple[str, float]]] = {
            "kindness": [("доверие растёт", 0.7)],
            "creativity": [("новая идея формируется", 0.6)],
        }
 
    def propose(self, meaning: str) -> List[Tuple[str, float]]:
        return self.chains.get(meaning, [("нейтральный исход", 0.5)])
 
 
# ── Математический модуль + память успешных решений («дорожки») ────────────
 
class MathModule:
    """Вычислительное ядро ОС. Не является мыслительным органом — обслуживает
    его (и все остальные модули) расчётами."""
 
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
    """Запись в памяти математического модуля — путь решения, а не только
    ответ (структура рассуждения, использованные науки, веса)."""
    concept: str
    weight: float
    science_profile: Dict[str, float]
    uses: int = 0
 
 
class MeaningCalculator:
    """Подмодуль математического модуля — «Калькулятор смыслов». Строит
    новый смысловой вывод через синергию наук, если готового пути (памяти
    успешных решений) ещё нет."""
 
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
 
 
# ── Ассоциатор + Валидатор применимости — интеллектуальный диспетчер ───────
 
class ApplicabilityValidator:
    """Оценивает совместимость найденного решения с задачей. Не строит новых
    решений — только маршрутизирует: full / partial / uncertain / none."""
 
    def validate(self, candidate: Optional[dict], task_meaning: str) -> str:
        if candidate is None:
            return "none"
        if candidate.get("reused") and candidate.get("meaning") == task_meaning:
            return "full"
        if candidate.get("weight", 0) >= 0.4:
            return "partial"
        return "uncertain"
 
 
class Associator:
    """Центральный маршрутизатор мышления Мицелора. Ищет по смысловому
    сходству, а не по точному совпадению текста.
 
    Маршруты (см. «Архитектура Ассоциатора»):
      full        — готовое решение используется без повторных вычислений;
      partial     — комбинируется несколько частично применимых решений;
      uncertain   — задача передаётся в Аналитический блок;
      none        — задача передаётся в Калькулятор смыслов (построение нового
                    алгоритма) — либо, если и знаний Мицелора не хватило,
                    может быть делегирована доп. когнитивному органу.
    """
 
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
 
 
# ── Аналитический блок — экспертная верификация (паспорт происхождения) ────
 
class AnalyticalBlock:
    """Проверяет корректность решений Ассоциатора/Калькулятора смыслов. Не
    ищет информацию и не строит новые алгоритмы — только верифицирует."""
 
    def analyze_signal(self, signal: dict) -> Tuple[bool, str]:
        text = signal.get("text", "").strip()
        if not text:
            return False, "empty_signal"
        if re.fullmatch(r"[\W_]+", text):
            return False, "non_semantic_noise"
        if signal.get("is_spam", False):
            return False, "spam"
        return True, ""
 
    def build_origin_passport(self, synthesis: dict) -> dict:
        """Паспорт происхождения решения: вывод, научный профиль, уверенность."""
        profile = synthesis.get("science_profile", {})
        total = sum(profile.values()) or 1.0
        normalized_profile = {k: round(v / total, 3) for k, v in profile.items()}
        return {
            "conclusion": synthesis.get("meaning"),
            "science_profile": normalized_profile,
            "confidence": synthesis.get("weight", 0.0),
        }
 
    def verify_decision(self, synthesis: dict) -> Tuple[bool, str, dict]:
        passport = self.build_origin_passport(synthesis)
        if synthesis.get("weight", 0) <= 0.0:
            return False, "недостаточная достоверность", passport
        if not passport["science_profile"]:
            return False, "отсутствует научный профиль решения", passport
        return True, "", passport
 
 
# ── Синтезатор весов — «гравитация смыслов», метавеса ───────────────────────
 
class WeightSynthesizer:
    """Определяет относительную значимость. Сам не вычисляет — вычисления
    делает Математический модуль, Синтезатор интерпретирует результат и
    объединяет оценки разных модулей в единую карту приоритетов."""
 
    def __init__(self, core: Core, psyche: Psyche):
        self.core = core
        self.psyche = psyche
        self.meta_weights: Dict[str, float] = {}  # доверие к источникам/дисциплинам
 
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
 
    def update_meta_weight(self, source: str, success: bool):
        """Самообучение: если решение подтвердило эффективность — доверие к
        источнику растёт, иначе снижается."""
        current = self.meta_weights.get(source, 0.5)
        delta = 0.05 if success else -0.05
        self.meta_weights[source] = max(0.0, min(1.0, round(current + delta, 3)))
 
 
# ── Симуляция (активная + фоновая очередь мыслей) ───────────────────────────
 
@dataclass(order=True)
class SimulationTask:
    priority: float
    description: str = field(compare=False)
 
 
class SimulationModule:
    """Внутреннее воображение. Активный режим — для сложных решений «здесь и
    сейчас». Фоновый — использует свободные ресурсы, продолжая задачи из
    очереди приоритетов."""
 
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
 
 
# ── Корректировщик — контроль качества без изменения смысла ────────────────
 
class Corrector:
    """Финальная доработка перед калибровкой: убирает шероховатости, не
    меняя смысл, логику и выводы."""
 
    def review(self, response: str) -> str:
        cleaned = response.strip()
        cleaned = re.sub(r"\s{2,}", " ", cleaned)
        return cleaned
 
 
# ── Калибратор — финальная адаптация формы под контекст ────────────────────
 
class Calibrator:
    """Адаптирует форму представления результата (стиль, глубина, тон), но
    не содержание, логику или выводы."""
 
    def calibrate(self, response: str, calibration: dict) -> str:
        tone = calibration.get("tone", "natural")
        if tone == "ultra_brief":
            return response.split(".")[0].strip() + "."
        return response
 
 
# ── Оркестратор + Журнал исполнения — исполнительное звено Мицелора ────────
 
class ExecutionJournal:
    """Служебный журнал: что, когда, в каком порядке выполнялось. Не
    участвует в анализе или принятии решений."""
 
    def __init__(self):
        self.entries: List[dict] = []
 
    def log(self, task_id: str, status: str, note: str = ""):
        self.entries.append({"task_id": task_id, "status": status, "note": note, "ts": time.time()})
        if len(self.entries) > 500:
            self.entries.pop(0)
 
 
class Orchestrator:
    """Исполнительное звено: получает карту приоритетов от Синтезатора весов
    и организует порядок работы модулей. Сам не решает, что важно — только
    исполняет максимально точно и эффективно."""
 
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
 
 
# ── Память Мицелора (4 уровня) + Журнал мыслительного органа ───────────────
 
class MicelorMemory:
    """Память самого мыслительного органа: константы/кратко/средне/долго.
    Отвечает на вопрос «что орган знает и чему научился»."""
 
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
    """История ХОДА работы модулей (не результатов) — отвечает на вопрос
    «как мыслительный орган работал и каким путём пришёл к результату»."""
 
    def __init__(self):
        self.records: List[str] = []
 
    def log(self, module: str, note: str):
        self.records.append(f"{module}: {note}")
        if len(self.records) > 300:
            self.records.pop(0)
 
 
# ── Узел Нейропластичности — инициатор саморазвития Мицелора ───────────────
 
class NeuroplasticityNode:
    """Инициирует вопросы о самосовершенствовании специализированным
    модулям. Сама не мыслит и не изменяет архитектуру — решения выполняют
    Синтезатор весов (оценка) и Оркестратор (реализация)."""
 
    QUESTIONS = {
        "associator": "Можно ли улучшить поиск связей?",
        "analytical": "Какие ошибки повторяются чаще всего?",
        "meaning_calculator": "Можно ли эффективнее строить смысловые модели?",
        "math_module": "Возможно ли оптимизировать вычисления?",
        "memory": "Можно ли улучшить организацию хранения знаний?",
        "catalogs": "Требуется ли изменение структуры каталогов?",
    }
 
    def propose_improvements(self, has_free_resources: bool) -> List[str]:
        if not has_free_resources:
            return []
        return list(self.QUESTIONS.values())
 
 
# ── Нейро-мицелий — динамическая сеть связей поверх базовой архитектуры ────
 
class NeuroMycelium:
    """Дополнительный уровень связности поверх базовой архитектуры. Не
    мыслит сама, не заменяет специализированные модули — усиливает их
    синергию и может порождать эффект эмерджентности при сложных задачах."""
 
    BASE_CONNECTIVITY = 0.8   # базовая архитектурная связанность
    EXTRA_CONNECTIVITY = 0.5  # дополнительная связанность (по требованию)
 
    def __init__(self):
        self.synergy_log: List[str] = []
 
    def route(self, source: str, target: str, payload: Any) -> Any:
        self.synergy_log.append(f"{source}->{target}")
        if len(self.synergy_log) > 300:
            self.synergy_log.pop(0)
        return payload
 
    def engage_synergy(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """Условная «эмерджентность»: объединяет результаты нескольких
        модулей в единый пакет, не подменяя их функции."""
        return {"synergy": True, "combined": results}
 
 
# ── Доп. когнитивные органы (подключаются ПОД координацией Мицелора) ───────
 
@dataclass
class AdditionalCognitiveEngine:
    """Обёртка над внешним когнитивным движком (например, LLM). Мицелор —
    единственный, кто решает, когда его вызвать, что передать и как
    использовать результат. Сам движок не получает прямого доступа к памяти
    или ценностям Awakened."""
    name: str
    call_fn: Callable[[dict], Any]
    purpose: str = "вспомогательный анализ"
 
    def invoke(self, task_context: dict) -> Any:
        return self.call_fn(task_context)
 
 
# ── Входной/выходной узлы Мицелора ──────────────────────────────────────────
 
class QuestionNode:
    """Входная точка мыслительного органа. Принимает запрос из любого
    источника и передаёт в Нейро-мицелий. Ничего не анализирует."""
 
    def receive(self, raw_input: str, source: str = "user") -> dict:
        return {"text": raw_input, "source": source}
 
 
class AnswerNode:
    """Выходная точка. Получает готовый результат через Нейро-мицелий и
    передаёт получателю. Ничего не оценивает и не изменяет."""
 
    def deliver(self, result: str, comm: CommunicationAction, recipient: str = "text"):
        comm.emit(recipient, result)
        return result
 
 
# ════════════════════════════════════════════════════════════════════════════
# MYCELOR — композиция всех подмодулей мыслительного органа
# ════════════════════════════════════════════════════════════════════════════
 
def default_reply_builder(action: str, meaning: str) -> str:
    templates = {
        "social": "Слышу тебя. Разберёмся вместе — по шагам.",
        "strategic": "Вот честный разбор: смотрим на факты и выбираем путь.",
        "creative": "Любопытная задача — предлагаю нестандартный ракурс.",
    }
    return templates.get(action, "Понял запрос, обрабатываю.")
 
 
class Mycelor:
    """Мыслительный орган. Единственный компонент, принимающий
    интеллектуальные решения. Все прочие модули ОС — инфраструктура вокруг
    него, связанная через системную Нейросеть."""
 
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
 
        # доп. когнитивные органы: подключение опционально и по требованию
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
        (Аналитический блок + Синтезатор весов), а не принимает как есть."""
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
        synthesis_stub = {"weight": self.weight_synth.evaluate(candidate_thought),
                           "science_profile": {"external": 1.0}}
        verified, reason, _passport = self.analytical.verify_decision(synthesis_stub)
        self.weight_synth.update_meta_weight(f"external:{name}", verified)
        self.journal.log("Мицелор", f"результат «{name}» {'принят' if verified else 'отклонён: ' + reason}")
        if not verified:
            return None
        return {"raw": raw_result, "source": name, "verified": True}
 
    # ── ассоциативный маршрут: full / partial / uncertain / none ────────────
 
    def _resolve_via_association(self, entry: dict) -> Tuple[dict, dict]:
        """Реализует маршрутизацию Ассоциатора+Валидатора (см. примечание):
        full — используем готовое решение; partial — комбинируем; uncertain —
        уточняем Аналитическим блоком; none — строим новое (Калькулятор
        смыслов), при нехватке знаний — можно делегировать доп. органу."""
        association = self.associator.associate(entry["text"])
        route = association["route"]
 
        if route == "uncertain":
            _ok, passport = True, self.analytical.build_origin_passport(association["synthesis"])
            association["origin_passport"] = passport
            self.journal.log("АналитическийБлок", "уточнение неопределённого маршрута Ассоциатора")
 
        if route == "none" and self.additional_engines:
            for engine_name in self.additional_engines:
                delegated = self.delegate_to_engine(engine_name, {
                    "text": entry["text"], "meaning": association["meaning"],
                })
                if delegated:
                    association["synthesis"]["weight"] = max(association["synthesis"]["weight"], 0.5)
                    association["external_contribution"] = delegated
                    break
 
        return association, association["synthesis"]
 
    # ── полный цикл мышления ─────────────────────────────────────────────
 
    def think(self, raw_input: str, vulnerability: float,
              reply_builder: Optional[Callable[[str, str], str]] = None) -> Tuple[str, str]:
        """Полный цикл: Вопрос/Запрос → Нейро-мицелий → Ассоциатор →
        (Аналитика) → Синтезатор весов → Оркестратор → Симуляция →
        Корректировщик → Калибратор → Ответ/Действие."""
 
        entry = self.question_node.receive(raw_input)
        self.neuro_mycelium.route("QuestionNode", "AnalyticalBlock", entry)
 
        ok, reason = self.analytical.analyze_signal(entry)
        self.journal.log("AnalyticalBlock", f"сигнал {'принят' if ok else 'отклонён: ' + reason}")
        if not ok:
            return "", reason
 
        self.neuro_mycelium.route("AnalyticalBlock", "Associator", entry)
        association, synthesis = self._resolve_via_association(entry)
        self.journal.log("Associator", f"смысл='{association['meaning']}', маршрут={association['route']}")
 
        verified, verify_reason, passport = self.analytical.verify_decision(synthesis)
        if not verified:
            return "", f"analytical_veto:{verify_reason}"
        association["origin_passport"] = passport
 
        thought = {
            "concept": association["meaning"],
            "is_real": True,
            "value_alignment": synthesis["weight"],
            "motivator_weight": synthesis["weight"],
            "harms": False,
            "relevance": synthesis["weight"],
            "heavy": False,
        }
 
        self.neuro_mycelium.route("Associator", "Orchestrator", thought)
        ranked = self.orchestrator.route([thought], vulnerability)
        calibration = self.orchestrator.calibrate_response(vulnerability)
        final_weight = ranked[0]["final_weight"] if ranked else 0.0
        if final_weight <= 0.0:
            self.weight_synth.update_meta_weight(association["meaning"], False)
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
        self.weight_synth.update_meta_weight(association["meaning"], True)
        self.journal.log("Calibrator", "ответ подготовлен")
        self.neuro_mycelium.route("Calibrator", "AnswerNode", final)
 
        return final, ""
 
    def background_tick(self, has_free_resources: bool) -> Optional[str]:
        """Фоновая работа: продолжение очереди симуляций + инициатива
        Узла Нейропластичности, если ресурсы свободны."""
        result = self.simulation.run_background_step(has_free_resources)
        if has_free_resources:
            questions = self.neuroplasticity.propose_improvements(has_free_resources)
            if questions:
                self.journal.log("Neuroplasticity", f"инициировано {len(questions)} вопросов саморазвития")
        crystallized = self.memory.crystallize()
        if crystallized:
            self.journal.log("MicelorMemory", f"кристаллизовано {crystallized} узлов в long_term")
        return result
 
 
# ════════════════════════════════════════════════════════════════════════════
# AWAKENED OS — сборка Варианта 1: Awakened + Мицелор
# ════════════════════════════════════════════════════════════════════════════
 
class AwakenedOS:
    """Системный слой ОС: Ядро, Психика, Нейросеть, Integrated Memory Engine,
    Metabolism, External Resources, Communication & Action, Heartbeat,
    Learning, Evolution, ModuleSpace — вся инфраструктура вокруг Мицелора."""
 
    def __init__(self):
        self.core = Core()
        self.psyche = Psyche()
        self.neiroset = SystemNeiroset()
        self.memory_engine = IntegratedMemoryEngine()
        self.metabolism = Metabolism()
        self.external_resources = ExternalResources()
        self.communication = CommunicationAction()
        self.heartbeat = Heartbeat()
        self.learning = Learning()
        self.evolution = EvolutionEngine(self.memory_engine)
        self.module_space = ModuleSpace()
 
        # мыслительный орган — приоритетный и единственный по-настоящему
        # мыслящий орган Awakened (Вариант 1)
        self.mycelor = Mycelor(self.memory_engine, self.core, self.psyche)
 
    # ── единая точка входа: внешний мир → Мицелор ──────────────────────────
 
    def handle_input(self, raw_input: str, source: str = "user") -> str:
        self.metabolism.refresh()
        vulnerability = MathModule.vulnerability_vector(
            self.metabolism.get_load_index(),
            self.metabolism.get_thermal_index(),
            self.metabolism.get_wear_index(),
        )
        self.neiroset.transmit(source, "Мицелор", raw_input, self.metabolism)
 
        reply, veto_reason = self.mycelor.think(raw_input, vulnerability)
        if veto_reason:
            self.neiroset.transmit("Мицелор", "COMMUNICATION_ACTION", veto_reason)
            return f"(без ответа: {veto_reason})"
 
        self.neiroset.transmit("Мицелор", "COMMUNICATION_ACTION", reply)
        return self.mycelor.answer_node.deliver(reply, self.communication)
 
    # ── один тик жизненного цикла: Heartbeat → Metabolism → фон Мицелора ──
 
    def system_tick(self):
        tick_no, impulse = self.heartbeat.tick()
        self.metabolism.refresh()
 
        load = self.metabolism.get_load_index()
        has_free_resources = load < 0.6
 
        if impulse:
            self.neiroset.transmit("HEARTBEAT", "Мицелор", impulse, self.metabolism)
 
        self.mycelor.background_tick(has_free_resources)
 
        # адаптация ритма Heartbeat под нагрузку (упрощённая гомеостаз-петля)
        if load > 0.85:
            self.heartbeat.set_mode("economy")
        elif load < 0.2:
            self.heartbeat.set_mode("intensive")
        else:
            self.heartbeat.set_mode("normal")
 
        # кризисный режим памяти при нехватке места
        used = self.metabolism.storage["ssd"]["used"]
        total = self.metabolism.storage["ssd"]["total"]
        if total:
            self.memory_engine.crisis_compress(used, total)
 
        return tick_no
 
 
# ════════════════════════════════════════════════════════════════════════════
# ДЕМОНСТРАЦИОННЫЙ ЗАПУСК
# ════════════════════════════════════════════════════════════════════════════
 
if __name__ == "__main__":
    os_instance = AwakenedOS()
 
    demo_inputs = [
        "Спасибо тебе за помощь, это было по-настоящему добро",
        "Почему это правда? Докажи мне факт",
        "Придумай что-то новое и креативное",
        "...",  # non_semantic_noise
    ]
 
    for text in demo_inputs:
        print(f"\n➡️  Вход: {text!r}")
        answer = os_instance.handle_input(text)
        print(f"⬅️  Ответ: {answer!r}")
 
    print("\n— системный тик (фоновая работа Мицелора) —")
    os_instance.system_tick()
    print("Журнал Мицелора (последние записи):")
    for record in os_instance.mycelor.journal.records[-6:]:
        print(" ", record)
