#!/usr/bin/env python
# coding: utf-8

# # Pappus hexagon theorem
# 
# This is an attempt to use Z3 to prove the _Pappus Hexagon theorem_ from Euclidean geometry. Our first step is to define collinearity.
def collinear(ax, ay, bx, by, cx, cy):
    return (cx - ax) * (by - ay) == (bx - ax) * (cy - ay)

from z3 import *
set_param('parallel.enable', True)
enable_trace('Pappus: ')

def distinct(x1, y1, x2, y2):
        return Or(x1 != x2, y1 != y2)

Px = Real('Px')
Qx = Real('Qx')
Rx = Real('Rx')
Py = Real('Py')
Qy = Real('Qy')
Ry = Real('Ry')
s = Solver()

def check(ax, ay, bx, by, cx, cy, Ax, Ay, Bx, By, Cx, Cy, add_distinct = True, saveable = False):
    


    # First that $a$, $b$, $c$ are collinear, as are $A$, $B$, $C$.
    s.add(collinear(ax, ay, bx, by, cx, cy))
    s.add(collinear(Ax, Ay, Bx, By, Cx, Cy))

    # Next, to say that $P$, $Q$ and $R$ are appropriate intersection points, we add collinearity conditions.
    s.add(collinear(ax, ay, Px, Py, Bx, By))
    s.add(collinear(Ax, Ay, Px, Py, bx, by))

    s.add(collinear(ax, ay, Qx, Qy, Cx, Cy))
    s.add(collinear(Ax, Ay, Qx, Qy, cx, cy))

    s.add(collinear(bx, by, Rx, Ry, Cx, Cy))
    s.add(collinear(Bx, By, Rx, Ry, cx, cy))


    # We now add a contradiction by assuming $P$, $Q$ and $R$ are not collinear.
    s.add(Not(collinear(Px, Py, Qx, Qy, Rx, Ry)))

    def addDistinct():
        xs = [ax, bx, cx, Ax, Bx, Cx]
        ys = [ay, by, cy, Ay, By, Cy]
        for i in range(0, 6):
            for j in range(0, 6):
                if i != j:
                    s.add(distinct(xs[i], ys[i], xs[j], ys[j]))

    if add_distinct:
        addDistinct()


    print("Added all conditions, seeking satisfyability")
    if saveable:
        output = s.sexpr()+'(check-sat)\n'
        print(output)
        f = open("pappus.smt2", "w")
        f.write(output)
        f.close()
    result = s.check()
    print('The conditions are: % s' % result)
    return result

def general():    
    ax = Real('ax')
    bx = Real('bx')
    cx = Real('cx')
    Ax = Real('Ax')
    Bx = Real('Bx')
    Cx = Real('Cx')
    ay = Real('ay')
    by = Real('by')
    cy = Real('cy')
    Ay = Real('Ay')
    By = Real('By')
    Cy = Real('Cy')

    check(ax, ay, bx, by, cx, cy, Ax, Ay, Bx, By, Cx, Cy)

import random
def pick_rational(n):
        return Q(random.randint(0, n), n)
def randomPoints(n):
    ax = pick_rational()
    ay = pick_rational()
    Ax = pick_rational()
    Ay = pick_rational()
    bx = pick_rational()
    by = pick_rational()
    Bx = pick_rational()
    By = pick_rational()
    cx = Real('cx')
    cy = Real('cy')
    Cx = Real('Cx')
    Cy = Real('Cy')

    check(ax, ay, bx, by, cx, cy, Ax, Ay, Bx, By, Cx, Cy)

# Assume that the lines intersect at the origin and one is horizontal. The latter means that y coordinates of A, B, C vanish
# Further coordinates of b and c are determined by a scale.
def good_coordinates():
    ax = Real('ax')
    b_scale = Real('b_scale')
    c_scale = Real('c_scale')
    bx = ax * b_scale
    cx = ax * c_scale
    Ax = Int(1)
    Bx = Real('Bx')
    Cx = Real('Cx')
    ay = Real('ay')
    by = ay * b_scale
    cy = ay * c_scale
    Ay = Int(0)
    By = Int(0)
    Cy = Int(0)
    s.add(Int(1) < b_scale)
    s.add(b_scale < c_scale)
    s.add(Int(0)< ax)
    s.add(Int(0)< ay)

    check(ax, ay, bx, by, cx, cy, Ax, Ay, Bx, By, Cx, Cy, False, True)

good_coordinates()
# randomPoints(100)