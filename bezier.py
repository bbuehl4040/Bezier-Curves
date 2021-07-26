#!python3
# bezier_fun.py - bezier plotting

from matplotlib import pyplot as plt

def get_point(p1, p2, dist):
    return (1-dist) * p1 + (dist * p2)

def get_coord(t, points=[]):
    # base case
    if len(points) < 2:
        return points
    
    # find midpoints between points
    midpoints = []
    i_0 = 0
    i_1 = 1
    while i_1 < len(points):
        m_x = get_point(points[i_0][0], points[i_1][0], t)
        m_y = get_point(points[i_0][1], points[i_1][1], t)
        midpoints.append((m_x, m_y))
        i_0 += 1
        i_1 += 1
    
    point = get_coord(t, midpoints)

    return point


if __name__ == '__main__':
    print('\noutput: \n')

    points = [(0,0), (3.33,0), (0, 10), (10,10)]
    x_positions = []
    y_positions = []
    times = [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1]

    for t in times:
        coord = get_coord(t, points)[0]
        x_positions.append(coord[0])
        y_positions.append(coord[1])

    plt.plot(x_positions, y_positions)
    plt.title("stupid curve")
    plt.xlabel = "X"
    plt.ylabel = "Y"
    plt.show()

    print('\ndone.')
