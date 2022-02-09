# Ejercicio 8.5

class FormatoTabla(object):
    def encabezado(self, headers):
        """Crea el encabezado de la tabla

        Args:
            headers (list): lista de encabezados

        Raises:
            NotImplementedError: Aún no implementado!
        """
        raise NotImplementedError()

    def fila(self, rowdata):
        """Crea una única fila de datos de la tabla

        Args:
            rowdata (list): lista de datos

        Raises:
            NotImplementedError: Aún no implementado!
        """
        raise NotImplementedError()


class FormatoTablaTXT(FormatoTabla):
    """
    Generar una tabla en formato .txt
    """

    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-' * 10 + ' ') * len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()


class FormatoTablaCSV(FormatoTabla):
    """
    Generar una tabla en formato .csv
    """

    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))


class FormatoTablaHTML(FormatoTabla):
    """
    Generar una tabla en formato .html
    """

    def encabezado(self, headers):
        print('<tr>', end='')
        for h in headers:
            print('<th>', h, '</th>', sep='', end='')
        print('</tr>')

    def fila(self, data_fila):
        print('<tr>', end='')
        for d in data_fila:
            print('<td>', d, '</td>', sep='', end='')
        print('</tr>')


def crear_formateador(fmt):
    if fmt == 'txt':
        formateador = FormatoTablaTXT()
    elif fmt == 'csv':
        formateador = FormatoTablaCSV()
    elif fmt == 'html':
        formateador = FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {fmt}')

    return formateador
