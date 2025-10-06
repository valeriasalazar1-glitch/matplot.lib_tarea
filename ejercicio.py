import numpy as np 
import matplotlib.pyplot as plt 

rng = np.random.default_rng(42)
valores = rng.random(720)
print(valores.size)

m = valores.reshape((120,6))
print(m.shape) 

mT= m.T
copyF = np.array(mT, order = 'F', copy = True)
copyC = np.array(mT, order = 'C', copy = True)
print(mT.shape)
print('transpuesta: ', mT.shape)
print()