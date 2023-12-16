import matplotlib.pyplot as plt
from random_walk import RandomWalk

# построение случайного блуждания
while True:
    rw = RandomWalk()
    rw.fill_walk()

    # Нанеение точек на диаграму
    plt.style.use("ggplot")
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=5)
    plt.savefig('MPL_points.jpg', bbox_inches='tight')
    plt.show()
    keep_running = input("Make anower walk? (y/n)")
    if keep_running == 'n':
        break