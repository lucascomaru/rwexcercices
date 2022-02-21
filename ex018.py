import math
angulo = float(input('Digite o angulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O ângulo digitado tem o seno de{seno:.2f} o cosseno de {cosseno:.2f} e a tangente de {tangente:.2f} ')