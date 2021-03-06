from z3 import *
import math

n = int(input("Upper bound for triples: "))
X = [Bool("x_%s" % (i + 1)) for i in range(0, n + 1)]

def not_monochrome(x, y, z):
    return And(Or(x, y, z), Not(And(x, y, z)))

solver = Solver()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        hyp_square = i * i + j * j
        k = int(math.sqrt(hyp_square))
        if k * k == hyp_square and k <= n:
            # print("%s^2 + %s^2 = %s^2" % (i, j, k))
            exp = not_monochrome(X[i-1], X[j-1], X[k-1])
            solver.add(exp)
# solver.add(And(X[2], X[3], X[4]))
# print(solver.sexpr())

print(solver.sexpr())
f = open("pyth"+str(n)+".smt2", "w")
f.write('(set-logic QF_UF)\n'+solver.sexpr()+'(check-sat)\n')
f.close()
status = solver.check()
values = {}
print("Result:" + str(status))


input("Press enter to see values...")
if status == sat:
    m = solver.model()
    for i in range(2, n):
        values[i + 1] = m.evaluate(X[i])
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            hyp_square = i * i + j * j
            k = int(math.sqrt(hyp_square))
            if k * k == hyp_square and k <= n:
                print("%s^2 + %s^2 = %s^2; %s, %s, %s" % (i, j, k , values[i], values[j], values[k]))
