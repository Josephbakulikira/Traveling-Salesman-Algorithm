import time
import pygame
import random
import os
from points import Point

#window setting
pygame.font.init()
os.environ['SDL_VIDEO_CENTERED']='1'
pygame.init()
width, height = 1920, 1080
pygame.display.set_caption("Traveling salesman ")
screen = pygame.display.set_mode((width, height))
fps = 100
clock = pygame.time.Clock()


#Colors and BackGround
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
green = (0, 138, 78)

#variables
points = []
offset_screen = 50
number_of_point = 10
smallest_path = []
record_distance = 0
#Generate points
for n in range(number_of_point):
    x = random.randint(offset_screen, width-offset_screen)
    y = random.randint(offset_screen, height-offset_screen)

    point = Point(x, y)
    points.append(point)



#shuffle points list
def shuffle(a, b, c):
    temp = a[b]
    a[b] = a[c]
    a[c] = temp

#distance betweenpoints
def calculate_distance(points_list):
    total = 0
    for n in range(len(points)-1):
        distance = ((points[n].x - points[n+1].x )**2 + (points[n].y - points[n+1].y )**2) ** 0.5
        total += distance;
    return total

dist= calculate_distance(points)
record_distance = dist

slice_object = slice(number_of_point)
smallest_path = points.copy()

myfont = pygame.font.SysFont('Comic Sans MS', 20)
a =[]
for n in range(len(smallest_path)):
    a.append((smallest_path[n].x, smallest_path[n].y))

textsurface = myfont.render("the smallest path is: " , False, (255, 255, 255))
textsurface1 = myfont.render(str(a), False, (255, 255, 255))
textsurface3 = myfont.render("the distance is :", False, (25, 41, 255))
textsurface4 = myfont.render(str(record_distance), False, (255, 255, 0))


run = True;
while run:
    screen.fill(black)
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #draw lines between points

    for n in range(len(points)):
        pygame.draw.circle(screen, white, (points[n].x, points[n].y), 8)

    a = random.randint(0, len(points)-1)
    b = random.randint(0, len(points)-1)
    shuffle(points, a, b)

    dist = calculate_distance(points)
    if dist < record_distance:
        record_distance = dist;
        smallest_path = points.copy()

    for m in range(len(points)-1):
        pygame.draw.line(screen, white, (points[m].x, points[m].y), (points[m+1].x, points[m+1].y), 1)


    for m in range(len(smallest_path)-1):
        pygame.draw.line(screen, green, (smallest_path[m].x, smallest_path[m].y), (smallest_path[m+1].x, smallest_path[m+1].y), 5)

    pygame.display.update()

screen.blit(textsurface,(0,0))
screen.blit(textsurface1,(20,20))
screen.blit(textsurface3,(20,40))
screen.blit(textsurface4,(130,60))
pygame.display.update()

time.sleep(5)
pygame.quit()
