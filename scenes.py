from random import randint


class Scene(object):

    def enter(self):
        print("Scene ikke konfigurert.")

        return True
class DørTerskel(Scene):
    
    def enter(self):
        print("Dette er DørTerskel")

        return True

class SykkelTur(Scene):
    
    def enter(self):
        print("Dette er SykkelTur")

        return True
class Kasjotten(Scene):
    
    def enter(self):
        print("Dette er Kasjotten")

        politikamp = Fight("spiller", "Politiet")
        politikamp.fight()
        return True
        
        
class Sagelva(Scene):
    
    def enter(self):
        print("Dette er Sagelva")

        return True
class NitElvBrua(Scene):
    
    def enter(self):
        print("Dette er NitElvBrua")

        return True

class Ferdig(Scene):
    
    def enter(self):
        print("Dette er Ferdig")
class entity(object):
    def __init__(self, name, weapon = None):
        self.name = name
        self.weapon = weapon

        
class Fight(object):
    
    def __init__(self, hero, enemy):
        self.hero = entity(hero)
        self.enemy = entity(enemy)

    def fight(self):
        print(f"Slåsskamp mellom {self.hero.name} and {self.enemy.name}!")

        weapons = {11:"spoon", 10:"Lightsaber", 9:"Railgun", 
        8:"Super-Ultra-Mega-Blaster", 7:"Blaster",
        6: "AK-47", 5:"Revolver", 4: "Sword", 3: "Dagger",
        2:"Kitchen knife", 1:"Stick"}

        print("You shalt now engage in fight.\nYou pull  out your best weapon from your back pocket.")
        w1index = randint(1, 11)
        w2index = randint(1, 11)

        self.hero.weapon = weapons.get(w1index)
        self.enemy.weapon = weapons.get(w2index)

        print(f"You got a {self.hero.weapon}, your opponent has a {self.enemy.weapon}!")
        if w1index - w2index <= 2 and w1index - w2index >= -2:
            print("You have pretty similar weapons. What do do?")
            print("Options: \"shoot\", \"dodge\", \"pray to the almighty flying spaghettimonster\".\nWhat do you do?")
            action = input(">>>")

            if "shoot" in action:
                print("You miss your enemy and it shoots you.")
                return 'death'
            elif "dodge" in action:
                print("You dodge and you get shot.")
                return 'death'
            elif "pray" in action:
                print("Nice move! Through a long series of unlikely events you have won!")
                return 'win'
        elif w1index > w2index:
            print("You have a far superior weapon, you win!")
            return 'win'
        elif w2index > w1index:
            print("You have a far inferior weapon. You lose.")
            return 'death'


scene_list = ["DørTerskel", "SykkelTur", "Kasjotten", "Sagelva", "NitElvBrua", "Ferdig"]

scene_dict = {0 : DørTerskel(), 1 : SykkelTur(), 2 : Kasjotten(), 3 : Sagelva(), 4 : NitElvBrua(), 5 : Ferdig()}
