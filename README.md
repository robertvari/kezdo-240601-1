## Adattípusok
```python
# string (str)
"Hello my name is Robert Vari."
'Hello my name is Kiss Csaba.'
"It's my birthday!"
'It\'s my birthday!'

# boolean (bool)
True, False

# Numbers
# integers (int)
1, 2, 100, 200, -1, -2, -100, -200

# float
3.14, -3.14

# lists
["Kriszta", "Csaba", "Tamás"]
[1, 2, 3, 4]
```

## String parancsok
Néhány példa a string-ekkel gyakran használt parancsokról.

**upper()** Minden nagybetű.
```python 
print("Hello World!".upper())
```

**lower()** Minden kisbetű.
```python 
print("Hello World!".lower())
```

**title()** Minden kezdőbetű nagy.
```python
print("kiss csaba".title())
```

**replace("from", "to")** Keres és kicserél. Fontos, hogy itt meg kell adnod a parancs paramétereinél, hogy mit mire cseréljen!
```python
print("Hello World!".replace("World", "Csaba"))
```

**split()** Szétválasztja a mondatokat a ```space``` karakternél és visszakapsz egy listát.
```python
print("Hello World!".split())
>>>['Hello', 'World!']
```
A ```split()``` parancsnak megadhatsz egy karaktert vagy szót is amit a szétválasztáshoz használni akarsz. 
```python
print("Hello".split("e"))
>>>['H', 'llo']
```

## Változók
A változó egy adat tárolására szolgál. Lényegében adatot tárolsz a memóriában egy “cimke” (változó neve) segítségével. Amire figyelni kell változó névnél:
- A változó neve nem kezdődhet számmal
- Nem lehetnek ékezetes karakterek a névben
- Nem lehet ```space``` a névben

**Változó deklarálása**
```python
name = "Csaba"
address = "Pécs"
age = 26
```

Miután deklaráltál egy változót a benne tárolt értéket elő trudod hívni a print() paranccsal:
```python
print(name)
>>>Csaba
```
>**Fontos!**  
A változót mindig előbb deklaráljuk és csak utána használhatjuk!

A változókat egy sorban is deklarálhatod: 
```python
name, age, address = "Robert", 42, "Budapest"
```

## Gyakorló feladatok
[Gyakorló feladatok megoldásokkal (angol)](https://www.w3schools.com/python/exercise.asp?filename=exercise_syntax1)