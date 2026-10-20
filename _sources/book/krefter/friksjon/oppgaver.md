# Friksjon: Oppgaver 


::::{hint} Viktige formler
* Dynamisk friksjon $R = \mu_d N$
* Statisk friksjon $R_s \leq R_{\mathrm{maks}}$ der $R_\mathrm{maks} = \mu_s N$
* Gravitasjon $G = mg$
* Bruk $g = 9{,}81 \en{m/s^2}$
::::

> I alle utregninger i dette oppgavesettet, brukes tidligere svar som har riktig antall gjeldende sifre. For eksempel hvis du får $a = 2{,}3 \en{m/s^2}$ i en deloppgave selv om det egentlig var flere siffer i svaret, så brukes $a = 2{,}3 \en{m/s^2}$ i etterfølgende deloppgaver i fasit og løsningsforslag.


:::::::::::::::{exercise} Oppgave 1 
En boks ligger på et vannrett gulv. 

Tegn et fritt-legemediagram for hvert tilfelle nedenfor. Diagrammene skal ha:
1. Riktig angrepspunkt
2. Riktige lengder relativ til hverandre
3. Koordinatsystem som viser positiv retning for aksene


:::::::::::::{part} a
Boksen ligger i ro på gulvet og ingen skyver på boksen.


:::::{answer}
:::{plot}
width: 60%
axis: equal
axis: off
let: s = 8
let: Ax = 0
let: Ay = 0
let: Bx = s
let: By = 0
let: Cx = s
let: Cy = s
let: Dx = 0
let: Dy = s
polygon: (Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy), blue, 0.1
let: Gx = s/2
let: Gy = s/2
let: G = 0.8 * s
point: (Gx, Gy)
vector: (Gx, Gy), 0, -G, red
text: Gx, Gy - G, "$\vec G$", bottom-center
let: N = G
let: Nx = 0.75 * s
let: Ny = 0
point: (Nx, Ny)
vector: (Nx, Ny), 0, N, blue
text: Nx, Ny + N, "$\vec N$", top-center
lw: 5
let: x0 = -0.5 * s
let: y0 = s
let: dx = 0.2 * s
let: dy = 0.2 * s
vector: (x0, y0), dx, 0, black
vector: (x0, y0), 0, dy, black
text: x0 + dx, y0, "$x$", center-right
text: x0, y0 + dy, "$y$", top-center
:::

:::::


:::::::::::::



:::::::::::::{part} b
En person drar i boksen *mot* høyre, men boksen forblir stille.



:::::{answer}
La $T$ være drakraften fra personen og $R$ være friksjonskraften. Siden boksen ikke beveger seg, er $T = R$ og må derfor ha vektorpiler som er like lange.


:::{plot}
width: 60%
axis: equal
axis: off
let: s = 8
let: Ax = 0
let: Ay = 0
let: Bx = s
let: By = 0
let: Cx = s
let: Cy = s
let: Dx = 0
let: Dy = s
polygon: (Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy), blue, 0.1
let: Gx = s/2
let: Gy = s/2
let: G = 0.8 * s
point: (Gx, Gy)
vector: (Gx, Gy), 0, -G, red
text: Gx, Gy - G, "$\vec G$", bottom-center
let: N = G
let: Nx = 0.75 * s
let: Ny = 0
point: (Nx, Ny)
vector: (Nx, Ny), 0, N, blue
text: Nx, Ny + N, "$\vec N$", top-center
let: x0 = -0.5 * s
let: y0 = s
let: dx = 0.2 * s
let: dy = 0.2 * s
vector: (x0, y0), dx, 0, black
vector: (x0, y0), 0, dy, black
text: x0 + dx, y0, "$x$", center-right
text: x0, y0 + dy, "$y$", top-center
let: Tx = s
let: Ty = 0.5 * s
let: T = 0.4 * s
point: (Tx, Ty)
vector: (Tx, Ty), T, 0, blue
text: Tx + T, Ty, "$\vec T$", center-right
let: Rx = 0.2 * s
let: Ry = 0
let: R = 0.4 * s
point: (Rx, Ry)
line-segment: (Rx, Ry), (Rx, Ry - 0.5), red, solid
vector: (Rx, Ry - 0.5), -R, 0, red
text: Rx - R, Ry - 0.5, "$\vec R$", center-left
:::
:::::


:::::::::::::


:::::::::::::{part} c
En person dytter boksen mot høyre (fra venstre side av boksen). Boksen forblir liggende i ro.



:::::{answer}
Hvis vi kaller dyttekraften for $\vec D$, så må friksjonskraften $\vec R$ være like stor, men peke i motsatt retning. Derfor vil vektorpilene være like lange, altså $D = R$. Diagrammet kan da se slik ut:

:::{plot}
width: 60%
axis: equal
axis: off
let: s = 8
let: Ax = 0
let: Ay = 0
let: Bx = s
let: By = 0
let: Cx = s
let: Cy = s
let: Dx = 0
let: Dy = s
polygon: (Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy), blue, 0.1
let: Gx = s/2
let: Gy = s/2
let: G = 0.8 * s
point: (Gx, Gy)
vector: (Gx, Gy), 0, -G, red
text: Gx, Gy - G, "$\vec G$", bottom-center
let: N = G
let: Nx = 0.75 * s
let: Ny = 0
point: (Nx, Ny)
vector: (Nx, Ny), 0, N, blue
text: Nx, Ny + N, "$\vec N$", top-center
let: x0 = -0.5 * s
let: y0 = s
let: dx = 0.2 * s
let: dy = 0.2 * s
vector: (x0, y0), dx, 0, black
vector: (x0, y0), 0, dy, black
text: x0 + dx, y0, "$x$", center-right
text: x0, y0 + dy, "$y$", top-center
let: Tx = 0
let: Ty = 0.8 * s
let: T = 0.4 * s
point: (Tx, Ty)
vector: (Tx, Ty), T, 0, blue
text: Tx + T, Ty, "$\vec D$", center-right
let: Rx = 0.2 * s
let: Ry = 0
let: R = 0.4 * s
point: (Rx, Ry)
line-segment: (Rx, Ry), (Rx, Ry - 0.5), red, solid
vector: (Rx, Ry - 0.5), -R, 0, red
text: Rx - R, Ry - 0.5, "$\vec R$", center-left
:::
:::::


:::::::::::::


:::::::::::::{part} d
Personen dytter med en stor nok kraft til at boksen akselerer mot høyre.



:::::{answer}
Dyttekraften $\vec D$ må nå være større enn friksjonskraften siden boksen akselererer mot høyre. Da får vi et diagram som kan se slik ut: 


