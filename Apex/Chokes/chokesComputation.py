import subprocess

k = 0

for i in range(2):
    for j in range(2):
        if (i < j):
            k += 1
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

let zone1 = distleq(40, treshold1)
let zone2 = distleq(40, treshold2)

let union = zone1 & zone2 & !treshold1 & !treshold2


save "./output/union''' +str(k)+'''.png" union''')
            voxfile.close()
            sp = subprocess.Popen(["/bin/bash", "-i", "-c", "voxlogica mountChokes.imgql"])
            sp.communicate()
