# Oppgaver: Posisjonsgrafer og fartsgrafer


:::::::::::::::{exercise} Oppgave 1
---
level: 1
---
I figuren nedenfor vises posisjonsgrafen til en lekebil som kjører fremover og rygger bakover langs en rett linje.


:::{plot}
width: 80%
function: x, (0, 3), blue
function: -2*(x - 3) + 3, (3, 6), blue
function: -3, (6, 8), blue
function: 3*(x - 8) - 3, (8, 9), blue
xmin: -1
xmax: 11
ymin: -6
ymax: 6
xlabel: $t / \mathrm{s}$
ylabel: $s / \mathrm{m}$
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Gi en beskrivelse av bevegelsen til bilen som har med: 

1. Startposisjonen til bilen.
2. Sluttposisjonen til bilen.
3. Farten til bilen på de ulike tidsintervallene (Husk at den kan være positiv eller negativ).



::::{solution}
1. Startposisjonen til bilen er $s = 0\,\mathrm{m}$ ved $t = 0\,\mathrm{s}$.
2. Sluttposisjonen til bilen er $s = 0\,\mathrm{m}$ ved $t = 9\,\mathrm{s}$.
3. Farten til bilen er:

| $t/ \mathrm{s}$ | $v / (\mathrm{m/s})$ |
|:------------------:|:-----------------------:|
| $\langle 0, 3\rangle$          | $1$                   |
| $\langle 3, 6\rangle$          | $-2$                  |
| $\langle 6, 8\rangle$          | $0$                  |
| $\langle 8, 9\rangle$          | $3$                   |

:::::::::::::


:::::::::::::{tab-item} b
Tegn fartsgrafen til bilen.


::::{answer}
:::{plot}
width: 100%
function: 1, (0, 3), blue
function: -2, (3, 6), blue
function: 0, (6, 8), blue
function: 3, (8, 9), blue
xlabel: $t / \mathrm{s}$
ylabel: $v / (\mathrm{m/s})$
xmin: -1
xmax: 11
ymin: -5
ymax: 5
lw: 3
:::
::::


:::::::::::::


:::::::::::::{tab-item} c
Hvor lenge står bilen i ro?


::::{answer}
Bilen står i ro når $t \in \langle 6, 8 \rangle$ som svarer til 2 sekunder.
::::

:::::::::::::


:::::::::::::{tab-item} d
Er det noen tidspunkter det bilen bråstopper og rygger? I så fall hvilke?


::::{answer}
Bilen bråstopper og rygger når $t = 3$ siden da skifter farten fra positiv verdi til negativ verdi umiddelbart.
::::


:::::::::::::


:::::::::::::{tab-item} e
Hva er den totale avstanden bilen kjører?


::::{answer}
$$
12 \, \mathrm{m}
$$
::::

:::::::::::::


::::::::::::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 2
---
level: 1
---

I figuren nedenfor vises fartsgrafen til en lekebil som kjører langs en rett linje.

:::{plot}
width: 80%
function: 2, (0, 3), blue
function: 0, (3, 4), blue
function: -1, (4, 5), blue
function: 0, (5, 6), blue
function: -2, (6, 8), blue 
function: 0, (8, 10), blue
xlabel: $t / \mathrm{s}$
ylabel: $v / (\mathrm{m/s})$
xmin: -1
xmax: 11
lw: 3.5
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
I hvilke tidsintervaller kjører bilen fremover?


::::{answer}
Bilen kjører fremover når $t \in \langle 0, 3 \rangle \, \mathrm{s}$ siden da er $v > 0$ (positiv). 
::::

:::::::::::::


:::::::::::::{tab-item} b
I hvilke tidsintervaller står bilen i ro?

::::{answer}
Bilen står i ro når $v = 0 \, \mathrm{m/s}$ som er tilfellet for

$$
t \in \langle 3, 4 \rangle \cup \langle 5, 6 \rangle \cup \langle 8, 10 \rangle \, \mathrm{s}
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
I hvilke tidsintervaller rygger bilen? 



