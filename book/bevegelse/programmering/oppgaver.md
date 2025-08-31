# Oppgaver: Programmering av posisjonsgrafer


:::::::::::::::{exercise} Oppgave 1

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Nedenfor vises et program som skriver ut noen tall.

Les programmet og forsutsi hvilke tall som skrives ut:


:::{interactive-code}
---
predict:
---
t = 0
while t < 4:
    print(t)
    t = t + 1


:::


:::::::::::::


:::::::::::::{tab-item} b

Nedenfor vises et program som skriver ut noen tall.

Les programmet og forsutsi hvilke tall som skrives ut:


:::{interactive-code}
---
predict:
---
t = 0
while t < 4:
    print(t)
    t = t + 0.5 # <-- legg merke til forskjellen fra forrige program


:::

:::::::::::::


:::::::::::::{tab-item} c

Nedenfor vises et program som skriver ut noen tall.

Les programmet og forsutsi hvilke tall som skrives ut:


:::{interactive-code}
---
predict:
---
t = 0
while t < 4:
    print(t)
    t = t + 0.1 # <-- legg merke til forskjellen fra forrige program


:::

:::::::::::::


::::::::::::::
:::::::::::::::


---



:::{margin} Tips: Oppgave 2
Tegn fartsgrafen for farten som er brukt i hvert program først!

Du kan forvente små avvik fra det eksakte svaret når du kjører programmene, spesielt i oppgave **c**.
:::

:::::::::::::::{exercise} Oppgave 2
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Nedenfor vises et program som regner ut posisjonen til en gjenstand.

Bestem ved regning hvilken verdi som skrives ut av programmet. Sjekk svaret ditt nedenfor!

:::{interactive-code}
---
predict:
---
s = 0
t = 0
dt = 1
while t < 5:
    v = 2
    s = s + v * dt

    t = t + dt

print(s)
:::

:::::::::::::


:::::::::::::{tab-item} b
Nedenfor vises et program som regner ut posisjonen til en gjenstand.

Bestem ved regning hvilken verdi som skrives ut av programmet. Sjekk svaret ditt nedenfor!

:::{interactive-code}
---
predict:
---
s = 0
t = 0
dt = 0.1
while t < 10:
    v = t - 5
    s = s + v * dt

    t = t + dt

print(s)
:::

:::::::::::::


:::::::::::::{tab-item} c
Nedenfor vises et program som regner ut posisjonen til en gjenstand.

Bestem ved regning hvilken verdi som skrives ut av programmet. Sjekk svaret ditt nedenfor!

:::{interactive-code}
---
predict:
---
s = 2
t = 0
dt = 0.01
while t < 5:
    v = 2*t
    s = s + v * dt

    t = t + dt

print(s)
:::

:::::::::::::


::::::::::::::
:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 3
I figuren nedenfor vises strategien for å bestemme arealet under en fartsgraf.


:::{figure} ./figurer/teori/rektangelmetoden/annotert.svg
---
class: no-click, adaptive-figure
width: 80%
---
:::



::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Programmet nedenfor bruker strategien som er vist i figuren, men programmet er plassert i tilfeldig rekkefølge.

Sett sammen programmet i riktig rekkefølge.
:::::::::::::


:::::::::::::{tab-item} b
Forklar hva betydningen til `dt`{l=python} i programmet har i figuren ovenfor.


:::::::::::::


:::::::::::::{tab-item} c
Forklar hva linje 6 i programmet betyr ut ifra figuren ovenfor.

:::::::::::::


:::::::::::::{tab-item} d
Hva er det kodelinje 8 gjør?


:::::::::::::


:::::::::::::{tab-item} e
Hvilken startposisjon er brukt i programmet?

Bruk programmet til å bestemme sluttposisjonen til bevegelsen (du må nok gjøre `dt`{l=python} litt mindre)
:::::::::::::


::::::::::::::

:::{parsons-puzzle}
s = 0;t = 0;dt = 1
while t < 8:
    v = -t + 4.5
    s = s + v * dt

    t = t + dt

print(s)
:::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 4
I figuren nedenfor vises fartsgrafen til en gjenstand. Vi antar startposisjonen er $s = 0 \, \mathrm{m}$.


:::{plot}
width: 80%
function: x - 4, (0, 8)
xmin: -1
xmax: 9
ymin: -5
ymax: 5
xlabel: $t / \mathrm{s}$
ylabel: $v / (\mathrm{m/s})$
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a
Bestem sluttposisjonen til gjenstanden ved regning (for hånd!). 


:::::::::::::

:::::::::::::{tab-item} b
Fyll ut formlene som mangler i programmet nedenfor og kjør programmet. 

Hva forteller utskriften om bevegelsen?
:::::::::::::


:::::::::::::{tab-item} c
Prøv å endre på verdien til bredden `dt`{l=python} slik at du bruker flere rektangler.

Hva skjer med verdien som skrives ut av programmet?
:::::::::::::



::::::::::::::


:::{interactive-code}
s = 0 # startposisjon i meter
t = 0 # starttid i sekunder
dt = 0.1 # bredde på rektangler i sekunder

while t < 8: # regn ut posisjonen over 8 sekunder
    v = # FYLL INN
    s = # FYLL INN

    t = t + dt # Gå videre til neste tidpunkt


print(s)
:::



:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 5
I figuren nedenfor vises fartsgrafen til ball som kastet rett opp i luften før den faller ned igjen og treffer bakken.

Startposisjonen til ballen er $s = 2 \, \mathrm{m}$ over bakken. Funksjonsuttrykket til farten (i m/s) er gitt ved 

