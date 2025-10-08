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
arquivo = open('Regula-falsi.txt', 'r')
entry = arquivo.readlines()
arquivo.close()
arquivo = open('saida.txt', 'w')

def f(x):
    var = eval(entry[0], {"__builtins__": None}, {"x": x, **matematica})
    return var

a = float(entry[1])
b = float(entry[2])
p = float(entry[3])
p2 = float(entry[4])
it = float(entry[5])
fa = f(a)
fb = f(b)

arquivo.write("Metodo Regula-falsi\n")
if math.fabs(b - a) < p:
    e = a
else:
    if math.fabs(fa) < p2:
        e = a
    else:
        if math.fabs(fb) < p2:
            e = b
        else:
            k = 1
            M = fa
            x = ((a * fb - b * fa) / (fb - fa))
            while math.fabs(x) > p and k < it:
                if M * f(x) > 0:
                    a = x
                    if math.fabs(b - a) < p:
                        break
                else:
                    b = x
                if math.fabs(b - a) < p:
                    break
                arquivo.write("Iteracao: " + str(k) + "\n")
                k = k + 1
                fa = f(a)
                fb = f(b)
                M = fa
                x = ((a * fb - b * fa) / (fb - fa))
            e = x
            arquivo.write("Resultado: " + str(e) + "\n")
arquivo.close()