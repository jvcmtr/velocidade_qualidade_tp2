
ALFABETO = "abcdefghijklmnopqrstuvwxyz"

def letras_ausentes(str):
    alf_map={ x:0 for x in ALFABETO }
    
    for c in str:
        if alf_map.get(c) == None:
            continue
        alf_map[c] += 1
    
    return [x for x in alf_map.keys() if alf_map[x] == 0]

def test(str):
    print(f"\ttexto: \"{str}\"\t|  letras ausentes: {', '.join(letras_ausentes(str))}")

if __name__ == "__main__":
    test(ALFABETO.replace("c", "_"))
    test(ALFABETO.replace("h", "_H_"))
    test(ALFABETO.replace("j", "JOAO"))
    test(ALFABETO.replace("z", "?"))
    test(ALFABETO.replace("a", "ã_"))
    test(ALFABETO.replace("b", "").replace("d", "_").replace("f", "_"))
    print("__________________________________________")