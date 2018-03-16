import math 
import pygame, sys 
from pygame.locals import * 

#x=r*cos(a); y=r*sin(a); a=wt; t 

pygame.init() 

(windows_width, windows_height, windows_title) = (1000, 768, "Betatron") 
screen = pygame.display.set_mode((windows_width,windows_height),0,32) 
pygame.display.set_caption(windows_title) 
windows_bgcolor = (255,255,255) 
mainLoop = True 

#initial data here 
circle_1_color = (0,0,0) 
circle_1_pos = (500,384) 
circle_1_radius = 100 
circle_1_width = 5
circle_2_color = (0,0,0) 
circle_2_pos = (500,384) 
circle_2_radius = 250 
circle_2_width = 5
circle_3_color = (0,0,255) 
circle_3_pos = (500,384) 
circle_3_radius = 10 
circle_3_width = 0

a = 0.00000001
x = 0
y = 0
r = 200
t = 0
w = 0.001

while mainLoop: 
  for event in pygame.event.get(): 
   if event.type == QUIT: 
    mainLoop = False 
  screen.fill(windows_bgcolor) 

  #create frame here 
  pygame.draw.circle(screen, circle_1_color, circle_1_pos, circle_1_radius, circle_1_width)
  pygame.draw.circle(screen, circle_2_color, circle_2_pos, circle_2_radius, circle_2_width)
  pygame.draw.circle(screen, circle_3_color, (circle_3_pos[0] + x, circle_3_pos[1] + y), circle_3_radius, circle_3_width)
  w += a*t
  t += 1
  x = r*math.cos(w*t)
  y = r*math.sin(w*t)
  pygame.display.update() 
  
pygame.quit() 
#destroy data here 
