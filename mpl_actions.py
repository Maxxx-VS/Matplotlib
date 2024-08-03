import matplotlib.pyplot as plt #библиотека для построения графиков, изучим в следующей части урока
import numpy as np #библиотека для работы с векторами и матрицами, изучим в следующей части урока
import datetime #библиотека для работы с датой

# Функция скользящей средней
def moving_average(a, n = 3): # аргумент n - период скользящей средней, задаем по умолчанию равным 3, в нашем случае 3 месяца
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / float(n)


x = np.array([datetime.datetime(2023, i, 1, 0, 0) for i in range(1, 13)]) # создаем диапазон из 12 месяцев
y = np.random.randint(50, 62, size=x.shape) # Для каждой даты (х) задаем случайную точку в диапазоне (50, 62)
z= moving_average(y) # рассчитываем скользящую среднюю к стоимости акций

fig, ax = plt.subplots(figsize=(9, 6)) # Задаем область рисования
ax.set_title("Соотношение положительных отзывов о компании к цене ее акций", fontsize=16) # Устанавливаем заголовок графика
ax.set_xlabel("Дата", fontsize=14) # Задаем подпись оси Х (снизу)
ax.set_ylabel("Цена за акцию", fontsize=14) # Задаем область оси Y (слева)

ax2 = ax.twinx() # Объявляем вторую ось
ax2.set_ylabel("Отношение к компании") # Задаем подпись для второй оси Y (справа)

ax.plot(x, y, 'r-') # Рисуем первый график красным цветом
z1 = z / max(z) # скользящую среднюю нормируем, т.е. делим на максимальное значение (приводим ее к интервалу от 0 до 1)
# z1 - имеет меньшее число точек чем (х), так как скользящая средняя запаздывает, поэтому разницу заполним нормированным значение цен акций
y1 = y[0: len(x)-len(z)]/max(y) # Берем столько нормированных цен акций сколько не хватает на точек
Y = np.concatenate([y1, z1]) # Объединяем 2 диапазона нормированные цены акций и нормированную скользящую среднюю

ax2.plot(x, Y, 'g-') # Рисуем второй график зеленым цветом.

ax.legend(['Цена за акцию'], loc = 'upper left') # Задаем легенду для первого графика цен
ax2.legend(['Отношение к компании'], loc = 'upper right') # Задаем легенду для второго графика отношений
plt.show() # Отображаем на экране область рисования