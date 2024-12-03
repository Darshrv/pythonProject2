class Dog:
    #A
    name=None
    breed=None
    height=None
    weight=None


    def __init__(self,chow,breed):
        print("PC")
        self.name=chow
        self.breed=breed

     #B
    def bark(self):
        print("Barking")
    def sleep(self):
        print("sleep")
    def talk(self):
        pass


#object Ref
chow_ref=Dog("chow","mastiff")
mow_ref=Dog("mow","husky")

print(chow_ref.name)
print(mow_ref.name)