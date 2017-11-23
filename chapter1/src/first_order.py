import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

K=2
tau=3
E=4

lti=signal.lti([K*E],[tau,1])
t,y=lti.step()
plt.plot(t,y)
plt.xlabel("temps (s)")
plt.ylabel("sortie")
plt.savefig("../fig1.png")
