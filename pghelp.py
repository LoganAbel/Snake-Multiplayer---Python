import pygame as pg

def keys(k):
	def axis(a,b):
		return (k == a) - (k == b)
	def dual_axis(a,b,c,d):
		return axis(a,b) + axis(c,d) * 1j
	return dual_axis

arrow_keys = [
	[pg.K_RIGHT, pg.K_LEFT, pg.K_DOWN, pg.K_UP],
	[pg.K_d, pg.K_a, pg.K_s, pg.K_w],
	[pg.K_h, pg.K_f, pg.K_g, pg.K_t],
	[pg.K_l, pg.K_j, pg.K_k, pg.K_i],
]

def split_rect(w,h,r):
	h_c = min(h,w/r)
	w_c = h_c*r
	if r < 1:
		w_c = min_c = round(w_c/16)*16
	else:
		h_c = min_c = round(h_c/16)*16

	screen_c = pg.Surface((w_c,h_c))