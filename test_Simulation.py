from unittest import TestCase

from Simulation import Animal


THOROUGHTESTING: bool = False


class TestAnimal(TestCase):
    def setUp(self):
        self.animal = Animal()


class TestInit(TestAnimal):
    def test_initial_health(self):
        self.assertEqual(Animal.maxHealth, self.animal.health)

    def test_initial_foodLevel(self):
        self.assertEqual(Animal.maxFoodLevel, self.animal.foodLevel)

    def test_all_actions_are_callable(self):
        for action in self.animal.actions:
            self.assertEqual(True, callable(getattr(self.animal, action, None)))

    def test_initial_gender(self):
        self.assertIn(self.animal.gender, ["male", "female"])

    def test_settable_gender(self):
        maleAnimal = Animal(male=True)
        femaleAnimal = Animal(male=False)
        self.assertEqual("male", maleAnimal.gender)
        self.assertEqual("female", femaleAnimal.gender)

    def test_initial_age(self):
        self.assertEqual(0, self.animal.age)


class TestAge(TestAnimal):
    def test_age_increases_with_days(self):
        age = self.animal.age
        self.animal.simulateDay()
        self.assertEqual(age + 1, self.animal.age)

    def test_age_in_years(self):
        newAnimal = Animal()
        newAnimal.simulateDay()
        self.assertEqual(newAnimal.age/365, newAnimal.ageInYears)

    # This is a LONG test (~320ms) - only activated when THOROUGH is True
    def test_animal_eventually_dies_from_natural_causes(self):
        self.assertEqual(True, self.animal.alive)
        if THOROUGHTESTING:
            # Test over double the years of the animal's life expectancy (by then animal must be dead)
            for year in range(2 * Animal.lifeExpectancyYears):
                for day in range(365):
                    # Age the animal
                    self.animal.simulateDay()
                    # Feed the animal so it can't die from hunger
                    self.animal.eat(Animal.foodLevelExpelledPerDay)
    
            self.assertEqual(False, self.animal.alive)


class TestGender(TestAnimal):
    def test_compatible_mates(self):
        maleAnimal = Animal(male=True)
        femaleAnimal = Animal(male=False)
        self.assertEqual(True, maleAnimal.sexuallyCompatible(femaleAnimal))

    def test_incompatible_mates(self):
        maleAnimal1 = Animal(male=True)
        maleAnimal2 = Animal(male=True)
        femaleAnimal1 = Animal(male=False)
        femaleAnimal2 = Animal(male=False)
        self.assertEqual(False, maleAnimal1.sexuallyCompatible(maleAnimal2))
        self.assertEqual(False, femaleAnimal1.sexuallyCompatible(femaleAnimal2))

    def test_self_incompatibility(self):
        self.assertEqual(False, self.animal.sexuallyCompatible(self.animal))


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
        self.animal.hunger(5)
        initialFoodLevel = self.animal.foodLevel
        self.animal.eat(5)
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