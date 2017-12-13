"""Build a player model."""


class Player(object):
    """Model for Player."""

    def __init__(self, name=None, health=None, magic=None, strength=None,
                 home=None, backpack=None, size=None):
        """."""
        self.name = name
        self.health = health
        self.magic = magic
        self.strength = strength
        self.home = home
        self.backpack = backpack
        self.size = size
        if self.magic == 'X-MAS':
            self.name = 'Kris Kringle'
            self.health = 'INF'
            self.strength = 'INF'
            self.home = 'North Pole'
            self.sleigh = {
                'all_toys': 'For all the good litlle childeren',
                'all_reindeer': {
                    1: 'donner',
                    2: 'so forth',
                    3: 'rudolph of course'
                }
            }
            self.backpack = self.sleigh
            self.size = 'Santa size'

    def show_player(self):
        """Dislplay attributes."""


if __name__ == '__main__':
    res = input('Create your player\n Options are:\nname, health, magic, strength, home, backpack, and size\nPut in the following order and in ""(you must include all):\n"name", "health", ...and so forth\n')
    res = list(res)
    you = Player(res)
    import pdb; pdb.set_trace()
    you.show_player()
