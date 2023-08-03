import unittest

from army import Army
from unit import Unit
from model import Model
from weapon import Weapon

class TestClassCreation(unittest.TestCase):

    def test_army(self):

        army = Army("2K orks", 2000)
        self.assertEqual(army.name, "2K orks")
        self.assertEqual(army.units, [])

    def test_unit(self):

        unit = Unit("WARBOSS")
        self.assertEqual(unit.name, "WARBOSS")
        self.assertEqual(unit.models, [])

    def test_model(self):

        model = Model("Weirdboy", 6, 5, 5, 4, 7, 1)
        self.assertEqual(model.toughness, 5)
        self.assertEqual(model.weapons, [])

    def test_weapon(self):

        weapon = Weapon("big shoota", "ranged", 3, 4, 5, 0, 1)
        self.assertEqual(weapon.strength, 5)

class TestClassMethods(unittest.TestCase):

    def test_add_weapon(self):

        model = Model("Weirdboy", 6, 5, 5, 4, 7, 1)
        weapon = Weapon("big shoota", "ranged", 3, 4, 5, 0, 1)
        model.add_weapon(weapon)
        self.assertIn(weapon, model.weapons)

if __name__ == '__main__':
    unittest.main()