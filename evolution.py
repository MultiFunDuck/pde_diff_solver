import numpy as np
from pt import point
from conv import converter
from init import initior


class evolutor:
    def __init__(self, init_cur_mesh, init_prev_mesh):
        self.cur_mesh = init_cur_mesh
        self.prev_mesh = init_prev_mesh


    def evolution(self, t_num):
        x_num, y_num = self.cur_mesh.shape
        con = converter()
        
        for t in range (0, t_num):
            con.mesh_to_bin(t, self.cur_mesh)
            buf_mesh = self.evol_step(x_num, y_num)
            self.prev_mesh = self.cur_mesh
            self.cur_mesh = buf_mesh

    def evol_step(self, x_num, y_num):
        next_mesh = np.empty((x_num, y_num), dtype=point)
        for x in range(1, x_num - 1):
            for y in range(1, y_num - 1):
                next_mesh[x, y] = self.evolved_point(x, y)
        for x in range (0, x_num):
            next_mesh[x, 0] = point(0, x, 0)
            next_mesh[x, y_num - 1]  = point(0, x, y_num - 1)
        for y in range (1, y_num):
            next_mesh[0, y] = point(0, 0, y)
            next_mesh[x_num - 1, y]  = point(0, x_num - 1, y)
        return next_mesh

    def evolved_point(self, x, y):
        # sub_prev_mesh = self.prev_mesh[x - 1:x + 2, y - 1:y + 2]
        # sub_cur_mesh = self.cur_mesh[x - 1:x + 2, y - 1:y + 2]
        # next_heat = self.evolve_func(sub_cur_mesh, sub_prev_mesh)

        next_heat = self.evolve_func(x, y)
        return point(next_heat, x, y)
    
    def evolve_func(self, x, y):
        k = 0.2
        return (2*self.cur_mesh[x, y].heat - self.prev_mesh[x, y].heat) + k*(self.cur_mesh[x - 1, y].heat + self.cur_mesh[x + 1, y].heat + self.cur_mesh[x, y - 1].heat + self.cur_mesh[x, y + 1].heat - 4*self.cur_mesh[x, y].heat)

    # def evolve_func(self, cur, prev):
    #     k = 0.1
    #     return (2*cur[0,0].heat - prev[0,0].heat) + k*(cur[-1,0].heat + cur[1,0].heat - 2*cur[0,0].heat)


def main():
    t_num=500
    x_num=120
    y_num=120


    ior = initior(0)

    cur_mesh = ior.init_cur_mesh(x_num, y_num)
    prev_mesh = ior.init_prev_mesh(x_num, y_num)

    ev = evolutor(cur_mesh, prev_mesh)
    print('evolution starts')
    ev.evolution(t_num)
    con = converter()


    print('converting to jpg')
    for t in range (0, t_num):
        con.bin_mesh_to_jpg(t)

    print('generating gif')
    con.jpg_to_gif(t_num)


if __name__ == "__main__":
    main()


