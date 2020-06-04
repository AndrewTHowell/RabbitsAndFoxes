import random


class Animal:
    __health: float
    maxHealth = 100.
    hungerDamage = 5.

    __foodLevel: float
    maxFoodLevel = 100.
    foodLevelExpelledPerDay = 5.
    hungerLevel = maxFoodLevel / 5

    actions = {"locateFood"}

    def __init__(self):
        self.__health = Animal.maxHealth
        self.__foodLevel = Animal.maxFoodLevel

        self.__actions = Animal.actions

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
    def act(self) -> None:
        action = random.choice(self.actions)

        if action == "locateFood":
            # self.moveTowardsFood()
            pass

    # Every time step:
    def step(self):
        if self.alive:
            self.hunger(Animal.foodLevelExpelledPerDay)

            if self.hungry:
                self.damage(Animal.hungerDamage)

        if self.alive:
            self.act()
