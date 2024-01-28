import numpy as np
from PIL import Image
import imageio
from datetime import datetime



class converter:

    bin_path = 'mesh_bin/'
    jpg_path = 'mesh_jpg/'
    gifs_path = 'gifs/'
    file_name = 'evol_'

    def __init__(self, bin_path = 'mesh_bin/', jpg_path = 'mesh_jpg/', file_name = 'evol_'):  
        self.bin_path = bin_path  
        self.jpg_path = jpg_path  
        self.file_name = file_name 



    def mesh_to_bin(self, step, mesh):
        np.save(self.bin_path + self.file_name + str(step), mesh, allow_pickle=True)

    def get_heat_map(self, mesh):
        x_num, y_num = mesh.shape
        heat_map = np.empty((x_num, y_num))
        for x in range(0, x_num):
            for y in range(0, y_num):
                heat_map[x][y] = mesh[x][y].heat
        return heat_map

    def scale_heat_map(self, heat_map):
        max_heat = np.amax(heat_map)
        min_heat = np.amin(heat_map)
        scd_heat_map = (heat_map - min_heat)/(max_heat - min_heat)
        return scd_heat_map

    def img_from_heat_map(self, heat_map):
        scd_heat_map = self.scale_heat_map(heat_map)
        x_num, y_num = heat_map.shape

        rgbArray = np.zeros((x_num,y_num,3), 'uint8')
        rgbArray[..., 0] = 0.8*scd_heat_map*256
        rgbArray[..., 2] = 0.8*(1 - scd_heat_map)*256

        return Image.fromarray(rgbArray)

    def bin_mesh_to_jpg(self, step):
    
        
        mesh = np.load(self.bin_path + self.file_name + str(step) + '.npy', allow_pickle=True)

        heat_map = self.get_heat_map(mesh)
        img = self.img_from_heat_map(heat_map)
        img.save(self.jpg_path + self.file_name + str(step) + '.jpg')
        
        # with open('mesh_jpg' + '/evol_' + str(step) + '.txt', 'w') as f:
        #     csv.writer(f, delimiter=' ').writerows(heat_map)


    def jpg_to_gif(self, num_of_pics):
        images = []
        path = self.jpg_path + self.file_name

        for num in range (0, num_of_pics):
            images.append(imageio.imread(path + str(num) + '.jpg'))
        imageio.mimsave(self.gifs_path + datetime.now().strftime('%Y-%m-%d_%H_%M_%S') + '.gif', images)
