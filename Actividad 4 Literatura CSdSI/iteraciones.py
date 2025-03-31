with open('iteraciones.txt', 'r') as fichero:
    for linea in fichero.readlines():
        print(linea, end='')

    from datetime import datetime
    datetime.strptime('2012-02-10' , '%Y-%m-%d')
datetime.datetime(2012, 2, 10, 0, 0)

from datetime import date

def diff_dates(date1, date2):
    return abs(date2-date1).days
def main():
    d1 = date(2013,1,1)
    d2 = date(2013,9,13)
    result1 = diff_dates(d2, d1)
    print('{} days between {} and {}'.format(result1, d1, d2))
    print("Happy programmer's day!")

main()

#Contenido de la primera línea
#Contenido de la segunda línea
#Contenido de la tercera línea
#Contenido de la cuarta línea