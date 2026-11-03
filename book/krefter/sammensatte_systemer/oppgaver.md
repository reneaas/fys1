# Sammensatte systemer: Oppgaver



:::::::::::::::{exercise} Oppgave 1

:::{plot}
figsize: (6, 3)
width: 400px
align: right
axis: off
axis: equal 
let: l_A = 1
let: l_B = 1
let: d = 2
let: x0 = -1
let: y0 = d
let: s = 0.8
vector: (x0, y0), s, 0, black
vector: (x0, y0), 0, s, black
text: x0 + s, y0, "$x$", center-right
text: x0, y0 + s, "$y$", top-center
polygon: (0, 0), (l_A, 0), (l_A, l_A), (0, l_A), blue, 0.2
polygon: (l_A + d, 0), (l_A + d + l_B, 0), (l_A + d + l_B, l_B), (l_A + d, l_B), blue, 0.2
line-segment: (l_A, l_B/2), (l_A + d, l_B/2), black, solid
point: (d + l_A + l_B, l_B/2)
vector: (d + l_A + l_B, l_B/2), 1, 0, blue
text: d + l_A + l_B + 1, l_B / 2, "$\vec T$", center-right
text: l_A/2, l_A, "A", top-center
text: l_A + d + l_B/2, l_B, "B", top-center
fontsize: 24
:::


To klosser er sammenbundet med en masseløs snor og trekkes av en ytre kraft $\vec T$ langs et horisontalt underlag.

Figuren til høyre viser alle de **ytre** kreftene i $x$-retning.

* Kloss $A$ har massen $m_A = 2{,}0 \en{kg}$ 
* Kloss $B$ har massen $m_B = 2{,}0 \en{kg}$. 
* Styrken på den ytre kraften er $T = 20 \en{N}$. 


Se bort ifra friksjon og luftmotstand.

:::::::::::::{part} a
Bestem akselerasjonen til systemet.



:::::{answer}
$$
a = 5{,}0 \en{m/s^2}
$$

::::{solution}
Den eneste ytre kraften i $x$-retning er $\vec T$ som betyr at summen av kreftene på totalsystemet er

$$
\sum F_x = T
$$

Med Newtons 2. lov får vi at 

$$
\sum F_x = (m_A + m_B)a = T \liff a = \dfrac{T}{m_A + m_B}
$$

Dermed blir akselerasjonen

$$
a = \dfrac{20{,}0 \en{N}}{2{,}0 \en{kg} + 2{,}0 \en{kg}} = 5{,}0 \en{m/s^2}
$$
::::
:::::

:::::::::::::


:::::::::::::{part} b
La $\vec S$ være snorkraften som virker på kloss A fra kloss B.

Tegn et fritt-legemediagram som viser alle kreftene som virker på kloss A.


:::::{answer}
:::{plot}
figsize: (6, 3)
width: 70%
axis: off
axis: equal 
let: l = 2
let: d = 1.5
let: x0 = -1.5*d
let: y0 = d
let: s = 0.8
vector: (x0, y0), s, 0, black
vector: (x0, y0), 0, s, black
text: x0 + s, y0, "$x$", center-right
text: x0, y0 + s, "$y$", top-center
polygon: (0, 0), (l, 0), (l, l), (0, l), blue, 0.1
point: (l/2, l/2)
vector: (l/2, l/2), 0, -2.2, red
text: l/2, l/2 - 2.2, "$\vec G_A$", bottom-center
point: (3*l/4, 0)
vector: (3*l/4, 0), 0, 2.2, red
text: 3*l/4, 2.2, "$\vec N_A$", top-center
point: (l, l/2)
vector: (l, l/2), 1.3, 0, red
text: l + 1.3, l/2, "$\vec S$", center-right
fontsize: 24
:::
:::::


:::::::::::::


:::::::::::::{part} c
Bestem styrken $S$ på snorkraften som virker på kloss A.


:::::{answer}
$$
S = 10 \en{N}
$$


::::{solution}
:::{plot}
figsize: (6, 3)
width: 400px
align: right
axis: off
axis: equal 
let: l = 2
let: d = 1.5
let: x0 = -1.5*d
let: y0 = d
let: s = 0.8
vector: (x0, y0), s, 0, black
vector: (x0, y0), 0, s, black
text: x0 + s, y0, "$x$", center-right
text: x0, y0 + s, "$y$", top-center
polygon: (0, 0), (l, 0), (l, l), (0, l), blue, 0.1
point: (l/2, l/2)
vector: (l/2, l/2), 0, -2.2, red
text: l/2, l/2 - 2.2, "$\vec G_A$", bottom-center
point: (3*l/4, 0)
vector: (3*l/4, 0), 0, 2.2, red
text: 3*l/4, 2.2, "$\vec N_A$", top-center
point: (l, l/2)
vector: (l, l/2), 1.3, 0, red
text: l + 1.3, l/2, "$\vec S$", center-right
fontsize: 24
:::

Fra oppgave **b)** har vi fritt-legemediagrammet til kloss A.

Summen av kreftene i $x$-retning på klossen er

$$
\sum F_{x, A} = S
$$

Fra Newtons 2. lov får vi da at 

$$
\sum F_{x, A} = m_A a
$$

Akselerasjonen til kloss A er den samme som akselerasjonen til totalsystemet som betyr at 

$$
S = m_A a = 2{,}0 \en{kg} \cdot 5{,}0 \en{m/s^2} = 10 \en{N}
$$
::::
:::::

