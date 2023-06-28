import math

# CALCULATORS
def calc(op='', resultado='', msg_error='syntax_error'):
    while True:
        if not resultado:
            resultado = input('Ingresa el primer número: ')
            if resultado.lower() == 'salir':
                break
            resultado = int(resultado)

        numero2 = input('Ingresa el siguiente número: ')
        if numero2.lower() == 'salir':
            break
        numero2 = int(numero2)

        op = input('Ingresa la operación que quieras utilizar: ')
        if op.lower() == 'salir':
            break

        if op.lower() == 'suma':
            resultado += numero2

        if op.lower() == 'resta':
            resultado -= numero2

        if op.lower() == 'multi':
            resultado *= numero2

        if op.lower() == 'div':
            resultado /= numero2

        if op.lower() == 'elev':
            resultado **= numero2

        if op.lower() == 'raiz':
            resultado = math.isqrt(numero2)

        print(f'El resultado de la operación es {resultado}')


def coin_conv(resultado2='', moneda='', moneda2='', msg_error='syntax error'):
    while True:

        resultado2 = input('Ingresa el número de monedas: ')
        if resultado2.lower() == 'salir':
            break
        resultado2_float = float(resultado2)

        moneda = input('Ingresa de qué moneda es esa cantidad: ')
        if moneda.lower() == 'salir':
            break
        moneda2 = input('Ingresa a qué moneda lo quieres pasar: ')
        if moneda2 == 'salir':
            break

        if moneda == 'dolar' and moneda2 == 'euro':
            resultado2_float *= 0.726089
        elif moneda == 'euro' and moneda2 == 'dolar':
            resultado2_float /= 0.726089
        elif moneda == 'euro' and moneda2 == 'peseta':
            resultado2_float *= 166.386
        elif moneda == 'peseta' and moneda2 == 'euro':
            resultado2_float /= 166.386
        elif moneda == 'dolar' and moneda2 == 'peseta':
            resultado2_float *= 166.94000
        elif moneda == 'peseta' and moneda2 == 'dolar':
            resultado2_float /= 166.94000
        
        
        else:
            print(msg_error)
            break

        print(f'El resultado de la conversión es {resultado2_float}')


