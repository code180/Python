class User:
    def __init__(self, first_name, last_name):
        self.first_Name = first_name
        self.last_Name = last_name

    def firstname(self):
        return self.first_Name

    def lastname(self):
        return self.last_Name

    def Name(self):
        return f"firstname: {self.first_Name}, lastname: {self.last_Name}"


user1 = User("Darth", "Vader")