:::::::::::::


:::::::::::::::


:::::::::::::::{exercise} Oppgave 2

:::{plot}
figsize: (6, 3)
width: 400px
align: right
axis: off
axis: equal 
let: l_A = 2
let: l_B = 1
let: d = 1.5
let: x0 = -2
let: y0 = d
let: s = 0.8
vector: (x0, y0), s, 0, black
vector: (x0, y0), 0, s, black
text: x0 + s, y0, "$x$", center-right
text: x0, y0 + s, "$y$", top-center
polygon: (0, 0), (l_A, 0), (l_A, l_A), (0, l_A), blue, 0.2
polygon: (l_A + d, 0), (l_A + d + l_B, 0), (l_A + d + l_B, l_B), (l_A + d, l_B), blue, 0.2
line-segment: (l_A, l_B/2), (l_A + d, l_B/2), black, solid
point: (d + l_A + l_B, l_B/2)
vector: (d + l_A + l_B, l_B/2), 1, 0, blue
text: d + l_A + l_B + 1, l_B / 2, "$\vec T$", center-right
text: l_A/2, l_A, "A", top-center
text: l_A + d + l_B/2, l_B, "B", top-center
fontsize: 24
:::


To klosser er sammenbundet med en masseløs snor og trekkes av en ytre kraft $\vec T$ langs et horisontalt underlag.

Figuren til høyre viser alle de **ytre** kreftene i $x$-retning.

* Kloss $A$ har massen $m_A = 2{,}0 \en{kg}$ 
* Kloss $B$ har massen $m_B = 1{,}0 \en{kg}$
* Trekkraften har styrken $T = 24 \en{N}$


Se bort ifra friksjon og luftmotstand.

:::::::::::::{part} a
Bestem akselerasjonen til systemet.



:::::{answer}
$$
a = 8{,}0 \en{m/s^2}
$$

::::{solution}
Vi har at summen av kreftene i $x$-retning på totalsystemet er

$$
\sum F_x = T
$$

Videre gir Newtons 2. lov for totalsystemet at 

$$
\sum F_x = (m_A + m_B)a
$$

Dermed får vi at 

$$
(m_A + m_B)a = T \limplies a = \dfrac{T}{m_A + m_B}
$$

Vi regner så ut akselerasjonen:

$$
a = \dfrac{24 \en{N}}{2{,}0 \en{kg} + 1{,}0 \en{kg}} = 8{,}0 \en{m/s^2}
$$
::::
:::::

:::::::::::::

:::::::::::::{part} b
La $\vec S$ være snorkraften som virker på kloss B fra kloss A.

Tegn et fritt-legemediagram som viser alle kreftene som virker på kloss B.


:::::{answer}
:::{plot}
figsize: (6, 3)
width: 100%
axis: off
axis: equal 
let: l = 2
let: d = 1.5
let: x0 = -1.5*d
let: y0 = 1.5*d
let: s = 0.8
vector: (x0, y0), s, 0, black
vector: (x0, y0), 0, s, black
text: x0 + s, y0, "$x$", center-right
text: x0, y0 + s, "$y$", top-center
polygon: (0, 0), (l, 0), (l, l), (0, l), blue, 0.1
point: (l/2, l/2)
vector: (l/2, l/2), 0, -2.5, red
text: l/2, l/2 - 2.5, "$\vec G_B$", bottom-center
point: (3*l/4, 0)
vector: (3*l/4, 0), 0, 2.5, red
text: 3*l/4, 2.5, "$\vec N_B$", top-center
point: (0, l/2)
vector: (0, l/2), -1.3, 0, red
text: - 1.3, l/2, "$\vec S$", center-left
fontsize: 20
point: (l, l/2)
vector: (l, l/2), 2, 0, blue
text: l + 2, l/2, "$\vec T$", center-right
:::
:::::


:::::::::::::


:::::::::::::{part} c
Bestem styrken på snorkraften $\vec S$ som virker på kloss B.



:::::{answer}

$$
S = 16 \en{N}
$$

::::{solution}

:::{plot}
figsize: (6, 3)
width: 400px
align: right
axis: off
axis: equal 
let: l = 2
let: d = 1.5
let: x0 = -1.5*d
let: y0 = 1.5*d
let: s = 0.8
vector: (x0, y0), s, 0, black
vector: (x0, y0), 0, s, black
text: x0 + s, y0, "$x$", center-right
text: x0, y0 + s, "$y$", top-center
polygon: (0, 0), (l, 0), (l, l), (0, l), blue, 0.1
point: (l/2, l/2)
vector: (l/2, l/2), 0, -2.5, red
text: l/2, l/2 - 2.5, "$\vec G_B$", bottom-center
point: (3*l/4, 0)
vector: (3*l/4, 0), 0, 2.5, red
text: 3*l/4, 2.5, "$\vec N_B$", top-center
point: (0, l/2)
vector: (0, l/2), -1.3, 0, red
text: - 1.3, l/2, "$\vec S$", center-left
fontsize: 20
point: (l, l/2)
vector: (l, l/2), 2, 0, blue
text: l + 2, l/2, "$\vec T$", center-right
:::


Fra oppgave **b)** har vi fritt-legemediagrammet for kreftene som virker på kloss B.

Summen av kreftene i $x$-retning på kloss B er 

$$
\sum F_{x, B} = T - S
$$

Fra Newtons 2. lov har vi at 

$$
\sum F_{x, B} = m_B a
$$

som betyr at 

