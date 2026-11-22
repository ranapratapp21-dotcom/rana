# My Pet Care Dashboard (ACP starter, DSCM2L6). Python 3 standard library only.
# Run it in Google Colab (one cell) or as pet_care_dashboard.py. It runs now; do TODO 1 to TODO 4 in order.
# Lines marked (given) are done for you.


class Pet:                               # (given) A: the parent class
    def __init__(self, name, health):
        self.name = name
        self.__health = 50               # private: stored as _Pet__health
        self.set_health(health)

    def get_health(self):
        return self.__health

    def set_health(self, value):
        # TODO 1: set ok to True only when value is an int from 0 to 100.
        #   Check: "Snowy: health must be a whole number from 0 to 100, not 120." and health 50.
        ok = True  # (given) placeholder: replace this line
        if ok:                           # (given) B
            self.__health = value
        else:
            print(f"{self.name}: health must be a whole number from 0 to 100, not {value!r}.")

    def show_info(self):                 # (given) C
        print(f"{self.name}: health {self.get_health()}")

    def care_action(self):
        print(f"{self.name} needs general care.")


class Dog(Pet):                          # (given) D: a worked example of overriding
    def care_action(self):
        print(f"{self.name} needs a walk and playtime.")


class Cat(Pet):
    def care_action(self):
        # TODO 2: print the name and "needs brushing and a quiet nap.".
        #   Check: "Misty needs brushing and a quiet nap.".
        super().care_action()  # (given) placeholder: replace this line


class Rabbit(Pet):
    def care_action(self):
        # TODO 3: print the name and "needs hay and a clean hutch.".
        #   Check: "Snowy needs hay and a clean hutch.".
        super().care_action()  # (given) placeholder: replace this line


pets = [Dog("Buddy", 85), Cat("Misty", 75), Rabbit("Snowy", 120)]   # (given) E: 120 is too high
# TODO 4: loop over pets and call show_info() then care_action().
#   Check: six lines, two for each pet.
print("Dashboard loop not written yet.")  # (given) placeholder: replace this line
pets[0].set_health(90)                   # (given) F: valid and invalid updates
pets[1].set_health("high")
print("Buddy now has health", pets[0].get_health())
