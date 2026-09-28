# Bevegelse


:::{hint} Sentrale likninger
$$
\begin{align}
s &= \frac{1}{2}at^2 + v_0t
&\qquad 2as &= v^2 - v_0^2 \\[6pt]
v &= at + v_0
&\qquad \bar{v} &= \frac{\Delta s}{\Delta t} \\[6pt]
s &= \frac{v_0+v}{2}t
&\qquad \bar{a} &= \frac{\Delta v}{\Delta t}
\end{align}
$$
:::



:::::::::::::::{exercise} Oppgave 1
En elev går $12{,}0 \en{m}$ på $8{,}00 \en{s}$. 

:::::::::::::{part} a
Bestem elevens gjennomsnittsfart. 


:::::{answer}
$$
\bar{v} = 1{,}50 \en{m/s}
$$

::::{solution}
Gjennomsnittsfarten er

$$
\begin{align*}
\bar{v} &= \dfrac{\Delta s}{\Delta t} \\
\\
&= \dfrac{12{,}0 \en{m}}{8{,}00 \en{s}} \\
\\
&= 1{,}50 \en{m/s}
\end{align*}
$$
::::
:::::


:::::::::::::


Eleven står stille i $2{,}00 \en{s}$. Deretter går eleven $18{,}0 \en{m}$ på $12{,}00 \en{s}$.

:::::::::::::{part} b
Bestem elevens gjennomsnittsfart gjennom hele bevegelsen, inkludert pausen.


:::::{answer}
$$
\bar{v} = 1{,}36 \en{m/s}
$$


::::{solution}
Hele bevegelsen tilbakelegger en forflytning på

$$
\Delta s = 12{,}0 \en{m} + 18{,}0 \en{m} = 30{,}0 \en{m}
$$

Den totale tiden som har passert er da:

$$
\Delta t = 2{,}00 \en{s} + 8{,}00 \en{s} + 12{,}00 \en{s} = 22{,}00 \en{s}
$$

Gjennomsnittsfarten gjennom hele bevegelsen er da:

$$
\bar{v} = \frac{\Delta s}{\Delta t} = \frac{30{,}0 \en{m}}{22{,}00 \en{s}} = 1{,}36 \en{m/s}
$$
::::
:::::

:::::::::::::

Anna regner ut at gjennomsnittsfarten er $1{,}50 \en{m/s}$ i **b)**.


:::::::::::::{part} c
Hvilken feil kan Anna ha gjort?


:::::{answer}
Anna har ikke tatt med pausen i beregningen av den totale tiden som gir en høyere gjennomsnittsfart.

:::::

:::::::::::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 2
En vogn beveger seg langs en rett skinne. Vi velger positiv retning til høyre.

Ved $t = 0$ er $v = 6{,}0 \en{m/s}$. Ved $t = 4{,}0 \en{s}$ er $v = -2{,}0 \en{m/s}$.


:::::::::::::{part} a
Finn gjennomsnittsakselerasjonen.


:::::{answer}
$$
\bar{a} = -2{,}0 \en{m/s^2}
$$

::::{solution}
Vi har at 

$$
\Delta v = v_\mathrm{slutt} - v_\mathrm{start} = -2{,}0 \en{m/s} - 6{,}0 \en{m/s}
$$

og $\Delta t = 4{,}0 \en{s}$. Da er gjennomsnittsakselerasjonen

$$
\bar{a} = \frac{\Delta v}{\Delta t} = \frac{-2{,}0 \en{m/s} - 6{,}0 \en{m/s}}{4{,}0 \en{s}} = -2{,}0 \en{m/s^2}
$$
::::
:::::


:::::::::::::


Anta at vognen har konstant akselerasjon gjennom bevegelsen.


:::::::::::::{part} b
Bestem hvor lang tid det tar før vognen snur.


:::::{answer}
$t = 3{,}0 \en{s}$

::::{solution}
Siden akselerasjonen er konstant, kan vi bruke en av bevegelseslikningene. Vognen snur når $v = 0$. Akselerasjonen $a = -2{,}0 \en{m/s^2}$ siden gjennomsnittsakselerasjonen fra **a)** må være lik den konstante akselerasjonen. Dermed har vi følgende kjente og ukjente størrelser:

$$
\begin{align*}
v_0 &= 6{,}0 \en{m/s} \\
\\
v &= 0 \en{m/s} \\
\\
a &= -2{,}0 \en{m/s^2} \\
\\
t &= ?
\end{align*}
$$

