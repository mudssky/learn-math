import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, Tuple, List


def generate_colors(num_colors: int):
    '''
        生成任意数量的均匀分布的颜色列表
        '''
    rgb_colors = []
    count = 0
    while count < num_colors:
        # 生成三个 0 到 255 之间的随机整数
        r, g, b = np.random.randint(0, 256, size=(3))
        # 将颜色转换为字符串表示，例如 "#FF0000"
        color = "#{:02X}{:02X}{:02X}".format(r, g, b)
        # 如果颜色不在已用颜色列表中，则返回该颜色
        if color not in rgb_colors:
            rgb_colors.append(color)
            count += 1

    # 生成均匀分布的颜色值
    # hues = np.linspace(0, 1, num_colors + 1)[:-1]
    # saturations = np.ones(num_colors)
    # values = np.ones(num_colors)

    # # 转换为 RGB 颜色
    # hsv_colors = np.column_stack((hues, saturations, values))
    # rgb_colors = np.array([np.array(color) for color in hsv_colors])
    return rgb_colors


def paint_vectors2d(vectorlist: List[Dict[str, Tuple[float, float]]]):
    '''
    绘制多个向量，用列表传入
    {
    'start':(0,0),
    'v':(1,1)
    }
    起点默认是原点
    '''
    v_count = len(vectorlist)
    color_list = generate_colors(v_count)
    # 创建绘图对象
    fig, ax = plt.subplots()
    # 边框置于原点
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    max = 5
    for vector_dict in vectorlist:
        start_point = np.array([0, 0])
        if 'start' in vector_dict:
            start_point = vector_dict['start']
        vv = start_point+vector_dict['v']
        vmax = np.max(np.abs(vv))
        if vmax > max:
            max = vmax
    # print(f'max:{max}')
    # 设置坐标轴范围
    ax.set_xlim([-max, max])
    ax.set_ylim([-max, max])
    # print(f'colorlist:{color_list}')
    for index, vector_dict in enumerate(vectorlist):
        vector = vector_dict['v']
        start_point = np.array([0, 0])
        if 'start' in vector_dict:
            start_point = vector_dict['start']
        ax.quiver(start_point[0], start_point[1], vector[0], vector[1], angles='xy',
                  scale_units='xy', scale=1, color=color_list[index],
                  label=np.array2string(vector))
    plt.legend()
    plt.show()


def paint_vector2d(vector):
    paint_vectors2d([{'v': vector}])
