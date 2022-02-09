def propagar_a_derecha(m):
    l = m.copy()
    n = len(l)
    for i, e in enumerate(l):
        if e == 1 and i < n-1:
            if l[i+1] == 0:
                l[i+1] = 1
    return l
# %


def propagar_a_izquierda(l):
    return propagar_a_derecha(l[::-1])[::-1]
# %


def propagar(l):
    ld = propagar_a_derecha(l)
    lp = propagar_a_izquierda(ld)
    return lp


# %%
l = [0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]
print("Estado original:  ", l)
print("Propagando...")
lp = propagar(l)
print("Estado original:  ", l)
print("Estado propagado: ", lp)
