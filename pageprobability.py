ns = int(input("Numero studenti: "))
pi = int(input("Pagina iniziale: "))
pf = int(input("Pagina finale: "))

pt = pf - pi + 1

sums = []
prob = []

for i in range(21): print("-", end="")
print("\nQuesto programma calcola la probabilità di ogni studente di essere chiamato secondo la corrispondenza con somma delle cifre del numero di pagina\nScritto da Fritzky")
for i in range(21): print("-", end="")
print(f"\nNumero studenti: {ns}\nPagina iniziale: {pi}\nPagina finale: {pf}\nTotale pagine: {pt}\n")
for i in range(21): print("-", end="")
print("\n")

for p in range(pi, pf):
    sum = 0
    for d in str(p):  
        sum += int(d)
    sums.append(sum)
    
res = {k: sums.count(k) for k in sums}

for i in res:
    print(f"|{i}:\t|Casi: {res[i]}\t| {res[i] / pt * 100:.3f}%\t|")
