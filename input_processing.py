# input_processing.py
# Edmund Yu, ENSF 692 Spring 2025
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.).
# You may import any modules from the standard Python library.
# Remember to include your name and comments.


# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:
    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    # The initial default values are a green traffic light, no pedestrian, and no vehicle.
    def __init__(self):
        self.light = "green"
        self.pedestrian = "no"
        self.vehicle = "no"

        """
        Purpose:
            Modifies the internal state of the Sensor object according to the provided condition and status.
            Prints an error message if an invalid condition or status is provided.
        Args:
            condition (int): The type of status to update.
                - 1: Update the traffic light status.
                - 2: Update the pedestrian status.
                - 3: Update the vehicle status.
            status (str): The new status value to set.
                - For condition 1: "green", "yellow", or "red".
                - For condition 2 and 3: "yes" or "no".
        Returns:
            None
        """

    def update_status(
        self, condition, status
    ):  # You may decide how to implement the arguments for this function
        match condition:
            case 1:
                if status == "green":
                    self.light = "green"
                elif status == "yellow":
                    self.light = "yellow"
                elif status == "red":
                    self.light = "red"
                else:
                    print("Invalid vision change. \n")
            case 2:
                if status == "yes":
                    self.pedestrian = "yes"
                elif status == "no":
                    self.pedestrian = "no"
                else:
                    print("Invalid vision change. \n")
            case 3:
                if status == "yes":
                    self.vehicle = "yes"
                elif status == "no":
                    self.vehicle = "no"
                else:
                    print("Invalid vision change. \n")
            case _:
                print("Invalid condition \n")


# The sensor object should be passed to this function to print the action message and current status
"""
    Purpose:
        Prints an action message (Proceed, Caution, or STOP) based on the current state of the sensor object.
        Also prints the current status of the traffic light, pedestrian, and vehicle detection.
    Args:
        sensor (Sensor): An instance of the Sensor class containing the current detection statuses.
    Returns:
        None
"""


def print_message(sensor):
    if sensor.light == "red" or sensor.pedestrian == "yes" or sensor.vehicle == "yes":
        print("\n")
        print("STOP\n")
    elif (
        sensor.light == "yellow"
        and sensor.pedestrian == "no"
        and sensor.vehicle == "no"
    ):
        print("\n")
        print("Caution\n")
    elif (
        sensor.light == "green" and sensor.pedestrian == "no" and sensor.vehicle == "no"
    ):
        print("\n")
        print("Proceed\n")
    print(
        f"Light = {sensor.light}, Pedestrian = {sensor.pedestrian}, Vehicle = {sensor.vehicle}. \n"
    )


# Complete the main function below
"""
Purpose:
    Orchestrates the Car Vision Detector menu loop, handles user input and
    delegates status updates to Sensor, then prints action messages.
Args:
    None
Returns:
    None
"""


def main():
    s = Sensor()
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    running = True

    while running:
        print("Are changes detected in the vision input?")
        userInput = input(
            "Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program:"
        )
        try:
            userInputInt = int(userInput)
        except ValueError:
            print("You must select either 1, 2, 3, or 0.\n")
            continue

        match userInputInt:
            case 1:
                change = input("What change has been identified?: ")
                s.update_status(userInputInt, change)
                print_message(s)
            case 2:
                change = input("What change has been identified?: ")
                s.update_status(userInputInt, change)
                print_message(s)
            case 3:
                change = input("What change has been identified?: ")
                s.update_status(userInputInt, change)
                print_message(s)
            case 0:
                print("Exiting program.\n")
                running = False

            case _:
                print("Invalid Selection. \n")


# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == "__main__":
    main()
