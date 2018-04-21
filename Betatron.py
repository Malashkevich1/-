# -*- coding: cp1251 -*-
import math 
import pygame, sys 
from pygame.locals import * 

#x=r*cos(a); y=r*sin(a); a(угол)=wt; t 

pygame.init() 


(windows_width, windows_height, windows_title) = (1000, 768, "Betatron") 
screen = pygame.display.set_mode((windows_width,windows_height),0,32) 
pygame.display.set_caption(windows_title) 
windows_bgcolor = (255,255,255)
font = pygame.font.Font(None, 25)

mainLoop = True 

#initial data here 
(circle_1_color, circle_1_pos, circle_1_radius, circle_1_width) = ([0,0,0], [500,384], 100, 5)
(circle_2_color, circle_2_pos, circle_2_radius, circle_2_width) = ([0,0,0], [500,384], 250, 5)
(circle_3_color, circle_3_pos, circle_3_radius, circle_3_width) = ([0,0,255], [500,384], 5, 0)
(line_1_color, line_1_start_pos, line_1_end_pos, line_1_width) = ([0,0,0], [733,380], [745,380], 2)
(line_2_color, line_2_start_pos, line_2_end_pos, line_2_width) = ([0,0,0], [733,383], [745,383], 2)
(line_3_color, line_3_start_pos, line_3_end_pos, line_3_width) = ([0,0,0], [733,386], [745,386], 2)
(rect_1_color, rect_1_rect, rect_1_width)  = ([0,0,0], Rect([720,370],[13,26]), 2)

#(circle_4_color, circle_4_pos, circle_4_radius, circle_4_width) = ([0,255,0], [500,415], 5, 0)
#(circle_5_color, circle_5_pos, circle_5_radius, circle_5_width) = ([255,0,0], [500,360], 5, 0) 

(textpos_1, textpos_2, textpos_3, textpos_4, textpos_5) = ([10,10], [10,40], [10,70], [10,100], [10,130])

(b, E, x, y, t, w, v) = (0, 0, 0, 0, 0, 0, 0)

#const

r = 228
a = 1
c = 299792458
m_0 = 9.10938356 * 10**-31

while mainLoop: 
  for event in pygame.event.get(): 
   if event.type == QUIT: 
    mainLoop = False

  screen.fill(windows_bgcolor) 

  #create frame here
  text_1 = font.render("Time (s) = " + str(t), True, [0, 0, 0])
  text_2 = font.render("Acceleration (mps^2) = " + str(a), True, [0, 0, 0])
  text_3 = font.render("Speed (mps)  = " + str(v), True, [0, 0, 0])
  text_4 = font.render("Energy k(MeV)  = " + str(E), True, [0, 0, 0])
  text_5 = font.render("Electron mass (kg)  = " + str(m_0), True, [0, 0, 0])
  screen.blit(text_1, textpos_1)
  screen.blit(text_2, textpos_2)
  screen.blit(text_3, textpos_3)
  screen.blit(text_4, textpos_4)
  screen.blit(text_5, textpos_5)
  pygame.draw.circle(screen, circle_1_color, circle_1_pos, circle_1_radius, circle_1_width)
  pygame.draw.circle(screen, circle_2_color, circle_2_pos, circle_2_radius, circle_2_width)
  pygame.draw.circle(screen, circle_3_color, (circle_3_pos[0] + x, circle_3_pos[1] + y), circle_3_radius, circle_3_width)
  pygame.draw.line(screen, line_1_color, line_1_start_pos, line_1_end_pos, line_1_width)
  pygame.draw.line(screen, line_2_color, line_2_start_pos, line_2_end_pos, line_2_width)
  pygame.draw.line(screen, line_3_color, line_3_start_pos, line_3_end_pos, line_3_width)
  pygame.draw.rect(screen, rect_1_color, rect_1_rect, rect_1_width)
  #pygame.draw.circle(screen, circle_4_color, (circle_4_pos[0] + x, circle_4_pos[1] + y), circle_4_radius, circle_4_width)
  #pygame.draw.circle(screen, circle_5_color, (circle_5_pos[0] + x, circle_5_pos[1] + y), circle_5_radius, circle_5_width)
  t += 0.0021
  v += a*t
  b = v/c
  E = (m_0*c*c/math.sqrt(1-b*b-m_0*c*c))*6.241506363094 * 10**12
  w += v/r*0.000264
  x = r*math.cos(w*t)
  y = r*math.sin(w*t)
  
  pygame.display.update() 
  
pygame.quit() 
#destroy data here 