:::{plot}
width: 60%
axis: equal
axis: off
let: s = 8
let: Ax = 0
let: Ay = 0
let: Bx = s
let: By = 0
let: Cx = s
let: Cy = s
let: Dx = 0
let: Dy = s
polygon: (Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy), blue, 0.1
let: Gx = s/2
let: Gy = s/2
let: G = 0.8 * s
point: (Gx, Gy)
vector: (Gx, Gy), 0, -G, red
text: Gx, Gy - G, "$\vec G$", bottom-center
let: N = G
let: Nx = 0.8 * s
let: Ny = 0
point: (Nx, Ny)
vector: (Nx, Ny), 0, N, blue
text: Nx, Ny + N, "$\vec N$", top-center
let: x0 = -0.5 * s
let: y0 = s
let: dx = 0.2 * s
let: dy = 0.2 * s
vector: (x0, y0), dx, 0, black
vector: (x0, y0), 0, dy, black
text: x0 + dx, y0, "$x$", center-right
text: x0, y0 + dy, "$y$", top-center
let: Tx = 0
let: Ty = 0.8 * s
let: T = 0.6 * s
point: (Tx, Ty)
vector: (Tx, Ty), T, 0, blue
text: Tx + T, Ty, "$\vec D$", center-right
let: Rx = 0.2 * s
let: Ry = 0
let: R = 0.4 * s
point: (Rx, Ry)
line-segment: (Rx, Ry), (Rx, Ry - 0.5), red, solid
vector: (Rx, Ry - 0.5), -R, 0, red
text: Rx - R, Ry - 0.5, "$\vec R$", center-left
:::
:::::


:::::::::::::


:::::::::::::{part} e
Etter en liten stund hvor personen har dyttet som i oppgave d, så slipper personen taket og lar boksen skli *mot* høyre frem til den stopper. 

Tegn et fritt-legemediagram som viser kreftene etter at personen har sluppet taket frem til boksen stopper.



:::::{answer}
:::{plot}
width: 60%
axis: equal
axis: off
let: s = 8
let: Ax = 0
let: Ay = 0
let: Bx = s
let: By = 0
let: Cx = s
let: Cy = s
let: Dx = 0
let: Dy = s
polygon: (Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy), blue, 0.1
let: Gx = s/2
let: Gy = s/2
let: G = 0.8 * s
point: (Gx, Gy)
vector: (Gx, Gy), 0, -G, red
text: Gx, Gy - G, "$\vec G$", bottom-center
let: N = G
let: Nx = 0.8 * s
let: Ny = 0
point: (Nx, Ny)
vector: (Nx, Ny), 0, N, blue
text: Nx, Ny + N, "$\vec N$", top-center
let: x0 = -0.5 * s
let: y0 = s
let: dx = 0.2 * s
let: dy = 0.2 * s
vector: (x0, y0), dx, 0, black
vector: (x0, y0), 0, dy, black
text: x0 + dx, y0, "$x$", center-right
text: x0, y0 + dy, "$y$", top-center
let: Tx = 0
let: Ty = 0.8 * s
let: T = 0.6 * s
let: Rx = 0.2 * s
let: Ry = 0
let: R = 0.4 * s
point: (Rx, Ry)
line-segment: (Rx, Ry), (Rx, Ry - 0.5), red, solid
vector: (Rx, Ry - 0.5), -R, 0, red
text: Rx - R, Ry - 0.5, "$\vec R$", center-left
:::
:::::



:::::::::::::




:::::::::::::::





---



:::::::::::::::{exercise} Oppgave 2
En kloss med masse $5{,}0 \en{kg}$ ligger på et vannrett bord.
En elev trekker klossen vannrett med en kraftmåler og observerer følgende: 

* Klossen begynner å skli idet kraftmåleren viser $20 \en{N}$
* Etter at klossen begynner å skli, kan eleven holde en konstant fart på klossen med en trekkraft på $12 \en{N}$



:::::::::::::{part} a
Tegn et fritt-legemediagram for situasjonen rett før klossen begynner å skli.



:::::{answer}
Vi lar $\vec T$ være trekkraften fra eleven på boksen. Da vil figuren nedenfor vise et fritt-legemediagram for situasjonen der både $\vec T$ og den statiske friksjonskraften $\vec R_s$ er like store. 

:::{plot}
width: 60%
axis: equal
axis: off
let: s = 8
let: Ax = 0
let: Ay = 0
let: Bx = s
let: By = 0
let: Cx = s
let: Cy = s
let: Dx = 0
let: Dy = s
polygon: (Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy), blue, 0.1
let: Gx = s/2
let: Gy = s/2
let: G = 0.8 * s
point: (Gx, Gy)
vector: (Gx, Gy), 0, -G, red
text: Gx, Gy - G, "$\vec G$", bottom-center
let: N = G
let: Nx = 0.75 * s
let: Ny = 0
point: (Nx, Ny)
vector: (Nx, Ny), 0, N, blue
text: Nx, Ny + N, "$\vec N$", top-center
let: x0 = -0.5 * s
let: y0 = s
let: dx = 0.2 * s
let: dy = 0.2 * s
vector: (x0, y0), dx, 0, black
vector: (x0, y0), 0, dy, black
text: x0 + dx, y0, "$x$", center-right
text: x0, y0 + dy, "$y$", top-center
let: Tx = s
let: Ty = 0.5 * s
let: T = 0.4 * s
point: (Tx, Ty)
vector: (Tx, Ty), T, 0, blue
text: Tx + T, Ty, "$\vec T$", center-right
let: Rx = 0.2 * s
let: Ry = 0
let: R = 0.4 * s
point: (Rx, Ry)
line-segment: (Rx, Ry), (Rx, Ry - 0.5), red, solid
vector: (Rx, Ry - 0.5), -R, 0, red
text: Rx - R, Ry - 0.5, "$\vec R_s$", center-left
:::


:::::

:::::::::::::


:::::::::::::{part} b
Tegn et fritt-legemediagram for situasjonen når klossen har begynt å skli med konstant fart.


:::::{answer}
Vi lar $\vec T$ være trekkraften fra eleven på boksen. Siden boksen beveger seg med konstant fart, vil $\vec T$ og den dynamiske friksjonskraften $\vec R_d$ være like store. Diagrammet kan da se slik ut:

:::{plot}
width: 60%
axis: equal
axis: off
let: s = 8
let: Ax = 0
let: Ay = 0
let: Bx = s
let: By = 0
let: Cx = s
let: Cy = s
let: Dx = 0
let: Dy = s
polygon: (Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy), blue, 0.1
let: Gx = s/2
let: Gy = s/2
let: G = 0.8 * s
point: (Gx, Gy)
vector: (Gx, Gy), 0, -G, red
text: Gx, Gy - G, "$\vec G$", bottom-center
let: N = G
let: Nx = 0.75 * s
let: Ny = 0
point: (Nx, Ny)
vector: (Nx, Ny), 0, N, blue
text: Nx, Ny + N, "$\vec N$", top-center
let: x0 = -0.5 * s
let: y0 = s
let: dx = 0.2 * s
let: dy = 0.2 * s
vector: (x0, y0), dx, 0, black
vector: (x0, y0), 0, dy, black
text: x0 + dx, y0, "$x$", center-right
text: x0, y0 + dy, "$y$", top-center
let: Tx = s
let: Ty = 0.5 * s
let: T = 0.4 * s
point: (Tx, Ty)
vector: (Tx, Ty), T, 0, blue
text: Tx + T, Ty, "$\vec T$", center-right
let: Rx = 0.2 * s
let: Ry = 0
let: R = 0.4 * s
point: (Rx, Ry)
line-segment: (Rx, Ry), (Rx, Ry - 0.5), red, solid
vector: (Rx, Ry - 0.5), -R, 0, red
text: Rx - R, Ry - 0.5, "$\vec R_d$", center-left
:::
:::::

