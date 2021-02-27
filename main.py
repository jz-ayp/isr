"""
Inserta el encabezado aquí y escribe tu código abajo


# Declaraciones
CONSTANTE = valor

# Entradas
entrada = input()

# Proceso


# Salidas
print(salida)

"""

"""
Calcular el importe de ISR correspondiente a un sueldo mensual
"""

# Entradas
sueldo = eval(input("Introduzca el sueldo mensual: "))
	
# Proceso
if sueldo <= 3644.94:
	lim_inf = 0.01
	c_fija = 12.88
	porc_exc = 0.10
elif sueldo <= 7446.19:
	lim_inf = 3644.95
	c_fija = 303.76
	porc_exc = 0.20
elif sueldo <= 10298.35:
	lim_inf = 7446.20
	c_fija = 1063.92
	porc_exc = 0.30
else:
	lim_inf = 10298.36
	c_fija = 3327.42
	porc_exc = 0.35

excedente = sueldo - lim_inf
marginal = excedente * porc_exc
isr = c_fija + marginal
	
# Salidas
print("El ISR es:", isr)
