import numpy as np
from pt import point

class initior:
    def __init__(self, type_of_distr):
        self.type_of_distr = type_of_distr
        
    def heat_distr(self, x, y, x_num, y_num):

        if(x < x_num//4 and y < y_num//4):
            return 1
        if(x > 3*x_num//4 and y > 3*y_num//4):
            return -1
        return 0.01
        
    # def heat_distr(self, x, y, x_num, y_num):

    #     if(x < x_num//8):
    #         return 1
    #     if(x > 3*x_num//8):
    #         return -1
    #     return 0.01


    def init_mesh(self, x_num, y_num):
        mesh = np.empty((x_num, y_num), dtype=point)
        for x in range(0, x_num):
            for y in range(0, y_num):
                mesh[x, y] = point(self.heat_distr(x, y, x_num, y_num), x, y)
        return mesh