:::::::::::::


:::::::::::::{part} c
Bestem normalkraften som virker på klossen.


:::::{answer}
$$
N = 49 \en{N}
$$

::::{solution}
Summen av kreftene i $y$-retning er lik $0$. Fra Newtons 2.lov får vi da 

$$
\sum F_y = N - G = 0 \limplies N = G = mg
$$

Normalkraften er derfor gitt ved 

$$
N = mg = 5{,}0 \en{kg} \cdot 9{,}81 \en{m/s^2} = 49 \en{N}
$$
::::
:::::

:::::::::::::


:::::::::::::{part} d
Bestem det statiske friksjonstallet $\mu_s$ mellom klossen og bordet.


:::::{answer}
$$
\mu_s = 0{,}41
$$

::::{solution}
Det statiske friksjonstallet får vi vet å bruke maksimalverdien for den statiske friksjonskraften:

$$
R_\mathrm{maks} = \mu_s N \limplies \mu_s = \dfrac{R_\mathrm{maks}}{N}
$$

Siden klossen *akkurat* begynner å skli når kraftmåleren viser $20 \en{N}$, så er $R_\mathrm{maks} = 20 \en{N}$. Vi får da

$$
\mu_s = \dfrac{20 \en{N}}{49 \en{N}} = 0{,}41
$$
::::
:::::

:::::::::::::


:::::::::::::{part} e
Bruk Newtons 2.lov til å finne det dynamiske friksjonstallet $\mu_d$ mellom klossen og bordet.


:::::{answer}
$$
\mu_d = 0{,}24
$$

::::{solution}
Siden klossen sklir med konstant fart, så betyr det at den dynamiske friksjonskraften og trekkraften er like store. Fra Newtons 2.lov har vi derfor:

$$
\sum F_x = T - R_d = 0 \limplies T = R_d
$$

Den dynamiske friksjonskraften er

$$
R_d = \mu_d N = \mu_d mg
$$

Dermed får vi

$$
T = \mu_d mg \limplies \mu_d = \dfrac{T}{mg}
$$

$$
\mu_d = \dfrac{12 \en{N}}{5{,}0 \en{kg} \cdot 9{,}81 \en{m/s^2}} = 0{,}24
$$
::::
:::::

:::::::::::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 3
En kloss med masse $m = 10{,}0 \en{kg}$ sklir bortover et vannrett gulv med en startfart på $5{,}0 \en{m/s}$. Mellom klossen og underlaget virker det en friksjonskraft som har et dynamisk friksjonstall $\mu_d = 0{,}20$.

Et tau er festet til klossen og en person trekker i tauet for å *stoppe* klossen. Personen trekker med en kraft på $T = 20 \en{N}$ mot venstre.



:::::::::::::{part} a
Tegn et fritt-legemediagram som viser alle kreftene som virker på klossen.


:::::{answer}
:::{plot}
width: 60%
axis: equal
axis: off
let: s = 8
let: Ax = 0
let: Ay = 0
let: Bx = s
let: By = 0
let: Cx = s
let: Cy = s
let: Dx = 0
let: Dy = s
polygon: (Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy), blue, 0.1
let: Gx = s/2
let: Gy = s/2
let: G = 0.8 * s
point: (Gx, Gy)
vector: (Gx, Gy), 0, -G, red
text: Gx, Gy - G, "$\vec G$", bottom-center
let: N = G
let: Nx = 0.75 * s
let: Ny = 0
point: (Nx, Ny)
vector: (Nx, Ny), 0, N, blue
text: Nx, Ny + N, "$\vec N$", top-center
let: x0 = -0.5 * s
let: y0 = s
let: dx = 0.2 * s
let: dy = 0.2 * s
vector: (x0, y0), dx, 0, black
vector: (x0, y0), 0, dy, black
text: x0 + dx, y0, "$x$", center-right
text: x0, y0 + dy, "$y$", top-center
let: Tx = 0
let: Ty = 0.5 * s
let: T = 0.3 * s
point: (Tx, Ty)
vector: (Tx, Ty), -T, 0, blue
text: Tx - T, Ty, "$\vec T$", center-left
let: Rx = 0.2 * s
let: Ry = 0
let: R = 0.4 * s
point: (Rx, Ry)
line-segment: (Rx, Ry), (Rx, Ry - 0.5), red, solid
vector: (Rx, Ry - 0.5), -R, 0, red
text: Rx - R, Ry - 0.5, "$\vec R$", center-left
vector: (0.5 * s, 1.2 * s), 0.3 * s, 0, teal
text: 0.5 * (0.5 * s + 0.5 * s + s * 0.3), 1.2 * s, "$\vec v$", top-center
:::
:::::

:::::::::::::


:::::::::::::{part} b
Bruk Newtons 2.lov til å finne et uttrykk for akselerasjonen som virker på klossen.


:::::{answer}
$$
a = -4{,}0 \en{m/s^2}
$$

::::{solution}
Først bruker vi Newtons 2.lov for $y$-retning for å bestemme normalkraften:

$$
\sum F_y = N - G = 0 \limplies N = G = mg
$$

Fra Newtons 2.lov i $x$-retning får vi at 

$$
\sum F_x = -T - R = ma \limplies a = -\dfrac{T + R}{m}
$$

Friksjonskraften er gitt ved 

$$
R = \mu_d N = \mu_d mg
$$

Dermed får vi at akselerasjonen er 

$$
a = -\dfrac{T + \mu_d mg}{m} = -\dfrac{20 \en{N} + 0{,}20 \cdot 10{,}0 \en{kg} \cdot 9{,}81 \en{m/s^2}}{10{,}0 \en{kg}} = -4{,}0 \en{m/s^2}
$$
::::
:::::

:::::::::::::



:::::::::::::{part} c
Bestem hvor langt klossen sklir før den stopper.


:::::{answer}
$$
s = 3{,}1 \en{m}
$$

::::{solution}
:::{sidebar}
$$
\begin{align*}
a &= -4{,}0 \en{m/s^2} \\
v_0 &= 5{,}0 \en{m/s} \\
v &= 0 \\
s &= ?
\end{align*}
$$
:::

Vi systematiserer opplysningene som vist til høyre. Da passer det å bruke bevegelseslikningen

$$
2as = \underbrace{v^2}_{=0} - v_0^2 = -v_0^2
$$

$$
s = -\frac{v_0^2}{2a} = -\frac{(5{,}0 \en{m/s})^2}{2 \cdot (-4{,}0 \en{m/s^2})} = 3{,}1 \en{m}
$$
::::
:::::


:::::::::::::



:::::::::::::::


---




:::::::::::::::{exercise} Oppgave 4
En boks har massen $m = 6{,}0 \en{kg}$ og ligger på et vannrett gulv. Mellom klossen og gulvet virker det friksjon. Da gjelder følgende friksjonstall:
* Det *statiske* friksjonstallet er $\mu_s = 0{,}50$
* Det *dynamiske* friksjonstallet er $\mu_d = 0{,}30$

