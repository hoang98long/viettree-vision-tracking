class DirectionRule:
    def __init__(self, direction="down"):
        """
        direction: 'down' | 'up'
        """
        self.direction = direction

    def check(self, prev_y, curr_y):
        if self.direction == "down":
            return prev_y < curr_y
        if self.direction == "up":
            return prev_y > curr_y
        return True