::::{answer}
Bilen rygger når $v < 0$ (negativ fart) som er tilfellet for

$$
t \in \langle 4, 5 \rangle \cup \langle 6, 8 \rangle \, \mathrm{s}
$$
::::


:::::::::::::


:::::::::::::{tab-item} d
Vi antar startposisjonen til bilen er $s = 0\,\mathrm{m}$ ved $t = 0\,\mathrm{s}$.

Tegn posisjonsgrafen til bilen.


::::{answer}
:::{plot}
width: 100%
function: 2*x, (0, 3), blue
function: 6, (3, 4), blue
function: -(x - 4) + 6, (4, 5), blue
function: 5, (5, 6), blue
function: -2*(x - 6) + 5, (6, 8), blue
function: 1, (8, 10), blue
xlabel: $t / \mathrm{s}$
ylabel: $s / \mathrm{m}$
xmin: -1
xmax: 11
ymin: -6
ymax: 8
lw: 2.5
:::

::::

:::::::::::::


:::::::::::::{tab-item} e
Hva blir sluttposisjonen til bilen?


::::{answer}
Sluttposisjonen blir $s = 1 \, \mathrm{m}$ ved $t = 10 \, \mathrm{s}$.
::::

:::::::::::::

::::::::::::::




:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 3
---
level: 2
---
Nedenfor vises en uferdig fartsgraf og en uferdig posisjonsgraf for bevegelsen til en gjenstand.


:::::{grid} 2
---
gutter: 0
---
::::{grid-item-card}
:::{plot}
width: 100%
function: x + 2, (0, 2), blue
function: 4, (2, 3), blue
function: 2*(x - 3) + 4, (3, 5), blue
xmin: -1
xmax: 11
ymin: -8
ymax: 10
ystep: 2
xlabel: $t / \mathrm{s}$
ylabel: $s / \mathrm{m}$, -40
lw: 4
fontsize: 26
:::
::::

::::{grid-item-card}
:::{plot}
width: 100%
function: 0, (5, 6), blue
function: -3, (6, 7), blue
function: -2, (7, 9), blue
function: 1, (9, 10), blue
xlabel: $t / \mathrm{s}$
ylabel: $v / (\mathrm{m/s})$, -40
xmin: -1
xmax: 11
ymin: -5
ymax: 5
lw: 4
fontsize: 26
:::
::::

:::::



::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem farten til gjenstanden for $t \in [0, 5] \, \mathrm{s}$. 


::::{answer}
| $t / \mathrm{s}$ | $v / (\mathrm{m/s})$ |
|------------------|---------------------|
| $\langle 0, 2 \rangle$               | $1$                  |
| $\langle 2, 3 \rangle$                | $0$                   |
| $\langle 3, 5 \rangle$                | $2$                   |

::::


:::::::::::::


:::::::::::::{tab-item} b
Beskriv når gjenstanden 
1. beveger seg fremover
2. står i ro
3. beveger seg i negativ retning (bakover)


::::{answer}
Fremover ($v > 0$)
: $t \in \langle 0, 2 \rangle \cup \langle 3, 5 \rangle \cup \langle 9, 10 \rangle \, \mathrm{s}$

I ro ($v = 0$)
: $t \in \langle 2, 3 \rangle \cup \langle 5, 6 \rangle \, \mathrm{s}$

Bakover ($v < 0$)
: $t \in \langle 6, 9 \rangle \, \mathrm{s}$

::::

:::::::::::::


:::::::::::::{tab-item} c
Tegn ferdig fartsgrafen til gjenstanden.


::::{answer}
:::{plot}
width: 100%
function: 1, (0, 2), blue
function: 0, (2, 3), blue
function: 2, (3, 5), blue
function: 0, (5, 6), blue
function: -3, (6, 7), blue
function: -2, (7, 9), blue
function: 1, (9, 10), blue
xmin: -1
xmax: 11
ymin: -5
ymax: 5
xlabel: $t / \mathrm{s}$
ylabel: $v / (\mathrm{m/s})$
lw: 3.5
:::

::::

