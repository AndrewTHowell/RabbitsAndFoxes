from unittest import TestCase

from Simulation import Animal


class TestAnimal(TestCase):
    def setUp(self):
        self.animal = Animal()


class TestInit(TestAnimal):
    def test_initial_health(self):
        self.assertEqual(Animal.maxHealth, self.animal.health)

    def test_initial_foodLevel(self):
        self.assertEqual(Animal.maxFoodLevel, self.animal.foodLevel)


class TestHealth(TestAnimal):
    def test_damage(self):
        initialHealth = self.animal.health
        self.animal.damage(5)
        self.assertEqual(self.animal.health, initialHealth - 5)

    def test_multiple_damage(self):
        initialHealth = self.animal.health
        for _ in range(3):
            self.animal.damage(5)
        self.assertEqual(self.animal.health, initialHealth - (3 * 5))

    def test_damage_below_zero(self):
        self.animal.damage(105)
        self.assertEqual(self.animal.health, 0)

    def test_heal(self):
        self.animal.damage(5)
        initialHealth = self.animal.health
        self.animal.heal(5)
        self.assertEqual(self.animal.health, initialHealth + 5)

    def test_multiple_heal(self):
        self.animal.damage(15)
        initialHealth = self.animal.health
        for _ in range(3):
            self.animal.heal(5)
        self.assertEqual(self.animal.health, initialHealth + (3 * 5))

    def test_heal_above_max(self):
        self.animal.heal(5)
        self.assertEqual(self.animal.health, Animal.maxHealth)

    def test_alive(self):
        self.assertEqual(True, self.animal.alive)

    def test_alive_after_damage(self):
        self.animal.damage(Animal.maxHealth + 5)
        self.assertEqual(False, self.animal.alive)


class TestFoodLevel(TestAnimal):
    def test_hunger(self):
        initialFoodLevel = self.animal.foodLevel
        self.animal.hunger(5)
        self.assertEqual(self.animal.foodLevel, initialFoodLevel - 5)

    def test_multiple_hunger(self):
        initialFoodLevel = self.animal.foodLevel
        for _ in range(3):
            self.animal.hunger(5)
        self.assertEqual(self.animal.foodLevel, initialFoodLevel - (3 * 5))

    def test_hunger_below_zero(self):
        self.animal.hunger(105)
        self.assertEqual(self.animal.foodLevel, 0)

    def test_eat(self):
        print(self.animal.foodLevel)
        self.animal.hunger(5)
        initialFoodLevel = self.animal.foodLevel
        print(self.animal.foodLevel)
        self.animal.eat(5)
        print(self.animal.foodLevel)
        self.assertEqual(self.animal.foodLevel, initialFoodLevel + 5)

    def test_multiple_eat(self):
        self.animal.hunger(15)
        initialFoodLevel = self.animal.foodLevel
        for _ in range(3):
            self.animal.eat(5)
        self.assertEqual(self.animal.foodLevel, initialFoodLevel + (3 * 5))

    def test_eat_above_max(self):
        self.animal.eat(5)
        self.assertEqual(self.animal.foodLevel, Animal.maxHealth)

    def test_hungry(self):
        self.assertEqual(False, self.animal.hungry)

    def test_hungry_after_hunger(self):
        self.animal.hunger(Animal.maxFoodLevel + 5)
        self.assertEqual(True, self.animal.hungry)