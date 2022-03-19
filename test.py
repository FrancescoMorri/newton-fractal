import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial import Polynomial
from numpy.polynomial.polynomial import polyroots
from random import randint
import matplotlib as mlp
from tqdm import tqdm


def newton_method(f, f_d, iter, roots, Re_range, Im_range, precision):
    grid = np.zeros((len(Re_range),len(Im_range)))
    colors = {}
    flag_root = False
    for i,r in enumerate(roots):
        colors[r] = i+1
    for i,x in enumerate(tqdm(Re_range)):
        for j,y in enumerate(Im_range):
            z = complex(x,y)
            for _ in range(iter):
                z -= p(z)/pder(z)
                for r in roots:
                    d = abs(z-r)
                    if d < precision:
                        grid[i,j] = colors[r]
                        flag_root = True
                        break
            if not flag_root:
                grid[i,j] = 0
                flag_root = False
    return grid


print("Max coefficient of polynomial:")
max_coeff = int(input())
coeff = []
for i in range(max_coeff+1):
    print("Insert the coefficient of %d order"%(i))
    coeff.append(int(input()))

title = "Function: "
for i,c in enumerate(coeff):
    if c == 0:
        continue
    title += "%dx^%d + "%(c,i)
    if i == max_coeff:
        title += "%dx^%d"%(c,i)



p = Polynomial(coeff)
pder = p.deriv()

roots = p.roots()

real_range = np.linspace(-2.5,1,500)
imag_range = np.linspace(-1,1,500)

fractal = newton_method(p, pder, 25, roots, real_range, imag_range, 0.1)

fig, ax = plt.subplots()

ax.imshow(fractal)
ax.set_title(title)


plt.show()