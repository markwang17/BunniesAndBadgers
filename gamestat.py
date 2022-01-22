

class Stat:
    """

    """
    def __init__(self):
        self.accuracy = [0, 0]
        self.badtimer = 100
        self.health_point = 194
        self.game_on = True
        self.percentage = 0.00

    def compute_accuracy(self):
        self.percentage = self.accuracy[0] / self.accuracy[1] * 100 if \
            self.accuracy[1] > 0 else 0
        self.percentage = '%.2f' % self.percentage
