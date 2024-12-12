from sympy import *

t = symbols('t')
x = Function('x')
y = Function('y')
z = Function('z')

dx = -13*x(t) + 17*y(t) + z(t)
dy = -10*x(t) + 13*y(t)
dz = -2*x(t) + 5*y(t) - z(t)

deq = (Eq(diff(x(t), t), dx), Eq(diff(y(t), t), dy), Eq(diff(z(t), t), dz))
ysoln = dsolve(deq, [x(t), y(t), z(t)], ics={x(0):1, y(0):1, z(0):1}) 
#ics={y(0):1, diff(y(t), t).subs(t, 0):1

print(list(map(lambda x: x.rhs, ysoln)))

#plot(ysoln.rhs, (t, -20, 1))