:::::::::::::{part} a
Bestem den største mulige statiske friksjonskraften $R_\mathrm{maks}$ som kan virke på boksen før den begynner å skli.


:::::{answer}
$$
R_\mathrm{maks} = 30 \en{N}
$$
:::::

:::::::::::::


En maskin virker med en dyttekraft $D = 20 \en{N}$ på boksen *mot* høyre.


:::::::::::::{part} b
Tegn et fritt-legemediagram som viser alle kreftene som virker på boksen.



:::::{answer}
:::{plot}
width: 60%
axis: equal
axis: off
let: s = 8
let: Ax = 0
let: Ay = 0
let: Bx = s
let: By = 0
let: Cx = s
let: Cy = s
let: Dx = 0
let: Dy = s
polygon: (Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy), blue, 0.1
let: Gx = s/2
let: Gy = s/2
let: G = 0.8 * s
point: (Gx, Gy)
vector: (Gx, Gy), 0, -G, red
text: Gx, Gy - G, "$\vec G$", bottom-center
let: N = G
let: Nx = 0.75 * s
let: Ny = 0
point: (Nx, Ny)
vector: (Nx, Ny), 0, N, blue
text: Nx, Ny + N, "$\vec N$", top-center
let: x0 = -0.5 * s
let: y0 = s
let: dx = 0.2 * s
let: dy = 0.2 * s
vector: (x0, y0), dx, 0, black
vector: (x0, y0), 0, dy, black
text: x0 + dx, y0, "$x$", center-right
text: x0, y0 + dy, "$y$", top-center
let: Tx = 0
let: Ty = 0.8 * s
let: T = 0.4 * s
point: (Tx, Ty)
vector: (Tx, Ty), T, 0, blue
text: Tx + T, Ty, "$\vec D$", center-right
let: Rx = 0.2 * s
let: Ry = 0
let: R = 0.4 * s
point: (Rx, Ry)
line-segment: (Rx, Ry), (Rx, Ry - 0.5), red, solid
vector: (Rx, Ry - 0.5), -R, 0, red
text: Rx - R, Ry - 0.5, "$\vec R$", center-left
:::
:::::

:::::::::::::



:::::::::::::{part} c
Avgjør om boksen begynner å skli fra dyttekraften eller ikke.


:::::{answer}
Siden dyttekraften $D \leq R_\mathrm{maks}$, så vil ikke boksen begynne å skli.


:::::


:::::::::::::


Maskinen øker dyttekraften til $D = 35 \en{N}$ virker på boksen *mot* høyre.


:::::::::::::{part} d
Bruk Newtons 2.lov til å finne akselerasjonen til boksen når den begynner å skli.


:::::{answer}
$$
a = 2{,}9 \en{m/s^2}
$$


::::{solution}
:::{plot}
width: 100%
align: right
axis: equal
axis: off
let: s = 8
let: Ax = 0
let: Ay = 0
let: Bx = s
let: By = 0
let: Cx = s
let: Cy = s
let: Dx = 0
let: Dy = s
polygon: (Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy), blue, 0.1
let: Gx = s/2
let: Gy = s/2
let: G = 0.8 * s
point: (Gx, Gy)
vector: (Gx, Gy), 0, -G, red
text: Gx, Gy - G, "$\vec G$", bottom-center
let: N = G
let: Nx = 0.8 * s
let: Ny = 0
point: (Nx, Ny)
vector: (Nx, Ny), 0, N, blue
text: Nx, Ny + N, "$\vec N$", top-center
let: x0 = -0.5 * s
let: y0 = s
let: dx = 0.2 * s
let: dy = 0.2 * s
vector: (x0, y0), dx, 0, black
vector: (x0, y0), 0, dy, black
text: x0 + dx, y0, "$x$", center-right
text: x0, y0 + dy, "$y$", top-center
let: Tx = 0
let: Ty = 0.8 * s
let: T = 0.6 * s
point: (Tx, Ty)
vector: (Tx, Ty), T, 0, blue
text: Tx + T, Ty, "$\vec D$", center-right
let: Rx = 0.2 * s
let: Ry = 0
let: R = 0.4 * s
point: (Rx, Ry)
line-segment: (Rx, Ry), (Rx, Ry - 0.5), red, solid
vector: (Rx, Ry - 0.5), -R, 0, red
text: Rx - R, Ry - 0.5, "$\vec R$", center-left
fontsize: 24
:::


Fra fritt-legemediagrammet til høyre kan vi sette opp Newtons 2.lov for $y$-retning først:

$$
\sum F_y = N - G = 0 \limplies N = G = mg
$$

Det betyr at friksjonskraften nå er 

$$
R = \mu_d N = \mu_d mg
$$

Så bruker vi Newtons 2.lov for $x$-retning:

$$
\sum F_x = D - R = ma 
$$

som gir 

$$
\begin{align*}
a &= \dfrac{D - R}{m} \\
\\
&= \frac{D - \mu_d mg}{m} \\
\\
&= \frac{35 \en{N} - 0{,}30 \cdot 6{,}0 \en{kg} \cdot 9{,}81 \en{m/s^2}}{6{,}0 \en{kg}} = 2{,}9 \en{m/s^2}
\end{align*}
$$


::::


:::::


:::::::::::::



Dyttekraften virker på boksen i $2{,}0 \en{s}$ før maskinen bråstopper og lar boksen skli bortover gulvet.

:::::::::::::{part} e
Bestem farten til boksen idet maskinen slutter å dytte.



:::::{answer}
$$
v = 5{,}8 \en{m/s}
$$


::::{solution}
Startfarten $v_0 = 0$, som betyr at vi kan finne farten med 

$$
v = \cancelto{0}{v_0} + at = at = 2{,}9 \en{m/s^2} \cdot 2{,}0 \en{s} = 5{,}8 \en{m/s}
$$
::::


:::::

:::::::::::::


:::::::::::::{part} f
Bestem hvor langt boksen sklir sammenlagt fra maskinen begynner å dytte, til boksen stopper helt opp.


:::{hint} Hint
Del opp bevegelsen i to faser:
* Fase 1: Boksen blir akselerert av maskinen med $a = 2{,}9 \en{m/s^2}$ i $2{,}0 \en{s}$.
* Fase 2: Boksen sklir bortover gulvet der det bare er friksjon som virker på boksen i $x$-retning. Du kan finne en ny akselerasjon med Newtons 2.lov.

Regn ut hvor langt boksen forflytter seg i hver fase.
:::

:::::{answer}
$$
s_\mathrm{total} = 11{,}5 \en{m}
$$

::::{solution}
Vi deler opp boksens bevegelses i to faser:
* Fase 1: Boksen blir akselerert av maskinen med $a = 2{,}9 \en{m/s^2}$. 
* Fase 2: Det er bare den dynamiske friksjonskraften som påvirker akselerasjonen til boksen i $x$-retning siden dyttekraften ikke lenger virker.


**Fase 1**:

Vi vet at farten til boksen ble $v = 5{,}8 \en{m/s}$ etter $t = 2{,}0 \en{s}$ med en akselerasjon på $a = 2{,}9 \en{m/s^2}$. Startfarten $v_0 = 0$ som betyr at vi kan bruke bevegelseslikningen

