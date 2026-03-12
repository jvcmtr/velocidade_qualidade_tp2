import random
import time

def selection_sort(a):
    array = list(a)
    comparacoes = 0
    trocas = 0

    def trocar_pos(arr, a, b):
        c = arr[a]
        arr[a] = arr[b] 
        arr[b] = c

    def idx_menor_num(arr, offset):
        min = offset
        comparacoes = 0
        for i in range(offset, len(arr)):
            comparacoes += 1
            if arr[i] < arr[min]:
                min = i
        return min, comparacoes

    def ordenar_indice(arr, target_idx):
        idx, comparacoes = idx_menor_num(arr, target_idx)
        trocar_pos(arr, target_idx, idx) 
        return 1, comparacoes

    for i in range(len(array)):
        t, c = ordenar_indice(array, i)
        trocas += t
        comparacoes += c

    return comparacoes, trocas

def test(array_size, n_tests=1, n_tests_offset=0, array_orderring=None):
    def get_test_array(order):
        if order == "ORDENADO":
            return range(0, array_size)
        if order == "INVERTIDO":
            return range(-array_size, 0)
        if order == "DESORDENADO" or None:
            return [random.randint(0, array_size) for x in  range(array_size)]
    
    total_t = 0
    for i in range(n_tests):
        test_arr = get_test_array(array_orderring)
        
        start = time.time()
        c, t = selection_sort(test_arr)
        total_t += time.time() - start
        print(f"Teste{i+n_tests_offset}\t| {array_orderring}\t | elementos: {array_size} \t| Duracao: {(total_t/n_tests):.5f}\t| Comparacoes: {c}\t | Trocas:{t}")
    
    # print(f"Medias {n_tests_offset}-{n_tests+n_tests_offset-1} \t| {array_orderring}\t |  n elementos: {array_size} \t |  Duracao media: {(total_t/n_tests):.5f}\t| ")
    # print(f"__________________________________________________________")
    return n_tests+n_tests_offset



if __name__ == "__main__":
    n = 0
    n_tests = 4
    tipo = ["ORDENADO", "DESORDENADO", "INVERTIDO"]
    tamanhos = [100, 1000, 10000]

    for j in tamanhos:
        print(f"______ Testes com {j:,} elementos ________________________________")
        for i in tipo:
            n = test(array_size=j, array_orderring=i, n_tests=n_tests, n_tests_offset=n)

    print("")