:::::::::::::


:::::::::::::{tab-item} d
Tegn ferdig posisjonsgrafen til gjenstanden.


::::{answer}
:::{plot}
width: 100%
function: x + 2, (0, 2), blue
function: 4, (2, 3), blue
function: 2*(x - 3) + 4, (3, 5), blue
function: 8, (5, 6), blue
function: -3*(x - 6) + 8, (6, 7), blue
function: -2*(x - 7) + 5, (7, 9), blue
function: 1 * (x - 9) + 1, (9, 10), blue
xlabel: $t / \mathrm{s}$
ylabel: $s / \mathrm{m}$
xmin: -1
xmax: 11
ymin: -7
ymax: 10
lw: 2.5
:::

::::

:::::::::::::


:::::::::::::{tab-item} e
Hvor er det gjenstanden ender opp til slutt?


::::{answer}
Gjenstanden stopper i $s = 2 \, \mathrm{m}$.
::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 4
---
level: 2
---
I figuren nedenfor vises fartsgrafen til en heis.

:::{plot}
width: 80%
function: x, (0, 3), blue
function: 3, (3, 7), blue
function: -(x - 7) + 3, (7, 10), blue
xlabel: $t / \mathrm{s}$
ylabel: $v / (\mathrm{m/s})$
xmin: -1
xmax: 11
ymin: -2
ymax: 5
lw: 3
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Gi en beskrivelse av bevegelsen til heisen.
1. Går heisen oppover eller nedover?
2. Når øker farten til heisen?
3. Når bremser heisen?
4. Når stopper heisen?


::::{answer}
1. Heisen går oppover siden $v > 0$ i hele fartsgrafen.
2. Farten til heisen øker når $t \in \langle 0, 3 \rangle \, \mathrm{s}$.
3. Heisen bremser når $t \in \langle 7, 10 \rangle \, \mathrm{s}$.
4. Heisen stopper når $t = 10 \, \mathrm{s}$.
::::


:::::::::::::


:::::::::::::{tab-item} b
Bruk arealberegninger til å tegne posisjonsgrafen til heisen for $t \in [0, 3] \, \mathrm{s}$.

::::{answer}
$s(t)$ vil være arealet under fartsgrafen fra $t = 0$ og opp til en verdi for $t$. Vi kan lage en tabell ved å bruke at arealet av figuren vil være arealet av en trekant med grunnlinje $t$ og høyde $v(t)$. Da får vi:

| $t / \mathrm{s}$ | $s(t) / \mathrm{m}$ |
|:------------------:|:---------------------:|
| $0$               | $0$                  |
| $1$               | $\dfrac{1}{2}$     |
| $2$               | $2$     |
| $3$               | $\dfrac{9}{2}$     |


<br>

Dette gir posisjonsgrafen nedenfor for $t \in [0, 3] \, \mathrm{s}$.


:::{plot}
width: 80%
function: 0.5 * x**2, (0, 3), blue
xlabel: $t / \mathrm{s}$
ylabel: $s / \mathrm{m}$
xmin: -1
xmax: 11
ymin: -1
ymax: 10
lw: 2.5
:::

::::

:::::::::::::


:::::::::::::{tab-item} c
Tegn resten av posisjonsgrafen til heisen for $t \in [0, 10] \, \mathrm{s}$.


::::{answer}
Vi bruker arealberegninger på tilsvarende måte for resten av figuren ved å regne ut arealet av under fartsgrafen fra $t = 0$ opptil bestemte $t$ verdier og tegner grafen:

:::{plot}
width: 80%
function: 0.5 * x**2, (0, 3), blue
function: 3*(x - 3) + 9/2, (3, 7), blue
function: 33/2 + (-x**2 + 20*x - 91)/2, (7, 10), blue
xlabel: $t / \mathrm{s}$
ylabel: $s / \mathrm{m}$
xmin: -1
xmax: 11
ymin: -2
ymax: 26
lw: 2.5
ystep: 2
:::

::::

:::::::::::::


:::::::::::::{tab-item} d
Hvor langt unna startposisjonen er det heisen stopper?


