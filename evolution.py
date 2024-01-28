import numpy as np
from pt import point
from conv import converter
from init import initior




def evolved_point(x, y, mesh):

    k = 0.25
    x_num, y_num = mesh.shape

    if(0 < x and 0 < y and x < x_num  - 1 and y < y_num - 1):
        left = mesh[x - 1][y]
        right = mesh[x + 1][y]
        up = mesh[x][y + 1]
        down = mesh[x][y - 1]
        cur = mesh[x][y]
        next_heat = cur.heat + k*(left.heat + right.heat + up.heat + down.heat - 4*cur.heat)
        return point(next_heat, cur.x_num, cur.y_num)
    return mesh[x][y]


def evol_step(x_num, y_num, mesh):
    next_mesh = np.empty((x_num, y_num), dtype=point)
    for x in range(0, x_num):
        for y in range(0, y_num):
            next_mesh[x, y] = evolved_point(x, y, mesh)

    return next_mesh



def evolution(mesh, t_num):
    x_num, y_num = mesh.shape
    con = converter()
    for t in range (0, t_num):
        con.mesh_to_bin(t, mesh)
        mesh = evol_step(x_num, y_num, mesh)
    print('evolution is over')


def main():
    t_num=2000
    x_num=480
    y_num=360


    ior = initior(0)

    mesh = ior.init_mesh(x_num, y_num)
    evolution(mesh, t_num)
    con = converter()

    for t in range (0, t_num):
        con.bin_mesh_to_jpg(t)

    con.jpg_to_gif(t_num)


if __name__ == "__main__":
    main()


