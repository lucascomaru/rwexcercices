s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 == s2 == s3:
    print('Os segmentos acima podem formar um triângulo EQUILÁTERO! ')
elif s1 != s2 != s3 and s1 != s3:
    print('Os segmentos acima podem formar um triângulo ESCALENO! ')
else:
    print('Os segmentos acima podem formar um triângulo ISÓSCELES! ')