$$
2as = v^2 - \underbrace{v_0^2}_{= 0} \limplies s = \frac{v^2}{2a} = \frac{(5{,}8 \en{m/s})^2}{2 \cdot 2{,}9 \en{m/s^2}} = 5{,}8 \en{m}
$$

**Fase 2**:

Siden dyttekraften ikke virker lenger, vil summen av kreftene i $x$-retning gi at

$$
\sum F_x = -R = ma \limplies a = -\frac{R}{m} = -\frac{\mu_d mg}{m} = -\mu_d g
$$

Altså er akselerasjonen nå:

$$
a = -\mu_d g = -0{,}30 \cdot 9{,}81 \en{m/s^2} = -2{,}94 \en{m/s^2}
$$

Startfarten er nå sluttfarten fra fase 1, altså $v_0 = 5{,}8 \en{m/s}$. Sluttfarten $v = 0$ siden boksen stopper opp helt når bevegelsen er ferdig. Vi kan da bruke bevegelseslikningen

$$
2as = \underbrace{v^2}_{= 0} - v_0^2 \limplies s = -\frac{v_0^2}{2a} = -\frac{(5{,}8 \en{m/s})^2}{2 \cdot -2{,}94 \en{m/s^2}} = 5{,}7 \en{m}
$$

**Samlet avstand:**

Den samlede avstanden blir summen av de to avstandene fra hver fase:

$$
s_\mathrm{total} = s_\mathrm{fase 1} + s_\mathrm{fase 2} = 5{,}8 \en{m} + 5{,}7 \en{m} = 11{,}5 \en{m}
$$

::::
:::::

:::::::::::::

:::::::::::::::




---




:::::::::::::::{exercise} Oppgave 5

En kloss med masse $m = 4{,}0 \en{kg}$ sklir mot høyre på et vannrett gulv med en startfart på $8{,}0 \en{m/s}$.

En drone flyr rett over klossen og begynner å presse den loddrett nedover med en konstant kraft $P = 20 \en{N}$ for å bremse klossen.

Dronen følger klossen slik at den hele tiden har samme fart som klossen. Vi antar at dronen bare virker på klossen med en loddrett kraft og at det ikke virker noen statisk friksjonskraft mellom de to.

Det dynamiske friksjonstallet mellom klossen og gulvet er $\mu_d = 0{,}25$.

:::::::::::::{part} a

Tegn et fritt-legemediagram som viser alle kreftene som virker på klossen mens dronen presser den nedover.

:::::{answer}

La $\vec P$ være kraften fra dronen på klossen. Kreftene som virker på klossen er:

- Tyngdekraften $\vec G$ nedover.
- Kraften $\vec P$ fra dronen nedover.
- Normalkraften $\vec N$ fra gulvet oppover.
- Den dynamiske friksjonskraften $\vec R$ mot venstre.

Siden klossen ikke akselererer i $y$-retning, må normalkraften være like stor som summen av tyngdekraften og kraften fra dronen.

Friksjonskraften peker mot venstre siden klossen sklir mot høyre.



:::{plot}
width: 60%
axis: equal
axis: off
let: s = 8
let: Ax = 0
let: Ay = 0
let: Bx = s
let: By = 0
let: Cx = s
let: Cy = s
let: Dx = 0
let: Dy = s
polygon: (Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy), blue, 0.1
let: Gx = s/2
let: Gy = s/2
let: G = 0.8 * s
point: (Gx, Gy)
vector: (Gx, Gy), 0, -G, red
text: Gx, Gy - G, "$\vec G$", bottom-center
let: x0 = -0.5 * s
let: y0 = s
let: dx = 0.2 * s
let: dy = 0.2 * s
vector: (x0, y0), dx, 0, black
vector: (x0, y0), 0, dy, black
text: x0 + dx, y0, "$x$", center-right
text: x0, y0 + dy, "$y$", top-center
let: Px = 0.2 * s
let: Py = s
let: P = 0.4 * s
point: (Px, Py)
vector: (Px, Py), 0, -P, blue
text: Px, Py - P, "$\vec P$", center-right
let: Rx = 0.2 * s
let: Ry = 0
let: R = 0.6 * s
point: (Rx, Ry)
line-segment: (Rx, Ry), (Rx, Ry - 0.5), red, solid
vector: (Rx, Ry - 0.5), -R, 0, red
text: Rx - R, Ry - 0.5, "$\vec R$", center-left
let: N = G + P
let: Nx = 0.8 * s
let: Ny = 0
point: (Nx, Ny)
vector: (Nx, Ny), 0, N, blue
text: Nx, Ny + N, "$\vec N$", top-center
:::




:::::

:::::::::::::

:::::::::::::{part} b

Bruk Newtons 2.lov til å bestemme normalkraften $N$ som virker på klossen.

:::::{answer}

$$
N = 59 \en{N}
$$

:::::{solution}

Vi bruker Newtons 2.lov i $y$-retning. Siden klossen ikke akselererer i denne retningen, får vi

$$
\sum F_y = N - G - P = 0
$$

Dermed er normalkraften gitt ved

$$
N = G + P = mg + P
$$

Vi setter inn verdiene og får

$$
N = 4{,}0 \en{kg} \cdot 9{,}81 \en{m/s^2} + 20 \en{N}
= 59 \en{N}
$$

:::::

:::::

:::::::::::::

:::::::::::::{part} c

Bruk Newtons 2.lov til å bestemme akselerasjonen til klossen mens dronen presser den nedover.

:::::{answer}

$$
a = -3{,}7 \en{m/s^2}
$$

:::::{solution}

Friksjonskraften er gitt ved

$$
R = \mu_d N = \mu_d (mg + P)
$$

Fra Newtons 2.lov i $x$-retning får vi

$$
\sum F_x = -R = ma
$$

som gir

$$
a = -\frac{R}{m} = -\frac{\mu_d (mg + P)}{m}
$$

Vi setter inn verdiene:

$$
a = -\frac{0{,}25 \cdot (4{,}0 \en{kg} \cdot 9{,}81 \en{m/s^2} + 20 \en{N})}{4{,}0 \en{kg}}
= -3{,}7 \en{m/s^2}
$$

:::::

:::::

:::::::::::::

:::::::::::::{part} d

Bestem hvor lang tid det tar fra dronen begynner å presse klossen nedover til klossen stopper.

:::::{answer}

$$
t = 2{,}2 \en{s}
$$

:::::{solution}

Vi vet at startfarten er $v_0 = 8{,}0 \en{m/s}$ og at sluttfarten er $v = 0$ når klossen stopper.

Fra oppgave c fant vi akselerasjonen $a = -3{,}7 \en{m/s^2}$.

Vi bruker bevegelseslikningen

$$
v = v_0 + at
$$

og løser med hensyn på $t$:

$$
t = \frac{v - v_0}{a}
$$

Vi setter inn verdiene og får

$$
t = \frac{0 - 8{,}0 \en{m/s}}{-3{,}7 \en{m/s^2}}
= 2{,}2 \en{s}
$$

:::::

:::::

:::::::::::::

:::::::::::::{part} e

