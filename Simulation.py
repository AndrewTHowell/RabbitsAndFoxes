import random
from scipy.stats import norm


class Animal:
    ID: int
    ID = 1

    __gender: str

    __age: int
    # Arbitrary params that give rough mortality averaged around 10 years of life
    lifeExpectancyYears = 10 * 2
    deviationYears = 3
    mortalityDistribution = norm(lifeExpectancyYears * 365, deviationYears * 365)

    __health: float
    maxHealth = 100.
    hungerDamage = 5.

    __foodLevel: float
    maxFoodLevel = 100.
    foodLevelExpelledPerDay = 5.
    hungerLevel = maxFoodLevel / 5

    __actions: list
    potentialActions = ["seekFood", "seekMate", "wander", "flee"]

    def __init__(self, male=None):
        self.ID = Animal.ID
        Animal.ID += 1

        if male is None:
            self.__gender = random.choice(["male", "female"])
        elif male:
            self.__gender = "male"
        elif not male:
            self.__gender = "female"
        else:
            self.__gender = random.choice(["male", "female"])

        self.__age = 0

        self.__health = Animal.maxHealth
        self.__foodLevel = Animal.maxFoodLevel

        # Inherit all actions from Animal class for which this animal has callable methods for
        self.__actions = [action for action in Animal.potentialActions if callable(getattr(self, action, None))]

    def report(self) -> None:
        print(f"\nAnimal {self.ID}:")
        print(f"Age: {self.age}")
        print(f"Health: {self.health}")
        print(f"Hungry: {self.hungry}")
        print(f"Food Level: {self.foodLevel}")

    # Gender Methods
    @property
    def gender(self):
        return self.__gender

    def sexuallyCompatible(self, potentialMate):
        return potentialMate.gender != self.__gender and self != potentialMate

    # Age methods
    @property
    def age(self):
        return self.__age

    @property
    def ageInYears(self):
        return self.__age / 365

    def ageDeath(self):
        # Probability that the animal will die
        probabilityDeath = Animal.mortalityDistribution.cdf(self.age)

        if random.random() <= probabilityDeath:
            self.__health = 0

    # Health Methods
    @property
    def health(self) -> float:
        return self.__health

    @property
    def alive(self) -> bool:
        return self.__health > 0

    def damage(self, amount: float) -> None:
        # Reduce health by amount, not going below 0
        self.__health = max(0., self.__health - amount)

    def heal(self, amount: float) -> None:
        # Increase health by amount, not going above animal's maximum health
        self.__health = min(Animal.maxHealth, self.__health + amount)

    # Food Level Methods
    @property
    def foodLevel(self) -> float:
        return self.__foodLevel

    @property
    def hungry(self) -> bool:
        return self.__foodLevel <= Animal.hungerLevel

    def hunger(self, amount: float) -> None:
        # Reduce food level by amount, not going below 0
        self.__foodLevel = max(0., self.__foodLevel - amount)

    def eat(self, amount: float) -> None:
        # Increase food level by amount, not going above animal's maximum food level
        self.__foodLevel = min(Animal.maxFoodLevel, self.__foodLevel + amount)

    # Action Methods
    @property
    def actions(self) -> list:
        return self.__actions

    def act(self) -> None:
        actionFunction = random.choice(self.__actions)

        # Call the actionFunction
        eval("self." + actionFunction + "()")

    def seek(self, targetLocation):
        # TODO - Add seek functionality
        pass

    def seekFood(self):
        # TODO - Choose nearest food source
        nearestFoodSource = None
        self.seek(nearestFoodSource)

    def seekMate(self):
        # TODO - Choose nearest suitable mate
        nearestSuitableMate = None
        self.seek(nearestSuitableMate)

    def wander(self):
        # TODO - Choose random position on the play space
        randomLocation = None
        self.seek(randomLocation)

    # Every time step:
    def simulateDay(self):
        if self.alive:
            # Check if it should die naturally
            self.ageDeath()

            self.hunger(Animal.foodLevelExpelledPerDay)

            if self.hungry:
                self.damage(Animal.hungerDamage)
                pass

        if self.alive:
            self.act()
            self.__age += 1


if __name__ == "__main__":
    numAnimals = 2

    animals = []
    for _ in range(numAnimals):
        animals.append(Animal())

    # Run the simulation
    for animal in animals:
        animal.simulateDay()
        animal.report()
