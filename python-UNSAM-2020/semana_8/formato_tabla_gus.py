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

    def encabezado(self, headers, nombre_archivo_salida):
        file = nombre_archivo_salida + '.html'
        with open(file, 'wt') as f:
            print('<html>', file=f)
            print('<head>', file=f)
            print('<style>', file=f)
            print('''table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th, h1 {
  border: 1px solid #dddddd;
  text-align: center;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}''', file=f)
            print('</style>', file=f)
            print('</head>', file=f)
            print('<body>', file=f)
            print('<h1 style="border:2px solid Tomato">Tabla de resultados</h1>', file=f)
            print('<table style="width:100%">', file=f)
            print('\t<tr>', file=f)
            for h in headers:
                print('\t\t<th>', f'{h:^10s}', '</th>', sep='', file=f)
            print('\t</tr>', file=f)

    def fila(self, data_fila, nombre_archivo_salida):
        file = nombre_archivo_salida + '.html'
        with open(file, 'a') as f:
            print('\t<tr>', end='', file=f)
            for d in data_fila:
                print('\t\t<td>', f'{d:^10s}', '</td>', sep='', end='', file=f)
            print('\t</tr>', file=f)

    def fin_html(self, nombre_archivo_salida):
        file = nombre_archivo_salida + '.html'
        with open(file, 'a') as f:
            print('</table>', file=f)
            print('</body>', file=f)
            print('</html>', file=f)


def crear_formateador(fmt):
    if fmt == 'txt':
        formateador = formato_tabla.FormatoTablaTXT()
    elif fmt == 'csv':
        formateador = formato_tabla.FormatoTablaCSV()
    elif fmt == 'html':
        formateador = formato_tabla.FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {fmt}')
    imprimir_informe(data_informe, formateador)
