from base import tile, group

class stack(list):
	def push(t,x):
		if len(t) == 0: return t
		t[1:]=t[:-1]
		t[0]=x
		return t

lerp = lambda a,b,c: a * c + b * (1-c)

class Snake:
	def __init__(t,head,d):
		t.alive = True
		t.color = head.c

		t.head = head
		t.dist = 0
		t.body = stack([head])

		t.d = d
		t.nd = d
	def tail(t):
		return tile(lerp(t.body[-2].p, t.body[-1].p, t.dist),t.color) if len(t.body)>=2 else t.head
	def obj(t):
		return group(
			t.body[:-1] + [t.tail(), t.head]
		)
	def move(t,speed):
		if not t.alive: return

		t.dist += speed
		t.head.p += t.d*speed

		if t.dist+speed/2 >= 1:
			t.dist -= 1
			t.body.push(tile(t.head.p,t.color))
			t.d = t.nd
	def grow(t):
		t.body[-1] = t.tail()
		t.body += [t.body[-1]]
	def die(t):
		t.color = '#5f574f'
		for cell in t.body:
			cell.c = t.color
		t.head.c = t.color
		t.alive = False

	def update(t,g,paxis,speed):
		if paxis != -t.d:
			side = paxis if t.d == 0 else (paxis.imag * 1j if t.d.real else paxis.real)
			if not (g.cols().at(t.head.p+side*(.5+speed)) and t.d == 0) and side:
				t.nd = side

		if t.d and g.cols().at(t.head.p+t.d*(.5+speed)):
			t.move((t.dist > .5)-t.dist)
			t.die()

		t.move(speed)

		apple = g.apples.at(t.head.p+t.d*(-.5+speed))
		if apple:
			t.grow()
			apple.p = g.random_tile().p