::::{answer}
$$
21 \, \mathrm{m}
$$
::::

:::::::::::::


:::::::::::::{tab-item} e
Anta det er ca. 3 meter mellom hver estasje i bygningen heisen er i.

Hvor mange etasjer bevegde heisen seg?


::::{answer}
Siden heisen beveget seg $21 \, \mathrm{m}$ og det er ca. $3 \, \mathrm{m}$ mellom hver etasje, så bevegde heisen seg omtrent

$$
\frac{21 \, \mathrm{m}}{3 \, \mathrm{m/etasje}} = 7 \, \mathrm{etasjer}
$$
::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 5
---
level: 2
---
I figuren nedenfor vises fartsgrafen til en bil.

:::{plot}
width: 80%
function: 2, (0, 2), blue
function: (x - 2) + 2, (2, 4), blue,
function: 4, (4, 6), blue
function: -4*(x - 6) + 4, (6, 7), blue
xlabel: $t / \mathrm{s}$
ylabel: $v / (\mathrm{m/s})$
xmin: -1
xmax: 9
ymin: -5
ymax: 5
lw: 3
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Gi en beskrivelse av bevegelsen til bilen med utgangspunkt i spørsmålene nedenfor.
1. Når øker farten til bilen? 
2. Når kjører bilen med konstant fart?
3. Når bremser bilen?
4. Når har bilen stoppet fullstendig? 


::::{answer}
1. Farten til bilen øker når $t \in \langle 2, 4\rangle \, \mathrm{s}$.
2. Bilen kjører med konstant fart når $t \in \langle 0, 2\rangle \cup \langle 4, 6\rangle  \, \mathrm{s}$
3. Bilen bremser når $t \in \langle 6, 7\rangle \, \mathrm{s}$.
4. Bilen har stoppet fullstendig når $t = 7 \, \mathrm{s}$.
::::

:::::::::::::

:::::::::::::{tab-item} b
Vi velger at startposisjonen til bilen er $s = 0 \, \mathrm{m}$ ved $t = 0 \, \mathrm{s}$.

Hva er posisjonen til bilen etter $2 \, \mathrm{s}$?

::::{answer}
Arealet under fartsgrafen fra $t = 0 \, \mathrm{s}$ til $t = 2 \, \mathrm{s}$ gir oss verdien til $s(2)$. 

Arealet under fartsgrafen fra $t = 0 \, \mathrm{s}$ til $t = 2 \, \mathrm{s}$ er et rektangel med bredde $t = 2 \, \mathrm{s}$ og høyde $v = 2 \, \mathrm{m/s}$. Arealet blir derfor:

$$
s(2) = 2 \, \mathrm{m/s} \cdot 2 \, \mathrm{s} = 4 \, \mathrm{m}
$$
::::
:::::::::::::


:::::::::::::{tab-item} c
Bestem posisjonen til bilen etter $4 \, \mathrm{s}$.


::::{answer}
Vi har allerede arealet fra $t = 0 \, \mathrm{s}$ til $t = 2 \, \mathrm{s}$ som er $4 \, \mathrm{m}$. Vi må legge på arealet fra $t = 2 \, \mathrm{s}$ til $t = 4 \, \mathrm{s}$ for å posisjonen etter $4 \, \mathrm{s}$, altså $s(4)$. Selv om dette er et trapes, er det like greit å bare dele opp området i et rektangel med høyde $2 \, \mathrm{m/s}$ og en trekant med høyde $2 \, \mathrm{m/s}$. Både rektangelet og trekanten har en like stor grunnlinje på $2 \, \mathrm{s}$. Da får vi at arealet under fartsgrafen på intervallet $t \in \langle 2, 4 \rangle \, \mathrm{s}$ er:

$$
\dfrac{1}{2} \cdot 2 \, \mathrm{s} \cdot 2 \, \mathrm{m/s} + 2 \, \mathrm{m/s} \cdot 2 \, \mathrm{s} = 2 \, \mathrm{m} + 4 \, \mathrm{m} = 6 \, \mathrm{m}
$$

