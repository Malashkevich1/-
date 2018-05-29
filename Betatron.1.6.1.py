# -*- coding: cp1251 -*-
from pygame.locals import *
import math 
import pygame, sys 

#x=r*cos(a); y=r*sin(a); a(����)=wt; t 

pygame.init()

(windows_width, windows_height, windows_title) = (1350, 700, "Betatron")
bg = pygame.image.load('���.jpg')
screen = pygame.display.set_mode((windows_width,windows_height),0,32)
pygame.display.set_caption(windows_title)
windows_bgcolor = (255,255,255)
font = pygame.font.Font(None, 25)
clock = pygame.time.Clock()

mainLoop = True

#initial data here 
(circle_3_color, circle_3_pos, circle_3_radius, circle_3_width) = ([0,0,255], [875,305], 5, 0)
(rect_1_rect, rect_1_width)  = (Rect([610,603],[40,26]), 2)
(rect_2_rect, rect_2_width)  = (Rect([880,655],[40,26]), 2)
(rect_3_color, rect_3_rect, rect_3_width)  = ([47,50,98], Rect([33,590],[330,32]), 1)
(rect_4_color, rect_4_rect, rect_4_width)  = ([236,52,52], Rect([33,645],[330,30]), 1)
color_unfocused_1 = pygame.Color(0,0,0)
color_unfocused_2 = pygame.Color(0,0,0)
color_focused_1 = pygame.Color(0,0,255)
color_focused_2 = pygame.Color(0,0,255)
color_1 = color_unfocused_1
color_2 = color_unfocused_2
focused_1 = False
focused_2 = False
text_a = ''
text_b = ''

#(circle_4_color, circle_4_pos, circle_4_radius, circle_4_width) = ([0,255,0], [500,415], 5, 0)
#(circle_5_color, circle_5_pos, circle_5_radius, circle_5_width) = ([255,0,0], [500,360], 5, 0) 

(textpos_1, textpos_2, textpos_3, textpos_4, textpos_5, textpos_6) = ([10,60], [10,90], [10,120], [10,150], [10,180], [10,210])

#const

e = 1.6021764874*10**-19
r = 180
c = 299792458
m_0 = 9.10938356 * 10**-31
pi = math.pi
U = 0.0000001
r_0 = 0.05

(E, x, y, t, w, v, n, a, m, E_l, z) = (0, 0, 0, 0, 0, 0, 0, 0, m_0, 0, 0)

start_ticks=pygame.time.get_ticks()

while mainLoop:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      mainLoop = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      if rect_3_rect.collidepoint(event.pos):
        z += 1
      if rect_4_rect.collidepoint(event.pos):
        mainLoop = False
      if rect_1_rect.collidepoint(event.pos):
        focused_1 = not focused_1
      else:
        focused_1 = False
      color_1 = color_focused_1 if focused_1 else color_unfocused_1
      if rect_2_rect.collidepoint(event.pos):
        focused_2 = not focused_2
      else:
        focused_2 = False
      color_2 = color_focused_2 if focused_2 else color_unfocused_2
    if event.type == pygame.KEYDOWN:
      if focused_1:
        if event.key == pygame.K_RETURN:
          text_a = ''
        elif event.key == pygame.K_BACKSPACE:
          text_a = text_a[:-1]
        else:
          text_a += event.unicode
      if focused_2:
        if event.key == pygame.K_RETURN:
          text_b = ''
        elif event.key == pygame.K_BACKSPACE:
          text_b = text_b[:-1]
        else:
          text_b += event.unicode    
  if z >= 1: 
    t = (pygame.time.get_ticks()-start_ticks)/1000
    E_l = U/2*pi*r_0
    m = m_0/math.sqrt(1-((v*v)/(c*c)))
    a = (e*E_l)/m
    v += a*t
    E = 2*pi*r_0*E_l*n
    w += v/r_0
    n = v*t/2*pi*r_0
    x = r*math.cos(w*t)
    y = r*math.sin(w*t)
        

  screen.fill(windows_bgcolor)
  
  #create frame here
  text_1 = font.render("Time (s) = " + str(t), True, [0, 0, 0])
  text_2 = font.render("Acceleration (mps^2) = " + str(a), True, [0, 0, 0])
  text_3 = font.render("Speed (mps)  = " + str(v), True, [0, 0, 0])
  text_4 = font.render("Energy k(MeV)  = " + str(E), True, [0, 0, 0])
  text_5 = font.render("Electron mass (kg)  = " + str(m), True, [0, 0, 0])
  text_6 = font.render("Number of turnovers  = " + str(n), True, [0, 0, 0])
  txt_a_surface = font.render(text_a, True, color_1)
  txt_b_surface = font.render(text_b, True, color_2)
  rect_1_rect.w = max(200, txt_a_surface.get_width()+10)
  rect_2_rect.w = max(200, txt_b_surface.get_width()+10)
  screen.blit(bg,(0,0))
  screen.blit(text_1, textpos_1)
  screen.blit(text_2, textpos_2)
  screen.blit(text_3, textpos_3)
  screen.blit(text_4, textpos_4)
  screen.blit(text_5, textpos_5)
  screen.blit(text_6, textpos_6)
  screen.blit(txt_a_surface, (rect_1_rect.x+5, rect_1_rect.y+5))
  screen.blit(txt_b_surface, (rect_2_rect.x+5, rect_2_rect.y+5))
  pygame.draw.circle(screen, circle_3_color, (circle_3_pos[0] + x, circle_3_pos[1] + y), circle_3_radius, circle_3_width)
  pygame.draw.rect(screen, color_1, rect_1_rect, rect_1_width)
  pygame.draw.rect(screen, color_2, rect_2_rect, rect_2_width)
  pygame.draw.rect(screen, rect_3_color, rect_3_rect, rect_3_width)
  pygame.draw.rect(screen, rect_4_color, rect_4_rect, rect_4_width)

  #pygame.draw.circle(screen, circle_4_color, (circle_4_pos[0] + x, circle_4_pos[1] + y), circle_4_radius, circle_4_width)
  #pygame.draw.circle(screen, circle_5_color, (circle_5_pos[0] + x, circle_5_pos[1] + y), circle_5_radius, circle_5_width)

  clock.tick(60)
  
  pygame.display.flip()
  
pygame.quit() 
#destroy data here 
