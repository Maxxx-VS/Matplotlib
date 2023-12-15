import matplotlib.pyplot as plt


input_values = [1, 2, 3, 4, 5] # входные значения
squares = [1, 4, 9, 16, 25] # пораметры по которым строим график

# x_values = [1, 2, 3, 4, 5] # значения для построения точек
# y_values = [1, 4, 9, 16, 25] # значения для построения точек

x_values = list(range(1,  1001)) # значения для построения точек + цикл
y_values = [x**2 for x in x_values] # значения для построения точек + цикл

plt.style.use("ggplot") # стили
fig, ax = plt.subplots() # fig представляет весь рисунок,ax представляет одну диаграмму
#ax.plot(input_values, squares, linewidth=3) # функция построения
#ax.scatter(x_values, y_values, s=10, c=(0.9, 0.5, 0.2))  # построение точек + цвет в формате RGB
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Blues)  # построение точек + цвет градиентом


ax.set_title ("Square Numbers", fontsize=24) # заголовки диаграмм и метки осей
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params (axis='both', labelsize=14) # назначение размера шрифта дления осей

ax.axis([0, 1100, 0, 1100000]) # назначение диапазона для каждой оси

plt.savefig('MPL_diagramm.jpg', bbox_inches='tight')
plt.show() # открывает окно просмотра