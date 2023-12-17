# Define a 'User' class
class User:
    def __init__(self, name, role) -> None:
        self.name = name
        self.role = role

    def printName(self):
        print("Name = " + self.name)

    def printRole(self):
        print("Role = " + self.role)

# Define a 'UserSettings' class
class UserSettings:
    def __init__(self, bgColor, fontSize) -> None:
        self.bgColor = bgColor
        self.fontSize = fontSize

    def setBgColor(self, newBgColor):
        self.bgColor = newBgColor

    def setFontSize(self, newFontSize):
        self.fontSize = newFontSize

# Define an 'AdminUser' class that inherits from both 'User' and 'UserSettings'
class AdminUser(User, UserSettings):
    def __init__(self, name, role, bgColor, fontSize) -> None:
        # Call the constructors of the parent classes
        User.__init__(self, name, role)
        UserSettings.__init__(self, bgColor, fontSize)

# Create an instance of the 'AdminUser' class
josh = AdminUser("Josh", "Admin", "Blue", 12)

# Print user details
josh.printName()
josh.printRole()

# Modify user settings
josh.setBgColor("Red")
josh.setFontSize(14)

# Print user settings
print(josh.bgColor)
print(josh.fontSize)

# Check if the instance is an instance of 'User' and 'UserSettings'
print(isinstance(josh, User))
print(isinstance(josh, UserSettings))
