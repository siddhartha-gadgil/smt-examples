#!/usr/bin/env python
# coding: utf-8

# # Pappus hexagon theorem
# 
# This is an attempt to use Z3 to prove the _Pappus Hexagon theorem_ from Euclidean geometry. Our first step is to define collinearity.
def collinear(ax, ay, bx, by, cx, cy):
    return (cx - ax) * (by - ay) == (bx - ax) * (cy - ay)

from z3 import *

ax = Real('ax')
bx = Real('bx')
cx = Real('cx')
Ax = Real('Ax')
Bx = Real('Bx')
Cx = Real('Cx')
Px = Real('Px')
Qx = Real('Qx')
Rx = Real('Rx')
ay = Real('ay')
by = Real('by')
cy = Real('cy')
Ay = Real('Ay')
By = Real('By')
Cy = Real('Cy')
Py = Real('Py')
Qy = Real('Qy')
Ry = Real('Ry')


# We setup a solver to add conditions.
s = Solver()


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

# print("Sanity check: some conditions satisfied")
# print(s.check())

# We now add a contradiction by assuming $P$, $Q$ and $R$ are not collinear.
s.add(Not(collinear(Px, Py, Qx, Qy, Rx, Ry)))

def distinct(x1, y1, x2, y2):
    return Or(x1 != x2, y1 != y2)

xs = [ax, bx, cx, Ax, Bx, Cx]
ys = [ay, by, cy, Ay, By, Cy]
for i in range(0, 6):
    for j in range(0, 6):
        if i != j:
            s.add(distinct(xs[i], ys[i], xs[j], ys[j]))

print("Added all conditions, seeking satisfyability")
s.smtlib2_log="filename.smt2" 
print(s.sexpr())
f = open("pappus.smt", "w")
f.write(s.sexpr())
result = s.check()
print(result)