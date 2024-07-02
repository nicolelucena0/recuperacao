# calculadora de media
# desenvolvido por 
# Nicole Cardoso
# Layz Santana

from calc_media import CalculadoraDeMedia

nota1 = float(input("Digite a nota 1: "))

while nota1 < 0 or nota1 > 10:
    print('A nota não pode ser menor que 0 ou maior que 10')
    nota1 = float(input('Digite a nota novamente: '))

nota2 = float(input('Digite a nota 2: '))

while nota2 < 0 or nota2 > 10:
    print('A nota não pode ser menor que 0 ou maior que 10')
    nota2 = float(input('Digite a nota novamente: '))

nota3 = float(input('Digite a nota 3: '))

while nota3 < 0 or nota3 > 10:
    print('A nota não pode ser menor que 0 ou maior que 10')
    nota3 = float(input('Digite a nota novamente: '))

media = CalculadoraDeMedia.calcular(nota1, nota2, nota3)
print(f'Resultado é {media}')