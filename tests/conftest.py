import numpy as np
import pytest

from cicd_demo.src import Assassin


@pytest.fixture
def test_assassin1():
    return Assassin(
        name="Xiao",
        hp=np.random.randint(1000, 2000),
        damage=np.random.randint(30, 50),
        crit_rate=np.random.rand(1),
        crit_dmg=np.random.randint(50, 2 * 100),
    )


@pytest.fixture
def test_assassin2():
    return Assassin(name="Test Assassin", hp=100, damage=10, crit_rate=0.5, crit_dmg=20)


@pytest.fixture
def test_target1():
    return Assassin(
        name="Keli",
        hp=np.random.randint(1000, 2000),
        damage=np.random.randint(30, 50),
    )