$$
T - S = m_B a \limplies S = T - m_B a
$$

Dermed får vi styrken på snorkraften:

$$
S = 24 \en{N} - 1{,}0 \en{kg} \cdot 8{,}0 \en{m/s^2} = 16 \en{N}
$$


::::
:::::

:::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 3
:::{plot}
figsize: (6, 3)
width: 400px
align: right
axis: off
axis: equal 
let: l_A = 2
let: l_B = 1
let: d = 1.5
let: x0 = -2
let: y0 = d
let: s = 0.8
vector: (x0, y0), s, 0, black
vector: (x0, y0), 0, s, black
text: x0 + s, y0, "$x$", center-right
text: x0, y0 + s, "$y$", top-center
polygon: (0, 0), (l_A, 0), (l_A, l_A), (0, l_A), blue, 0.2
polygon: (l_A + d, 0), (l_A + d + l_B, 0), (l_A + d + l_B, l_B), (l_A + d, l_B), blue, 0.2
line-segment: (l_A, l_B/2), (l_A + d, l_B/2), black, solid
point: (d + l_A + l_B, l_B/2)
vector: (d + l_A + l_B, l_B/2), 1, 0, blue
text: d + l_A + l_B + 1, l_B / 2, "$\vec T$", center-right
text: l_A/2, l_A, "A", top-center
text: l_A + d + l_B/2, l_B, "B", top-center
fontsize: 24
:::


To klosser er sammenbundet med en masseløs snor og trekkes av en ytre kraft $\vec T$ langs et horisontalt underlag.

* Kloss $A$ har massen $m_A = 2{,}0 \en{kg}$ 
* Kloss $B$ har massen $m_B = 1{,}0 \en{kg}$. 
* Systemet trekkes av en ytre kraft $T = 24 \en{N}$. 
* Kloss A opplever en friksjonskraft fra underlaget med friksjonstall $\mu = 0{,}30$.
* Kloss B sklir friksjonsfritt på underlaget.



:::::::::::::{part} a
Tegn et fritt-legemediagram som viser alle **ytre** krefter på totalsystemet. 



:::::{answer}
:::{plot}
figsize: (8, 4)
width: 100%
axis: off
axis: equal 
let: l_A = 2
let: l_B = 1
let: d = 1.5
let: x0 = -1.5*d
let: y0 = d
let: s = 0.8
vector: (x0, y0), s, 0, black
vector: (x0, y0), 0, s, black
text: x0 + s, y0, "$x$", center-right
text: x0, y0 + s, "$y$", top-center
polygon: (0, 0), (l_A, 0), (l_A, l_A), (0, l_A), blue, 0.2
polygon: (l_A + d, 0), (l_A + d + l_B, 0), (l_A + d + l_B, l_B), (l_A + d, l_B), blue, 0.2
line-segment: (l_A, l_B/2), (l_A + d, l_B/2), black, solid
point: (d + l_A + l_B, l_B/2)
vector: (d + l_A + l_B, l_B/2), 1.5, 0, blue
text: d + l_A + l_B + 1, l_B / 2, "$\vec T$", top-right
text: 0, l_A, "A", top-left
text: l_A + d, l_B, "B", top-left
fontsize: 20
point: (l_A/2, l_A/2)
vector: (l_A/2, l_A/2), 0, -3, red
text: l_A/2, l_A/2 - 3, "$\vec G_A$", bottom-center
point: (3*l_A/4, 0)
vector: (3*l_A/4, 0), 0, 3, red
text: 3*l_A/4, 3, "$\vec N_A$", top-center
point: (l_A + d + l_B/2, l_B/2)
vector: (l_A + d + l_B/2, l_B/2), 0, -1.5, red
point: (1/4 * l_A, 0)
line-segment: (1/4 * l_A, 0), (1/4 * l_A, -0.25), red, solid
vector: (1/4 * l_A, -0.25), -0.8, 0, red
text: 1/4 * l_A - 0.8, -0.25, "$\vec R_A$", bottom-center
text: l_A + d + l_B/2, l_B/2 - 1.5, "$\vec G_B$", bottom-center
point: (l_A + d + 3*l_B/4, 0)
vector: (l_A + d + 3*l_B/4, 0), 0, 1.5, red
text: l_A + d + 3*l_B/4, 1.5, "$\vec N_B$", top-center
:::
:::::


:::::::::::::


:::::::::::::{part} b
Bestem et uttrykk for friksjonskraften $R_A$ på kloss $A$.


:::::{answer}

$$
R_A = \mu m_A g
$$

::::{solution}
Summen av kreftene i $y$-retning for kloss $A$ er 

$$
\sum F_{y, A} = N_A - G_A
$$

Siden kloss $A$ ikke akselererer i $y$-retning, så får vi fra Newtons 2. lov at 

$$
\sum F_{y, A} = 0 \limplies N_A - G_A = 0 \limplies N_A = G_A = m_A g
$$

Dermed er friksjonskraften på kloss $A$ gitt ved

$$
R_A = \mu N_A = \mu m_A g
$$
::::

:::::

:::::::::::::


:::::::::::::{part} c
Bestem et uttrykk for $\sum F_x$ for totalsystemet.


:::::{answer}

$$
\sum F_x = T - \mu m_A g
$$

::::{solution}
Summen av kreftene på totalsystemet er 

$$
\sum F_x = T - R_A = T - \mu m_A g
$$
::::
:::::

:::::::::::::


