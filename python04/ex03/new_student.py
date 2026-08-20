import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random 15-character lowercase identifier."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Dataclass representing a student with automated login and ID."""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """Initialize computed fields after dataclass creation."""
        self.login = self.name[0] + self.surname