Bestem hvor langt klossen sklir fra dronen begynner å presse den nedover til den stopper.

:::::{answer}

$$
s = 8{,}6 \en{m}
$$

:::::{solution}

Vi vet at

$$
v_0 = 8{,}0 \en{m/s}, \qquad
v = 0, \qquad
a = -3{,}7 \en{m/s^2}
$$

Vi bruker bevegelseslikningen

$$
2as = v^2 - v_0^2
$$

Siden sluttfarten er $v = 0$, får vi

$$
2as = \underbrace{v^2}_{=0} - v_0^2 = -v_0^2
$$

Dermed blir strekningen

$$
s = -\frac{v_0^2}{2a}
$$

Vi setter inn verdiene og får

$$
s = -\frac{(8{,}0 \en{m/s})^2}{2 \cdot (-3{,}7 \en{m/s^2})}
= 8{,}6 \en{m}
$$

:::::

:::::

:::::::::::::

:::::::::::::::




---



:::::::::::::::{exercise} Oppgave 6

To kasser $A$ og $B$ sklir mot høyre på et vannrett gulv. Kassene har massene

* Kasse $A$: $m_A = 4{,}0 \en{kg}$
* Kasse $B$: $m_B = 8{,}0 \en{kg}$

Begge kassene har samme startfart $v_0 = 8{,}0 \en{m/s}$.

Det dynamiske friksjonstallet mellom kassene og gulvet er $\mu_d = 0{,}25$.

Vi ser bort fra luftmotstand, og det virker ingen andre horisontale krefter på kassene enn friksjon.

:::::::::::::{part} a

Tegn et fritt-legemediagram for hver av kassene mens de sklir mot høyre.

Pass på at vektorpilene har riktige lengder relativt til hverandre i de to diagrammene.

:::::{answer}

Begge kassene påvirkes av tre krefter:

* Tyngdekraften $\vec G$ nedover.
* Normalkraften $\vec N$ oppover.
* Den dynamiske friksjonskraften $\vec R$ mot venstre.

Siden kasse $B$ har dobbelt så stor masse som kasse $A$, vil både tyngdekraften, normalkraften og friksjonskraften være dobbelt så store for kasse $B$. Men fritt-legemediagrammene vil ellers se like ut slik at den relative lengden mellom kreftene er like slik som vist i figuren nedenfor:



:::{plot}
width: 60%
axis: equal
axis: off
let: s = 8
let: Ax = 0
let: Ay = 0
let: Bx = s
let: By = 0
let: Cx = s
let: Cy = s
let: Dx = 0
let: Dy = s
polygon: (Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy), blue, 0.1
let: Gx = s/2
let: Gy = s/2
let: G = 0.8 * s
point: (Gx, Gy)
vector: (Gx, Gy), 0, -G, red
text: Gx, Gy - G, "$\vec G$", bottom-center
let: N = G
let: Nx = 0.8 * s
let: Ny = 0
point: (Nx, Ny)
vector: (Nx, Ny), 0, N, blue
text: Nx, Ny + N, "$\vec N$", top-center
let: x0 = -0.5 * s
let: y0 = s
let: dx = 0.2 * s
let: dy = 0.2 * s
vector: (x0, y0), dx, 0, black
vector: (x0, y0), 0, dy, black
text: x0 + dx, y0, "$x$", center-right
text: x0, y0 + dy, "$y$", top-center
let: Tx = 0
let: Ty = 0.8 * s
let: T = 0.6 * s
let: Rx = 0.2 * s
let: Ry = 0
let: R = 0.4 * s
point: (Rx, Ry)
line-segment: (Rx, Ry), (Rx, Ry - 0.5), red, solid
vector: (Rx, Ry - 0.5), -R, 0, red
text: Rx - R, Ry - 0.5, "$\vec R$", center-left
:::


:::::

:::::::::::::

:::::::::::::{part} b

Bestem normalkraften og friksjonskraften som virker på hver av kassene.

:::::{answer}

**Kasse A:**

$$
N_A = 39 \en{N}
\qog
R_A = 9{,}8 \en{N}
$$

**Kasse B:**

$$
N_B = 78 \en{N}
\qog
R_B = 20 \en{N}
$$

:::::{solution}

Vi bruker Newtons 2.lov i $y$-retning. Siden kassene ikke akselererer i denne retningen, får vi

$$
\sum F_y = N - G = 0
\limplies N = G = mg
$$

**Kasse A:**

Normalkraften er

$$
N_A = m_A g = 4{,}0 \en{kg} \cdot 9{,}81 \en{m/s^2}
= 39 \en{N}
$$

Friksjonskraften blir

$$
R_A = \mu_d N_A = 0{,}25 \cdot 39 \en{N}
= 9{,}8 \en{N}
$$

**Kasse B:**

Normalkraften er

$$
N_B = m_B g = 8{,}0 \en{kg} \cdot 9{,}81 \en{m/s^2}
= 78 \en{N}
$$

Friksjonskraften blir

$$
R_B = \mu_d N_B = 0{,}25 \cdot 78 \en{N}
= 20 \en{N}
$$

Vi ser at både normalkraften og friksjonskraften dobles når massen dobles.

:::::
:::::

:::::::::::::

:::::::::::::{part} c

Bruk Newtons 2.lov til å bestemme akselerasjonen til hver av kassene.

Sammenlign akselerasjonene og forklar hvorfor de blir like eller forskjellige.

:::::{answer}

$$
a_A = a_B = -2{,}5 \en{m/s^2}
$$

Akselerasjonene blir like fordi både friksjonskraften og massen dobles for kasse $B$.

:::::{solution}

Vi bruker Newtons 2.lov i $x$-retning.

Friksjonskraften virker mot venstre, så vi får

$$
\sum F_x = -R = ma
$$

Dermed er akselerasjonen gitt ved

$$
a = -\frac{R}{m}
$$

**Kasse A:**

$$
a_A = -\frac{R_A}{m_A}
= -\frac{9{,}8 \en{N}}{4{,}0 \en{kg}}
= -2{,}5 \en{m/s^2}
$$

**Kasse B:**

$$
a_B = -\frac{R_B}{m_B}
= -\frac{20 \en{N}}{8{,}0 \en{kg}}
= -2{,}5 \en{m/s^2}
$$

Vi ser at kassene får **samme akselerasjon**, selv om kasse $B$ har dobbelt så stor masse.

Dette kan vi forklare ved å sette inn uttrykket for friksjonskraften i Newtons 2.lov:

$$
\begin{align*}
-R &= ma \\[8pt]
-\mu_d N &= ma \\[8pt]
-\mu_d mg &= ma
\end{align*}
$$

Vi deler på $m$ og får

$$
\boxed{a = -\mu_d g}
$$

Vi ser at massen $m$ forsvinner fra uttrykket for akselerasjonen.

Det betyr at akselerasjonen **ikke er avhengig av massen** så lenge friksjonstallet er det samme og normalkraften er lik tyngdekraften.

:::::
:::::

:::::::::::::

:::::::::::::{part} d

Bestem farten og strekningen hver av kassene har tilbakelagt etter $2{,}0 \en{s}$.

:::::{answer}

Begge kassene har farten

