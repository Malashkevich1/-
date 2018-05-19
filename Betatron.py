# -*- coding: cp1251 -*-
from pygame.locals import *
import math 
import pygame, sys 

#x=r*cos(a); y=r*sin(a); a(угол)=wt; t 

pygame.init() 


(windows_width, windows_height, windows_title) = (1000, 768, "Betatron") 
screen = pygame.display.set_mode((windows_width,windows_height),0,32) 
pygame.display.set_caption(windows_title) 
windows_bgcolor = (255,255,255)
font = pygame.font.Font(None, 25)
clock = pygame.time.Clock()


mainLoop = True 

#initial data here 
(circle_1_color, circle_1_pos, circle_1_radius, circle_1_width) = ([0,0,0], [500,384], 200, 5)
(circle_2_color, circle_2_pos, circle_2_radius, circle_2_width) = ([0,0,0], [500,384], 250, 5)
(circle_3_color, circle_3_pos, circle_3_radius, circle_3_width) = ([0,0,255], [500,384], 5, 0)
(line_1_color, line_1_start_pos, line_1_end_pos, line_1_width) = ([0,0,0], [733,380], [745,380], 2)
(line_2_color, line_2_start_pos, line_2_end_pos, line_2_width) = ([0,0,0], [733,383], [745,383], 2)
(line_3_color, line_3_start_pos, line_3_end_pos, line_3_width) = ([0,0,0], [733,386], [745,386], 2)
(rect_1_color, rect_1_rect, rect_1_width)  = ([0,0,0], Rect([720,370],[13,26]), 2)

#(circle_4_color, circle_4_pos, circle_4_radius, circle_4_width) = ([0,255,0], [500,415], 5, 0)
#(circle_5_color, circle_5_pos, circle_5_radius, circle_5_width) = ([255,0,0], [500,360], 5, 0) 

(textpos_1, textpos_2, textpos_3, textpos_4, textpos_5) = ([10,10], [10,40], [10,70], [10,100], [10,130])

#const

e = 1.6021764874*10**-19
U = 0.0000001
r = 228
c = 299792458
m_0 = 9.10938356 * 10**-31
pi = math.pi
r_0 = 0.05

(E, x, y, t, w, v, n, a, m, E_l) = (0, 0, 0, 0, 0, 0, 0, 0, m_0, 0)


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

  t += 0.01
  E_l = U/2*pi*r_0
  m = m_0/math.sqrt(1-((v*v)/(c*c)))
  a = (e*E_l)/m
  v += a*t
  E = 2*pi*r_0*E_l*n
  w += v/r_0
  n = w/2*pi*r_0
  x = r*math.cos(w*t)
  y = r*math.sin(w*t)

  clock.tick(50)
  
  pygame.display.flip() 
  
pygame.quit() 
#destroy data here 
