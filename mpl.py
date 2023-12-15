import matplotlib.pyplot as plt


input_values = [1, 2, 3, 4, 5] # входные значения
squares = [1, 4, 9, 16, 25] # пораметры по которым строим график

plt.style.use("ggplot") # стили
fig, ax = plt.subplots() # fig представляет весь рисунок,ax представляет одну диаграмму
ax.plot(input_values, squares, linewidth=3) # функция построения
ax.scatter(2, 4, s=200)  # построение точки


ax.set_title ("Square Numbers", fontsize=24) # заголовки диаграмм и метки осей
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params (axis='both', labelsize=14) # назначение размера шрифта дления осей

plt.show() # открывает окно просмотра