$$
v = 3{,}0 \en{m/s}
$$

og har tilbakelagt strekningen

$$
s = 11 \en{m}
$$

:::::{solution}

Siden begge kassene har samme startfart og akselerasjon, vil de også ha samme fart og ha tilbakelagt samme strekning etter $2{,}0 \en{s}$.

Vi bruker bevegelseslikningen

$$
v = v_0 + at
$$

og setter inn verdiene:

$$
v = 8{,}0 \en{m/s} + (-2{,}5 \en{m/s^2}) \cdot 2{,}0 \en{s}
= 3{,}0 \en{m/s}
$$

For å bestemme strekningen bruker vi bevegelseslikningen

$$
s = v_0 t + \frac{1}{2}at^2
$$

som gir

$$
\begin{align*}
s &= 8{,}0 \en{m/s} \cdot 2{,}0 \en{s} + \frac{1}{2} \cdot (-2{,}5 \en{m/s^2}) \cdot (2{,}0 \en{s})^2 = 11 \en{m}
\end{align*}
$$

:::::
:::::

:::::::::::::

:::::::::::::{part} e

Bestem hvor lang tid det tar før kassene stopper helt opp.

:::::{answer}

$$
t = 3{,}2 \en{s}
$$

Begge kassene stopper samtidig.

:::::{solution}

Vi vet at sluttfarten er $v = 0$ når kassene stopper.

Vi bruker bevegelseslikningen

$$
v = v_0 + at
$$

og løser med hensyn på $t$:

$$
t = \frac{v-v_0}{a}
$$

Dermed får vi

$$
t = \frac{0 - 8{,}0 \en{m/s}}{-2{,}5 \en{m/s^2}}
= 3{,}2 \en{s}
$$

Siden kassene har samme startfart og akselerasjon, stopper de samtidig.

:::::
:::::

:::::::::::::

:::::::::::::{part} f

Bestem hvor langt hver av kassene sklir fra start til de stopper helt opp.

Forklar hvorfor bremselengden blir lik eller forskjellig for kassene.

:::::{answer}

$$
s = 13 \en{m}
$$

Begge kassene har samme bremselengde fordi de har samme startfart og akselerasjon.

:::::{solution}

Vi bruker bevegelseslikningen

$$
2as = v^2 - v_0^2
$$

Siden sluttfarten er $v = 0$, får vi

$$
2as = \underbrace{v^2}_{=0} - v_0^2
= -v_0^2
$$

Dermed er bremselengden gitt ved

$$
s = -\frac{v_0^2}{2a}
$$

Vi setter inn verdiene:

$$
s = -\frac{(8{,}0 \en{m/s})^2}{2 \cdot (-2{,}5 \en{m/s^2})}
= 13 \en{m}
$$

Begge kassene har samme bremselengde.

Selv om kasse $B$ har dobbelt så stor friksjonskraft som kasse $A$, har den også dobbelt så stor masse.

Dermed får kassene samme akselerasjon. Siden startfarten også er den samme, vil bremselengden bli lik.

:::::
:::::

:::::::::::::

:::::::::::::::



---




:::::::::::::::{exercise} Oppgave 7

En kloss med masse $m = 5{,}0 \en{kg}$ sklir mot høyre gjennom en trang passasje mellom et vannrett gulv og et fjærbelastet tak.

Taket presser ned på klossen med en konstant normalkraft $N_t = 25 \en{N}$. Klossen er i kontakt med både gulvet og taket mens den sklir.

Det dynamiske friksjonstallet $\mu_d = 0{,}20$ gjelder både mellom klossen og gulvet, og mellom klossen og taket.

Klossen har en startfart på $v_0 = 12 \en{m/s}$ mot høyre.

:::::::::::::{part} a

Tegn et fritt-legemediagram som viser alle kreftene som virker på klossen mens den sklir mot høyre.

:::::{answer}

Det virker fem krefter på klossen:

* Tyngdekraften $\vec G$ nedover.
* Normalkraften $\vec N_g$ fra gulvet oppover.
* Normalkraften $\vec N_t$ fra taket nedover.
* Friksjonskraften $\vec R_g$ fra gulvet mot venstre.
* Friksjonskraften $\vec R_t$ fra taket mot venstre.

Siden klossen ikke akselererer i $y$-retning, må normalkraften fra gulvet være like stor som summen av tyngdekraften og normalkraften fra taket.

Begge friksjonskreftene peker mot venstre fordi klossen sklir mot høyre i forhold til både gulvet og taket.

Lengden til friksjonskreftene er overdrevet for å få vise dem tydelig i fritt-legemediagrammet.


:::{plot}
width: 60%
axis: equal
axis: off
let: s = 8
let: Ax = 0
let: Ay = 0
let: Bx = s
let: By = 0
let: Cx = s
let: Cy = s
let: Dx = 0
let: Dy = s
polygon: (Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy), blue, 0.1
let: Gx = s/2
let: Gy = s/2
let: G = 0.8 * s
point: (Gx, Gy)
vector: (Gx, Gy), 0, -G, red
text: Gx, Gy - G, "$\vec G$", bottom-center
let: x0 = -s
let: y0 = s
let: dx = 0.2 * s
let: dy = 0.2 * s
vector: (x0, y0), dx, 0, black
vector: (x0, y0), 0, dy, black
text: x0 + dx, y0, "$x$", center-right
text: x0, y0 + dy, "$y$", top-center
let: Ntx = 0.35 * s
let: Nty = s
let: Nt = 0.5 * G
point: (Ntx, Nty)
vector: (Ntx, Nty), 0, -Nt, blue
text: Ntx, Nty - Nt, "$\vec N_t$", bottom-center
let: N = G + Nt
let: Nx = 0.8 * s
let: Ny = 0
point: (Nx, Ny)
vector: (Nx, Ny), 0, N, blue
text: Nx, Ny + N, "$\vec N_g$", top-center
let: mu = 0.45
let: Rtx = 0.2 * s
let: Rty = s
let: Rt = mu * Nt
point: (Rtx, Rty)
line-segment: (Rtx, Rty), (Rtx, Rty + 0.5), red, solid
vector: (Rtx, Rty + 0.5), -Rt, 0, red
text: Rtx - Rt, Rty + 0.5, "$\vec R_t$", center-left
let: Rx = 0.2 * s
let: Ry = 0
let: R = mu * N
point: (Rx, Ry)
line-segment: (Rx, Ry), (Rx, Ry - 0.5), red, solid
vector: (Rx, Ry - 0.5), -R, 0, red
text: Rx - R, Ry - 0.5, "$\vec R_g$", center-left
:::



:::::

:::::::::::::

:::::::::::::{part} b

Bruk Newtons 2.lov til å bestemme normalkraften $N_g$ fra gulvet på klossen.

:::::{answer}

$$
N_g = 74 \en{N}
$$

:::::{solution}

Vi bruker Newtons 2.lov i $y$-retning.

Siden klossen ikke akselererer i denne retningen, får vi

$$
\sum F_y = N_g - N_t - G = 0
$$

Dermed er normalkraften fra gulvet gitt ved

$$
N_g = N_t + G = N_t + mg
$$

Vi setter inn verdiene:

