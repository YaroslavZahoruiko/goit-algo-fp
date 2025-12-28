from abc import ABC
import uuid
from typing import Optional


class BaseNode(ABC):
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.left: Optional[BaseNode] = None
        self.right: Optional[BaseNode] = None
