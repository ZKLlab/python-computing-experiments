from swampy.TurtleWorld import *


def koch(t, n):
    if n < 3:
        t.fd(n)
        return
    m = n / 3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    koch(t, m)
    t.lt(120)
    koch(t, m)
    t.rt(60)
    koch(t, m)


def snowflake(t, n):
    times = 5
    for i in range(times):
        koch(t, n)
        t.rt(360 / times)


if __name__ == '__main__':
    world = TurtleWorld()
    bob = Turtle()
    bob.delay = 0

    bob.x = -90
    bob.y = 130
    bob.redraw()

    snowflake(bob, 80)

    world.mainloop()
