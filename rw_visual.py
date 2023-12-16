import matplotlib.pyplot as plt
from random_walk import RandomWalk

# построение случайного блуждания
while True:
    rw = RandomWalk()
    rw.fill_walk()

    # нанеение точек на диаграму
    plt.style.use("ggplot")
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, s=10, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none')
    plt.savefig('MPL_points.jpg', bbox_inches='tight')

    # выделение первой и последней точки
    ax.scatter(0, 0, c='green', s=50, cmap=plt.cm.Blues, edgecolors='none')
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)

    # удаление осей
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make anower walk? (y/n): ")
    if keep_running == 'n':
        break