Bevegelseslikningen som inneholder alle disse variablene der én er ukjent er 

$$
v = v_0 + a t
$$

Vi løser likningen for $t$:

$$
v - v_0 = at 
$$

$$
\dfrac{v - v_0}{a} = t
$$

Vi regner ut:

$$
\begin{align*}
t &= \dfrac{v - v_0}{a} \\
\\
t &= \dfrac{0 \en{m/s} - 6{,}0 \en{m/s}}{-2{,}0 \en{m/s^2}} \\
\\
t &= 3{,}0 \en{s}
\end{align*}
$$

Altså snur vognen etter $3{,}0 \en{s}$.
::::
:::::

:::::::::::::


En annen vogn har konstant akselerasjon $a = 2{,}0 \en{m/s^2}$. Etter $4{,}0 \en{s}$ hadde vognen en fart på $11 \en{m/s}$.

:::::::::::::{part} c
Bestem startfarten til vognen ved $t = 0$.

:::::{answer}
$v_0 = 3{,}0 \en{m/s}$

::::{solution}
De kjente og ukjente størrelsene kan oppsummeres som:


$$
\begin{align*}
a &= 2{,}0 \en{m/s^2} \\
\\
t &= 4{,}0 \en{s} \\
\\
v &= 11 \en{m/s} \\
\\
v_0 &= \, ?
\end{align*}
$$

Da kan vi bruke bevegelseslikningen

$$
v = at + v_0
$$

og løse den for $v_0$ for å bestemme startfarten:

$$
v_0 = v - at = 11 \en{m/s} - 2{,}0 \en{m/s^2} \cdot 4{,}0 \en{s} = 3{,}0 \en{m/s}
$$

Altså startet vognen med en fart $v_0 = 3{,}0 \en{m/s}$.

::::
:::::

:::::::::::::



:::::::::::::{part} d
Finn farten til vognen etter $10 \en{s}$.


:::::{answer}
$v = 23 \en{m/s}$

::::{solution}
Vi setter nå $t = 0$ til å være da vognen har en fart på $v_0 = 11 \en{m/s}$. Akselerasjonen er konstant $a = 2{,}0 \en{m/s^2}$, og vi ønsker å finne farten etter $10 \en{s}$. Vi kan oppsummere de kjente og ukjente størrelsene som:


$$
\begin{align*}
v_0 &= 11 \en{m/s} \\
\\
a &= 2{,}0 \en{m/s^2} \\
\\
t &= 10 \en{s} - 4{,}0 \en{s} = 6{,}0 \en{s} \\
\\
v &= \, ?
\end{align*}
$$

Vi bruker bevegelseslikningen $v = a t + v_0$ for å regne ut farten:

$$
v = v_0 + a t = 11 \en{m/s} + 2{,}0 \en{m/s^2} \cdot 6{,}0 \en{s} = 23 \en{m/s}
$$
::::
:::::


:::::::::::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 3
En robots posisjon har beveget seg med konstant fart på ulike tidsintervaller som vist i tabellen nedenfor.

:::{table}
---
transpose: true
width: 60%
---
labels: $t / \mathrm{s}$, $s / \mathrm{m}$
$0{,}00$, $0{,}00$
$2{,}00$, $6{,}00$
$5{,}00$, $6{,}00$
$9{,}00$, $-2{,}00$
:::


Posisjonsgrafen til roboten er vist nedenfor.


:::{plot}
width: 60%
xmin: 0
xmax: 10
ymin: -4
ymax: 8
xstep: 1
ystep: 2
line-segment: (0, 0), (2, 6), blue
line-segment: (2, 6), (5, 6), blue
line-segment: (5, 6), (9, -2), blue
xlabel: $t / \mathrm{s}$
ylabel: $s / \mathrm{m}$
:::



:::::::::::::{part} a
Finn farten til roboten på hvert tidsintervall.


