import numpy as np
import matplotlib.pyplot as plt

def funcion1():
    archivoEntrada = open('COVID-19.csv', 'r')
    archivoSalida = open('Salida.txt','w')
    
    indice = 0
    for linea in archivoEntrada:
    
        if "Argentina" in linea:
            lineaN = linea.strip('\n').split(',')
            lineaN.insert(0, str(indice))
            indice += 1
            print(lineaN[0], lineaN[1], lineaN[5], lineaN[6], lineaN[10], file = archivoSalida)
        
    archivoEntrada.close()
    archivoSalida.close()
    
def funcion2():
    with open('COVID-19.csv', 'r') as fileI, open('textoSalida2.txt', 'w') as fileO:
        for linea in fileI:
            lineaN = linea.strip('\n')
            
            print(lineaN, file = fileO)
        # print(type(lineaN))
        print(lineaN)

def funcion3():
    with open('Archivito.txt', 'w') as file:
        file.write('hola!')


def infoCovid(pais):
    with open('COVID-19.csv', 'r') as fileI:
        cantCasesTotal = 0
        cantDeathTotal = 0
        for line in fileI:
            if pais.lower() in line.lower():
                lineN = line.split(',')
                cantCasesTotal += int(lineN[4])
                cantDeathTotal += int(lineN[5])
        print('El país', pais, 'tiene', cantCasesTotal, 'casos totales confirmados y', cantDeathTotal, 'muertes totales.')
        
def grafCovid(pais, tipo, funcion):
    with open('COVID-19.csv', 'r') as fileI:
        dailyCases = []
        dailyCasesLog = []
        dailyDeath = []
        dailyDeathLog = []
        totalCases = []
        totalCasesLog = []
        totalCasesN = 0
        totalDeath = []
        totalDeathLog = []
        totalDeathN = 0
        
        for line in fileI:
            if pais.lower() in line.lower():
                lineN = line.split(',')
                dailyCases.append(int(lineN[4]))
                dailyDeath.append(int(lineN[5]))
        dailyCases.reverse()
        dailyDeath.reverse()
        for valor in dailyCases:
            totalCasesN += valor
            totalCases.append(totalCasesN)
        for valor in dailyDeath:
            totalDeathN += valor
            totalDeath.append(totalDeathN)
        
        if tipo == 'diario':
            if funcion == 'lineal':
                plt.plot(range(len(dailyCases)), dailyCases)
                plt.plot(range(len(dailyDeath)), dailyDeath)
                plt.legend(['Casos diarios', 'Muertes diarias'])
            elif funcion == 'log':
                for value in dailyCases:
                    dailyCasesLog.append(value ** 0.5)
                for value in dailyDeath:
                    dailyDeathLog.append(value ** 0.5)
                plt.plot(range(len(dailyCasesLog)), dailyCasesLog)
                plt.plot(range(len(dailyDeathLog)), dailyDeathLog)
                plt.legend(['Casos diarios (log)', 'Muertes diarias (log)'])
        elif tipo == 'total':
            if funcion == 'lineal':
                plt.plot(range(len(totalCases)), totalCases)
                plt.plot(range(len(totalDeath)), totalDeath)
                plt.legend(['Casos diarios', 'Muertes diarias'])
            elif funcion == 'log':
                for value in totalCases:
                    totalCasesLog.append(value ** 0.5)
                for value in totalDeath:
                    totalDeathLog.append(value ** 0.5)
                plt.plot(range(len(totalCasesLog)), totalCasesLog)
                plt.plot(range(len(totalDeathLog)), totalDeathLog)
                plt.legend(['Casos totales (log)', 'Muertes totales (log)'])
        
        


pais = 'united_states'
tipo = 'total'
funcion = 'log'
# pais = 'Afghanistan'
# pais = 'united_states_of_america'

# infoCovid(pais)

grafCovid(pais, tipo, funcion)