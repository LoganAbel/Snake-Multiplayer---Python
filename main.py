from game import game
import pygame as pg
from pghelp import *
from snake import Snake
from base import *

pg.init()
screen = pg.display.set_mode((640,640),pg.RESIZABLE)
pg.display.set_caption('pySnake')
clock = pg.time.Clock()
colors = '#00e436','#29ADFF','#ffec27','#ffa300'

def main():
	g = game()
	g.snakes += [
		Snake(tile(complex(15.5,15.5),colors[0]), 0),
		Snake(tile(complex(.5,.5),colors[1]), 0),
		Snake(tile(complex(.5,15.5),colors[2]), 0),
		Snake(tile(complex(15.5,.5),colors[3]), 0),
	]

	while 1:
		ps = [0,0,0,0]
		for e in pg.event.get():
			if e.type == pg.QUIT:
				pg.quit()
				exit()
			if e.type == pg.KEYDOWN:
				axises = keys(e.key)
				for i,ks in zip(range(len(ps)), arrow_keys):
					ps[i] += axises(*ks)
				if e.key == pg.K_SPACE and all(not snake.alive for snake in g.snakes):
					main()
					return

		g.update(ps)
		draw_scr(g)

		pg.display.flip()
		clock.tick(60)

def draw_scr(g):
	w,h = screen.get_width(), screen.get_height()
	
	g_r = 1.3
	g_h = min(h,w/g_r)
	g_w = g_h*g_r
	g_h = g_min = g_h//16*16

	g_x, g_y = g_p = (g_w-g_min)/2, (g_h-g_min)/2

	g_screen = pg.Surface((g_w,g_h))
	font = pg.font.Font('PICO-8 mono.ttf',int(g_h/24))
	scores = [font.render(str(len(g.snakes[i].body)), 0, color) for i,color in enumerate(colors)]
	
	g_screen.blit(scores[1], (g_x-scores[0].get_rect().right, 0))
	g_screen.blit(scores[2], (g_x-scores[1].get_rect().right, g_min-scores[1].get_rect().bottom))
	g_screen.blit(scores[3], (g_x+g_min*(1+1/64), 0))
	g_screen.blit(scores[0], (g_x+g_min*(1+1/64), g_min-scores[3].get_rect().bottom))

	g2_screen = pg.Surface((g_min,g_min))
	g._objs.obj().draw(g2_screen)

	g_screen.blit(g2_screen, g_p)
	screen.blit(g_screen, ((w-g_w)/2, (h-g_h)/2))

main()