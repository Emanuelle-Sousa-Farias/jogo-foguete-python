#bibliotecas
import math
import matplotlib.pyplot as plt

#entradas
velocidade = float(input("Velocidade inicial: "))
angulo = float(input("Ângulo: "))

#gravidade
g = 9.81

#calculos e resultados
angulo_rad = math.radians(angulo) #converte para radianos
vx = velocidade * math.cos(angulo_rad) #calcula componente horizontal
vy = velocidade * math.sin(angulo_rad) #calcula componente vertical

print("\n--- Componentes da Velocidade ---")
print(f"Componente horizontal: {vx:.2f} m/s")
print(f"Componente vertical: {vy:.2f} m/s")

tempo_voo = (2*vy)/g #calcula tempo de voo
altura_max = (math.pow(vy, 2))/(2*g) #calcula altura maxima
alcance = vx*tempo_voo #calcula o alcance

print("\n--- Resultados ---")
print(f"tempo de voo: {tempo_voo:.2f} s")
print(f"altura máxima: {altura_max:.2f} m")
print(f"alcance: {alcance:.2f} m")

#tabela de posicoes
print("\n--- Tabela de Posições ---")
print("Tempo (s) | Altura (m) | Alcance (m)")

#numero de vezes que o programa vai calcular a posicao do foguete (9 por que sao 10 pontos, incluindo o ponto inicial)
n_intervalos = 9

#guardam os valores pra fazer o grafico
tempos = []
posicoes_x = []
posicoes_y = []

#faz a tabela
for i in range(n_intervalos +1):
    t = tempo_voo*i/n_intervalos
    x = vx*t
    y = vy*t - ((math.pow((g*t), 2))/2)

    tempos.append(t)
    posicoes_x.append(x)
    posicoes_y.append(y)
    print(f"{t:.2f} | {y:.2f} | {x:.2f} ")

#grafico
plt.plot(posicoes_x, posicoes_y, marker="o") #desnha a trajetoria, com "o" marcando os pontos
plt.title("Caminho do Foguete") #titulo do grafico
plt.xlabel("Alcance (m)") #nome do eixo x
plt.ylabel("Altura (m)") #nome do eixo y
plt.grid(True) #poe grid (achei bonitinho)
plt.show() #mostra o grafico