:::::::::::::{part} d
Bestem akselerasjonen til totalsystemet.



:::::{answer}
$$
a = 6{,}0 \en{m/s^2}
$$

::::{solution}
Fra oppgave **c)** har vi at 

$$
\sum F_x = T - \mu m_A g
$$

Fra Newtons 2. lov har vi at 

$$
\sum F_x = (m_A + m_B) a
$$

som betyr at 

$$
(m_A + m_B) a = T - \mu m_A g
$$

som gir 

$$
a = \frac{T - \mu m_A g}{m_A + m_B}
$$

Vi regner ut akselerasjonen til totalsystemet:

$$
a = \dfrac{24 \en{N} - 0{,}3 \cdot 2{,}0 \en{kg} \cdot 9{,}81 \en{m/s^2}}{2{,}0 \en{kg} + 1{,}0 \en{kg}} = 6{,}0 \en{m/s^2}
$$
::::
:::::

:::::::::::::


:::::::::::::{part} e
Bestem styrken $S$ på snorkraften som virker mellom kloss A og kloss B.


:::::{answer}

$$
S = 18 \en{N}
$$

::::{solution}
:::{plot}
figsize: (6, 3)
width: 350px
align: right
axis: off
axis: equal 
let: l = 2
let: d = 1.5
let: x0 = -1.5*d
let: y0 = d
let: s = 0.8
vector: (x0, y0), s, 0, black
vector: (x0, y0), 0, s, black
text: x0 + s, y0, "$x$", center-right
text: x0, y0 + s, "$y$", top-center
polygon: (0, 0), (l, 0), (l, l), (0, l), blue, 0.1
point: (l/2, l/2)
vector: (l/2, l/2), 0, -2.2, red
text: l/2, l/2 - 2.2, "$\vec G_A$", bottom-center
point: (3*l/4, 0)
vector: (3*l/4, 0), 0, 2.2, red
text: 3*l/4, 2.2, "$\vec N_A$", top-center
point: (l/4, 0)
line-segment: (l/4, 0), (l/4, -0.3), solid, red
vector: (l/4, -0.3), -1, 0, red
text: l/4 - 1, -0.3, "$\vec R_A$", center-left
point: (l, l/2)
vector: (l, l/2), 1.3, 0, red
text: l + 1.3, l/2, "$\vec S$", center-right
fontsize: 24
:::


Vi velger oss én av klossene for å regne ut styrken på snorkraften. 

Fritt-legemediagrammet til høyre viser alle kreftene som virker på kloss A.

Summen av kreftene i $x$-retning er da gitt ved 

$$
\sum F_{x, A} = S - R_A
$$

Fra Newtons 2. lov har vi at $\sum F_{x, A} = m_A a$ som betyr at 

$$
m_A a = S - R_A \limplies S = m_A a + R_A
$$

Vi vet at $R_A = \mu m_A g$ som betyr at 

$$
S = m_A a + \mu m_A g = m_A(a + \mu g)
$$

Dermed blir styrken på snorkraften

$$
S = 2{,}0 \en{kg} \cdot (6{,}04 \en{m/s^2} + 0{,}30 \cdot 9{,}81 \en{m/s^2}) = 18 \en{N}
$$
::::
:::::

:::::::::::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 4

:::{plot}
figsize: (6, 3)
width: 350px
align: right
axis: off
axis: equal 
let: l_A = 1
let: l_B = 1
let: d = 2
polygon: (0, 0), (l_A, 0), (l_A, l_A), (0, l_A), blue, 0.2
polygon: (l_A + d, 0), (l_A + d + l_B, 0), (l_A + d + l_B, l_B), (l_A + d, l_B), blue, 0.2
line-segment: (l_A, l_B/2), (l_A + d, l_B/2), black, solid
point: (d + l_A + l_B, l_B/2)
vector: (d + l_A + l_B, l_B/2), 1, 0, blue
text: d + l_A + l_B + 1, l_B / 2, "$\vec T$", center-right
text: l_A/2, l_A, "A", top-center
text: l_A + d + l_B/2, l_B, "B", top-center
fontsize: 24
:::


To klosser er sammenbundet med en masseløs snor og trekkes av en ytre kraft $\vec T$ langs et horisontalt underlag.

* Kloss $A$ har massen $m_A = 2{,}0 \en{kg}$ 
* Kloss $B$ har massen $m_B = 2{,}0 \en{kg}$. 
* Styrken på den ytre kraften er $T = 20 \en{N}$ 
* Klossene opplever begge to en friksjonskraft fra underlaget med friksjonstall $\mu = 0{,}30$


:::::::::::::{part} a

Tegn et fritt-legemediagram som viser alle de **ytre** kreftene på totalsystemet.


:::::{answer}