$$
\begin{align*}
N_g &= 25 \en{N} + 5{,}0 \en{kg} \cdot 9{,}81 \en{m/s^2} \\[8pt]
&= 74 \en{N}
\end{align*}
$$

:::::
:::::

:::::::::::::

:::::::::::::{part} c

Bruk Newtons 2.lov til å bestemme akselerasjonen til klossen.

:::::{answer}

$$
a = -4{,}0 \en{m/s^2}
$$

:::::{solution}

Det virker to friksjonskrefter på klossen. Friksjonskraften fra gulvet er

$$
R_g = \mu_d N_g
$$

og friksjonskraften fra taket er

$$
R_t = \mu_d N_t
$$

Begge friksjonskreftene virker mot venstre. Fra Newtons 2.lov i $x$-retning får vi derfor

$$
\sum F_x = -R_g - R_t = ma
$$

Dermed er akselerasjonen gitt ved

$$
a = -\frac{R_g + R_t}{m}
$$

Vi setter inn uttrykkene for friksjonskreftene:

$$
a = -\frac{\mu_d N_g + \mu_d N_t}{m}
$$

som gir

$$
\begin{align*}
a &= -\frac{0{,}20 \cdot 74 \en{N} + 0{,}20 \cdot 25 \en{N}}{5{,}0 \en{kg}} \\[8pt]
&= -4{,}0 \en{m/s^2}
\end{align*}
$$

:::::
:::::

:::::::::::::


:::::::::::::{part} d

Bestem hvor lang tid det tar før klossen stopper helt opp, og hvor langt den har sklidd sammenlagt når den stopper.

:::::{answer}

Tiden det tar før klossen stopper er

$$
t = 3{,}0 \en{s}
$$

Den samlede strekningen er

$$
s = 18 \en{m}
$$

:::::{solution}

**Stopptid:**

Vi bruker bevegelseslikningen

$$
v = v_0 + at
$$

Når klossen stopper, er sluttfarten $v = 0$. Dermed får vi

$$
t = \frac{v-v_0}{a}
$$

Vi setter inn verdiene:

$$
t = \frac{0 - 12 \en{m/s}}{-4{,}0 \en{m/s^2}}
= 3{,}0 \en{s}
$$

**Samlet strekning:**

Vi bruker bevegelseslikningen

$$
2as = v^2 - v_0^2
$$

Siden sluttfarten er $v = 0$, får vi

$$
2as = \underbrace{v^2}_{=0} - v_0^2
= -v_0^2
$$

Dermed er strekningen gitt ved

$$
s = -\frac{v_0^2}{2a}
$$

Vi setter inn verdiene:

$$
s = -\frac{(12 \en{m/s})^2}{2 \cdot (-4{,}0 \en{m/s^2})}
= 18 \en{m}
$$

:::::
:::::

:::::::::::::

:::::::::::::::




---



:::::::::::::::{exercise} Oppgave 8
En iskube med masse $25 \en{g}$ slippes fra ro ned på et transportbånd som beveger seg med en konstant fart mot høyre på $0{,}80 \en{m/s}$ i forhold til bakken. Mellom iskuben og transportbåndet virker det en dynamisk friksjonskraft med friksjonstallet $\mu_d = 0{,}020$.

Vi antar at når iskuben lander på transportbåndet, er startfarten $v_0 = 0$ i forhold til bakken, og iskuben spretter ikke opp igjen.



:::::::::::::{part} a
Tegn et fritt-legemediagram som viser alle kreftene som virker på iskuben rett etter den har landet på transportbåndet.



:::::{answer}
Transportbåndet beveger seg mot høyre i figuren nedenfor. Siden iskuben ligger i *ro* i utgangspunktet vil den akselerere mot høyre før den eventuelt oppnår samme fart som transportbåndet den sklir på. Derfor må friksjonskraften peke i samme retning som transportbåndet beveger seg. Normalkraften og gravitasjonskraften fungerer som vanlig.

:::{plot}
width: 60%
axis: equal
axis: off
let: s = 8
let: Ax = 0
let: Ay = 0
let: Bx = s
let: By = 0
let: Cx = s
let: Cy = s
let: Dx = 0
let: Dy = s
polygon: (Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy), blue, 0.1
let: Gx = s/2
let: Gy = s/2
let: G = 0.8 * s
point: (Gx, Gy)
vector: (Gx, Gy), 0, -G, red
text: Gx, Gy - G, "$\vec G$", bottom-center
let: N = G
let: Nx = 0.3 * s
let: Ny = 0
point: (Nx, Ny)
vector: (Nx, Ny), 0, N, blue
text: Nx, Ny + N, "$\vec N$", top-center
let: x0 = -0.5 * s
let: y0 = s
let: dx = 0.2 * s
let: dy = 0.2 * s
vector: (x0, y0), dx, 0, black
vector: (x0, y0), 0, dy, black
text: x0 + dx, y0, "$x$", center-right
text: x0, y0 + dy, "$y$", top-center
let: Tx = 0
let: Ty = 0.8 * s
let: T = 0.6 * s
let: Rx = 0.8 * s
let: Ry = 0
let: R = 0.4 * s
point: (Rx, Ry)
line-segment: (Rx, Ry), (Rx, Ry - 0.5), red, solid
vector: (Rx, Ry - 0.5), R, 0, red
text: Rx + R, Ry - 0.5, "$\vec R$", center-right
:::
:::::

:::::::::::::


:::::::::::::{part} b
Bruk Newtons 2.lov til å bestemme akselerasjonen iskuben opplever i forhold til bakken.



:::::{answer}
$$
a = 0{,}20 \en{m/s^2}
$$

::::{solution}
Iskuben akselererer ikke i $y$-retning som betyr at Newtons 2.lov i denne retningen gir

$$
\sum F_y = N - G = 0 \limplies N = G = mg
$$

Derfor blir friksjonskraften

$$
R = \mu_d N = \mu_d mg
$$

Newtons 2.lov i $x$-retning gir:

$$
\sum F_x = R = ma 
$$

$$
a = \frac{R}{m} = \frac{\mu_d mg}{m} = \mu_d g = 0{,}020 \cdot 9{,}81 \en{m/s^2} = 0{,}20 \en{m/s^2}
$$

::::
:::::

:::::::::::::


:::::::::::::{part} c
Bestem hvor langt iskuben beveger seg langs bakken før den beveger seg med samme fart som transportbåndet.


:::::{answer}
$$
s = 1{,}6 \en{m}
$$

::::{solution}
Fra oppgave **b)** har vi at $a = 0{,}20 \en{m/s^2}$. Startfarten til klossen er $v_0 = 0$ i forhold til bakken, og sluttfarten er $v = 0{,}80 \en{m/s}$ når iskuben har samme fart som transportbåndet. Da kan vi bruke bevegelseslikningen

$$
2as = v^2 - v_0^2
$$

$$
s = \frac{v^2 - v_0^2}{2a} = \frac{(0{,}80 \en{m/s})^2 - (0 \en{m/s})^2}{2 \cdot 0{,}20 \en{m/s^2}} = 1{,}6 \en{m}
$$
::::
:::::


:::::::::::::


:::::::::::::::