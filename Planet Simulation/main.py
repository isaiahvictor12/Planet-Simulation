import pygame
from Planet import Planet
import settings 
import math
import button

pygame.init()

WIN = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption("Planet Simulation");

start_img = pygame.image.load('images/start.png').convert_alpha()
stop_img = pygame.image.load('images/stop.png').convert_alpha()


start_button = button.Button(100, 600, start_img, 1)
stop_button = button.Button(300, 600, stop_img, 1)

def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, settings.YELLOW, 1.98892 * 10**30, "Sun")
    sun.sun= True

    earth = Planet(-1 * Planet.AU, 0, 16, settings.BLUE, 5.9742 * 10**24, "Earth")
    earth.y_vel = 29.783 * 1000

    mars = Planet(-1.524 * Planet.AU, 0, 12, settings.RED, 6.39 * 10**23, "Mars")
    mars.y_vel = 24.077 * 1000
    
    mercury = Planet(0.387 * Planet.AU, 0, 14, settings.DARK_GREY, 3.3 * 10**23, "Mercury")
    mercury.y_vel = -47.4 * 1000

    venus = Planet(0.723 * Planet.AU, 0, 14, settings.YELLOW, 4.8685 * 10**24, "Venus")
    venus.y_vel = -35.02 * 1000

    jupiter = Planet(5.204 * Planet.AU, 0, 22, settings.ORANGE, 1898 * 10**24, "Jupiter")
    jupiter.y_vel = -13.1 * 1000

    saturn = Planet(9.572 * Planet.AU, 0, 20, settings.PURPLE, 568 * 10**24, "Saturn")
    saturn.y_vel = -9.7 * 1000

    uranus = Planet(19.164 * Planet.AU, 0, 17, settings.WHITE, 86.8 * 10**24, "Uranus")
    uranus.y_vel = -6.8 * 1000

    neptune = Planet(30.18 * Planet.AU, 0, 17, settings.BLUE_NEPTUNE, 102 * 10**24, "Neptune")
    neptune.y_vel = -5.4 * 1000

    planets = [sun, earth, mars, mercury, venus, jupiter, saturn, uranus, neptune]

    pause = 0
    while run:
        clock.tick(60)
        
        if start_button.draw(WIN):
            pause = 0    
        if stop_button.draw(WIN):
            pause = 1

        if not pause:
            WIN.fill((0, 0, 0))
            for planet in planets:
                planet.update_position(planets)
                planet.draw(WIN)
            start_button.draw(WIN)
            stop_button.draw(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()
    
main()