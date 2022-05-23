from snake import Snake
from base import *

def apple(tile):
	tile.c = '#ff77a8'
	return tile

class game:
	def __init__(g):
		g._objs = group([])

		g.bounds = Bounds(complex(0,0), complex(16,16))
		g._objs += [g.bounds]

		g.snakes = group([])
		g._objs += [g.snakes]

		g.apples = group(apple(g.random_tile()) for i in range(5))
		g._objs[:1] += [g.apples]

	def cols(g):
		return group([g.snakes.obj(),g.bounds.obj()])

	def random_tile(g):
		while 1:
			p = g.bounds.random_in()
			if not g._objs.obj().at(p):
				break
		return tile(p)

	def update(g, ps):
		for p, snake in zip(ps, g.snakes):
			snake.update(g,p,.1)