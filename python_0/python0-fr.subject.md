# Piscine d'entraînement Python for Data Science - 0

## Starting

*Résumé : Aujourd'hui, tu vas apprendre les bases du langage de programmation Python.*

*Version : 1.3*

---

## Sommaire

- **I** — Règles générales
- **II** — Exercice 00
- **III** — Exercice 01
- **IV** — Exercice 02
- **V** — Exercice 03
- **VI** — Exercice 04
- **VII** — À partir de maintenant, tu dois suivre ces règles supplémentaires
- **VIII** — Exercice 05
- **IX** — Exercice 06
- **X** — Exercice 07
- **XI** — Exercice 08
- **XII** — Exercice 09
- **XIII** — Rendu et évaluation par les pairs

---

## Chapitre I — Règles générales

- Tu dois rendre tes modules depuis un ordinateur du cluster ou en utilisant une machine virtuelle :
  - Tu peux choisir le système d'exploitation de ta machine virtuelle.
  - Ta machine virtuelle doit disposer de tous les logiciels nécessaires à la réalisation de ton projet. Ces logiciels doivent être installés et correctement configurés.
- Sinon, tu peux utiliser directement les ordinateurs du cluster si les outils nécessaires y sont disponibles.
  - Assure-toi d'avoir assez d'espace dans ta session pour installer toutes les dépendances requises pour les modules (utilise `goinfre` si ton campus le propose).
  - Tout doit être installé avant les évaluations.
- Tes fonctions ne doivent pas s'arrêter de manière inattendue (segmentation fault, bus error, double free, etc.), sauf en cas de comportement indéfini. Si un tel problème survient, ton projet sera considéré comme non fonctionnel et recevra un **0** lors de l'évaluation.
- Nous t'encourageons à créer des programmes de test pour ton projet, même si ces tests **ne sont pas à rendre et ne seront pas notés**. Ils te permettront de tester facilement ton travail et celui de tes pairs. Ces tests te seront particulièrement utiles lors de ta soutenance. En effet, pendant la soutenance, tu es libre d'utiliser tes propres tests et/ou ceux du pair que tu évalues.
- Rends ton travail sur ton dépôt Git assigné. Seul le travail présent sur le dépôt Git sera noté. Si Deepthought est chargé de noter ton travail, cela aura lieu après les évaluations par les pairs. Si une erreur survient dans n'importe quelle section de ton travail pendant la notation par Deepthought, l'évaluation s'arrête.
- Tu dois utiliser Python en **version 3.10**.
- Tu peux utiliser n'importe quelle fonction built-in, sauf interdiction explicite dans l'exercice.
- Tes imports de bibliothèques doivent être explicites. Par exemple, tu dois utiliser `import numpy as np`. Importer une bibliothèque avec `from pandas import *` n'est pas autorisé et entraînera un **0** à l'exercice.
- Les variables globales sont interdites.
- Par Odin, par Thor ! Utilise ta tête !!!

---

## Chapitre II — Exercice 00

|                       | Exercice 00 : First python script |
|-----------------------|------------------------------------|
| Dossier de rendu      | `ex00/`                            |
| Fichiers à rendre     | `Hello.py`                         |
| Fonctions autorisées  | Aucune                             |

Tu dois modifier la chaîne de caractères de chaque objet de données pour afficher les salutations suivantes : `"Hello World"`, `"Hello «pays de ton campus»"`, `"Hello «ville de ton campus»"`, `"Hello «nom de ton campus»"`.

```python
ft_list  = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set   = {"Hello", "tutu!"}
ft_dict  = {"Hello" : "titi!"}

#your code here

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
```

Sortie attendue :

```console
$>python Hello.py | cat -e
['Hello', 'World!']$
('Hello', 'France!')$
{'Hello', 'Paris!'}$
{'Hello': '42Paris!'}$
$>
```

---

## Chapitre III — Exercice 01

