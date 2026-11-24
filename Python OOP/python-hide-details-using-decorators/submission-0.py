class SuperHero:
    def __init__(self, name: str, health: int, power_level: int):
        self.name = name
        self.__health = health
        self.__power_level = power_level
        # TODO: Add the private attributes
    
    # TODO: Add the getter and setter methods
    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self,value):

        if 0<= value <=100:
            self.__health = value
        
        else:
            if value < 0:
                print("You can't set the health to less than 0")

            if value > 100:
                print("You can't set the health to more than 100")

    @property
    def power_level(self):
        return self.__power_level

    @power_level.setter
    def power_level(self,value):

        if 1<= value <=10:
            self.__power_level = value

        
        else:
            if value < 1:
                print("You can't set the power level to less than 1")

            else:
               
                print("You can't set the power level to more than 10")
        




super_hero = SuperHero("Batman", 80, 9)

print(super_hero.health) # this should print 80
super_hero.health = 110 # this should print You can't set the health to more than 100
super_hero.health =80 

print(super_hero.power_level) # this should print 9
super_hero.power_level = 11 # this should print You can't set the power level to more than 10
super_hero.power_level= 0 # this should print You can't set the power level to less than 1
super_hero.power_level = 9
# TODO: print the hero's attributes

print(f'{super_hero.name} has {super_hero.health} health and {super_hero.power_level} power level')
