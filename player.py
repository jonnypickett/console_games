class Player:
    """Manage Player"""
    def __init__(self, **kwargs):
        self.name = input("Name: ").title()

        for key, value in kwargs.items():
            setattr(self, key, value)
