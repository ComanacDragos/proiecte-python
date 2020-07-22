"""
Board
"""
from random import random


class Object:
    """
    Player
    """
    def __init__(self, x, y, width, height, image_url):
        self._position = (x, y)
        self._size = (width, height)
        self._image_url = image_url

    @property
    def position(self):
        return self._position

    @property
    def size(self):
        return self._size

    @property
    def image_url(self):
        return self._image_url

    def out_of_bounds(self, width, height):
        """
        Returns true if the object is out of bounds and false otherwise
        """
        width_cond = 50 <= self.position[0] <= width - self.size[0]
        height_cond = 50 <= self.position[1] <= height - self.size[1]
        if width_cond and height_cond:
            return False
        return True

    def is_in_proximity(self, x, y, danger_zone):
        """
        Returns true if the coordinates are too close to the object, false otherwise
        """
        cond1 = self.position[0] - danger_zone <= x <= self.position[0] + self.size[0] + danger_zone
        cond2 = self.position[1] - danger_zone <= y <= self.position[1] + self.size[1] + danger_zone
        if cond1 and cond2:
            return True
        return False

    def close_to(self, other_object, danger_zone):
        """
        Returns true if the current object is close to the given object
        """
        dx = min(self._position[0] + self._size[0] + danger_zone, other_object.position[0] + other_object.size[0]) - max(self.position[0] - danger_zone, other_object.position[0])
        dy = min(self._position[1] + self._size[1] + danger_zone, other_object.position[1] + other_object.size[1]) - max(self.position[1] - danger_zone, other_object.position[1])

        return dx >= 0 and dy >= 0


class Movable(Object):
    """
    Movable: inherits from object
    """
    def __init__(self, x, y, width, height, image_url, velocity, direction=(1, 0)):
        super().__init__(x, y, width, height, image_url)
        self._velocity = velocity
        self._direction = direction

    def move(self, direction):
        """
        Moves the object in the direction given as a tuple
        """
        new_x = self._position[0] + self._velocity * self._direction[0]
        new_y = self._position[1] + self._velocity * self._direction[1]
        self._position = (new_x, new_y)

    def is_in_direction(self, other_object):
        """
        Returns true if the other object is in the direction of the current object
        """
        x_range = range(self.position[0] + self.velocity, self.position[0] + self.size[0] - self.velocity)
        y_range = range(self.position[1] + self.velocity, self.position[1] + self.size[1] - self.velocity)

        other_x_range = range(other_object.position[0], other_object.position[0] + other_object.size[0])
        other_y_range = range(other_object.position[1], other_object.position[1] + other_object.size[1])

        x_set = set(x_range)
        y_set = set(y_range)

        other_x_set = set(other_x_range)
        other_y_set = set(other_y_range)

        if self.direction == (1, 0) and self.position[0] < other_object.position[0]:
            if len(y_set.intersection(other_y_set)) != 0:
                return True
            return False

        if self.direction == (-1, 0) and self.position[0] > other_object.position[0]:
            if len(y_set.intersection(other_y_set)) != 0:
                return True
            return False

        if self.direction == (0, 1) and self.position[1] < other_object.position[1]:
            if len(x_set.intersection(other_x_set)) != 0:
                return True
            return False

        if self.direction == (0, -1) and self.position[1] > other_object.position[1]:
            if len(x_set.intersection(other_x_set)) != 0:
                return True
            return False

        return False

    @property
    def direction(self):
        return self._direction

    @property
    def velocity(self):
        return self._velocity


class Player(Movable):
    """
    Player
    """
    def __init__(self, x, y, width, height, image_url, velocity, direction=(1, 0)):
        super().__init__(x, y, width, height, image_url, velocity, direction)

    def move(self, direction):
        if direction != self._direction:
            self._direction = direction
            self._image_url = "Files/Media/player_" + str(self.direction[0]) + str(self.direction[1]) + ".png"
            return
        Movable.move(self, direction)


class Bligon(Object):
    """
    Bligon: inherits from object
    """
    def __init__(self, x, y, width, height, image_url):
        super().__init__(x, y, width, height, image_url)

    def replace(self, new_position):
        """
        Replaces the bligon
        """
        self._position = new_position


class Star(Object):
    """
    Star: inherits from object
    """
    def __init__(self, x, y, width, height, image_url, danger_zone):
        super().__init__(x, y, width, height, image_url)
        self._danger_zone = danger_zone

    @property
    def danger_zone(self):
        return self._danger_zone


class Projectile(Movable):
    """
    Projectile
    """
    def __init__(self, x, y, width, height, image_url, velocity, distance_to_travel, direction=(1, 0)):
        super().__init__(x, y, width, height, image_url, velocity, direction)
        self._distance_to_travel = distance_to_travel

    def move(self, direction):
        """
        Moves the projectile in the given direction
        """
        Movable.move(self, direction)
        self._distance_to_travel -= self.velocity

    def can_travel(self):
        """
        Returns true if the distance to travel is greater than 0 and false otherwise
        """
        return self._distance_to_travel > 0


class GameLost(Exception):
    """
    Game lost exception
    """
    pass


class GameWon(Exception):
    """
    Game lost exception
    """
    pass


class CloseToBligon(Exception):
    """
    Close to bligon exception
    """
    pass
