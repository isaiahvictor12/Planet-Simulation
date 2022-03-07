import pygame
import math
import settings

class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 40/AU #250 / AU # 1 AU = 100 pixels
    TIMESTEP = 3600*24 # 1 day
    def __init__(self, x, y, radius, color, mass, name) -> None:
        self.x = x
        self.y = y
        self.radius = radius * self.SCALE * self.AU  / 125
        self.color = color
        self.mass = mass
        self.name = name
        

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0


    def draw(self, win):
        x = self.x * self.SCALE + settings.WIDTH/2
        y = self.y * self.SCALE + settings.HEIGHT/2
       
        if len(self.orbit)>2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + settings.WIDTH/2
                y = y * self.SCALE + settings.HEIGHT/2
                updated_points.append((x, y))
            pygame.draw.lines(win, self.color, False, updated_points, 2)

        pygame.draw.circle(win, self.color, (x,y), self.radius)

        if not self.sun:
            #distance_text = settings.pygame.font.SysFont("comicsans", 16).render(f"{round(self.distance_to_sun/1000, 1)}km", 1, settings.WHITE)
            name_text = settings.pygame.font.SysFont("comicsans", 16).render(self.name, 1, settings.WHITE)
            win.blit(name_text, (x - name_text.get_width()/2, y - name_text.get_height()/2 + 25))

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x**2 + distance_y**2)

        if other.sun:
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y 

    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue
            
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy
        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))