:::{plot}
figsize: (8, 4)
width: 100%
axis: off
axis: equal 
let: l_A = 1
let: l_B = 1
let: d = 1.5
let: x0 = -1.5*d
let: y0 = d
let: s = 0.8
vector: (x0, y0), s, 0, black
vector: (x0, y0), 0, s, black
text: x0 + s, y0, "$x$", center-right
text: x0, y0 + s, "$y$", top-center
polygon: (0, 0), (l_A, 0), (l_A, l_A), (0, l_A), blue, 0.2
polygon: (l_A + d, 0), (l_A + d + l_B, 0), (l_A + d + l_B, l_B), (l_A + d, l_B), blue, 0.2
line-segment: (l_A, l_B/2), (l_A + d, l_B/2), black, solid
point: (d + l_A + l_B, l_B/2)
vector: (d + l_A + l_B, l_B/2), 1, 0, blue
text: d + l_A + l_B + 1, l_B / 2, "$\vec T$", center-right
text: 0, l_A, "A", top-left
text: l_A + d, l_B, "B", top-left
fontsize: 20
point: (l_A/2, l_A/2)
vector: (l_A/2, l_A/2), 0, -1.5, red
text: l_A/2, l_A/2 - 1.5, "$\vec G_A$", bottom-center
point: (3*l_A/4, 0)
vector: (3*l_A/4, 0), 0, 1.5, red
text: 3*l_A/4, 1.5, "$\vec N_A$", top-center
point: (l_A + d + l_B/2, l_B/2)
vector: (l_A + d + l_B/2, l_B/2), 0, -1.5, red
point: (1/4 * l_A, 0)
line-segment: (1/4 * l_A, 0), (1/4 * l_A, -0.25), red, solid
vector: (1/4 * l_A, -0.25), -0.8, 0, red
text: 1/4 * l_A - 0.8, -0.25, "$\vec R_A$", bottom-center
text: l_A + d + l_B/2, l_B/2 - 1.5, "$\vec G_B$", bottom-center
point: (l_A + d + 3*l_B/4, 0)
vector: (l_A + d + 3*l_B/4, 0), 0, 1.5, red
text: l_A + d + 3*l_B/4, 1.5, "$\vec N_B$", top-center
point: (l_A + d + 1/4 * l_B, 0)
line-segment: (l_A + d + 1/4 * l_B, 0), (l_A + d + 1/4 * l_B, -0.25), red, solid
vector: (l_A + d + 1/4 * l_B, -0.25), -0.8, 0, red
text: l_A + d + 1/4 * l_B - 0.8, -0.25, "$\vec R_B$", bottom-center
:::
:::::

:::::::::::::


:::::::::::::{part} b
Bestem akselerasjonen til totalsystemet.


:::::{answer}
$$
a = 2{,}1 \en{m/s^2}
$$

::::{solution}
:::{plot}
figsize: (6, 4)
width: 400px
align: right
axis: off
axis: equal 
let: l_A = 1
let: l_B = 1
let: d = 1.5
let: x0 = -1.5*d
let: y0 = d
let: s = 0.8
vector: (x0, y0), s, 0, black
vector: (x0, y0), 0, s, black
text: x0 + s, y0, "$x$", center-right
text: x0, y0 + s, "$y$", top-center
polygon: (0, 0), (l_A, 0), (l_A, l_A), (0, l_A), blue, 0.2
polygon: (l_A + d, 0), (l_A + d + l_B, 0), (l_A + d + l_B, l_B), (l_A + d, l_B), blue, 0.2
line-segment: (l_A, l_B/2), (l_A + d, l_B/2), black, solid
point: (d + l_A + l_B, l_B/2)
vector: (d + l_A + l_B, l_B/2), 1, 0, blue
text: d + l_A + l_B + 1, l_B / 2, "$\vec T$", center-right
text: 0, l_A, "A", top-left
text: l_A + d, l_B, "B", top-left
fontsize: 20
point: (l_A/2, l_A/2)
vector: (l_A/2, l_A/2), 0, -1.5, red
text: l_A/2, l_A/2 - 1.5, "$\vec G_A$", bottom-center
point: (3*l_A/4, 0)
vector: (3*l_A/4, 0), 0, 1.5, red
text: 3*l_A/4, 1.5, "$\vec N_A$", top-center
point: (l_A + d + l_B/2, l_B/2)
vector: (l_A + d + l_B/2, l_B/2), 0, -1.5, red
point: (1/4 * l_A, 0)
line-segment: (1/4 * l_A, 0), (1/4 * l_A, -0.25), red, solid
vector: (1/4 * l_A, -0.25), -0.8, 0, red
text: 1/4 * l_A - 0.8, -0.25, "$\vec R_A$", bottom-center
text: l_A + d + l_B/2, l_B/2 - 1.5, "$\vec G_B$", bottom-center
point: (l_A + d + 3*l_B/4, 0)
vector: (l_A + d + 3*l_B/4, 0), 0, 1.5, red
text: l_A + d + 3*l_B/4, 1.5, "$\vec N_B$", top-center
point: (l_A + d + 1/4 * l_B, 0)
line-segment: (l_A + d + 1/4 * l_B, 0), (l_A + d + 1/4 * l_B, -0.25), red, solid
vector: (l_A + d + 1/4 * l_B, -0.25), -0.8, 0, red
text: l_A + d + 1/4 * l_B - 0.8, -0.25, "$\vec R_B$", bottom-center
:::

Fra fritt-legemediagrammet vi lagde i **a)** som er vist til høyre, kan vi skrive om summen av kreftene i $x$-retning for totalsystemet som

$$
\sum F_x = T - R_A - R_B
$$

Samtidig gir Newtons 2. lov for totalsystemet at

$$
\sum F_x = (m_A + m_B) a
$$

Siden $\sum F_{y, A} = 0$ og $\sum F_{y, B} = 0$, så vet vi at 

$$
N_A = G_A = m_A g \qog N_B = G_B = m_B g
$$

Dermed får vi at 

$$
R_A = \mu N_A = \mu m_A g \qog R_B = \mu N_B = \mu m_B g
$$

Siden $m_A = m_B$ kan vi la begge to være lik $m = 2{,}0 \en{kg}$ som betyr at vi også kan definere en felles styrke på friksjonskreftene:

