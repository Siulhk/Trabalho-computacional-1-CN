import math

matematica = {
    "sen": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "sqrt": math.sqrt,
    "log": math.log,
    "exp": math.exp,
    "pi": math.pi,
    "e": math.e,
    "log10": math.log10
}
arquivo = open("f.txt", "r")
entry = arquivo.readlines()
arquivo.close()
arquivo = open("saida.txt", "w")
a = float(entry[1])
b = float(entry[2])
p = float(entry[3])
n = float(entry[4])

def f(x):
    func = eval(entry[0])
    return func

k = 0
arquivo.write("Metodo bisseccao" + "\n")
if abs(b-a) < p:
    a = p
while abs(b-a) > p and k < n:
    k = k + 1
    arquivo.write("iteracao: " + str(k) + "\n")
    arquivo.write("a = " + str(a)+ "\n")
    arquivo.write("b = " + str(b)+ "\n")
    finicio = f(a)
    meio = (a+b)/2
    fmeio = f(meio)
    if finicio*fmeio<0:
        b = meio
    else:
        a = meio
arquivo.write("Raiz: " + str(meio))
arquivo.close()