:::::{answer}
:::{table}
labels: Tidsintervall, $v$ [$\mathrm{m/s}$]
$[0, 2{,}00\rangle \, \mathrm{ s}$, $3{,}00$
$[2{,}00, 5{,}00\rangle \, \mathrm{ s}$, $0{,}00$
$[5{,}00, 9{,}00\rangle \, \mathrm{ s}$, $-2{,}00$
:::



::::{solution}
Farten er gitt ved stigningstallet til posisjonsgrafen på hvert intervall.

I intervallet $[0, 2{,}00\rangle \en s$ har vi at farten er

$$
v_1 = \dfrac{\Delta s}{\Delta t} = \dfrac{6{,}00 \en{m} - 0 \en{m}}{2{,}00 \en s - 0 \en{s}} = 3{,}00 \en{m/s}
$$

I intervallet $[2{,}00, 5{,}00\rangle \en s$ har vi at 

$$
v_2 = \dfrac{\Delta s}{\Delta t} = \dfrac{6{,}00 \en{m} - 6{,}00 \en{m}}{5{,}00 \en s - 2{,}00 \en{s}} = 0 \en{m/s}
$$

I intervallet $[5{,}00, 9{,}00\rangle \en s$ har vi at 

$$
v_3 = \dfrac{\Delta s}{\Delta t} = \dfrac{-2{,}00 \en{m} - 6{,}00 \en{m}}{9{,}00 \en s - 5{,}00 \en{s}} = -2{,}00 \en{m/s}
$$


::::
:::::


:::::::::::::


:::::::::::::{part} b
Tegn fartsgrafen til roboten.


:::::{answer}
:::{plot}
width: 70%
xmin: 0
xmax: 10
ymin: -5
ymax: 5
xstep: 1
ystep: 1
line-segment: (0, 3), (2, 3), blue
line-segment: (2, 0), (5, 0), blue
line-segment: (5, -2), (9, -2), blue
xlabel: $t / \mathrm{s}$
ylabel: $v / (\mathrm{m/s})$
lw: 4
:::

:::::


:::::::::::::





:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 4
En syklist beveger seg i positiv retning. Farten til syklisten på ulike tidspunkter er vist i tabellen nedenfor.


:::{table}
---
width: 60%
transpose: true
---
labels: $t / \mathrm{s}$, $v / (\mathrm{m/s})$
$0{,}0$, $0{,}0$
$4{,}0$, $8{,}0$
$8{,}0$, $8{,}0$
$10$, $0{,}0$
:::

Syklisten har konstant akselerasjon på hvert tidsintervall som vist i figuren nedenfor.


:::{plot}
width: 60%
line-segment: (0, 0), (4, 8), blue
line-segment: (4, 8), (8, 8), blue
line-segment: (8, 8), (10, 0), blue
xmin: 0
xmax: 11
xstep: 1
ymin: 0
ymax: 9
ystep: 1
xlabel: $t / \mathrm{s}$
ylabel: $v / (\mathrm{m/s})$
:::


:::::::::::::{part} a
Finn akselerasjonen på hvert tidsintervall.


:::::{answer}

:::{table}
labels: Tidsintervall i sekunder, $a / (\mathrm{m/s^2})$
$[0, 4.0\rangle$, $2{,}0$
$[4.0, 8.0\rangle $, $0$
$[8.0, 10\rangle$, $-4{,}0$
:::



::::{solution}
Akselerasjonen på hvert tidsintervall er stigningstallet til fartsgrafen. 

For tidsintervallet $[0, 4.0\rangle \en s$ har vi at 

$$
a_1 = \dfrac{\Delta v}{\Delta t} = \dfrac{8{,}0 \en{m/s} - 0{,}0 \en{m/s}}{4{,}0 \en s - 0{,}0 \en{s}} = 2{,}0 \en{m/s^2}
$$

For tidsintervallet $[4.0, 8.0\rangle \en s$ er farten konstant, så akselerasjonen er $a_2 = 0$.

For tidsintervallet $[8.0, 10\rangle \en s$ har vi at 

$$
a_3 = \dfrac{\Delta v}{\Delta t} = \dfrac{0{,}0 \en{m/s} - 8{,}0 \en{m/s}}{10 \en s - 8{,}0 \en{s}} = -4{,}0 \en{m/s^2}
$$
::::
:::::


:::::::::::::


:::::::::::::{part} b
Tegn akselerasjonsgrafen til syklisten.


:::::{answer}

:::{plot}
width: 60%
line-segment: (0, 2), (4, 2), blue
line-segment: (4, 0), (8, 0), blue
line-segment: (8, -4), (10, -4), blue
xmin: 0
xmax: 11
xstep: 1
ymin: -5
ymax: 5
ystep: 1
xlabel: $t / \mathrm{s}$
ylabel: $a / (\mathrm{m/s^2})$
lw: 4
:::


:::::

:::::::::::::


:::::::::::::{part} c
Regn ut posisjonen ved hvert av tidspunktene i tabellen der vi antar at startposisjonen er $s = 0$.


:::::{answer}

:::{table}
---
width: 60%
transpose: true
---
labels: $t / \mathrm{s}$, $s / \mathrm{m}$
$0{,}0$, $0{,}0$
$4{,}0$, $16$
$8{,}0$, $48$
$10$, $56$
:::


::::{solution}
For å finne posisjonen, tar vi arealet under fartsgrafen der posisjonen ved $t = 0$ er $s = 0$.

Ved $t = 4{,} 0 \en s$ er posisjonen gitt ved arealet under fartsgrafen fra $t = 0$ til $t = 4{,}0 \en s$:

$$
s(4{,}0 \en s) = \frac{1}{2} \cdot 4{,}0 \en s \cdot 8{,}0 \en{m/s} = 16 \en m
$$

Arealet etter $t = 8{,}0 \en s$ er gitt ved arealet under fartsgrafen fra $t = 0$ til $t = 8{,}0 \en s$:

$$
s(8{,}0 \en s) = 16 \en m + 8{,}0 \en m/s \cdot 4{,}0 \en s = 48 \en m
$$

Arealet etter $t = 10 \en s$ er gitt ved arealet under fartsgrafen fra $t = 0$ til $t = 10 \en s$:

$$
s(10 \en s) = 48 \en m + \frac{1}{2} \cdot 2{,}0 \en s \cdot 8{,}0 \en{m/s} = 48 \en m + 8{,}0 \en m = 56 \en m
$$



::::
:::::

:::::::::::::


:::::::::::::{part} d
Tegn en skisse av posisjonsgrafen og marker de kjente punktene.


:::::{answer}

:::{plot}
width: 70%
let: a1 = 2
let: a2 = 0 
let: a3 = -4
let: v0 = 0
let: v1 = 8
let: v2 = 8
function: 1/2 * a1 * x**2 + v0 * x, (0, 4), blue
function: 16 + 8 * (x - 4), (4, 8), blue
function: 48 + v2 * (x - 8) + 1/2 * a3 * (x - 8)**2, (8, 10), blue
ticks: off
point: (4, 16)
text: 4, 16, "$(4, 16)$", top-left
point: (8, 48)
text: 8, 48, "$(8, 48)$", top-left
point: (10, 56)
text: 10, 56, "$(10, 56)$", top-left
ymax: 60
ymin: 0
xmax: 11
xmin: 0
xlabel: $t / \mathrm{s}$
ylabel: $s / \mathrm{m}$
:::

:::::

:::::::::::::




:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 5
En syklist øker farten jevnt fra $2{,}00 \en{m/s}$ til $10{,}0 \en{m/s}$ over $5{,}0 \en s$.


:::::::::::::{part} a
Bestem akselerasjonen til syklisten.

:::::{answer}
$a = 1{,}6 \en{m/s^2}$

::::{solution}
Vi kan bruke bevegelseslikningen 

$$
v = at + v_0
$$

der

* $v_0 = 2{,}00 \en{m/s}$
* $v = 10 \en{m/s}$
* $t = 5{,}0 \en s$
* $a = \, ?$

Så løser vi likningen for $a$:

$$
v = at + v_0 \liff a = \dfrac{v - v_0}{t}
$$

Dermed får vi

$$
a = \dfrac{v - v_0}{t} = \dfrac{10{,}0 \en{m/s} - 2{,}00 \en{m/s}}{5{,}0 \en s} = \dfrac{8{,}00 \en{m/s}}{5{,}0 \en s} = 1{,}6 \en{m/s^2}
$$
::::
:::::

:::::::::::::


:::::::::::::{part} b
Bestem hvor stor avstand syklisten har tilbakelagt.


:::::{answer}
$s = 30 \en m$

::::{solution}
Vi har at

* $v = 10{,}0 \en{m/s}$
* $v_0 = 2{,}00 \en{m/s}$
* $a = 1{,}6 \en{m/s^2}$
* $t = 5{,}0 \en s$
* $s = \, ?$

Vi kan da velge bevegelseslikningen

$$
s = \dfrac{v^2 - v_0^2}{2a} = \dfrac{(10{,}0 \en{m/s})^2 - (2{,}00 \en{m/s})^2}{2 \cdot 1{,}6 \en{m/s^2}} = \dfrac{100 - 4{,}00}{3{,}2} \en m = \dfrac{96}{3{,}2} \en m = 30 \en m
$$
::::
:::::

:::::::::::::


Syklisten fortsetter å akselerere med samme akselerasjon.

:::::::::::::{part} c
Hvor lang tid tar det før syklisten har en fart på $16{,}0 \en{m/s}$?


:::::{answer}
$t = 8{,}8 \en s$ fra start, eller $t = 3{,}8 \en s$ fra tidspunktet syklisten hadde $v = 10 \en{m/s}$.


::::{solution}
Vi har at

* $v = 16{,}0 \en{m/s}$
* $v_0 = 10 \en{m/s}$
* $a = 1{,}6 \en{m/s^2}$
* $t = \, ?$

Vi velger bevegelseslikningen $v = at + v_0$ og løser for $t$:

$$
v = at + v_0 \liff t = \frac{v - v_0}{a}
$$

Så regner vi ut:

$$
t = \frac{v - v_0}{a} = \frac{16{,}0 \en{m/s} - 10 \en{m/s}}{1{,}6 \en{m/s^2}} = \frac{6{,}0 \en{m/s}}{1{,}6 \en{m/s^2}} = 3{,}8 \en s
$$

Fra starten av bevegelsen tilsvarer dette $t = 5{,}0 \en s + 3{,}8 \en s = 8{,}8 \en s$.
::::
:::::


:::::::::::::


Syklisten bråbremset så med en konstant akselerasjon der bremselengden ble $20{,}0 \en m$.


:::::::::::::{part} d
Bestem akselerasjonen syklisten bremset med.


:::::{answer}
$ a = -6{,}40 \en{m/s^2}$

::::{solution}
Vi har at 

* $s = 20{,}0 \en m$
* $v_0 = 16{,}0 \en{m/s}$
* $v = 0 \en{m/s}$
* $a = \, ?$


Vi kan bruke bevegelseslikningen $2as = v^2 - v_0^2$ og løse for $a$:

$$
2as = v^2 - v_0^2 \liff a = \frac{v^2 - v_0^2}{2s}
$$

Så setter vi inn verdiene og regner ut:

$$
a = \frac{v^2 - v_0^2}{2s} = \frac{0 - (16{,}0 \en{m/s})^2}{2 \cdot 20{,}0 \en m} = \frac{-256 \en{m^2/s^2}}{40{,}0 \en m} = -6{,}40 \en{m/s^2}
$$

::::


:::::



:::::::::::::







:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 6
En ball slippes fra ro $50 \en m$ over bakken. Vi ser bort ifra luftmotstand.


:::::::::::::{part} a
Bestem hvor lang tid det tar før ballen treffer bakken.


:::::{answer}
$t = 3{,}2 \en s$

::::{solution}
Vi lar $s = 0$ være høyden der ballen slippes fra ro. Når ballen treffer bakken er

* $s = -50 \en m$
* $v_0 = 0 \en{m/s}$
* $a = -9{,}81 \en{m/s^2}$
* $t = \, ?$


Vi kan bruke bevegelseslikningen

$$
s = \dfrac{1}{2}at^2 + v_0 t
$$

for å finne tiden $t$. Vi har at $v_0 = 0$ som betyr at likningen kan forenkles til

$$
s = \dfrac{1}{2}at^2 \liff t = \sqrt{\frac{2s}{a}}
$$

så setter vi inn verdiene og regner ut:

$$
t = \sqrt{\frac{2\cdot (-50 \en m)}{-9{,}81 \en{m/s^2}}} = 3{,}2 \en s
$$


::::
:::::

:::::::::::::


:::::::::::::{part} b
Bestem farten ballen hadde rett før den traff bakken.


:::::{answer}
$v = -31 \en{m/s}$

::::{solution}
Ballen treffer bakken når $t = 3{,}2 \en s$. Rett før ballen treffer bakken kan vi bruke bevegelseslikningen

$$
v = at + v_0
$$

der $v_0 = 0$ for å finne farten til ballen rett før den treffer bakken. Da får vi:

$$
v = -9{,}81 \en{m/s^2} \cdot 3{,}2 \en s = -31 \en{m/s}
$$
::::
:::::

:::::::::::::


:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 7
På månen er tyngdeakselerasjonen ca. $1/6$ av tyngdeakselerasjonen på jorden. På månen er det ikke noen atmosfære, så vi trenger ikke ta hensyn til luftmotstand.


En kanonkule blir skutt opp fra månens overflate og treffer bakken igjen etter $t = 10 \en s$.

:::::::::::::{part} a
Bestem startfarten til kanonkulen.


:::::{answer}
$v_0 = 8{,}2 \en{m/s}$


::::{solution}
Vi lar $s = 0$ være overflaten på månen når kanonkulen skytes opp. Når kanonkulen treffer bakken igjen etter $t = 10 \en s$ har vi:

* $s = 0$
* $t = 10 \en s$
* $a = -\dfrac{1}{6} \cdot 9{,}81 \en{m/s^2} = -1{,}64 \en{m/s^2}$
* $v_0 = \, ?$

Vi bruker bevegelseslikningen

$$
s = \dfrac{1}{2} a t^2 + v_0 t
$$

som med null-verdiene vi har kan forenkles til

$$
0 = \dfrac{1}{2} a t^2 + v_0 t
$$

Så løser vi for $v_0$:

$$
v_0 t = -\frac{1}{2} a t^2 \liff v_0 = -\frac{1}{2} a t
$$

Så setter vi inn verdiene for $a$ og $t$:

$$
v_0 = -\frac{1}{2} \cdot (-1{,}64 \en{m/s^2}) \cdot 10 \en s = 8{,}2 \en{m/s}
$$
::::
:::::

:::::::::::::


:::::::::::::{part} b
Bestem hvor høyt over bakken kanonkula var på sitt høyeste.


:::::{answer}
$21 \en m$ over bakken.

::::{solution}
Kanonkula er på sitt høyeste over bakken når $v = 0$. Vi kan da bruke bevegelseslikningen

$$
2as = v^2 - v_0^2
$$

der $v = 0$. Da får vi at 

$$
2as = -v_0^2 \liff s = -\frac{v_0^2}{2a}
$$

Så setter vi inn verdiene for $v_0$ og $a$:

$$
s = -\frac{v_0^2}{2a} = -\frac{(8{,}2 \en{m/s})^2}{2 \cdot (-1{,}64 \en{m/s^2})} = 21 \en m
$$
::::
:::::

:::::::::::::




:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 8
En stein kastes opp i luften. Steinen kastes fra $2{,}0 \en m$ over bakken. Steinen er i sitt høyeste punkt etter $3{,}0 \en s$.

Vi ser bort ifra luftmotstand.

:::::::::::::{part} a
Bestem startfarten til steinen.


:::::{answer}
$v_0 = 29{,}4 \en{m/s}$


::::{solution}
Vi lar $s = 0$ være høyden steinen kastes fra når $t = 0$. Når steinen er på sitt høyeste punkt over bakken er

* $t = 3{,}0 \en{s}$
* $v = 0$
* $a = -9{,}81 \en{m/s^2}$
* $v_0 = \, ?$


Da kan vi bruke bevegelseslikningen $v = v_0 + at$ og løse for $v_0$:

$$
\underbrace{v}_{= 0} = v_0 + at \liff v_0 = -at
$$

som gir

$$
v_0 = -(-9{,}81 \en{m/s^2}) \cdot 3{,}0 \en s = 29{,}4 \en{m/s}
$$


::::
:::::


:::::::::::::



:::::::::::::{part} b
Bestem hvor langt over bakken steinen var i sitt høyeste punkt.


:::::{answer}
$46{,}1 \en m$


::::{solution}
Vi setter $s = 0$ der kastet startet når $t = 0$. Når steinen er i sitt høyeste punkt er

* $t = 3{,}0 \en{s}$
* $a = -9{,}81 \en{m/s^2}$
* $v_0 = 29{,}4 \en{m/s}$
* $v = 0$
* $s = \, ?$

Da har vi enten bruke 

$$
s = \dfrac{v_0 + v}{2}t \qeller s = \dfrac{1}{2} a t^2 + v_0 t
$$

for å regne ut $s$. Vi bruker den første likningen siden den gir minst regning:

$$
\begin{align*}
s &= \frac{v_0 + v}{2}t \\
\\
&= \frac{29{,}4 \en{m/s} + 0}{2} \cdot 3{,}0 \en s \\
\\
&= \frac{29{,}4 \en{m/s}}{2} \cdot 3{,}0 \en s \\
\\
&= 44{,}1 \en m
\end{align*}
$$

Steinen startet $2{,}0 \en m$ over bakken, så høyden over bakken i sitt høyeste punkt er $44{,}1 \en m + 2{,}0 \en m = 46{,}1 \en m$.

::::
:::::


:::::::::::::



:::::::::::::{part} c
Bestem hvor lang tid det tar før steinen treffer bakken.


:::::{answer}
$t = 6{,}1 \en s$

::::{solution}
Vi setter $s = 0$ når $t = 0$, altså da steinen kastes i utgangspunktet som ligger $2{,}0 \en{m}$ over bakken.

Når steinen treffer bakken er 

* $s = -2{,}0 \en m$
* $v_0 = 29{,}4 \en{m/s}$
* $a = -9{,}81 \en{m/s^2}$

Med disse opplysningene kan vi bruke bevegelseslikningen

$$
s = \dfrac{1}{2}a t^2 + v_0 t
$$

Vi ønsker å løse denne for $t$ som vi kan gjøre ved å første skrive om likningen til en andregradslikning i $t$ som er lik $0$:

$$
\dfrac{1}{2}a t^2 + v_0 t - s = 0
$$

Vi ganger med $2$ i hvert ledd for å bli kvitt alle brøker:

$$
at^2 + 2v_0 t - 2s = 0
$$

Med $abc$-formelen kan vi da finne $t$ ved 

$$
\begin{align*}
t &= \dfrac{-2v_0 \pm \sqrt{(2v_0)^2 - 4a(-2s)}}{2a} \\
\\
&= \dfrac{-2v_0 \pm \sqrt{4v_0^2 + 8as}}{2a} \\
\\
&= \dfrac{-v_0 \pm \sqrt{v_0^2 + 2as}}{a}
\end{align*}
$$

Så setter vi inn verdiene for $v_0$, $a$ og $s$ og regner ut:

$$
\begin{align*}
t &= \dfrac{-29{,}4 \en{m/s} \pm \sqrt{(29{,}4 \en{m/s})^2 + 2\cdot (-9{,}81 \en{m/s^2})\cdot (-2{,}0 \en m)}}{-9{,}81 \en{m/s^2}} \\
\\
&= \dfrac{-29{,}4 \en{m/s} \pm 30{,}1 \en{m/s}}{-9{,}81 \en{m/s^2}} \\
\end{align*}
$$

som gir

$$
t = -0{,}1 \en s \or t = 6{,}1 \en s
$$

Svaret vi leter etter er den positive løsningen, altså $t = 6{,}1 \en s$.
::::
:::::

:::::::::::::




:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 9
Anna jobber med å skyte opp vannraketter rett opp i luften på jorden. Hun skriver programmer der hun vil regne ut ulike størrelser knyttet til bevegelsen. 

Hun ser bort ifra luftmotstand. 


:::::::::::::{part} a
Anna har skrevet programmet nedenfor.

Bruk bevegelseslikningene til å forutsi hva programmet til Anna skriver ut. Sjekk svaret nedenfor.


::::{hint} Hint
Fra betingelsen i `while`{l=python}-løkka ser vi at programmet holder på så lenge `{s > 2}`{l=python} som betyr at at programmet stopper når $s = 2

Siden programmet skriver ut verdien til `t`{l=python} når løkka stopper, finner programmet ut hvor lang tid det tar før raketten kommer tilbake til starthøyden.
::::


:::{interactive-code}
---
predict:
---
s = 2.000001       # I praksis en starthøyde s = 2 m.
v = 40             # m/s
t = 0              # s
dt = 1e-3          # s

while s > 2:
    a = -9.81  # m/s^2
    v = v + a * dt
    s = s + v * dt
    t = t + dt

print(t)
:::



:::::::::::::



:::::::::::::{part} b
Anna har også skrevet programmet nedenfor.

Bruk bevegelseslikningene til å forutsi hva programmet til Anna skriver ut. Sjekk svaret nedenfor.

:::{hint} Hint
`while`{l=python}-løkka kjører så lenge raketten har positiv fart, altså så lenge den er på vei oppgaver. 

Når programmet stopper, skriver det ut verdien til `s`{l=python}, som er høyden raketten har nådd når den slutter å stige.
:::

:::{interactive-code}
---
predict:
---
s = 2       # m 
v = 40      # m/s
t = 0       # s
dt = 1e-3   # s

while v > 0:
    a = -9.81  # m/s^2
    v = v + a * dt
    s = s + v * dt
    t = t + dt

print(s)

:::


:::::::::::::




:::::::::::::::



