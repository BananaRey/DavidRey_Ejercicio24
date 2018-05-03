import numpy as np
import matplotlib.pyplot as plt

n_L=np.linspace(0.000001,100,5000) 
x=np.linspace(0.000001,100,5000) 
for i in range(len(n_L)):
	n_L[i]=(1/(n_L[i]**4.0))*np.exp(-(11.5/n_L[i]))

normalizacion=np.sum(n_L)*100.0/5000.0
n_L=n_L/normalizacion
#plt.ylim(0.0,1.0)
plt.plot(x,n_L)
plt.title('Decaimiento',fontsize=25)
plt.xlabel('lambda',fontsize=25)
plt.ylabel('prob.lambda',fontsize=25)
plt.show()
plt.savefig('Decaimiento.png')
plt.close()


