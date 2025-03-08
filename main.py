import pygame as py

from classeeee import Bag

from classeeee import Cherep

py.init()
w = py.display.set_mode((600, 600))
FPS = 60
clock = py.time.Clock()
gr = py.sprite.Group()
bag = Bag(gr)
ch = py.sprite.Group()
for i in range(100):
    Cherep(ch)
while True:
    w.fill((13, 145, 80))
    clock.tick(FPS)
    ch.draw(w)
    ch.update()
    gr.draw(w)
    gr.update()
    py.display.update()
    hits = py.sprite.spritecollide(bag, ch, True, py.sprite.collide_circle)
    print(hits)
    for s in ch:
        if s.rect.y > 600:
            exit()
    for event in py.event.get():
        if event.type == py.QUIT:
            exit()


