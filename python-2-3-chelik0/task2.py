'''
Наибольшая средняя температура
Highest Average Temperature

Напишите программу, которая принимает имя файла и обрабатывает содержимое 
CSV-файла. Содержимым будет месяц метеоданных, одна строка CSV-файла 
представляет собой один день.

Ваша программа должна определить, в какой день было наибольшее среднее значение 
температуры, где среднее значение температуры это среднее значение наибольшей и 
наименьшей температуры. Это не обычное вычисление средней температуры, но оно 
будет работать для данного демонстрационного примера.

Первая строка CSV-файла будет содержать названия столбцов:

Day,MaxT,MinT,AvDP,1HrP TPcn,PDir,AvSp,Dir,MxS,SkyC,MxR,Mn,R AvSLP
1,88,59,74,53.8,0,280,9.6,270,17,1.6,93,23,1004.5

День,максимальная температура, и минимальная температура - первые три столбца.
'''


import csv


'''
Напишите функцию get_next_day_and_avg, которая принимает на вход имя файла и
возвращает генератор, который возвращает пары (день, средняя температура) для каждого
дня метеоданных.
'''
def get_next_day_and_avg(csv_file):
    spamreader = csv.reader(csv_file, delimiter=',', quotechar='|')
    for row in spamreader:
        row = [i.strip() for i in row]
        if len(row) == 0:
            continue
        elif row[0] == "Day":
            continue
        
        max_avg_T = (int(row[1])+int(row[2]))/2
        yield int(row[0]), int(max_avg_T) if max_avg_T%1==0 else float(max_avg_T)

'''
Напишите функцию get_max_avg, которая принимает на вход имя файла и возвращает
пару (день, средняя температура) с максимальной средней температурой.
'''
def get_max_avg(filename):
    with open(file=str(filename), mode='r', encoding='utf-8') as file:
        spamreader = csv.reader(file, delimiter=' ', quotechar='|')
        for i, row in enumerate(spamreader):
            if i == 0:
                continue
            row = row[0].split(',')
            return int(row[0]), (int(row[1])+int(row[2]))/2