|                       | Exercice 01 : First use of package |
|-----------------------|-------------------------------------|
| Dossier de rendu      | `ex01/`                             |
| Fichiers à rendre     | `format_ft_time.py`                 |
| Fonctions autorisées  | `time`, `datetime` ou toute autre bibliothèque permettant de récupérer la date |

Écris un script qui formate les dates de cette manière. Bien sûr, ta date ne sera pas la même que la mienne comme dans l'exemple, mais elle doit être formatée de la même façon.

Sortie attendue :

```console
$>python format_ft_time.py | cat -e
Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
Oct 21 2022$
$>
```

---

## Chapitre IV — Exercice 02

|                       | Exercice 02 : First function python |
|-----------------------|--------------------------------------|
| Dossier de rendu      | `ex02/`                              |
| Fichiers à rendre     | `find_ft_type.py`                    |
| Fonctions autorisées  | Aucune                               |

Écris une fonction qui affiche les types des objets et retourne 42.

Voici comment elle doit être prototypée :

```python
def all_thing_is_obj(object: any) -> int:
        #your code here
```

Ton tester.py :

```python
from find_ft_type import all_thing_is_obj

ft_list  = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set   = {"Hello", "tutu!"}
ft_dict  = {"Hello" : "titi!"}

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))
```

Sortie attendue :

```console
$>python tester.py | cat -e
List : <class 'list'>$
Tuple : <class 'tuple'>$
Set : <class 'set'>$
Dict : <class 'dict'>$
Brian is in the kitchen : <class 'str'>$
Toto is in the kitchen : <class 'str'>$
Type not found$
42$
$>
```

> ℹ️ **Info** — Lancer ta fonction seule ne fait rien.

Sortie attendue :

```console
$>python find_ft_type.py | cat -e
$>
```

---

## Chapitre V — Exercice 03

|                       | Exercice 03 : NULL not found |
|-----------------------|-------------------------------|
| Dossier de rendu      | `ex03/`                       |
| Fichiers à rendre     | `NULL_not_found.py`           |
| Fonctions autorisées  | Aucune                        |

Écris une fonction qui affiche le type d'objet de tous les types de « Null ».
Retourne 0 si tout se passe bien et 1 en cas d'erreur.
Ta fonction doit afficher tous les types de « Null ».

Voici comment elle doit être prototypée :

```python
def NULL_not_found(object: any) -> int:
  #your code here
```

Ton tester.py :

```python
from NULL_not_found import NULL_not_found

Nothing = None
Garlic  = float("NaN")
Zero    = 0
Empty   = ""
Fake    = False

NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
```

Sortie attendue :

```console
$>python tester.py | cat -e
Nothing: None <class 'NoneType'>$
Cheese: nan <class 'float'>$
Zero: 0 <class 'int'>$
Empty:  <class 'str'>$
Fake: False <class 'bool'>$
Type not Found$
1$
$>
```

> ℹ️ **Info** — Lancer ta fonction seule ne fait rien.

Sortie attendue :

```console
$>python NULL_not_found.py | cat -e
$>
```

---

## Chapitre VI — Exercice 04

|                       | Exercice 04 : The Even and the Odd |
|-----------------------|-------------------------------------|
| Dossier de rendu      | `ex04/`                             |
| Fichiers à rendre     | `whatis.py`                         |
| Fonctions autorisées  | `sys` ou toute autre bibliothèque permettant de récupérer les arguments |

Crée un script qui prend un nombre en argument, vérifie s'il est pair ou impair, et affiche le résultat.

Si plus d'un argument est fourni, ou si l'argument n'est pas un entier, affiche une **AssertionError**.

Sortie attendue :

```console
$> python whatis.py 14
I'm Even.
$>
$> python whatis.py -5
I'm Odd.
$>
$> python whatis.py
$>
$> python whatis.py 0
I'm Even.
$>
$> python whatis.py Hi!
AssertionError: argument is not an integer
$>
$> python whatis.py 13 5
AssertionError: more than one argument is provided
$>
```

---

## Chapitre VII — À partir de maintenant, tu dois suivre ces règles supplémentaires

