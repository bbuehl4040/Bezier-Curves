#!python3
# bezier_fun.py - bezier plotting

from matplotlib import pyplot as plt

def get_coord(t, t_start, t_stop, start_val, stop_val, ease_out, ease_in):
    # single parameter bezier
    # time on x axis
    t_prog = 1 / (t_stop - t_start) * (t - t_start)
    p1 = (t_start, start_val)
    p4 = (t_stop, stop_val)
    p2 = ((p1[0] + (p4[0] - p1[0]) * ease_out), start_val)
    p3 = ((p1[0] + (p4[0] - p1[0]) * (1 - ease_in)), stop_val)
    
    x = ((1-t_prog)**3 * p1[0]) + (3 * (1-t_prog)**2 * t_prog * p2[0]) + (3 * (1-t_prog) * t_prog**2 * p3[0]) + (t_prog**3 * p4[0])
    y = ((1-t_prog)**3 * p1[1]) + (3 * (1-t_prog)**2 * t_prog * p2[1]) + (3 * (1-t_prog) * t_prog**2 * p3[1]) + (t_prog**3 * p4[1])
    
    print(f'x: {x}, y: {y}, t_prog: {t_prog}, p1: {p1}, p2: {p2}, p3: {p3}, p4: {p4}')

    return (x,y)

def get_coord2(t, p1, p2):
    x = ((1-t) * p1[0]) + (t * p2[0])
    y = ((1-t) * p1[1]) + (t * p2[1])

    return int(x), int(y)

def get_coord4(t, p1, p2, p3, p4):
    x = ((1-t)**3 * p1[0]) + (3 * (1-t)**2 * t * p2[0]) + (3 * (1-t) * t**2 * p3[0]) + (t**3 * p4[0])
    y = ((1-t)**3 * p1[1]) + (3 * (1-t)**2 * t * p2[1]) + (3 * (1-t) * t**2 * p3[1]) + (t**3 * p4[1])

    return round(x,2), round(y,2)
    
def easeCustom(t, t_start, t_stop, p1, p4, ease_out, ease_in):
    # 1/duration * (distance from animation start)
    t_trans = 1 / (t_stop-t_start) * (t - t_start)

if __name__ == '__main__':
    print('\noutput: \n')
    positions = 30
    x_positions = []
    y_positions = []

    # animation starts at 2s and goes to 7s
    times = [2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7]
    for t in times:
        x, y = get_coord(t, 2, 7, 0, 10, .4, 1)
        x_positions.append(x)
        y_positions.append(y)

    # for i in range(positions+1):
    #     t = i / positions
    #     # x, y = get_coord4(t, (3,10), (10,0), (0,0), (7,10))
    #     # x, y = get_coord4(t, (0,0), (3,0), (0,10), (10,10))
    #     x, y = get_coord2(t, (0,0), (10,10))
    #     x_positions.append(x)
    #     y_positions.append(y)

    plt.plot(x_positions, y_positions)
    plt.title("stupid curve")
    plt.xlabel = "Time"
    plt.ylabel = "Parameter"
    plt.show()

    print('\ndone.')