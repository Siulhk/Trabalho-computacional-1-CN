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
arquivo = open('MIL.txt', 'r')
entry = arquivo.readlines()
arquivo.close()
arquivo = open('saida.txt', 'w')

xo = float(entry[2])
p = float(entry[3])
it = float(entry[4])

def f(x):
    var = eval(entry[0],{"__builtins__":None}, {"x": x, **matematica})
    return var
def f2(x):
    var = eval(entry[1],{"__builtins__":None}, {"x": x, **matematica})
    return var
arquivo.write("Metodo MIL\n")
if abs(f(xo)<p):
    arquivo.write("Resultado: "+ str(xo) + "\n")
else:
    k = 1
    x1 = f2(xo)
    while math.fabs(f2(x1))>p and math.fabs(xo - x1)>p and k<it:
        arquivo.write("iteracao: " + str(k) + "\n")
        xo = x1
        arquivo.write("Aproximacao: " + str(xo) + "\n")
        x1 = f2(xo)
        k = k+1
    print("Resultado: " + str(xo) + "\n")
    print("iteracao: " + str(k) + "\n")
arquivo.close()