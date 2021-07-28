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

def get_graph(t, start_t, end_t, val_1, val_2, ease_out, ease_in):
    dur = end_t - start_t                               # duration of animation
    completion = (t - start_t) / dur                    # % through animation
    if t < start_t:
        return [(t, val_1)]
    if t > end_t:
        return [(t, val_2)]
    p1 = (start_t, val_1)                               # starting point
    p2 = (start_t + (dur * ease_out), val_1)            # bezier handle - ease out
    p3 = (start_t + (dur *  (1 - ease_in)), val_2)      # bezier handle - ease in
    p4 = (end_t, val_2)                                 # end point

    print(p1, p2, p3, p4)
    return get_coord(completion, [p1, p2, p3, p4])
    


if __name__ == '__main__':
    print('\noutput: \n')

    points = [(0,0), (0,0), (0, 1), (10,1)]
    x_positions = []
    y_positions = []
    times = [0, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 10]
    p = 10
    # for i in range(p+1):
    #     t = round(((1/p) * i), 1) 
    for i in times:
        t = i
        #coord = get_coord(t, points)[0]
        coord = get_graph(t, 2, 7, 10, 20, .5, .1)[0]
        x_positions.append(coord[0])
        y_positions.append(coord[1])
        print(f't: {t}, X: {round(coord[0], 2)} | Y: {round(coord[1], 2)}')

    plt.plot(x_positions, y_positions)
    plt.title("stupid curve")
    plt.xlabel = "X"
    plt.ylabel = "Y"
    plt.show()

    print('\ndone.')