- Pas de code dans le scope global. Utilise des fonctions !
- Chaque programme doit avoir son main et ne pas être un simple script :

```python
def main():
  # your tests and your error handling

if __name__ == "__main__":
  main()
```

- Toute exception non attrapée invalidera les exercices, même dans le cas d'une erreur que l'on t'a demandé de tester.
- Toutes tes fonctions doivent avoir une documentation (`__doc__`).
- Ton code doit respecter la norme :
  - `pip install flake8`
  - `alias norminette=flake8`

---

## Chapitre VIII — Exercice 05

|                       | Exercice 05 : First standalone program python |
|-----------------------|------------------------------------------------|
| Dossier de rendu      | `ex05/`                                        |
| Fichiers à rendre     | `building.py`                                  |
| Fonctions autorisées  | `sys` ou toute autre bibliothèque permettant de récupérer les arguments |

Cette fois, tu dois faire un vrai programme autonome, avec un main, qui prend une unique chaîne de caractères en argument et affiche le décompte de ses caractères majuscules, minuscules, de ponctuation, de ses chiffres et de ses espaces.

- Si rien n'est fourni, l'utilisateur est invité à saisir une chaîne.
- Si plus d'un argument est fourni au programme, affiche une **AssertionError**.

Sorties attendues :

```console
$>python building.py "Python 3.0, released in 2008, was a major revision that is not completely backward
    compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
The text contains 171 characters:
2 upper letters
121 lower letters
7 punctuation marks
26 spaces
15 digits
$>
```

Sorties attendues : (le retour chariot compte comme un espace, si tu ne veux pas faire de retour à la ligne utilise ctrl + D)

```console
$>python building.py
What is the text to count?
Hello World!
The text contains 13 characters:
2 upper letters
8 lower letters
1 punctuation marks
2 spaces
0 digits
$>
```

> ℹ️ **Info** — Par Odin, par Thor ! Utilise ta tête !!! Ne réinvente pas la roue, utilise les fonctionnalités du langage.

---

## Chapitre IX — Exercice 06

|                       | Exercice 06 |
|-----------------------|--------------|
| Dossier de rendu      | `ex06/`      |
| Fichiers à rendre     | `ft_filter.py`, `filterstring.py` |
| Fonctions autorisées  | `sys` ou toute autre bibliothèque permettant de récupérer les arguments |

### Partie 1 : Recoder la fonction filter

Recode ton propre `ft_filter`, il doit se comporter comme la fonction built-in originale (il doit retourner la même chose que `print(filter.__doc__)`), et tu dois utiliser les **list comprehensions** pour recoder ton `ft_filter`.

> ⚠️ **Attention** — Bien évidemment, utiliser le built-in `filter` original est interdit.

> ℹ️ **Info** — Tu peux valider le module à partir d'ici, mais nous t'encourageons à continuer car il y a des choses que tu devras savoir pour les projets suivants.

### Partie 2 : Le programme

Crée un programme qui accepte deux arguments : une chaîne de caractères (S) et un entier (N). Le programme doit afficher la liste des mots de **S** dont la longueur est strictement supérieure à **N**.

- Les mots sont séparés les uns des autres par des espaces.
- Les chaînes ne contiennent aucun caractère spécial (ponctuation ou invisible).
- Le programme doit contenir au moins une expression en **list comprehension** et une **lambda**.
- Si le nombre d'arguments est différent de 2, ou si le type d'un argument est mauvais, le programme affiche une **AssertionError**.

Sorties attendues :

```console
$> python filterstring.py 'Hello the World' 4
['Hello', 'World']
$>
```

```console
$> python filterstring.py 'Hello the World' 99
[]
$>
```

```console
$> python filterstring.py 3 'Hello the World'
AssertionError: the arguments are bad
$>
```

```console
$> python filterstring.py
AssertionError: the arguments are bad
$>
```

---

## Chapitre X — Exercice 07

