import random

# questao 1.1 e 1.2
def encontra_maior_numero_count(arr):
    if not arr or len(arr) < 1:
        return None, 0   

    max = None
    count = 0  
    for i in range(len(arr)):
        unico = True
        
        for j in range(len(arr)):
            count += 1
            if i != j and arr[i] == arr[j]:
                unico = False
                break
        
        if not unico :
            break

        if max is None or arr[i] > max:
            max = arr[i]
    
    return max, count

# questao 1.3 e 1.4
def encontra_maior_hash_count(arr):
    if not arr or len(arr) < 1:
        return None, 0   

    max = None
    count = 0  
    seen = {}

    for i in arr:
        if not seen.get(i):
            seen[i] = 0

        seen[i] += 1
        if seen[i] <=1 :
            continue
    
    for i in arr:
        count += 1
        if seen[i] > 1:
            continue
        if max==None or i > max:
            max = i

    return max, count

# questao 1.5
if __name__ == "__main__":
    print("===========================================")
    print(f"|\ttamanho\t|\taninhado\t\t|\thashtable\t\t|\tdiferenca\t\t|")
    total1 = 0
    total2 = 0
    count = 0
    prints = [10, 100, 1000, 5000, 10000, 50000, 100000, 500000, 1000000 ]

    for i in range(0, 1000, 10):
        count+=1
        list = [ random.randint(1, i) for x in range(i) ]
        m1, c1 = encontra_maior_numero_count(list)
        m2, c2 = encontra_maior_hash_count(list)
        total1 += c1
        total2 += c2
        if i in prints:
            print(f"|\t{i}\t|\t{c1} ({(c1/i):.2f})\t\t|\t{c2} ({(c2/i):.2f})\t\t|\t{c1-c2} ({((c1/i)-(c2/i)):.2f})\t\t|")



    for i in range(1000, 150000, 1000):
        count+=1
        list = [ random.randint(1, i) for x in range(i) ]
        m1, c1 = encontra_maior_numero_count(list)
        m2, c2 = encontra_maior_hash_count(list)
        total1 += c1
        total2 += c2
        if i in prints:
            print(f"|\t{i}\t|\t{c1} ({(c1/i):.2f})\t\t|\t{c2} ({(c2/i):.2f})\t\t|\t{c1-c2} ({((c1/i)-(c2/i)):.2f})\t\t|")


    for i in range(100000, 1000001, 100000):
        count+=1
        list = [ random.randint(1, i) for x in range(i) ]
        m1, c1 = encontra_maior_numero_count(list)
        m2, c2 = encontra_maior_hash_count(list)
        total1 += c1
        total2 += c2
        if i in prints:
            print(f"|\t{i}\t|\t{c1} ({(c1/i):.2f})\t\t|\t{c2} ({(c2/i):.2f})\t\t|\t{c1-c2} ({((c1/i)-(c2/i)):.2f})\t\t|")

    
    print("|\t---\t\t\t---\t\t\t\t---\t\t\t|")
    print(f"|\ttotal\t|\t{total1}\t\t|\t{total2}\t\t|\t{total1-total2}\t\t|")
    print(f"|\tmedia\t|\t{(total1/count):.2f}\t\t|\t{(total2/count):.2f}\t|\t{(total1-total2/count):.2f}\t\t|")
    print("===========================================")