
# self this olayı ile aynıdır . class içinde kullanılırken bir parametre alması lazım o yüzden self kullanılır parametre vermek istemsek de 

class Human:
    name = "halit"
    # built-in
    def __init__(self,name):
        self.name =name
        print(f"ben bir {self.name} adlı bir insanım")
    def __str__(self) -> str:
        return f"STR fonksiyonundan dönen değer: {self.name}"

    def talk(self,sentence):
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking")

human1 = Human("eren")
human1.talk("merhaba")
human1.walk()

print(human1)

human2 = Human("yaprak")
human2.talk("timam")
human2.walk()

