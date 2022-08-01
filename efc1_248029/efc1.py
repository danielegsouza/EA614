#Atividade Computacional 1 - EA614
#Daniele Souza Gonçalves   248029

import numpy as np
import matplotlib.pyplot as plt 

#Candidatos a equalizador 

w1 = [1,0.5,0.25,0.125,0.0625]
w2 = [1, -0.75,1.5,-0.2,0.3]

#Resposta ao impulso 

h = [1, -0.5,0,0,0]

# Item c) Queremos obter as respostas combinadas g1[n] e g2[n], onde g1[n] = w1[n]*h[n] e g2[n] = w2[n]*h[n]

def resposta_combinada(w,h):
     return np.convolve(w,h)

g1 = resposta_combinada(w1,h)
g2 = resposta_combinada(w2,h)

print("g1=",g1,"\n")
print("g2 =",g2,"\n")


s = np.random.uniform(0, 1, 100)
s[np.where(s < 0.25)] = 3
s[np.where(s < 0.5)] = 1
s[np.where(np.abs(s) < 0.75)] = -1
s[np.where(np.abs(s) < 1)] = -3


# Item d) Simular a trasmissão do sinal pela canal h[n]

x = resposta_combinada(s,h)
print("s[n] = ",s,"\n")
print("x[n] =", x)

plt.hist(s, label='s[n]')
plt.hist(x,label='x[n]')
plt.legend()


#Item e) Filtrar o sinal x[n] pelos equalizadores w1[n] e w2[n]

y1 = resposta_combinada(x,w1)
plt.figure()
y1_plot = plt.stem(y1,label ='y1[n]')
plt.setp(y1_plot,'color','r')
plt.stem(s,label='s[n]')
plt.xlabel('n')
plt.ylabel('Amplitudes')
plt.legend()
plt.show()

y2 = resposta_combinada(x,w2)

plt.figure()
y1_plot = plt.stem(y2,label ='y2[n]')
plt.setp(y1_plot,'color','r')
plt.stem(s,label='s[n]')
plt.xlabel('n')
plt.ylabel('Amplitudes')
plt.legend()
plt.show()