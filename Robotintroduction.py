class Robot:
    # Constructor to initialize the robot's name
    def __init__(self, name):
        self.name = name

    # Method to introduce the robot
    def introduce(self):
        print(f"Hello! My name is {self.name}.")

# Creating two Robot objects: Tom and Jerry
robot1 = Robot("Tom")
robot2 = Robot("Jerry")

# Calling the introduce method for both robots
robot1.introduce()
robot2.introduce()
