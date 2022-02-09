# -*- coding: utf-8 -*-
# Ejercicio 8.5 - Un problema de extensibilidad

class FormatoTabla:
    def encabezado(self, headers):
        '''Crea el encabezado de la tabla'''

        raise NotImplementedError()

    def fila(self, rowdata):
        '''Crea una unica fila de datos de la tabla'''

        raise NotImplementedError()

class FormatoTablaTXT(FormatoTabla):
    '''Genera una tabla en formato .txt'''

    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end='  ')
        print()
        print(('-'*10 + '  ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()

class FormatoTablaCSV(FormatoTabla):
    """Genera una tabla en formato .csv"""

    def encabezado(self, headers):
        h = ','.join(headers)
        print(h)

    def fila(self, rowdata):
        print(','.join(rowdata))

class FormatoTablaHTML(FormatoTabla):
    """Genera una tabla en formato HTML"""

    def encabezado(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def fila(self, rowdata):
        print('<tr>', end='')
        for data in rowdata:
            print(f'<td>{data}</td>', end='')


def crear_formateador(nombre):
    """Funcion que devuelve un objeto de Formato"""
    formato = None
    if nombre == 'txt':
        formato = FormatoTablaTXT()
    elif nombre == 'csv':
        formato = FormatoTablaCSV()
    elif nombre == 'html':
        formato = FormatoTablaHTML()
    return formato


def imprimir_tabla(data_informe, atrib, formateador):
    """
    Funcion que imprime tabla del contenido del camion de acuerdo
    a la lista de atributos que se le pase
    """
    formateador.encabezado(atrib)
    for data in data_informe:
        rowdata = [str(getattr(data, colname)) for colname in atrib]
        formateador.fila(rowdata)
