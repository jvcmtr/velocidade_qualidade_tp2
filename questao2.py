import random
import time

def el_comuns(arr1, arr2):
    existing = {}
    common = []
    for e1 in arr1:
        if not existing.get(e1):
            existing[e1] = 1
            continue
        existing[e1] += 1
    
    for e2 in arr2:
        if existing.get(e2):
            existing[e2] -=1
            common.append(e2)
    return common


def test(tamanho_array = 100000, n_testes=1):
    print(f"_____________")
    print(f"Iniciando testes com arrays de {tamanho_array:,} elementos.")
    
    for i in range(n_testes):
        arr1 = [ random.randint(0, tamanho_array ) for x in range(tamanho_array)]
        arr2 = [ random.randint(0, tamanho_array ) for x in range(tamanho_array)]
        
        inicio = time.time()
        comuns = el_comuns(arr1, arr2)
        fim = time.time()

        print(f"Teste: {i+1} \t| Duração: {fim-inicio:.4f} ms\t| elementos em comum: {len(comuns):,}")

if __name__ == "__main__":
    test(tamanho_array=100000, n_testes=10)
    test(tamanho_array=1000000, n_testes=10)
    test(tamanho_array=5000000, n_testes=5)