import numpy as np
from pt import point

class initior:
    def __init__(self, type_of_distr):
        self.type_of_distr = type_of_distr
        
    def heat_distr(self, x, y, x_num, y_num):
        if((x - x_num//2)*(x - x_num//2) + (y - y_num//2)*(y-y_num//2) < x_num*x_num//36 + y_num*y_num//36):
            return 1
        return 0.01

    
    # def heat_distr(self, x, y, x_num, y_num):

    #     if(x_num/24 < x and x < x_num//12 and y_num/24 < y and y < y_num//12):
    #         return 1
    #     if(22*x_num//24 < x and x < 23*x_num//24 and 22*y_num//24 < y and y < 23*y_num//24):
    #         return -1
    #     return 0.01
        
    # def heat_distr(self, x, y, x_num, y_num):

    #     if(x < x_num//8):
    #         return 1
    #     if(x > 3*x_num//8):
    #         return -1
    #     return 0.01
        
    # def heat_distr(self, x, y, x_num, y_num):
    #     return x*(x_num//2 - x)*y*(y_num//2 - y)/(x_num*x_num*y_num*y_num)


    def init_cur_mesh(self, x_num, y_num):
        mesh = np.empty((x_num, y_num), dtype=point)
        for x in range(0, x_num):
            for y in range(0, y_num):
                mesh[x, y] = point(self.heat_distr(x, y, x_num, y_num), x, y)
        return mesh
    
    def init_prev_mesh(self, x_num, y_num):
        mesh = np.empty((x_num, y_num), dtype=point)
        for x in range(0, x_num):
            for y in range(0, y_num):
                mesh[x, y] = point(0, x, y)
        return mesh

