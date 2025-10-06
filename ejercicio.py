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
print('copyF flags: ', copyF.flags['C_CONTIGUOUS'], 'F_CONTIGUOUS=', copyF.flags['F_CONTIGUOUS'])
print('copyC flags: C_CONTIGUOS =', copyC.flags['C_CONTIGUOUS'], 'F_CONTIGUOS =', copyC.flags['F_CONTIGUOUS'] )

