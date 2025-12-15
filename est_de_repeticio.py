# BUCLE FOR I FUNCIÓ PRINT() EN PYTHON
# =======================================

# 1. ITERACIÓ SOBRE SEQÜÈNCIES
# ------------------------------
print("=== 1. Iteració sobre caràcters ===")
for character in 'hello':
    print(character)

print("\n" + "="*40 + "\n")

# 2. ITERACIÓ AMB RANGE()
# ------------------------
print("=== 2. range(min_value, max_value) ===")
for i in range(5, 8):
    print(i)
# L'últim nombre NO s'inclou (imprimeix 5, 6, 7)

print("\n" + "="*40 + "\n")

# 3. FORMA REDUÏDA DE RANGE()
# ----------------------------
print("=== 3. range(max_value) ===")
for i in range(3):
    print(i)
# min_value és implícitament 0 (imprimeix 0, 1, 2)

print("\n" + "="*40 + "\n")

# 4. REPETIR UNA ACCIÓ DIVERSES VEGADES
# --------------------------------------
print("=== 4. Repetir acció 5 vegades ===")
for i in range(5):
    print('Hola!')

print("\n" + "="*40 + "\n")

# 5. SEQÜÈNCIES BUIDES
# ---------------------
print("=== 5. Seqüències buides (no s'executa res) ===")
for i in range(-5):
    print("Això no s'imprimeix")

for i in range(7, 3):
    print("Això tampoc s'imprimeix")

print("Les seqüències buides no executen el bloc for")

print("\n" + "="*40 + "\n")

# 6. EXEMPLE: SUMA D'ENTERS DE 1 A N
# -----------------------------------
print("=== 6. Suma d'enters de 1 a n ===")
n = 5
suma = 0
for i in range(1, n + 1):
    suma += i
    print(f"i = {i}, suma parcial = {suma}")
print(f"Resultat final: {suma}")
# Resultat: 15 (1+2+3+4+5)

print("\n" + "="*40 + "\n")

# 7. RANGE() AMB PAS (STEP)
# --------------------------
print("=== 7. range() amb pas decreixent ===")
for i in range(10, 0, -2):
    print(i)
# Imprimeix: 10, 8, 6, 4, 2

print("\n" + "="*40 + "\n")

print("=== 8. range() amb pas creixent de 3 ===")
for i in range(0, 20, 3):
    print(i)
# Imprimeix: 0, 3, 6, 9, 12, 15, 18

print("\n" + "="*40 + "\n")

# 9. FUNCIÓ PRINT() AMB SEPARADOR (SEP)
# --------------------------------------
print("=== 9. print() amb separador personalitzat ===")
print(1, 2, 3, sep=', ')
print("A", "B", "C", sep=' -> ')
print("Barcelona", "Madrid", "València", sep=' | ')

print("\n" + "="*40 + "\n")

# 10. FUNCIÓ PRINT() AMB END PERSONALITZAT
# -----------------------------------------
print("=== 10. print() amb end personalitzat ===")
print('Hola', end='')
print(' món!')

print('Primera línia', end=' ... ')
print('segona línia')

print("\n" + "="*40 + "\n")

# 11. COMBINAR SEP I END
# ----------------------
print("=== 11. print() combinant sep i end ===")
print(1, 2, 3, sep=' -> ', end=' FI\n')
print(4, 5, 6, sep=' + ', end=' = 15\n')

print("\n" + "="*40 + "\n")

# 12. EXEMPLE PRÀCTIC: TAULA DE MULTIPLICAR
# ------------------------------------------
print("=== 12. Taula de multiplicar del 7 ===")
numero = 7
for i in range(1, 11):
    resultat = numero * i
    print(f"{numero} x {i} = {resultat}")

print("\n" + "="*40 + "\n")

# 13. EXEMPLE PRÀCTIC: COMPTAR ENRERE
# ------------------------------------
print("=== 13. Compte enrere des de 10 ===")
for i in range(10, 0, -1):
    print(i, end=' ')
print("Enlairament! 🚀")

print("\n" + "="*40 + "\n")

# 14. EXEMPLE PRÀCTIC: PATRÓ AMB ASTERISCS
# -----------------------------------------
print("=== 14. Patró amb asteriscs ===")
for i in range(1, 6):
    print('*' * i)

print("\n" + "="*40 + "\n")

# 15. EXEMPLE PRÀCTIC: SUMA DE NOMBRES PARELLS
# ---------------------------------------------
print("=== 15. Suma de nombres parells de 0 a 20 ===")
suma_parells = 0
for i in range(0, 21, 2):
    suma_parells += i
    print(f"Sumant {i}, total parcial: {suma_parells}")
print(f"Suma total de parells: {suma_parells}")

print("\n" + "="*40 + "\n")
print("FI DEL PROGRAMA")

# BUCLE WHILE
# =======================================

# COMPTADOR SIMPLE
# ---------------------------------------------
comptador = 0
while comptador < 5:
    print(f"Comptador: {comptador}")
    comptador += 1

# Sortida:
# Comptador: 0
# Comptador: 1
# Comptador: 2
# Comptador: 3
# Comptador: 4

# MENU AMB WHILE
# ---------------------------------------------

opcio = ""
while opcio != "sortir":
    print("\n--- Menú ---")
    print("1. Opció 1")
    print("2. Opció 2")
    print("Escriu 'sortir' per acabar")
    
    opcio = input("Tria una opció: ")
    
    if opcio == "1":
        print("Has seleccionat l'opció 1")
    elif opcio == "2":
        print("Has seleccionat l'opció 2")

# SUMA DE NOMBRES
# ---------------------------------------------

suma = 0
numero = 1

while numero <= 10:
    suma += numero
    numero += 1

print(f"La suma d'1 a 10 és: {suma}")  # 55
