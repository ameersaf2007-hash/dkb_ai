import numpy as np

markah = np.array((70,85,90,65,80))
print (markah)

purata =np.mean (markah)
print ("purata markah: ", purata)

tertinggi = np.max (markah)
print ('markah tertinggi: ',tertinggi)

terendah = np.min (markah)
print ("markah terendah: ", terendah)

sum = np.sum(markah)
print ("jumlah markah: ",sum)

markahBaru = markah + 5
print(markahBaru)