Vi legger dette på verdien for $s(2)$ for å få verdien til $s(4)$ som gir:

$$
s(4) = s(2) + 6 \, \mathrm{m} = 4 \, \mathrm{m} + 6 \, \mathrm{m} = 10 \, \mathrm{m}
$$

Altså er posisjonen $10 \, \mathrm{m}$ etter $4 \, \mathrm{s}$.
::::

:::::::::::::



:::::::::::::{tab-item} d
Hva blir sluttposisjonen til bilen?


::::{answer}
Vi deler opp figuren og regner ut arealet av hver del under hele fartsgrafen for å få sluttposisjonen. I figuren nedenfor vises arealene for hver del av figuren:


:::{plot}
width: 80%
function: 2, (0, 2), blue
function: (x - 2) + 2, (2, 4), blue,
function: 4, (4, 6), blue
function: -4*(x - 6) + 4, (6, 7), blue
xlabel: $t / \mathrm{s}$
ylabel: $v / (\mathrm{m/s})$, -30
xmin: -1
xmax: 9
ymin: -5
ymax: 5
lw: 3
vline: 2, 0, 2
vline: 4, 0, 4
hline: 2, 2, 4
vline: 6, 0, 4
text: 1, 1, "$4$", center-center, bbox
text: 3, 1, "$4$", center-center, bbox
text: 3.5, 2.7, "$2$", center-center, bbox
text: 5, 2, "$8$", center-center, bbox
text: 6.35, 0.8, "$2$", center-center, bbox
:::

Summen av arealene gir oss sluttposisjonen som blir:

$$
s(7) = 4 \, \mathrm{m} + 6 \, \mathrm{m} + 8 \, \mathrm{m} + 2 \, \mathrm{m} = 20 \, \mathrm{m}
$$

::::

:::::::::::::


:::::::::::::{tab-item} e
Tegn posisjonsgrafen til bilen.


::::{answer}
:::{plot}
width: 100%
function: 2*x, (0, 2), blue
function: 1/2*x**2 + 2, (2, 4), blue
function: 10 + 4*(x - 4), (4, 6), blue
function: 18 + (-2*x**2 + 28*x - 96), (6, 7), blue
xmin: -1
xmax: 9
ymin: -2
ymax: 22
ystep: 2
xlabel: $t / \mathrm{s}$
ylabel: $s / \mathrm{m}$ 
:::

::::

:::::::::::::




::::::::::::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 6
---
level: 2
---
En syklist sykler fra en horisontal slette, over til en motbakke, før syklisten så når toppen og sykler i nedoverbakke. Deretter ender syklisten opp på en horisontal slette igjen. 

Fartsgrafen til syklisten er vist nedenfor.


:::{plot}
width: 80%
function: 5, (0, 4), blue
function: -1.5*(x - 4) + 5, (4, 6), blue
function: 2, (6, 10), blue
function: 2*(x - 10) + 2, (10, 12), blue
function: 6, (12, 16), blue
function: -3 * (x - 16) + 6, (16, 18), blue
xlabel: $t / \mathrm{s}$
ylabel: $v / (\mathrm{m/s})$
xmin: -2
xmax: 20
ymin: -2
ymax: 7
xstep: 2
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Hvilke deler av fartsgrafen passer med beskrivelsen av syklistens bevegelse?

Beskriv hvordan delen passer!

::::{answer}
Fartsgrafen fra $t \in \langle 0, 16\rangle \, \mathrm{s}$ passer med beskrivelsen.

1. Fra $t \in \langle 0, 4\rangle \, \mathrm{s}$ sykler syklisten på en horisontal slette med konstant fart.
2. Fra $t \in \langle 4, 6\rangle \, \mathrm{s}$ sykler syklisten oppover i en motbakke der farten synker.
3. Fra $t \in \langle 6, 10\rangle \, \mathrm{s}$ sykler syklisten oppover bakken med en lavere konstant fart enn før.
4. Fra $t \in \langle 10, 12\rangle \, \mathrm{s}$ sykler syklisten nedover i en bakke der farten øker.
5. Fra $t \in \langle 12, 16\rangle \, \mathrm{s}$ sykler syklisten på en horisontal slette med konstant fart.

