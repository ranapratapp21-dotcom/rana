# Music Instrument Sound Show (ACP starter, DSCM2L5). Python 3 standard library only.
# Run it in Google Colab (one cell) or as instrument_sound_show.py. It runs now; do TODO 1 to TODO 4 in order.
# Lines marked (given) are done for you.
from abc import ABC, abstractmethod
import inspect


class Instrument(ABC):                   # (given) A: the parent class; (ABC) lets Python enforce abstract methods
    def __init__(self, name, family):
        self.name = name
        self.family = family

    def display_info(self):              # (given) B: inherited by every instrument
        print(f"{self.name} ({self.family})")

    # TODO 1: on a new line directly above def play_sound(self):
    #   (below these comments), add the decorator from the abc module that marks a
    #   method as abstract.
    #   Check: "Is Instrument abstract? True".
    def play_sound(self):                # (given) every child writes its own sound
        pass


class Guitar(Instrument):
    def __init__(self, name, family, strings):
        # TODO 2: call super().__init__ for name and family,
        #   then store strings.
        #   Check: "Acoustic Guitar (String)" instead of "(unknown)".
        self.name = name  # (given) placeholder: replace this line
        self.family = "unknown"  # (given) placeholder: replace this line
        self.strings = "?"  # (given) placeholder: replace this line

    def play_sound(self):                # (given) C
        print(f"{self.strings} strings go: Strum strum!")


class Tabla(Instrument):
    def __init__(self, name, family, drums):          # (given) the direct way, for comparison
        Instrument.__init__(self, name, family)
        self.drums = drums

    def play_sound(self):
        # TODO 3: print how many drums it has, then "go: Dha dhin dhin dha!".
        #   Check: "2 drums go: Dha dhin dhin dha!".
        print("(no sound yet)")  # (given) placeholder: replace this line


band = [Guitar("Acoustic Guitar", "String", 6), Tabla("Tabla", "Percussion", 2)]   # (given) D
# TODO 4: loop over band and call display_info() then play_sound() on each.
#   Check: four lines, the name line then the sound line for each instrument.
print("The show has not started yet.")  # (given) placeholder: replace this line
print("Is Instrument abstract?", inspect.isabstract(Instrument))
