import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    koka = pg.image.load("fig/3.png")
    koka=pg.transform.flip(koka,True,False)
    bg_img2=pg.transform.flip(bg_img,True,False)
    tmr = 0
    x=0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        x=tmr%3200
        screen.blit(bg_img, [-x,0])
        screen.blit(bg_img2, [-x+1600,0])
        screen.blit(bg_img, [-x+3200,0])
        screen.blit(bg_img2, [-x+4800,0])
        kk=koka.get_rect()##場所取得
        ba=kk.center =300,200
        screen.blit(koka, ba)##baのところに描画
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()