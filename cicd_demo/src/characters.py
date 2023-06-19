from typing import Optional

from cicd_demo.src import Character


class Assassin(Character):
    def __init__(
        self,
        name: str,
        hp: int,
        damage: int,
        crit_rate: Optional[float] = 0,
        crit_dmg: Optional[int] = 0,
    ) -> None:
        super().__init__(name, hp)
        self.damage = damage
        self.crit_rate = crit_rate
        self.crit_dmg = crit_dmg

    def attack(self, target) -> float:
        if self.crit_rate:
            total_dmg = self.damage + self.crit_dmg * self.crit_rate
        else:
            total_dmg = self.damage
        target.hp -= total_dmg
        print(f"{self.name} attacked {target.name} for {total_dmg} damage")
        return total_dmg

    def get_damage(self, damage):
        if damage <= 0:
            print("Missed!")
        elif self.hp < damage:
            self.hp = 0
            print(f"{self.name} died T.T")
        else:
            self.hp -= damage
            print(f"{self.name} ook {damage} damage!")
