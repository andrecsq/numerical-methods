import sympy as sp
import numpy as np

p = np.array([2.,3.])
f = np.array([0.39,0.18])
df = np.array([0.4,0.1])
h1 = p[1]-p[0]
eval_at = 2.5

print("p: ", p)
print("f: ", f)
print("df: ", df)
print()

x = sp.Symbol('x')
x0 = sp.Symbol('x0')
x1 = sp.Symbol('x1')
h = sp.Symbol('h')

phi = []
phi.append((1 + 2*(x-x0)/h)*((x-x1)**2)/h**2)
phi.append((1 - 2*(x-x1)/h)*((x-x0)**2)/h**2)

psi = []
psi.append((x-x0)*((x-x1)**2)/h**2)
psi.append((x-x1)*((x-x0)**2)/h**2)

for i in range(len(phi)):
    print(f"phi[{i}]: ", phi[i])
    phi[i] = phi[i].subs({x0: p[0], x1: p[1], h: h1})
    print(f"phi[{i}]: ", phi[i])
    phi[i] = phi[i].evalf()
    print(f"phi[{i}]: ", phi[i])
    phi[i] = sp.expand(phi[i])
    print(f"phi[{i}]: ", phi[i])
    print()
    
    print(f"psi[{i}]: ", psi[i])
    psi[i] = psi[i].subs({x0: p[0], x1: p[1], h: h1})
    print(f"psi[{i}]: ", psi[i])
    psi[i] = psi[i].evalf()
    print(f"psi[{i}]: ", psi[i])
    psi[i] = sp.expand(psi[i])
    print(f"psi[{i}]: ", psi[i])
    print()
    
h = f[0]*phi[0] + f[1]*phi[1] + df[0]*psi[0] + df[1]*psi[1]
print("h(x) = ", h)
print(f"h({eval_at}) = ", h.subs({x: eval_at}).evalf())

print()

h_dx = sp.diff(h, x)
print("h'(x) = ", h_dx)
h_dx = sp.diff(h, x)
print(f"h\'({eval_at}) = ", h_dx.subs({x: eval_at}).evalf())

# print()
# print("phi_1: ", phi_1)
# phi[i] = phi[i].subs({x0: p[0], x1: p[1], h: h1})
# print("phi[i]: ", phi_1)
# phi_1 = phi[i].evalf()
# print("phi[i]: ", phi_1)
# phi_1 = sp.expand(phi_1)
# print("phi[i]: ", phi_1)

# print(phi[i].subs({x0: p[0], x1: p[1], h: h1}).evalf())

# print(phi[i])
# print(phi_1)