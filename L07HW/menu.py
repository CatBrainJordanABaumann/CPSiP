# Basic somewhat generic TUI menu
class Menu:
    _options: list[str]

    # Empty Constructor that initializes a menu with no options to choose between
    def __init__(self):
        self._options = []

    # Adds an option that the user can choose
    def addOption(self, option: str):
        self._options.append(option)
    
    # Asks the user for which option in the menu they want
    # If user enters invalidly then reprompts indefinitely
    # Returns the index of the option desired
    def getInput(self) -> int:
        result = 0
        while True:
            for i, option in enumerate(self._options):
                print(i + 1, option)
            try:
                result = int(input(""))
                if result > 0 and result <= len(self._options):
                    return result
                print("Invalid index")
            except:
                print("Invalid input")