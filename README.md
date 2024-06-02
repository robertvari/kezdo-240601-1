## Adattípusok (data types)
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

## String parancsok (string methods)
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

**split()** Szétválasztja a mondatokat a ``space`` karakternél és visszakapsz egy listát.
```python
print("Hello World!".split())
>>>['Hello', 'World!']
```
A ```split()``` parancsnak megadhatsz egy karaktert vagy szót is amit a szétválasztáshoz használni akarsz. 
```python
print("Hello".split("e"))
>>>['H', 'llo']
```

## Változók (variables)
A változó egy adat tárolására szolgál. Lényegében adatot tárolsz a memóriában egy “cimke” (változó neve) segítségével. Amire figyelni kell változó névnél:
- A változó neve nem kezdődhet számmal
- Nem lehetnek ékezetes karakterek a névben
- Nem lehet ``space`` a névben

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

## Változók felülírása (override variables)
Helyet spórolunk a memóriában ha az adatokat ugyanazon változónév alatt tároljuk a program futása alatt. Ilyenkor felülírjuk a korábban tárolt adatokat a változóban. 

```python
name = "Csaba"
print(f"Hello {name}!")

name = "Kriszta"
print(f"Hello {name}!")

name = "Tamás"
print(f"Hello {name}!")
```

A fenti példában látod, hogy mindig ugyanazt a változó nevet használtam a név tárolására. 

>**Fontos!**  
Figyelj arra, hogy ha tároltál egy adatot a változóban akkor használd is mielőtt felülírod egy másik adattal. 

## A formázott string (formated string)
Most hogy ismered a változókat használhatod a formázott string-et olyan mondatok kiírására melyben egyes szavak változókból jönnek. A formázott stringeket ``f`` karakterrel jelöljük a string előtt.

```python
name = "Csaba"
address = "Pécs"
age = 26

# f = formated string
print(f"Hello {name}. You live in {address}. You are {age} years old.")
```

## Listák (lists)
A listák olyan adattípusok amikben több adatot is tárolhatsz. A lista megnyitásáhot a ``[]`` karaktereket használjuk és az elemeket ``,`` választja el egymástól.
**Lista deklarálása**
```python
my_friends = ["Csaba", "Kriszta", "Tamás", "Aladár"]
```

**Elemek lekérése**  
Listák elemeit az indexük megadásával kérheted le. Az indexelés mindig 0-val indul.
```python
print(my_friends[1])
>>>Kriszta
```

Egy lista utolsó eleme mindig a -1. helyen áll.
```python
print(my_friends[-1])
```

**Új elem hozzáadása**  
Listához az ``append()`` segítségével adhatsz új elemeket. A parancs az új elemet a lista végéhez adja.
```python
my_friends.append("Johnie")
```

Ha fontos hova kerül az új elem használd az ``insert()`` parancsot.
```python
my_friends.insert(1, "Johnie")
```

**Egy elem cseréje**  
A következő művelettel kicseréljük a listában a második elemet (0-tól számolva).
```python
my_friends[1] = "Balázs"
```

**Elemek törlése**
```python
my_friends.remove("Balázs")
```

Törölhetsz elemet a ``del`` paranccsal is ahol egy elem index értékét kell megadnod.
```python
del my_friends[0]
```

Ha a törlést és az elem lekérését egyszerre akarod akkor használd a ``pop()`` parancsot. Az alábbi példa azt mutaja, hogy törlöm és egy időben tárolom is a törölt elemet a listában. Ezt a parancsot akkor használjuk ha további müveleteket akarunk végezni a törölt elemmel.
```python
friend = my_friends.pop(0)
```

## Lista rendezése (sorting)
Egy lista elemeit rendezhetjül a sort() paranccsal. Az alábbi példa ABC sorrendbe rendezi a listát.
```python
my_friends = ["Csaba", "Kriszta", "Tamás", "Aladár"]
my_friends.sort()
print(my_friends)
```
A parancsnak megadható paraméternként az, hogy fordítsa meg a rendezést.
```python
my_friends.sort(reverse=True)
```

## Slicing
Listákat és string-eket szeletelhetünk a ``[::]`` operátorral. A következőben néhány példa egy string szeletelésére.

Kérem a karaktereket 0-4 indexig:
```python
address = "Budapest"
print(address[0:4])
>>>Buda
```

Ha az elemek lekérését a 0 indextől indítod az első szám kihagyható.
```python
print(address[:4])
>>>Buda
```

Kérem az elemeket a 2. indextől.
```python
print(address[2:])
>>>dapest
```

Minden második elem:
```python
print(address[::2])
>>>Bdps
```

Lista sorrendjének megfordítása:
```python
print(address[::-1])
>>>tsepaduB
```

## Szótárak (dictionaries)
A dictionary-ban az elemek nem indexeken helyezkednek el, hanem egy un. kulcs, vagy keresőszó megadásával kerülnek be. 

```python
phonebook = {
    "06201234567": {"name": "Kiss Csaba", "address": "Budapest", "age": 30},
    "06201235376": {"name": "Kovács Krisztina", "address": "Pécs", "age": 25}
}
```
Láthatod hogy egy dictionary-ban minden elem egy un. ``key:value`` párt alkot.

>**Fontos!**  
Egy dictionary-ban nem lehet két egyforma kulcs mivel a kulcsokat a lekérdezéshez használjuk.

**Elem hozzáadás**  
Egy új elem hozzáadásához mindössze annyit kell tenned hogy definiálsz egy új kulcsot.
```python
phonebook["06201239876"] = {"name": "Kiss Béla", "address": "Debrecen", "age": 42}
```

**Elem szerkesztése**  
Az előzőhoz hasonló itt viszont meglévő külcshoz adunk új értéket.
```python
phonebook["06201235376"] = {"name": "Kiss Béla", "address": "Debrecen", "age": 42}
phonebook["06201235376"]["address"] = "Budapest"
```

**Elem törlése**  
Itt használhatjuk a ``del`` parancsot.
```python
del phonebook["06201235376"]
```

## Gyakorló feladatok
[Gyakorló feladatok megoldásokkal (angol)](https://www.w3schools.com/python/exercise.asp?filename=exercise_syntax1)