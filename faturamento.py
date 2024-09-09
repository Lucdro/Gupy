import random

def calcular(faturamentos: list[float|None]) -> tuple[float,float,int]:
    menor = 0
    maior = 0
    soma = 0
    dias_invalidos = 0

    for faturamento in faturamentos:
        if faturamento == None:
            dias_invalidos += 1
            continue
        if faturamento < menor:
            menor = faturamento
        if faturamento > maior:
            maior = faturamento
        soma += faturamento

    if dias_invalidos == 365:
        print('Não há dias válidos para fazer a média')
        return (menor,maior,0)
    
    media_anual = soma/(365-dias_invalidos)
    def filtrar_dias_faturamento_superior(faturamento):
        if faturamento == None:
            return False
        if faturamento > media_anual:
            return True
        return False
    dias_faturamento_superior = len(list(filter(filtrar_dias_faturamento_superior,faturamentos)))
    return (menor,maior, dias_faturamento_superior)



if __name__ == "__main__":
    faturamentos = [(random.random() - 0.2) * 200 for _ in range(365)]
    dias_sem = [round(random.random()*365) for _ in range(round(random.random()*100))]
    for dia in dias_sem:
        faturamentos[dia] = None
    
    resultado = calcular(faturamentos)
    print(f'\tO menor faturamento foi de {round(resultado[0],2)} R$ e o maior faturamento foi de {round(resultado[1],2)} R$\n\tA média anual foi superada em {resultado[2]} dias')