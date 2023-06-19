from cicd_demo.src import Assassin


def test_assassin_instantiation(test_assassin1):
    assert isinstance(test_assassin1, Assassin)
    assert hasattr(test_assassin1, "name")
    assert hasattr(test_assassin1, "hp")
    assert hasattr(test_assassin1, "damage")
    assert hasattr(test_assassin1, "crit_rate")
    assert hasattr(test_assassin1, "crit_dmg")


def test_assassin_attack_v1(test_assassin1, test_target1):
    assert isinstance(test_target1, Assassin)
    initial_hp = test_target1.hp
    dmg = test_assassin1.attack(test_target1)
    assert test_target1.hp == initial_hp - dmg


def test_assassin_attack_v2(test_assassin2):
    target = Assassin("Target", 100, 0)
    damage_dealt = test_assassin2.attack(target)
    assert target.hp == 80  # Target's HP should be reduced by 20 (10 + 20 * 0.5)
    assert damage_dealt == 20  # Damage dealt should be equal to 20


def test_assassin_attack_no_crit(test_assassin2):
    target = Assassin("Target", 100, 10, 0, 0)
    damage_dealt = target.attack(test_assassin2)
    assert test_assassin2.hp == 90  # Target's HP should be reduced by 10 (damage value)
    assert damage_dealt == 10  # Damage dealt should be equal to 10


def test_assassin_get_damage(test_assassin2):
    test_assassin2.get_damage(50)
    assert test_assassin2.hp == 50  # Assassin's HP should be reduced by 50


def test_assassin_get_damage_fatal(test_assassin2):
    test_assassin2.get_damage(200)
    assert test_assassin2.hp == 0  # Assassin's HP should be reduced to 0


def test_assassin_get_damage_no_damage(test_assassin2):
    test_assassin2.get_damage(0)
    assert test_assassin2.hp == 100  # Assassin's HP should remain unchanged


def test_assassin_get_damage_negative_damage(test_assassin2):
    test_assassin2.get_damage(-10)
    assert test_assassin2.hp == 100  # Assassin's HP should remain unchanged
