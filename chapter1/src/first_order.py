import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

K=2
tau=3
E=4

lti=signal.lti([K],[tau,1])
t,y=lti.step()
plt.plot(t,E*y)
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


w2=np.linspace(1/tau, 10, num=100)
plt.figure()
ax = plt.gca()
w,G,phase=lti.bode(w=np.logspace(-2, 1, num=100))
plt.semilogx(w,G)
plt.plot([0.01,10],[20*np.log10(K),20*np.log10(K)],'r--')
plt.plot([1/tau,1/tau],[-25,6],'r--')
plt.plot([0.01,1/tau],[20*np.log10(K)-3,20*np.log10(K)-3],'r--')


plt.plot(w2,20*np.log10(K)-20*np.log10(w2*tau),'r--')
plt.xlabel("pulsation (rad/s)")
plt.ylabel("Gain (dB)")
ax.annotate('Basse Fréquence: 20.log10(K)', xy=(0.01, 20*np.log10(K)), xytext=(0.03,8),color='red',
            arrowprops=dict(width=1,color='red', shrink=0.005),
            )
ax.annotate('20.log10(K)-3', xy=(0.01, 20*np.log10(K)-3), xytext=(0.03,-5),color='red',
            arrowprops=dict(width=1,color='red', shrink=0.005),
            )

ax.text(1/tau-0.05, -26.5,'$1/\\tau$',color='red')
plt.savefig("../fig1.png")
plt.show()
