# %%
def propagar_al_vecino(l):
    modif = False
    n = len(l)
    for i, e in enumerate(l):
        if e == 1 and i < n-1 and l[i+1] == 0:
            l[i+1] = 1
            modif = True
        if e == 1 and i > 0 and l[i-1] == 0:
            l[i-1] = 1
            modif = True
    return modif


def propagar(l):
    m = l.copy()
    veces = 0
    while propagar_al_vecino(l):
        veces += 1

    print(f"Repetí {veces} veces la función propagar_al_vecino.")
    print(f"Con input {m}")
    print(f"Y obtuve  {l}")
    return l


# %%
propagar([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
# propagar([0, 0, 1, 0, 0])
# propagar([1, 0, 0, 0, 0])
