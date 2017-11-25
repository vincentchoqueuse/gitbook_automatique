import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

K=2
tau=3
E=4

lti=signal.lti([K*E],[tau,1])
t,y=lti.step()
plt.plot(t,y)
plt.plot([0,25],[K*E,K*E],'r--')
plt.plot([0,3*tau],[0.95*K*E,0.95*K*E],'r--')
plt.plot([3*tau,3*tau],[0,0.95*K*E],'r--')
ax = plt.gca()
ax.annotate('Valeur Finale: KE', xy=(20, K*E), xytext=(10,6),color='red',
            arrowprops=dict(width=1,color='red', shrink=0.005),
            )
ax.annotate('Temps de réponse', xy=(3*tau,0), xytext=(10,2),color='red',
            arrowprops=dict(width=1,color='red', shrink=0.005),
            )
ax.text(-2.2, 0.95*K*E-0.1,'0.95*KE',color='red')
ax.text(3*tau-0.4, -0.5,'3$\\tau$',color='red')

plt.xlabel("temps (s)")
plt.ylabel("sortie")
plt.ylim([0,9])
plt.xlim([0,20])
plt.savefig("../fig1.png")
plt.show()
