from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Event:
    event_id: str
    event_date: str