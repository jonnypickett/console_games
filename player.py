class Player:
    """Manage Player"""
    def __init__(self, **kwargs):
        self.name = input("Name: ").title()

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        """Print out the player."""
        return '{0.name}'.format(self)