# -*- coding: cp1251 -*-
from pygame.locals import *
import math 
import pygame, sys 

#x=r*cos(a); y=r*sin(a); a(угол)=wt; t 

pygame.init()

(windows_width, windows_height, windows_title) = (1350, 700, "Betatron")
bg = pygame.image.load('фон.jpg')
screen = pygame.display.set_mode((windows_width,windows_height),0,32)
pygame.display.set_caption(windows_title)
windows_bgcolor = (255,255,255)
font = pygame.font.Font(None, 25)
clock = pygame.time.Clock()

mainLoop = True

#initial data here 
(circle_3_color, circle_3_pos, circle_3_radius, circle_3_width) = ([0,0,255], [870,305], 5, 0)
(rect_1_rect, rect_1_width)  = (Rect([630,605],[40,26]), 2)
(rect_2_rect, rect_2_width)  = (Rect([1000,650],[40,26]), 2)
(rect_3_color, rect_3_rect, rect_3_width)  = ([255,0,0], Rect([50,605],[300,30]), 0)
(rect_4_color, rect_4_rect, rect_4_width)  = ([0,0,255], Rect([50,650],[300,30]), 0)
color_unfocused = pygame.Color(0,0,0)
color_focused = pygame.Color(0,0,255)
color = color_unfocused
focused = False
text_a = ''
text_b = ''

#(circle_4_color, circle_4_pos, circle_4_radius, circle_4_width) = ([0,255,0], [500,415], 5, 0)
#(circle_5_color, circle_5_pos, circle_5_radius, circle_5_width) = ([255,0,0], [500,360], 5, 0) 

(textpos_1, textpos_2, textpos_3, textpos_4, textpos_5, textpos_6) = ([10,10], [10,40], [10,70], [10,100], [10,130], [10,160] )

#const

e = 1.6021764874*10**-19
U = 0.0000001
r = 180
c = 299792458
m_0 = 9.10938356 * 10**-31
pi = math.pi
r_0 = 0.05

(E, x, y, t, w, v, n, a, m, E_l) = (0, 0, 0, 0, 0, 0, 0, 0, m_0, 0)




while mainLoop:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      mainLoop = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      if rect_3_rect.collidepoint(event.pos):
        print ('ok')
      if rect_4_rect.collidepoint(event.pos):
        mainLoop = False
      if rect_1_rect.collidepoint(event.pos):
        focused = not focused
      else:
        focused = False
      color = color_focused if focused else color_unfocused   
    if event.type == pygame.KEYDOWN:
      if focused:
        if event.key == pygame.K_RETURN:
          print (text_a)
          text_a = ''
        elif event.key == pygame.K_BACKSPACE:
          text_a = text_a[:-1]
        else:
          text_a += event.unicode
            

  screen.fill(windows_bgcolor)
  
  #create frame here
  text_1 = font.render("Time (s) = " + str(t), True, [0, 0, 0])
  text_2 = font.render("Acceleration (mps^2) = " + str(a), True, [0, 0, 0])
  text_3 = font.render("Speed (mps)  = " + str(v), True, [0, 0, 0])
  text_4 = font.render("Energy k(MeV)  = " + str(E), True, [0, 0, 0])
  text_5 = font.render("Electron mass (kg)  = " + str(m), True, [0, 0, 0])
  text_6 = font.render("Number of turnovers  = " + str(n), True, [0, 0, 0])
  txt_a_surface = font.render(text_a, True, color)
  txt_b_surface = font.render(text_b, True, color)
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
  #pygame.draw.circle(screen, circle_1_color, circle_1_pos, circle_1_radius, circle_1_width)
  #pygame.draw.circle(screen, circle_2_color, circle_2_pos, circle_2_radius, circle_2_width)
  pygame.draw.circle(screen, circle_3_color, (circle_3_pos[0] + x, circle_3_pos[1] + y), circle_3_radius, circle_3_width)
  #pygame.draw.line(screen, line_1_color, line_1_start_pos, line_1_end_pos, line_1_width)
  #pygame.draw.line(screen, line_2_color, line_2_start_pos, line_2_end_pos, line_2_width)
  #pygame.draw.line(screen, line_3_color, line_3_start_pos, line_3_end_pos, line_3_width)
  #pygame.draw.line(screen, line_4_color, line_4_start_pos, line_4_end_pos, line_4_width)
  #pygame.draw.line(screen, line_5_color, line_5_start_pos, line_5_end_pos, line_5_width)
  #pygame.draw.rect(screen, rect_1_color, rect_1_rect, rect_1_width)
  pygame.draw.rect(screen, color, rect_1_rect, rect_1_width) #pygame.draw.rect(screen, color, input_box, 2)
  pygame.draw.rect(screen, color, rect_2_rect, rect_2_width)
  pygame.draw.rect(screen, rect_3_color, rect_3_rect, rect_3_width)
  pygame.draw.rect(screen, rect_4_color, rect_4_rect, rect_4_width)

  #pygame.draw.circle(screen, circle_4_color, (circle_4_pos[0] + x, circle_4_pos[1] + y), circle_4_radius, circle_4_width)
  #pygame.draw.circle(screen, circle_5_color, (circle_5_pos[0] + x, circle_5_pos[1] + y), circle_5_radius, circle_5_width)

  t += 0.01*10**-5
  E_l = U/2*pi*r_0
  m = m_0/math.sqrt(1-((v*v)/(c*c)))
  a = (e*E_l)/m
  v += a*t
  E = 2*pi*r_0*E_l*n
  w += v/r_0
  n = w/2*pi
  x = r*math.cos(w*t)
  y = r*math.sin(w*t)

  clock.tick(50)
  
  pygame.display.flip()
  
pygame.quit() 
#destroy data here 
