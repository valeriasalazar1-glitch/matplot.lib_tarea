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

fig= plt.figure(figsizee=(14,9))
fig.suptitle('6 paneles', fontsize=14)
posiciones = [
    [0.05, 0.48, 0.45, 0.45]
    [0.55, 0.62, 0.40, 0.33]
    [0.05, 0.28, 0.25, 0.18]
    [0.32, 0.28, 0.28, 0.18]
    [0.62, 0.36, 0.33, 0.18]
    [0.05, 0.05, 0.90, 0.18]
]

axes =[fig.add_axes(pos) for pos in posiciones]
data_rows = mT

ax = axes[0]
x0 = np.arange(data_rows.shape[1])
ax.plot(x0, data_rows[0], label = 'fila 0')
ax.set_title('Line plot Fila 0')
ax.set_xlabel('columna indice')
ax.set_ylabel('valor')
ax.legend()
ax.grid(True)

ax = axes[1]
x1 = np.arange(data_rows.shape[1])
ax.plot(x1, data_rows[1], label = 'fila 1', s = 10)
ax.set_title('Scatter Fila 1')
ax.set_xlabel('indice')
ax.set_ylabel('valor')
ax.legend()
ax.grid(True)

ax = axes[2]
x2 = np.arange(data_rows.shape[1])
ax.plot(x2, data_rows[2], label = 'fila 2 bar')
ax.set_title('bar plot fila 2 (120 barrras)')
ax.set_xlabel('indice')
ax.set_ylabel('valor')
ax.legend()
ax.grid(True)

ax = axes[3]
ax.hist(data_rows[3], bins = 15, labe = 'fila 3 histograma')
ax.set_title('histograma fila 3')
ax.set_xlabel('valor')
ax.set_ylabel('frecuencia')
ax.legend()
ax.grid(True)

ax = axes[4]
row4 = data_rows[4]
grupos = row4.reshape(6,20).sum(axis=1)
labels_pie = [f'g{i+1}' for i in range(grupos.size)]
ax.pie(grupos,labels = labels_pie, autopct = '%1.1f%%', startangle=90)
ax.set_title('pie fila 4 (6 grupos)')
ax.legend(labels_pie, title = 'grupos', loc = 'upper left', bbox_to_anchor = (1.05, 1))

ax = axes[5]
ax.boxplot(data_rows[5], vert = True)
ax.set_title('boxplot fila 5')
ax.set_xlabel('fila 5')
ax.set_ylabel('valor')
ax.plot([],[], label = 'fila 5 boxplot')
ax.legend()
ax.grid(True)

plt.show()