$$
R = R_A = R_B = \mu mg
$$

Dermed får vi at 

$$
\sum F_x = T - R - R = T - 2R
$$

Newtons 2. lov gir oss at 

$$
\sum F_x = (m_A + m_B) a = 2ma
$$

som derfor betyr at 

$$
2ma = T - 2R \limplies a = \dfrac{T - 2R}{2m} = \dfrac{T - 2\mu mg}{2m}
$$

Vi regner ut akselerasjonen:

$$
a = \dfrac{20 \en{N} - 2 \cdot 0{,}30 \cdot 2{,}0 \en{kg} \cdot 9{,}81 \en{m/s^2}}{2 \cdot 2{,}0 \en{kg}} = 2{,}1 \en{m/s^2}
$$


::::
:::::

:::::::::::::



:::::::::::::{part} c
Bestem styrken på snorkraften mellom klossene.



:::::{answer}

$$
S = 10 \en{N}
$$

::::{solution}
:::{plot}
figsize: (4, 3)
width: 350px
align: right
axis: off
axis: equal 
let: l = 2
let: d = 1.5
let: x0 = -1.5*d
let: y0 = d
let: s = 0.8
vector: (x0, y0), s, 0, black
vector: (x0, y0), 0, s, black
text: x0 + s, y0, "$x$", center-right
text: x0, y0 + s, "$y$", top-center
polygon: (0, 0), (l, 0), (l, l), (0, l), blue, 0.1
point: (l/2, l/2)
vector: (l/2, l/2), 0, -2.2, red
text: l/2, l/2 - 2.2, "$\vec G_A$", bottom-center
point: (3*l/4, 0)
vector: (3*l/4, 0), 0, 2.2, red
text: 3*l/4, 2.2, "$\vec N_A$", top-center
point: (l, l/2)
vector: (l, l/2), 1.3, 0, red
text: l + 1.3, l/2, "$\vec S$", center-right
point: (1/4 * l, 0)
line-segment: (1/4 * l, 0), (1/4 * l, -0.25), red, solid
vector: (1/4 * l, -0.25), -0.8, 0, red
text: 1/4 * l - 0.8, -0.25, "$\vec R_A$", center-left
fontsize: 24
:::

Vi velger oss kloss $A$ for å finne styrken på snorkraften. Fritt-legemediagrammet til høyre viser alle kreftene som virker på kloss A.

Summen av kreftene i $x$-retning er da 

$$
\sum F_{x, A} = S - R_A
$$

Fra Newtons 2. lov har vi at 

$$
\sum F_{x, A} = m_A a
$$

Altså er 

$$
S - R_A = m_A a \limplies S = R_A + m_A a
$$

Vi vet at $R_A = \mu m_A g$, og vi har allerede funnet akselerasjonen $a = 2{,}1 \en{m/s^2}$. Dermed får vi at 

$$
S = \mu m_A g + m_A a = m_A(\mu g + a)
$$

Vi regner ut styrken på kraften:

$$
S = 2{,}0 \en{kg} \cdot (0{,}30 \cdot 9{,}81 \en{m/s^2} + 2{,}1 \en{m/s^2}) = 10 \en{N}
$$
::::
:::::


:::::::::::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 5


:::{plot}
width: 350px
axis: off
align: right
axis: equal
let: L = 4
let: lA = 1.5
let: Ax = L/2
let: Ay = lA/2
polygon: (Ax - lA/2, Ay - lA/2), (Ax + lA/2, Ay - lA/2), (Ax + lA/2, Ay + lA/2), (Ax - lA/2, Ay + lA/2), blue, 0.1
let: phi = pi/4
let: dy = lA / 2 * sin(phi)
let: dx = lA / 2 * cos(phi)
let: r = 0.15
let: Sx = L + dx + r * cos(phi)
let: Sy = dy + r * sin(phi)
let: lB = 0.8
circle: (Sx, Sy), r, black, solid
line-segment: (0, 0), (L, 0), black, solid
line-segment: (L, 0), (L + dx, dy), black, solid
line-segment: (Ax + lA/2, Sy + r), (Sx, Sy + r), black, solid
let: Bx = Sx + r
let: By = Sy - 0.25 * L - lB/2
line-segment: (Sx + r, Sy), (Sx + r, Sy - r - lB), solid, black
polygon: (Sx + r - lB/2, Sy - 0.25 * L), (Sx + r - lB/2, Sy - 0.25 * L - lB), (Sx + r + lB/2, Sy - 0.25 * L - lB), (Sx + r + lB/2, Sy - 0.25 * L), blue, 0.1
text: Ax, Ay, "A", center-center
text: Bx, By, "B", center-center
:::

To klosser A og B er sammenbundet med en trinse der kloss A ligger på et bord og kloss B henger utenfor bordet.

* Massen til kloss A er $m_A = 2{,}0 \en{kg}$
* Massen til kloss B er $m_B = 1{,}0 \en{kg}$

Kloss A sklir friksjonsfritt med underlaget. Systemet starter fra ro.


:::::::::::::{part} a
Tegn et fritt-legemediagram som viser alle de **ytre** kreftene på systemet.


:::::{answer}


