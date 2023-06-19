from abc import ABC
from abc import abstractmethod


class Character(ABC):
    def __init__(
        self,
        name: str,
        hp: int,
    ) -> None:
        self.name = name
        self.hp = hp

    def __str__(self) -> None:
        return f"{self.name} ({self.hp} HP)"

    @abstractmethod
    def attack(self, target: "Character") -> float:
        pass

    @abstractmethod
    def get_damage(self, damage: float) -> None:
        pass

    def get_name(self) -> str:
        return self.name

    def get_hp(self) -> float:
        return self.hp

    def is_alive(self) -> bool:
        return self.hp > 0