::::


:::::::::::::


:::::::::::::{tab-item} b
En av delen på fartsgrafen passer ikke. 

Hva kan denne delen fortelle om syklistens bevegelse?


::::{answer}
På intervallet $t \in \langle 16, 18\rangle \, \mathrm{s}$ viser fartsgrafen at syklisten stopper raskt som indikerer at syklisten bråbremser – kanskje en nesten-kollisjon? Hvem vet.
::::

:::::::::::::


:::::::::::::{tab-item} c
Bestem hvor mange langt syklisten sykler tilsammen.

::::{answer}
For å bestemme hvor langt syklisten sykler tilsammen, regner vi ut arealet under fartsgrafen for hele tidsintervallet $t \in \langle 0, 18\rangle \, \mathrm{s}$. Arealet under fartsgrafen gir oss posisjonen til syklisten. Vi kan dele opp figuren og regne ut arealet av hver mindre del først, og deretter legge de sammen som vist i figuren nedenfor:


:::{plot}
width: 100%
function: 5, (0, 4), blue
function: -1.5*(x - 4) + 5, (4, 6), blue
function: 2, (6, 10), blue
function: 2*(x - 10) + 2, (10, 12), blue
function: 6, (12, 16), blue
function: -3 * (x - 16) + 6, (16, 18), blue
xlabel: $t / \mathrm{s}$
ylabel: $v / (\mathrm{m/s})$, -30
xmin: -2
xmax: 20
ymin: -2
ymax: 7
xstep: 2
vline: 4, 0, 5
vline: 6, 0, 2
hline: 2, 4, 6
vline: 10, 0, 2
vline: 12, 0, 6
vline: 16, 0, 6
hline: 2, 10, 12

text: 2, 2.5, $20$, center-center, bbox
text: 5, 1, $4$, center-center, bbox
annotate: (6, 5), (4.5, 3), "$3$", -0.3
text: 8, 1, $8$, center-center, bbox
text: 11, 1, $4$, center-center, bbox
annotate: (10, 5), (11.5, 3), "$4$", 0.3
text: 14, 3, $24$, center-center, bbox
annotate: (18, 3.5), (16.5, 1), "$6$", -0.3
:::

Vi summerer alle arealene for å finne sluttposisjonen $s(18)$:

$$
s(18) = (20 + 4 + 3 + 8 + 4 + 4 + 24 + 6) \, \mathrm{m} = 73 \, \mathrm{m}
$$

::::


:::::::::::::


:::::::::::::{tab-item} d
Vi setter startposisjonen til syklisten til $s = 0 \, \mathrm{m}$ ved $t = 0 \, \mathrm{s}$.

Tegn en skisse av posisjonsgrafen til syklisten.

::::{answer}
:::{plot}
width: 100%
xmin: -2
xmax: 20
xstep: 2
ymin: -8
ymax: 78
ystep: 8
xlabel: $t / \mathrm{s}$
ylabel: $s / \mathrm{m}$
function: 5*x, (0, 4), blue
function: -3/4 * x**2 + 11*x - 12, (4, 6), blue
function: 2*x + 15, (6, 10), blue
function: x**2 - 18*x + 115, (10, 12), blue
function: 6*x - 29, (12, 16), blue
function: -3/2 * x**2 + 54*x - 413, (16, 18), blue
point: (4, 20)
text: 4, 20, "$(4, 20)$", top-left
point: (6, 27)
text: 6, 27, "$(6, 27)$", bottom-right
point: (10, 35)
text: 10, 35, "$(10, 35)$", top-left
point: (12, 43)
text: 12, 43, "$(12, 43)$", bottom-right
point: (16, 67)
text: 16, 67, "$(16, 67)$", top-left
point: (18, 73)
text: 18, 73, "$(18, 73)$", center-right
:::
::::

::::::::::::::

:::::::::::::::