:::{plot}
width: 70%
axis: off
axis: equal
let: L = 4
let: lA = 1.5
let: Ax = L/2
let: Ay = lA/2
polygon: (Ax - lA/2, Ay - lA/2), (Ax + lA/2, Ay - lA/2), (Ax + lA/2, Ay + lA/2), (Ax - lA/2, Ay + lA/2), blue, 0.1
let: phi = pi/4
let: dy = lA / 2 * sin(phi)
let: dx = lA / 2 * cos(phi)
let: r = 0.15
let: Sx = L + dx + r * cos(phi)
let: Sy = dy + r * sin(phi)
let: lB = 0.8
circle: (Sx, Sy), r, black, solid
line-segment: (0, 0), (L, 0), black, solid
line-segment: (L, 0), (L + dx, dy), black, solid
line-segment: (Ax + lA/2, Sy + r), (Sx, Sy + r), black, solid
let: Bx = Sx + r
let: By = Sy - 0.25 * L - lB/2
line-segment: (Sx + r, Sy), (Sx + r, Sy - r - lB), solid, black
polygon: (Sx + r - lB/2, Sy - 0.25 * L), (Sx + r - lB/2, Sy - 0.25 * L - lB), (Sx + r + lB/2, Sy - 0.25 * L - lB), (Sx + r + lB/2, Sy - 0.25 * L), blue, 0.1
point: (Ax, Ay)
vector: (Ax, Ay), 0, -2, red
text: Ax, Ay - 2, "$\vec G_A$", bottom-center
point: (Ax + 0.25 * Ax, 0)
vector: (Ax + 0.25 * Ax, 0), 0, 2, red
text: Ax + 0.25 * Ax, 2, "$\vec N_A$", top-center
point: (Bx, By)
vector: (Bx, By), 0, -1, red
text: Bx, By - 1, "$\vec G_B$", bottom-center
let: x0 = 0
let: y0 = L/2
let: s = 0.8
vector: (x0, y0), s, 0, black
vector: (x0, y0), 0, s, black
text: x0 + s, y0, "$x$", center-right
text: x0, y0 + s, "$y$", top-center
let: x1 = L + L/2
let: y1 = -L/2
let: s = 0.8
vector: (x1, y1), 0, -s, black
vector: (x1, y1), s, 0, black
text: x1 + s, y1, "$y$", center-right
text: x1, y1 - s, "$x$", bottom-center
:::


:::::


:::::::::::::


:::::::::::::{part} b
Bestem akselerasjonen til totalsystemet.

:::::{answer}
$$
a = 3{,}3 \en{m/s^2}
$$

::::{solution}
Summen av kreftene i $x$-retning på totalsystemet er

$$
\sum F_x = G_B = m_B g
$$

Newtons 2. lov for totalsystemet gir at 

$$
\sum F_x = (m_A + m_B)a 
$$

som betyr at 

$$
(m_A + m_B)a = m_B g
$$

Dermed blir akselerasjonen

$$
a = \dfrac{m_B g}{m_A + m_B} = \dfrac{1{,}0 \en{kg} \cdot 9{,}81 \en{m/s^2}}{1{,}0 \en{kg} + 2{,}0 \en{kg}} = 3{,}3 \en{m/s^2}
$$
::::
:::::

:::::::::::::


:::::::::::::{part} c
Kloss A ligger $1{,}0 \en{m}$ fra bordkanten. 

Bestem hvor lang tid klossen bruker på å nå bordkanten.

:::::{answer}
$$
t = 0{,}8 \en{s}
$$

::::{solution}
Vi har at 

$$
s = \dfrac{1}{2}at^2
$$

Vi har at 

* $s = 1{,}0 \en{m}$
* $a = 3{,}27 \en{m/s^2}$ (uten avrunding til riktig gjeldende siffer)

Vi løser likningen for $t$ og velger den positive løsningen:

$$
s = \dfrac{1}{2}at^2 \liff t^2 = \dfrac{2s}{a}
$$

$$
t = \sqrt{\dfrac{2s}{a}} = \sqrt{\dfrac{2 \cdot 1{,}0 \en{m}}{3{,}27 \en{m/s^2}}} = 0{,}8 \en{s}
$$
::::
:::::
:::::::::::::


:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 6

:::{plot}
width: 350px
axis: off
align: right
axis: equal
let: L = 4
let: lA = 1.5
let: Ax = L/2
let: Ay = lA/2
polygon: (Ax - lA/2, Ay - lA/2), (Ax + lA/2, Ay - lA/2), (Ax + lA/2, Ay + lA/2), (Ax - lA/2, Ay + lA/2), blue, 0.1
let: phi = pi/4
let: dy = lA / 2 * sin(phi)
let: dx = lA / 2 * cos(phi)
let: r = 0.15
let: Sx = L + dx + r * cos(phi)
let: Sy = dy + r * sin(phi)
let: lB = 0.8
let: d = 0.75
circle: (Sx, Sy), r, black, solid
line-segment: (0, 0), (L, 0), black, solid
line-segment: (L, 0), (L + dx, dy), black, solid
line-segment: (Ax + lA/2, Sy + r), (Sx, Sy + r), black, solid
let: Bx = Sx + r
let: By = Sy - d * L - lB/2
line-segment: (Bx, Sy), (Bx, By + lB/2), solid, black
polygon: (Bx - lB/2, By + lB/2), (Bx - lB/2, By - lB/2), (Bx + lB/2, By - lB/2), (Bx + lB/2, By + lB/2), blue, 0.1
text: Bx, By, "B", center-center
let: Cx = -Bx + L
let: Cy = By
polygon: (Cx - lB/2, Cy + lB/2), (Cx - lB/2, Cy - lB/2), (Cx + lB/2, Cy - lB/2), (Cx + lB/2, Cy + lB/2), blue, 0.1
let: Px = -dx - r * cos(phi)
let: Py = dy + r * sin(phi)
circle: (Px, Py), r, black, solid
line-segment: (0, 0), (-dx, dy), solid, black
line-segment: (Px, Py + r), (Ax - lA/2, Py + r), solid, black
line-segment: (Px - r, Py), (Cx, Cy + lB/2), solid, black
text: Cx, Cy, "C", center-center
text: Ax, Ay, "A", center-center
:::

