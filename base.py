from random import randint
import pygame as pg

class group(list):
	def at(t,p):
		for v in t:
			if v.at(p):
				return v
	def draw(t,screen):
		for v in t:
			v.draw(screen)
	def obj(t):
		return group([obj.obj() for obj in t])

class tile:
	def __init__(t,p,c='#ffffff'):
		t.c = c
		t.p = p
	def obj(t):
		return t
	def at(t,p):
		return t.p.real-.5 <= p.real and p.real < t.p.real+.5 \
		   and t.p.imag-.5 <= p.imag and p.imag < t.p.imag+.5
	def draw(t,screen):
		s = min(screen.get_width(), screen.get_height()) // 16
		p = (t.p-.5-.5j) * s

		pg.draw.rect(screen, t.c,
			pg.Rect((round(p.real),round(p.imag)),(s,s))
		)

class Bounds:
	def __init__(t,p1,p2):
		t.p1 = p1
		t.p2 = p2

	def obj(t):
		return t

	def at(t,p):
		return p.real < t.p1.real or t.p2.real < p.real \
		    or p.imag < t.p1.imag or t.p2.imag < p.imag

	def draw(t,screen):
		for x in range(int(t.p1.real),int(t.p2.real)):
			for y in range(int(t.p1.imag),int(t.p2.imag)):
				tile(complex(x,y)+.5+.5j,'#000000' if (x+y)%2==0 else '#1D2B53').draw(screen)

	def random_in(t):
		return complex(
			randint(t.p1.real,t.p2.real-1)+.5,
			randint(t.p1.imag,t.p2.imag-1)+.5
		)