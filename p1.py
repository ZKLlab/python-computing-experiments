import math

try:
    from swampy.TurtleWorld import *
except ImportError:
    # noinspection PyUnresolvedReferences
    from TurtleWorld import *


def square(t, length):
    for i in range(4):
        t.fd(length)
        lt(t)


def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    """Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0 / n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle / 2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle / 2)


def circle(t, r):
    """Draws a circle with the given radius.

    t: Turtle
    r: radius
    """
    arc(t, r, 360)


def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0 / n)


def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)


def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()


def move_draw(t, length):
    t.pd()
    t.fd(length)


def turn_round(t):
    t.rt()
    t.rt()


def leaf(t, r, angle):
    bob.rt()
    petal(t, r, -angle)
    turn_round(t)
    petal(t, r, angle)


def plant():
    bob.lt()
    move(bob, 50)
    flower(bob, 10, 60.0, 80.0)
    turn_round(bob)
    move_draw(bob, 115)
    leaf(bob, 40, 90)
    bob.rt()
    move_draw(bob, 20)
    move(bob, 60)


def emotion():
    # 脸
    radius1 = 60
    bob.pu()
    bob.fd(radius1)
    bob.lt()
    bob.pd()
    circle(bob, radius1)

    # 嘴
    radius2 = 50
    bob.pu()
    bob.lt()
    bob.fd(radius1 - radius2)
    bob.lt()
    bob.pd()
    arc(bob, radius2, -180)
    bob.rt()
    bob.fd(radius2 * 2)

    # 牙
    count = 4
    k = radius2 / (count + 1) * 2
    for j in range(count):
        bob.pu()
        bob.bk(k)
        bob.rt()
        bob.pd()
        width = (radius2 ** 2 - (radius2 - (j + 1) * k) ** 2) ** 0.5
        bob.fd(width)
        bob.pu()
        bob.bk(width)
        bob.lt()

    # 眼
    radius3 = 15
    bob.lt()
    bob.fd(24)
    bob.rt()
    bob.fd(radius3)
    bob.lt()
    bob.pd()
    arc(bob, radius3, 180)
    bob.pu()
    bob.lt()
    bob.fd(radius3 * 2 + k * 3)
    bob.lt()
    bob.pd()
    arc(bob, radius3, 180)
    bob.pu()

    # 眉
    radius4 = 6
    bob.lt()
    bob.fd(radius3)
    bob.lt()
    bob.fd(24)
    bob.rt()
    bob.fd(radius4)
    bob.lt()
    bob.pd()
    arc(bob, radius4, 180)
    bob.pu()
    bob.rt()
    bob.fd(k * 3 - radius4 * 2)
    bob.rt()
    bob.pd()
    arc(bob, radius4, 180)
    bob.pu()


if __name__ == '__main__':
    world = TurtleWorld()

    bob = Turtle()
    bob.delay = 1e-5

    bob.lt()
    bob.pu()
    move(bob, 40)
    bob.rt()

    plant()

    bob.lt()

    emotion()

    # 溜
    bob.rt()
    bob.fd(200)

    wait_for_user()
