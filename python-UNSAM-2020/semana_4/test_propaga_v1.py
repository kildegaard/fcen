import propaga_v1 as p


def test_propagar():
    lista1 = [0, 0, 0, 0, 1]
    lista2 = [0, 0, 1, 0, 0]
    lista3 = [1, 0, 0, 0, 0]

    assert p.propagar(lista1) == [1, 1, 1, 1, 1]
    assert p.propagar(lista2) == [1, 1, 1, 1, 1]
    assert p.propagar(lista3) == [1, 1, 1, 1, 1]
