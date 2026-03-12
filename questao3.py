import random
import time

def primeiro_valor_duplicado(arr):
    if not arr or len(arr) < 2:
        return None

    visto = {}

    for i in arr:
        if visto.get(str(i)):
            return i
        visto[str(i)] = True

    return None


def test(arr, group_size=5, n_duplicados=1, n_testes=1):
    s = set(arr)

    if group_size-n_duplicados > len(arr) or group_size-n_duplicados < 1 or n_duplicados*2>group_size:
        raise "Erro no valor dos argumentos" 
    
    def build_test_arr():
        test_arr = random.sample( list(s), (group_size-n_duplicados))
        dup = random.sample(test_arr, n_duplicados)

        for d in dup:
            insert_idx = random.choice(range(len(test_arr)))
            test_arr.insert(insert_idx, d)
        
        return test_arr

    for i in range(n_testes):
        test_subject = build_test_arr()

        start = time.time()
        found = primeiro_valor_duplicado(test_subject)
        t = time.time() - start
        spacing = "".join([" " for x in range(10-len(str(found)))])
        print(f"Teste {i} | Duração: {t:.4f}  | primeiro duplicado: {found}{spacing} | array: {test_subject}")
        

if __name__ == "__main__":
    nomes = ["Ana", "Bia", "Caio", "Davi", "Everaldo", "Fernando", "Helio" , "Guto", "Ian", "João", "Kauan","Larissa", "Mario", "Norberto", "Otto", "Pedro", "Ramon", "Silvia", "Tatiana", "Ulisses", "Vanessa",]
    numeros = [1, 22, 303, 4500, 50, 666, 7986, 8, 99 ]
    print("\n\tTeste com nomes - (2 itens duplicados por teste)")
    test(nomes, n_duplicados=2, n_testes=10)
    print("\n\tTeste com numeros - (1 item duplicado por teste)")
    test(numeros, n_duplicados=1, n_testes=10)
