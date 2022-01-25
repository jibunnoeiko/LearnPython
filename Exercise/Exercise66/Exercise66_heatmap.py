# Exercise 66 Generating a Heatmap to Visualize the Grades of Students
# ------------------------------------------------------------------------------



# Теперь введите следующий фрагмент кода, чтобы определить функцию тепловой
# карты. Сначала нужно подготовить график:
def heatmap(data, row_labels, col_labels, ax=None, cbar_kw={},
            cbarlabel='',
            **kwargs):
    if not ax:
        ax = plt.gca()
    im = ax.imshow(data, **kwargs)

# Определите цветовую полосу как colorbar, как указано в следующем фрагменте кода:
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va='bottom')

# Показать все галочки и пометить их соответствующими записями в списке:
    ax.set_xticks(np.arange(data.shape[1]))
    ax.set_yticks(np.arange(data.shape[0]))
    ax.set_xticklabels(col_labels)
    ax.set_yticklabels(row_labels)

# Настройте горизонтальные оси так, чтобы метки появлялись поверх графика:
    ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)

# Поверните метки галочек и установите их выравнивание:
#     plt.setp(ax.get_xticklabels(), rotation=-30, ha='right',
             # rotation_mode='anchor')

# Выключите рамку и создайте белую сетку для графика, как указано в следующем
# фрагменте кода:
    for edge, spine in ax.spines.items():
        spine.set_visible(False)

    # ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    # ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which='minor', color='w', linestyle='-', linewidth=3)
    ax.tick_params(which='minor', bottom=False, left=False)

# Вернуть тепловую карту:
    return im, cbar

# Это код, который вы получаете непосредственно из документации matplotlib.
# Функции heatmap помогают генерировать тепловую карту.

# Запустите данную ячейку, а в следующей ячейке введите и выполните следующий код.
# Вы определяете массив numpy для хранения наших данных и строите тепловую карту
# с помощью функций, определенных ранее:

import numpy as np
import matplotlib.pyplot as plt
data = np.array([
    [30, 20, 10,],
    [10, 40, 15],
    [12, 10, 20]
])

# Вы можете видеть, что тепловая карта довольно проста, без какой-либо текстовой
# информации, которая помогла бы нашим читателям понять график. Сейчас вы
# продолжите упражнение и добавите еще одну функцию, которая поможет нам
# аннотировать визуализацию тепловой карты.

# Введите и выполните следующий код в новой ячейке:

def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                     textcolors=["black", "white"],
                     threshold=None, **textkw):
    import matplotlib
    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[im.norm(data[i, j]) > threshold])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts

im, cbar = heatmap(data, ['Class-1', 'Class-2', 'Class-3'],  ['A', 'B', 'C'],
                   cmap='YlGn', cbarlabel='Number of Students')
texts = annotate_heatmap(im, valfmt="{x}")
plt.show()
