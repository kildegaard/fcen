from datetime import datetime

time_1 = '2020-05-07T22:28:20'
time_2 = '2020-05-07T22:30:24'
time_3 = '2020-05-07T22:31:34'
time_4 = '2020-05-07T22:33:13'
time_5 = '2020-05-07T22:34:29'
tiempoAux = [time_1, time_2, time_3, time_4, time_5]
tiempo = []
tiempo1 = datetime.strptime(time_1, '%Y-%m-%dT%H:%M:%S')
tiempo2 = datetime.strptime(time_2, '%Y-%m-%dT%H:%M:%S')
for times in tiempoAux:
    tiempo.append(datetime.strptime(times, '%Y-%m-%dT%H:%M:%S'))

print(tiempo1.ctime())
print(tiempo2)
print(round((tiempo2-tiempo1).total_seconds() / 60 / 60 / 24, 2), 'días')

gus =  '1988-06-02'
agus = '1990-03-18'

cumpleGus = datetime.strptime(gus, '%Y-%m-%d')
cumpleAgus = datetime.strptime(agus, '%Y-%m-%d')

print(cumpleGus)
print(cumpleAgus)

dif = str((cumpleAgus - cumpleGus))

diasDif = int(dif[:3])
print(diasDif)

