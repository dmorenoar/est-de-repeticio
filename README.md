# 👨‍🎓 Bucles `for` i Funció `print()` en Python

## ♦️ Bucle `for` amb `range()`

En les lliçons anteriors vam treballar amb programes seqüencials i condicions. Sovint un programa necessita repetir un bloc diverses vegades. Aquí és on els bucles són útils. A Python hi ha els operadors de bucle `for` i `while`; en aquesta lliçó tractem el `for`.

### Iteració sobre seqüències

El bucle `for` itera sobre qualsevol seqüència. Per exemple, qualsevol cadena de text (string) a Python és una seqüència dels seus caràcters, així que podem iterar sobre ells utilitzant `for`:
```python
for character in 'hello':
    print(character)
```

### Iteració amb `range()`

Un altre cas d'ús per al bucle `for` és iterar sobre una variable entera en ordre creixent o decreixent. Aquesta seqüència d'enters es pot crear utilitzant la funció `range(min_value, max_value)`:
```python
for i in range(5, 8):
    print(i)
# Imprimeix: 5, 6, 7
```

**Observació:** La funció `range(min_value, max_value)` genera una seqüència amb els nombres `min_value`, `min_value + 1`, ..., `max_value - 1`. L'últim nombre **no s'inclou**.

### Forma reduïda de `range()`

Hi ha una forma reduïda de `range()` → `range(max_value)`, en aquest cas `min_value` s'estableix implícitament a zero:
```python
for i in range(3):
    print(i)
# Imprimeix: 0, 1, 2
```

D'aquesta manera podem repetir alguna acció diverses vegades:
```python
for i in range(5):
    print('Hola!')
# Imprimeix "Hola!" 5 vegades
```

### Seqüències buides

`range()` pot definir una seqüència buida, com ara `range(-5)` o `range(7, 3)`. En aquest cas el bloc `for` no s'executarà.

### Exemple: Suma d'enters

Exemple més complex que suma els enters de 1 a n inclusivament:
```python
n = 5
suma = 0
for i in range(1, n + 1):
    suma += i
print(suma)
# Resultat: 15 (1+2+3+4+5)
```

**Atenció:** El valor màxim a `range()` és `n + 1` per fer que `i` sigui igual a `n` en l'últim pas.

### `range()` amb pas (step)

Per iterar sobre una seqüència decreixent, podem utilitzar una forma estesa de `range()` amb tres arguments → `range(start_value, end_value, step)`. Quan s'omet, el pas és implícitament igual a 1. No obstant això, pot ser qualsevol valor diferent de zero:
```python
for i in range(10, 0, -2):
    print(i)
# Imprimeix: 10, 8, 6, 4, 2
```

**Observació:** El bucle sempre inclou `start_value` i exclou `end_value` durant la iteració.

## ♦️ Configuració de la funció `print()`

Per defecte, la funció `print()` imprimeix tots els seus arguments separant-los amb un espai i afegeix un símbol de nova línia després. Aquest comportament es pot canviar utilitzant els arguments de paraula clau `sep` (separador) i `end` (final).

### Arguments `sep` i `end`
```python
# Canviar el separador
print(1, 2, 3, sep=', ')
# Imprimeix: 1, 2, 3

# Canviar el final
print('Hola', end='')
print(' món!')
# Imprimeix: Hola món!

# Combinar ambdós
print(1, 2, 3, sep=' -> ', end=' FI\n')
# Imprimeix: 1 -> 2 -> 3 FI
```

**Observació:** Igual que amb `if-else`, la indentació és el que especifica quines instruccions estan controlades pel `for` i quines no.
