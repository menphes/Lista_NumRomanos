# Reescrever toRoman
def unidade(num):
    digito = int(str(num)[-1:])
    if digito == 0:
        vDigito = str('')
    elif digito == 1:
        vDigito = str('I')
    elif digito == 2:
        vDigito = str('II')
    elif digito == 3:
        vDigito = str('III')
    elif digito == 4:
        vDigito = str('IV')
    elif digito == 5:
        vDigito = str('V')
    elif digito == 6:
        vDigito = str('VI')
    elif digito == 7:
        vDigito = str('VII')
    elif digito == 8:
        vDigito = str('VIII')
    elif digito == 9:
        vDigito = str('IX')
    else:
        vDigito = str('Desconhecido')
    return vDigito

def toRoman(num):
  qtdDigitos = len(str(num))
  if qtdDigitos == 2:
    decimal = int(str(num)[0])
    if decimal == 1:
      vDecimal = str('X')
    elif decimal == 2:
      vDecimal = str('XX')
    elif decimal == 3:
      vDecimal = str('XXX')
    elif decimal == 4:
      vDecimal = str('XL')
    elif decimal == 5:
      vDecimal = str('L')
    elif decimal == 6:
      vDecimal = str('LX')
    elif decimal == 7:
      vDecimal = str('LXX')
    elif decimal == 8:
      vDecimal = str('LXXX')
    elif decimal == 9:
      vDecimal = str('XC')
    else:
      vDecimal = str('Desconhecido')

    digito = int(str(num)[1])
    vDigito = unidade(num)
    valorRomano = str(vDecimal) + str(vDigito)
  else:
    vDigito = unidade(num)
    valorRomano = str(vDigito)
        
  return valorRomano

def test(value, expected):
  result = toRoman(value)
  if result == expected:
      print("✓ Teste {value} correto".format(value=value))
  else:
      print("✗ Teste {value} incorreto. Esperado {expected}, obtido {result}".format(value=value, expected=expected, result=result))

test(1, "I")
test(2, "II")
test(3, "III")
test(4, "IV")
test(5, "V")
test(6, "VI")
test(7, "VII")
test(8, "VIII")
test(9, "IX")

if True:
  test(10, "X")
  test(12, "XII")
  test(15, "XV")
  test(18, "XVIII")
  test(19, "XIX")
  test(29, "XXIX")
  test(38, "XXXVIII")
  test(47, "XLVII")
  test(56, "LVI")
  test(65, "LXV")
  test(74, "LXXIV")
  test(83, "LXXXIII")
  test(92, "XCII")