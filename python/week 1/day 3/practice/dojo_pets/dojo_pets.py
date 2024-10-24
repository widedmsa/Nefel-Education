class Ninja: 
    def __init__( self,first_name , last_name , treats , pet_food , pet ):
        self.first_name=first_name
        self.last_name=last_name
        self.treats=treats
        self.pet_food=pet_food
        self.pet=pet


    def walk(self) :
        self.pet.play()
        return self

    def feed(self) :
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self 





class Pet:
    def __init__( self,name , type , tricks,health,energy ):
        self.name = name
        self.type= type 
        self.tricks = tricks 
        self.health=health
        self.energy=energy



    def sleep (self) :
        self.energy += 25 
        print(f" {self.name}'s energy is increased by 25")
        return self


    def eat (self) :
        self.energy +=5 
        self.health += 10 
        print(f"{self.name}'s energy is increased by 5 and {self.name}'s health is increased by 10")
        return self


    def play(self) :
        self.health += 5 
        print(f"{self.name}'s health is increased by 5")
        return self


    def noise(self) :
        print(f"{self.name} is barking")
        return self

pet1 = Pet("Buddy", "Dog", "Roll over", 100, 80)
ninja1=Ninja("wided","msakem","gentle","meat", pet1)
ninja1.feed().walk().bathe()

