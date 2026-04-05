import pygame
import math
import datetime

pygame.init()

WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spider Clock")

CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 250

clock = pygame.time.Clock()


def draw_spider(angle, length, color):

    x = CENTER[0] + length * math.cos(angle)
    y = CENTER[1] + length * math.sin(angle)

    # Spider Body
    pygame.draw.circle(screen, color, (int(x), int(y)), 12)

    # Spider head
    head_x = x + 15 * math.cos(angle)
    head_y = y + 15 * math.sin(angle)

    pygame.draw.circle(screen, color, (int(head_x), int(head_y)), 6)

    # Spider Legs
    for i in range(-3,4):

        leg_angle = angle + i * 0.4

        leg_x = x + 30 * math.cos(leg_angle)
        leg_y = y + 30 * math.sin(leg_angle)

        pygame.draw.line(
            screen,
            color,
            (x, y),
            (leg_x, leg_y),
            3
        )

    # Web Line
    pygame.draw.line(
        screen,
        color,
        CENTER,
        (x, y),
        2
    )


running = True

while running:

    screen.fill((10, 10, 20))

    pygame.draw.circle(screen, (100,100,150), CENTER, RADIUS, 3)

    now = datetime.datetime.now()

    second = now.second
    minute = now.minute
    hour = now.hour % 12

    second_angle = math.radians(second * 6 - 90)
    minute_angle = math.radians(minute * 6 - 90)
    hour_angle = math.radians(hour * 30 + minute * 0.5 - 90)

    draw_spider(hour_angle, 130, (255,255,255))
    draw_spider(minute_angle, 180, (0,255,255))
    draw_spider(second_angle, 220, (255,50,50))

    pygame.draw.circle(screen, (255,255,255), CENTER, 8)

    font = pygame.font.SysFont("Arial", 26)

    for i in range(1,13):

        angle = math.radians(i * 30 - 90)

        x = CENTER[0] + (RADIUS - 30) * math.cos(angle)
        y = CENTER[1] + (RADIUS - 30) * math.sin(angle)

        num = font.render(str(i), True, (200,200,255))

        rect = num.get_rect(center=(x,y))

        screen.blit(num, rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()