|                       | Exercice 07 : Dictionaries SoS |
|-----------------------|---------------------------------|
| Dossier de rendu      | `ex07/`                         |
| Fichiers à rendre     | `sos.py`                        |
| Fonctions autorisées  | `sys` ou toute autre bibliothèque permettant de récupérer les arguments |

Fais un programme qui prend une chaîne de caractères en argument et l'encode en [code Morse](https://fr.wikipedia.org/wiki/Code_Morse_international).

- Le programme gère les espaces et les caractères alphanumériques.
- Un caractère alphanumérique est représenté par des points `.` et des tirets `-`.
- Les caractères Morse complets sont séparés par un espace simple.
- Un caractère espace est représenté par un slash `/`.

Tu dois utiliser un **dictionnaire** pour stocker ton code Morse.

```python
NESTED_MORSE = {    " ": "/ ",
                    "A": ".- ",
                    ...
```

Si le nombre d'arguments est différent de 1, ou si le type d'un argument est mauvais, le programme affiche une **AssertionError**.

```console
$> python sos.py "sos" | cat -e
... --- ...$
$> python sos.py 'h$llo'
AssertionError: the arguments are bad
$>
```

---

## Chapitre XI — Exercice 08

|                       | Exercice 08 : Loading ... |
|-----------------------|----------------------------|
| Dossier de rendu      | `ex08/`                    |
| Fichiers à rendre     | `Loading.py`               |
| Fonctions autorisées  | `os`                       |

Créons donc une fonction appelée `ft_tqdm`.
La fonction doit reproduire la fonction `tqdm` à l'aide de l'opérateur `yield`.

Voici comment elle doit être prototypée :

```python
def ft_tqdm(lst: range) -> None:
  #your code here
```

Ton tester.py : (tu compares ta version avec l'originale)

```python
from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in ft_tqdm(range(333)):
        sleep(0.005)
print()
for elem in tqdm(range(333)):
        sleep(0.005)
print()
```

Sortie attendue : (tu dois avoir une fonction aussi proche que possible de la version originale)

```console
$> python tester.py
100%|[===============================================================>]| 333/333
100%|                                          | 333/333 [00:01<00:00, 191.61it/s]
```

> ℹ️ **Info** — Tu peux utiliser `get_terminal_size` pour t'adapter à la taille de ton terminal.

---

## Chapitre XII — Exercice 09

|                       | Exercice 09 : My first package creation |
|-----------------------|------------------------------------------|
| Dossier de rendu      | `ex09/`                                  |
| Fichiers à rendre     | `*.py, *.txt, *.toml, README.md, LICENSE` |
| Fonctions autorisées  | PyPI ou toute bibliothèque de création de package |

Crée ton premier package en Python comme tu le souhaites. Il devra apparaître dans la liste des packages installés quand tu tapes la commande `pip list`, et afficher ses caractéristiques quand tu tapes `pip show -v ft_package` :

```console
$>pip show -v ft_package
Name: ft_package
Version: 0.0.1
Summary: A sample test package
Home-page: https://github.com/eagle/ft_package
Author: eagle
Author-email: eagle@42.fr
License: MIT
Location: /home/eagle/...
Requires:
Required-by:
Metadata-Version: 2.1
Installer: pip
Classifiers:
Entry-points:
$>
```

Le package sera installé via pip en utilisant l'une des commandes suivantes (les deux doivent fonctionner) :

- `pip install ./dist/ft_package-0.0.1.tar.gz`
- `pip install ./dist/ft_package-0.0.1-py3-none-any.whl`

Ton package doit pouvoir être appelé depuis un script comme celui-ci :

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
```

---

## Chapitre XIII — Rendu et évaluation par les pairs

Rends ton travail sur ton dépôt Git comme d'habitude. Seul le travail présent dans ton dépôt sera évalué pendant la soutenance. N'hésite pas à vérifier deux fois les noms de tes dossiers et fichiers pour t'assurer qu'ils sont corrects.

> ℹ️ **Info** — Le processus d'évaluation se déroulera sur l'ordinateur du groupe évalué.