$$
v(t) = -9.81 t + 50
$$


:::{plot}
width: 80%
function: -9.81 * x + 50, (0, 10.23)
xmin: -1
xmax: 11
ymin: -60
ymax: 60
ystep: 10
xlabel: $t / \mathrm{s}$
ylabel: $v / (\mathrm{m/s})$
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag en grov skisse av posisjonsgrafen til ballen.


:::::::::::::



:::::::::::::{tab-item} b
Du vil se noen nye kodelinjer i programmet nedenfor som er forklart med kommentarer. Du trenger ikke tenke så mye over disse utover at å forstå hva rollen deres er.


Fyll ut koden som mangler og kjør programmet. Sammenlign grafen din med skissa du tegnet i oppgave **a**.


:::{interactive-code}
tid = [] # liste som skal lagre tidspunkter
posisjon = [] # liste som skal lagre posisjoner

s = ???? # FYLL INN startposisjonen i meter
t = ???? # FYLL INN: starttiden i sekunder
dt = ???? # FYLL INN: velg bredde på rektanglene

while ????: # FYLL INN: Kjør løkka så lenge ballen er over bakken
    tid.append(t) # Legger til nåværende tid i lista
    posisjon.append(s) # Legger til nåværende posisjon i lista

    v = ???? # FYLL INN: formel for farten
    s = ???? # FYLL INN: regn ut neste posisjon

    t = ???? # FYLL INN: gå videre til neste tidpunkt



# Tegner posisjonsgrafen ut ifra beregningene ovenfor
import plotmath
plotmath.plot(
    xdata=tid,
    ydata=posisjon,
    xlabel="$t$ / s",
    ylabel="$s$ / m",
)
plotmath.show()
plotmath.close()

:::
:::::::::::::



::::::::::::::


:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 6
Farten $v(t)$ i m/s til en radiostyrt bil som kjører langs en rett linje er gitt ved 

$$
v(t) =  \dfrac{1}{2}t^2 - 3t + 4 \qfor t \in [0, 6] \, \mathrm{s}
$$


Vi antar at startposisjonen er $s = 0 \, \mathrm{m}$.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Fyll ut programmet nedenfor og tegn posisjonsgrafen til bilen.


:::::::::::::


:::::::::::::{tab-item} b
Hva er sluttposisjonen til bilen, ifølge fartsgrafen din?


:::::::::::::


:::::::::::::{tab-item} c
1. Når kjører bilen fremover?
2. Når rygger bilen?
3. Når stopper bilen helt opp?

> Det holder med omtrentlige verdier! 
:::::::::::::


::::::::::::::


:::{interactive-code}
tid = [] # liste som skal lagre tidspunkter
posisjon = [] # liste som skal lagre posisjoner

s = ???? # FYLL INN startposisjonen i meter
t = ???? # FYLL INN: starttiden i sekunder
dt = ???? # FYLL INN: velg bredde på rektanglene

while ????: # FYLL INN: Hvor lenge varer bevegelsen?
    tid.append(t) # Legger til nåværende tid i lista
    posisjon.append(s) # Legger til nåværende posisjon i lista

    v = ???? # FYLL INN: formel for farten
    s = ???? # FYLL INN: regn ut neste posisjon

    t = ???? # FYLL INN: gå videre til neste tidpunkt



# Tegner posisjonsgrafen ut ifra beregningene ovenfor
import plotmath
plotmath.plot(
    xdata=tid,
    ydata=posisjon,
    xlabel="$t$ / s",
    ylabel="$s$ / m",
)
plotmath.show()
plotmath.close()

:::






:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 7
Farten $v(t)$ i m/s til en bil er gitt ved et funksjonsuttrykk med **delt forskrift**. Det betyr at funksjonsuttrykket til farten er forskjellig på ulike tidsintervaller:


$$
v(t) = 
\begin{cases}
    2t,\quad 0 \leq t < 2 \\
    \\
    4, \quad 2 \leq t < 4 \\
    \\
    -t + 8, \quad 4 \leq t \leq 8. 
\end{cases}
$$

Vi antar at startposisjonen til bilen er $s = 0 \, \mathrm{m}$.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Tegn fartsgrafen til bilen.


:::::::::::::


:::::::::::::{tab-item} b
Fyll ut programmet nedenfor og tegn posisjonsgrafen til bilen.






:::::::::::::


:::::::::::::{tab-item} c
Hva blir sluttposisjonen til bilen?


:::::::::::::


:::::::::::::{tab-item} d
Hvor langt kjører bilen til sammen?


:::::::::::::

::::::::::::::


:::{interactive-code}
def v(t):
    if 0 <= t < 2:
        return 2*t
    elif ????:
        return 4
    elif ????:
        return ????


tid = [] # liste som skal lagre tidspunkter
posisjon = [] # liste som skal lagre posisjoner

s = ???? # FYLL INN startposisjonen i meter
t = ???? # FYLL INN: starttiden i sekunder
dt = ???? # FYLL INN: velg bredde på rektanglene

while ????: # FYLL INN: Hvor lenge varer bevegelsen?
    tid.append(t) # Legger til nåværende tid i lista
    posisjon.append(s) # Legger til nåværende posisjon i lista

    s = ???? # FYLL INN: regn ut neste posisjon

    t = ???? # FYLL INN: gå videre til neste tidpunkt



# Tegner posisjonsgrafen ut ifra beregningene ovenfor
import plotmath
plotmath.plot(
    xdata=tid,
    ydata=posisjon,
    xlabel="$t$ / s",
    ylabel="$s$ / m",
)
plotmath.show()
plotmath.close()

:::


:::::::::::::::


