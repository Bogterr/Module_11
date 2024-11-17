###############################   1   ###############################
# import matplotlib.pyplot as plt
#
# fig, ax = plt.subplots()
#
# packet = ['Хлеб', 'Картофель', 'Мясо', 'Молоко']
# counts = [126.5, 100.4, 58.6, 290]
# bar_labels = ['Оранжевый', 'Зеленый', 'Красный', 'Голубой']
# bar_colors = ['tab:orange', 'tab:green', 'tab:red', 'tab:blue']
#
# ax.bar(packet, counts, label=bar_labels, color=bar_colors)
#
# ax.set_ylabel('Продукты в кг')
# ax.set_title('Фрагмент потребительской корзины НСО 2020')
# ax.legend(title='Цвет продукта')
#
# plt.show()
#
#####################################################################
###############################   2   ###############################
#
# import pyautogui as pag
# from PIL import Image
#
#
# name = 'screenshot_exampl_ne_putalos.jpg'
#
# screenshot = pag.screenshot(name)
# print(screenshot)
#
# img = Image.open(name)
#
#
# for i in range(5):
#     img1 = img.resize((800, 600))
#     img2 = img.resize((1200, 800))
#     if i % 2 == 0:
#         img1.convert('L')
#         img1.save(f'{i}_'+ name)
#     else:
#         img2 = img.convert('1')
#         img2.save(f'{i}_' + name)
#
# img.show()
#
#####################################################################
###############################   3   ###############################
import numpy as np

mass = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# for i in range(len(mass)):
#     print(mass[i])
print(mass)

# Единицы, ноли, рандом. (длина массива)
mass_1 = np.ones(5)
print(mass_1)
mass_2 = np.zeros(5)
print(mass_2)
mass_r = np.random.rand(5)
print(mass_r)

# сложение массивов
print(mass_1 + mass_r)
print()
# индексация
print(mass[0])
print(mass[5:])
print(mass[:2])
print()
# Агрегирование
print(f'MAX = {mass_r.max()}\n'
      f'MIN = {mass_r.min()}\n'
      f'Среднее арифметическое = {mass_r.mean()}\n'
      f'Среднеквадратическое = {mass_r.std()}\n'
      f'Перемножение = {mass_r.prod()}\n')

matr = np.ones((5, 5))
print(matr)
print("###################################")
matr_3 = np.ones((5, 5, 5)) # и так далее наращивая объем структуры матрицы
print(matr_3)
