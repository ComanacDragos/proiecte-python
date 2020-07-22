import pygame
from Files.Domain import *
from random import random

screen_width = 800
screen_height = 800

player_size = 30
bligon_size = 30
projectile_width = 25
projectile_height = 25
projectile_range = 150

player_velocity = 5
projectile_velocity = 10


class GUI:
    """
    GUI
    """
    def __init__(self):
        self._window = pygame.display.set_mode((screen_width, screen_height))
        self._stars = list()
        self._bligons = list()
        self._number_of_bligons = 3
        self._projectiles = list()
        self._cheat_on = False
        self._last_cheat_key = ""

        self.generate_stars()
        is_placed = False
        while not is_placed:
            x = int(random() * 1000000) % (screen_width - player_size)
            y = int(random() * 1000000) % (screen_height - player_size)
            self._player = Player(x, y, player_size, player_size, "Files/Media/player_10.png", player_velocity)

            ok = True
            for star in self._stars:
                if star.close_to(self._player, star.danger_zone):
                    ok = False
                    break
            if not ok:
                continue
            is_placed = True
        self.generate_bligons()

        pygame.display.set_caption("Bligons")

        self._projectile_timer = 0
        run = True
        while run:
            if self._projectile_timer > 0:
                self._projectile_timer += 1
            if self._projectile_timer > 30:
                self._projectile_timer = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            try:
                self.move_projectiles()
                self.check_key_pressed()
                self.load_images()
            except GameLost:
                self.draw_game_over(False)
                run = False
            except GameWon:
                self.draw_game_over(True)
                run = False

    def load_images(self):
        """
        Loads all the images
        """
        bg = pygame.image.load("Files/Media/bg.jpg")
        self._window.blit(bg, (0, 0))

        self.place_objects(self._stars + self._projectiles + [self._player])
        self.place_bligons()
        pygame.display.update()

    def generate_stars(self):
        """
        Generates the stars
        """
        while len(self._stars) != 10:
            x = int(random() * 1000000) % screen_width
            y = int(random() * 1000000) % screen_height
            width = (int(random() * 1000) % 5 + 4) * 10 + (int(random() * 1000) % 5)
            height = (int(random() * 1000) % 5 + 4) * 10 + (int(random() * 1000) % 5)

            if not abs(width - height) <= 10:
                continue

            new_star = Star(x, y, width, height, "Files/Media/sun.png", width + height / 10)

            if new_star.out_of_bounds(screen_width - 50, screen_height - 50):
                continue

            ok = True
            for star in self._stars:
                if star.close_to(new_star, star.danger_zone):
                    ok = False
                    break
            if not ok:
                continue

            self._stars.append(new_star)

    def generate_bligons(self):
        """
        Generates the bligons
        """
        new_bligons = list()

        while len(new_bligons) != self._number_of_bligons:
            x = int(random() * 1000000) % (screen_width - bligon_size)
            y = int(random() * 1000000) % (screen_height - bligon_size)
            new_bligon = Bligon(x, y, bligon_size, bligon_size, "Files/Media/bligon.png")

            if self._player.close_to(new_bligon, 100):
                continue

            ok = True
            for star in self._stars:
                if star.close_to(new_bligon, star.danger_zone):
                    ok = False
                    break
            if not ok:
                continue

            ok = True
            for bligon in new_bligons:
                if bligon.close_to(new_bligon, bligon_size / 2):
                    ok = False
                    break
            if not ok:
                continue
            new_bligons.append(new_bligon)

        self._bligons = new_bligons

    def place_objects(self, objects):
        """
        Places objects on screen
        """
        for current_object in objects:
            img = pygame.image.load(current_object.image_url)
            img = pygame.transform.scale(img, current_object.size)
            self._window.blit(img, current_object.position)

    def place_bligons(self):
        """
        Places all bligons if the cheat is on, or only those close to the player otherwise
        """
        for bligon in self._bligons:
            if self._player.close_to(bligon, 100) or self._cheat_on:
                img = pygame.image.load(bligon.image_url)
                img = pygame.transform.scale(img, bligon.size)
                self._window.blit(img, bligon.position)

    def is_movable(self, movable_object, star_danger_zone=0, bligon_danger_zone=0):
        """
        Checks is the movable object can move
        """
        for star in self._stars:
            if movable_object.close_to(star, star_danger_zone) and movable_object.is_in_direction(star):
                return False

        for bligon in self._bligons:
            if movable_object.close_to(bligon, bligon_danger_zone):
                raise CloseToBligon
        return True

    def shoot_projectile(self):
        """
        Creates a new Projectile
        """
        self._projectile_timer = 1

        if len(self._projectiles) > 3:
            return

        direction = self._player.direction
        x = (2 * self._player.position[0] + self._player.size[0]) // 2 - 12
        y = (2 * self._player.position[1] + self._player.size[1]) // 2 - 12
        url = "Files/Media/projectile_" + str(direction[0]) + str(direction[1]) + ".png"
        projectile = Projectile(x, y, projectile_width, projectile_height, url, projectile_velocity, projectile_range, direction)
        self._projectiles.append(projectile)

    def move_projectiles(self):
        """
        Moves the projectiles
        """
        for projectile in self._projectiles:
            cond_1 = 0 < projectile.position[0] < screen_width and 0 < projectile.position[1] < screen_height
            try:
                if cond_1 and self.is_movable(projectile) and projectile.can_travel():
                    projectile.move(projectile.direction)
                else:
                    self._projectiles.pop(self._projectiles.index(projectile))
            except CloseToBligon:
                self._number_of_bligons -= 1
                if self._number_of_bligons == 0:
                    raise GameWon
                self.generate_bligons()

    def check_key_pressed(self):
        """
        Checks if a key is pressed
        """
        keys = pygame.key.get_pressed()

        try:
            if keys[pygame.K_a]:
                if self._player.position[0] > self._player.velocity and self.is_movable(self._player, bligon_danger_zone=20) or self._player.direction != (-1, 0):
                    self._player.move((-1, 0))

            if keys[pygame.K_d]:
                if self._player.position[0] < screen_width - self._player.size[0] - self._player.velocity and self.is_movable(self._player, bligon_danger_zone=20) or self._player.direction != (1, 0):
                    self._player.move((1, 0))

            if keys[pygame.K_w]:
                if self._player.position[1] > self._player.velocity and self.is_movable(self._player, bligon_danger_zone=20) or self._player.direction != (0, -1):
                    self._player.move((0, -1))

            if keys[pygame.K_s]:
                if self._player.position[1] < screen_height - self._player.size[1] - self._player.velocity and self.is_movable(self._player, bligon_danger_zone=20) or self._player.direction != (0, 1):
                    self._player.move((0, 1))
        except CloseToBligon:
            raise GameLost

        if keys[pygame.K_SPACE] and self._projectile_timer == 0:
            self.shoot_projectile()

        if keys[pygame.K_c]:
            if self._last_cheat_key != pygame.K_c:
                self._cheat_on = not self._cheat_on
                self._last_cheat_key = pygame.K_c
        else:
            self._last_cheat_key = ""

    def draw_game_over(self, won):
        """
        Game over draw
        """
        run = True
        bg = (0, 0, 0)
        if won:
            bg = (0, 255, 0)
        while run:
            self._window.fill(bg)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.update()