Tre klosser er sammenbundet med to masseløse snorer og trinser.

* Massen til kloss A er $m_A = 3{,}0 \en{kg}$
* Massen til kloss B er $m_B = 2{,}0 \en{kg}$
* Massen til kloss C er $m_C = 1{,}0 \en{kg}$

Kloss A sklir friksjonsfritt på bordet. Systemet starter fra ro.


:::::::::::::{part} a
Tegn et fritt-legemediagram som viser alle de **ytre** kreftene på totalsystemet.


:::::{answer}

:::{plot}
width: 70%
axis: off
axis: equal
let: L = 4
let: lA = 1.5
let: Ax = L/2
let: Ay = lA/2
polygon: (Ax - lA/2, Ay - lA/2), (Ax + lA/2, Ay - lA/2), (Ax + lA/2, Ay + lA/2), (Ax - lA/2, Ay + lA/2), blue, 0.1
let: phi = pi/4
let: dy = lA / 2 * sin(phi)
let: dx = lA / 2 * cos(phi)
let: r = 0.15
let: Sx = L + dx + r * cos(phi)
let: Sy = dy + r * sin(phi)
let: lB = 0.8
let: d = 0.75
circle: (Sx, Sy), r, black, solid
line-segment: (0, 0), (L, 0), black, solid
line-segment: (L, 0), (L + dx, dy), black, solid
line-segment: (Ax + lA/2, Sy + r), (Sx, Sy + r), black, solid
let: Bx = Sx + r
let: By = Sy - d * L - lB/2
line-segment: (Bx, Sy), (Bx, By + lB/2), solid, black
polygon: (Bx - lB/2, By + lB/2), (Bx - lB/2, By - lB/2), (Bx + lB/2, By - lB/2), (Bx + lB/2, By + lB/2), blue, 0.1
let: Cx = -Bx + L
let: Cy = By
polygon: (Cx - lB/2, Cy + lB/2), (Cx - lB/2, Cy - lB/2), (Cx + lB/2, Cy - lB/2), (Cx + lB/2, Cy + lB/2), blue, 0.1
let: Px = -dx - r * cos(phi)
let: Py = dy + r * sin(phi)
circle: (Px, Py), r, black, solid
line-segment: (0, 0), (-dx, dy), solid, black
line-segment: (Px, Py + r), (Ax - lA/2, Py + r), solid, black
line-segment: (Px - r, Py), (Cx, Cy + lB/2), solid, black
point: (Ax, Ay)
vector: (Ax, Ay), 0, -3, red
text: Ax, Ay - 3, "$\vec G_A$", bottom-center
point: (Bx, By)
vector: (Bx, By), 0, -2, red
text: Bx, By - 2, "$\vec G_B$", bottom-center
point: (Cx, Cy)
vector: (Cx, Cy), 0, -1, red
text: Cx, Cy - 1, "$\vec G_C$", bottom-center
point: (Ax * 1.2, 0)
vector: (Ax * 1.2, 0), 0, 3, red
text: Ax * 1.2, 3, "$\vec N_A$", top-center
:::::


:::::::::::::


:::::::::::::{part} b
Bestem akselerasjonen til totalsystemet.


:::::{answer}
$$
a = 1{,}6 \en{m/s^2}
$$

::::{solution}
Vi har at summen av kreftene på totalsystemet er 

$$
\sum F_x = G_B - G_C = m_B g - m_C g = (m_B - m_C)g
$$

Med Newtons 2. lov får vi at 

$$
\sum F_x = (m_A + m_B + m_C) a
$$

Dermed er 

$$
(m_A + m_B + m_C) a = (m_B - m_C)g
$$

som gir at 

$$
a = \dfrac{(m_B - m_C)g}{m_A + m_B + m_C}
$$

Derfor blir akselerasjonen

$$
a = \dfrac{(2{,}0 \en{kg} - 1{,}0 \en{kg}) \cdot 9{,}81 \en{m/s^2}}{6{,}0 \en{kg}} = 1{,}6 \en{m/s^2}
$$
::::
:::::


:::::::::::::


:::::::::::::{part} c
Kloss A ligger $2{,}0 \en{m}$ fra bordkanten. 

Bestem hvor lang tid det tar før klossen treffer bordkanten.


:::::{answer}
$$
t = 1{,}6 \en{s}
$$


::::{solution}
Vi bruker at $s = \dfrac{1}{2}at^2$ der vi har at 

* $s = 2{,}0 \en{m}$
* $a = 1{,}6 \en{m/s^2}$

Da får vi at 

$$
s = \dfrac{1}{2}at^2 \limplies t = \sqrt{\dfrac{2s}{a}}
$$

som gir at 

$$
t = \sqrt{\dfrac{2 \cdot 2{,}0 \en{m}}{1{,}6 \en{m/s^2}}} = 1{,}6 \en{s} 
$$
::::


:::::


:::::::::::::

:::::::::::::::