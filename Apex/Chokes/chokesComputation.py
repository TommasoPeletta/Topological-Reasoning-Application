import subprocess
import os
import matplotlib.image as mpimg
import numpy as np

k = 0

for i in range(57):
    for j in range(57):
        if (i < j):
            voxfile = open("mountChokes.imgql", "w")
            voxfile.write('''import "stdlib.imgql"
// filter function definition
let flt(x,a) = distleq(x,distgeq(x,!a))

// load original image

load image1 = "./Mount_Images/mountain_''' +str(i+1)+'''.jpg"
load image2 = "./Mount_Images/mountain_''' +str(j+1)+'''.jpg"

// read image components
let r1 = red(image1)
let r2 = red(image2)

let treshold1 = r1 >. 100
let treshold2 = r2 >. 100

let zone1 = distleq(3, treshold1)
let zone2 = distleq(3, treshold2)

let union = zone1 & zone2 & !treshold1 & !treshold2
let union1 = touch(union, treshold1) & touch(union, treshold2)

save "./output/union''' +str(k)+'''.png" union1''')
            print(i)
            voxfile.close()
            #os.system('source /home/tommyubuntu/.bashrc; voxlogica mountChokes.imgql')
            sp = subprocess.Popen(["/home/tommyubuntu/Documenti/VoxLogicA_0.5.5_linux-x64/VoxLogicA", "mountChokes.imgql"])
            sp.communicate()
            img = mpimg.imread('./output/union'+str(k)+'.png')
            im_array = np.array(img, dtype='uint8')
            if (np.sum(im_array) == 0):
                os.system('rm ./output/union'+str(k)+'.png')
            else:
                k += 1
