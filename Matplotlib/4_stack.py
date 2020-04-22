import matplotlib.pyplot as plt

plt.style.use("ggplot")

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

plt.stackplot(minutes, player1, player2, player3,
              labels=['P1', 'P2', 'P3'])

plt.legend(loc='upper left')	# loc=[0.07, 0.05]

plt.title("Stack Plot")

plt.tight_layout()

plt.savefig('img/4.png', dpi=300)

plt.show()