def dist_conv(resultado3='', dist1='', dist2='',msg_error='syntax error'):
    while True:
        resultado3 = input('Ingresa la distancia: ')
        if resultado3.lower() == 'salir':
            break
        resultado3_float = float(resultado3)

        dist1 = input('Ingresa de qué unidad se trata: ')
        if dist1.lower() == 'salir':
            break
        dist2 = input('Ingresa a qué unidad lo quieres pasar: ')

        if dist1 == 'mm' and dist2 == 'pulgada':
            resultado3_float *= 0.0393701
        elif dist1 == 'mm' and dist2 == 'pie':
            resultado3_float *= 0.00328084
        elif dist1 == 'mm' and dist2 == 'yarda':
            resultado3_float *= 0.00109361
        elif dist1 == 'mm' and dist2 == 'milla':
            resultado3_float *= 0.00000062137
        elif dist1 == 'mm' and dist2 == 'cm':
            resultado3_float *= 0.1
        elif dist1 == 'mm' and dist2 == 'm':
            resultado3_float *= 0.001
        elif dist1 == 'mm' and dist2 == 'km':
            resultado3_float *= 0.00001

        elif dist1== 'cm' and dist2 == 'pulgada':
            resultado3_float *= 0.393701
        elif dist1== 'cm' and dist2 == 'pie':
            resultado3_float *= 0.0328084
        elif dist1== 'cm' and dist2 == 'yarda':
            resultado3_float *= 0.0109361
        elif dist1== 'cm' and dist2 == 'milla':
            resultado3_float *= 0.0000062137
        elif dist1== 'cm' and dist2 == 'mm':
            resultado3_float *= 10.0
        elif dist1== 'cm' and dist2 == 'm':
            resultado3_float *= 0.01
        elif dist1== 'cm' and dist2 == 'km':
            resultado3_float *= 0.00001

        elif dist1== 'm' and dist2 == 'pulgada':
            resultado3_float *= 39.3701
        elif dist1== 'm' and dist2 == 'pie':
            resultado3_float *= 3.28084
        elif dist1== 'm' and dist2 == 'yarda':
            resultado3_float *= 1.09361
        elif dist1== 'm' and dist2 == 'milla':
            resultado3_float *= 0.000621371
        elif dist1== 'm' and dist2 == 'mm':
            resultado3_float *= 1000.0
        elif dist1== 'm' and dist2 == 'cm':
            resultado3_float *= 100.0
        elif dist1== 'm' and dist2 == 'km':
            resultado3_float *= 0.001
        
        elif dist1== 'km' and dist2 == 'pulgada':
            resultado3_float *= 39370.1
        elif dist1== 'km' and dist2 == 'yarda':
            resultado3_float *= 1093.61
        elif dist1== 'km' and dist2 == 'milla':
            resultado3_float *= 0.621371
        elif dist1== 'km' and dist2 == 'mm':
            resultado3_float *= 1000000.0
        elif dist1== 'km' and dist2 == 'cm':
            resultado3_float *= 100000.0
        elif dist1== 'km' and dist2 == 'm':
            resultado3_float *= 1000.0


        elif dist1== 'pulgada' and dist2 == 'pie':
            resultado3_float *= 0.0833333
        elif dist1== 'pulgada' and dist2 == 'yarda':
            resultado3_float *= 0.0277778
        elif dist1== 'pulgada' and dist2 == 'milla':
            resultado3_float *= 0.000015783
        elif dist1== 'pulgada' and dist2 == 'mm':
            resultado3_float *= 25.4
        elif dist1== 'pulgada' and dist2 == 'cm':
            resultado3_float *= 2.54
        elif dist1== 'pulgada' and dist2 == 'm':
            resultado3_float *= 0.0254
        elif dist1== 'pulgada' and dist2 == 'km':
            resultado3_float *= 0.0000254

        elif dist1== 'pie' and dist2 == 'pulgada':
            resultado3_float *= 12.0
        elif dist1== 'pie' and dist2 == 'yarda':
            resultado3_float *= 0.333333
        elif dist1== 'pie' and dist2 == 'milla':
            resultado3_float *= 0.000189394
        elif dist1== 'pie' and dist2 == 'mm':
            resultado3_float *= 304.8
        elif dist1== 'pie' and dist2 == 'cm':
            resultado3_float *= 30.48
        elif dist1== 'pie' and dist2 == 'm':
            resultado3_float *= 0.3048

        elif dist1== 'yarda' and dist2 == 'pulgada':
            resultado3_float *= 36
        elif dist1== 'yarda' and dist2 == 'pie':
            resultado3_float *= 3
        elif dist1== 'yarda' and dist2 == 'milla':
            resultado3_float *= 0.000568182
        elif dist1== 'yarda' and dist2 == 'mm':
            resultado3_float *= 914.4
        elif dist1== 'yarda' and dist2 == 'cm':
            resultado3_float *= 91.44
        elif dist1== 'yarda' and dist2 == 'm':
            resultado3_float *= 0.9144
        elif dist1== 'yarda' and dist2 == 'km':
            resultado3_float *= 0.0009144

        elif dist1== 'milla' and dist2 == 'pulgada':
            resultado3_float *= 63360.0
        elif dist1== 'milla' and dist2 == 'pie':
            resultado3_float *= 5280.0
        elif dist1== 'milla' and dist2 == 'yarda':
            resultado3_float *= 1760.0
        elif dist1== 'milla' and dist2 == 'mm':
            resultado3_float *= 1609000.0
        elif dist1== 'milla' and dist2 == 'cm':
            resultado3_float *= 160934.0
        elif dist1== 'milla' and dist2 == 'm':
            resultado3_float *= 1609.34
        elif dist1== 'milla' and dist2 == 'km':
            resultado3_float *= 1.60934

        elif dist1== 'salir':
            break
        else:
            print(msg_error)

        print(f'El resultado de la conversión es {resultado3_float}')

def mcm(*valor): #esto no se como hacer que funcione
    int(valor) 
    math.lcm(*valor)
    print(valor)
    
        


# MAIN MENU
while True:
    msg_error = 'syntax error'
    init_quest = input('[Escribe "salir" dentro de una calculadora para cerrarla, escribe "salir" aquí para cerrar el programa] Bienvenido a la calculadora multiusos. Aquí hay una calculadora basica (calc), un conversor de monedas (coin_conv), uno de distancias (dist_conv), . Para obtener información sobre una calculadora escribe el nombre de la alculadora pero con .info (por ejemplo, coin_conv.info). Elige una calculadora: ')
    if init_quest == 'calc':
        calc()
    elif init_quest == 'calc.info':
        string_random2 = 'a'
        for char in string_random2:
            print(' ')
            print('---la calculadora puede sumar (suma), restar (resta), multiplicar (multi), dividir (div), elevar numeros (elev), calcular la raiz cuadrada de un numero (raiz) [inserta el numero del que quieras saber la raiz cuadrada cuando el programa te diga "Ingresa el siguiente numero"]---')
            print(' ')
    elif init_quest == 'coin_conv':
        coin_conv()
    elif init_quest == 'coin_conv.info':
        string_random = 'a'
        for char in string_random:
            print(' ')
            print('---el conversor de monedas funciona con euros, dolares y pesetas. por ejemplo puedes pasar de pesetas a dolares, de dolares a euros, etc---')
            print(' ')
    elif init_quest == 'dist_conv':
        dist_conv()
    elif init_quest == 'dist_conv.info':
        string_random3 = 'a'
        for char in string_random3:
            print(' ')
            print('---el conversor de distancia es la calculadora mas completa de todas. Puedes pasar cualquier unidad del sistema imperial al metrico, unidades del sistema metrico a otra unidad del metrico y unidades del sistema imperial a otra unidad del sistema imperial---')
            print(' ')
    
    elif init_quest == 'salir':
        break
    