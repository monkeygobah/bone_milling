import os

path = '/Users/georgienahass/Desktop/alkureishiLab/thermal_camera/thermalData_expeirment_1'

file_list = []
for root, dirs,files in os.walk(path):
    for file in files:
        in_path =(os.path.join(root, file))
        underscore = file.split('_')
        out_path =(os.path.join(root, underscore[-1]))
        os.rename(in_path, out_path)

    
