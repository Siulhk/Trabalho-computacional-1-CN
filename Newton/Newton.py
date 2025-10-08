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
arquivo = open('Newton.txt', 'r')
entry = arquivo.readlines()
arquivo.close()
arquivo = open('saida.txt', 'w')

def f(x):
    var = eval(entry[0], {"__builtins__": None}, {"x": x, **matematica})
    return var

def fl(x):
    var = eval(entry[1], {"__builtins__": None}, {"x": x, **matematica})
    return var

xo = float(entry[2])
p = float(entry[3])
it = float(entry[4])
fx = f(xo)

arquivo.write("Metodo Newton\n")
if math.fabs(fx) > p:
    k = 1
    fxlinha = fl(xo)
    x1 = xo - (fx/fxlinha)
    fx = f(x1)
    while math.fabs(fx) > p and math.fabs(x1 - xo) > p and k < it:
        arquivo.write("iteracao: " + str(k) + "\n")
        k=k+1
        x0 = x1
        fxlinha = fl(x0)
        x1 = x0 - (fx/fxlinha)
        fx = f(x1)
        arquivo.write("Raiz aproximada: " + str(x1) + "\n")
    raiz = x1
    arquivo.write("Resultado: " + str(raiz) + "\n")
else:
    raiz = xo
arquivo.close()