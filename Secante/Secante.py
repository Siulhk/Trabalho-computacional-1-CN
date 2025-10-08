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
arquivo = open('Secante.txt', 'r')
entry = arquivo.readlines()
arquivo.close()
arquivo = open('saida.txt', 'w')

def f(x):
    var = eval(entry[0], {"__builtins__": None}, {"x": x, **matematica})
    return var

xo = float(entry[1])
x1 = float(entry[2])
p = float(entry[3])
it = float(entry[4])
fx = f(xo)

if math.fabs(f(xo))<p:
    e = xo
elif math.fabs(f(xo))<p or math.fabs(x1 - xo) < p:
        e = x1
else:
    k = 1
    x2 = x1 - ((f(x1)*(x1-xo))/(f(x1)-f(xo)))
    while math.fabs(f(x2)) > p and math.fabs(x2 - x1) > p and k < it:
        arquivo.write("Iteracao: " + str(k) + "\n")
        x0 = x1
        x1 = x2
        k = k+1
        x2 = x1 - ((f(x1)*(x1-x0))/(f(x1)-f(x0)))
        arquivo.write("xo aproximado: " + str(xo) + "\n")
        arquivo.write("x1 aproximado: " + str(x1) + "\n")
        arquivo.write("x2 aproximado: " + str(x2) + "\n")
    e = x2
    arquivo.write("Resultado: " + str(e) + "\n")
arquivo.close()