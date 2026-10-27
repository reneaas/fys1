# Hydrostatisk trykk og oppdrift


Når et legeme senkes ned i vann, så vil det oppleve en oppdriftskraft. Dette er kraften som lar et stort cruiseskip flyte på vannet til tross for at skipet veier enormt mye. Her skal vi se på hvor denne kraften kommer fra. 


Vi trenger først å definere to nye fysiske størrelser: Trykk og massetetthet.

:::::::::::::::{summary} Definisjon: Trykk
Trykk $P$ som virker på en overflate med areal $A$ er definert som

$$
P = \dfrac{F}{A}
$$

der $F$ er den samlede kraften som virker normalt på overflaten. 

Trykk er målt i $\mathrm{Pa}$ (Pascal) der $\mathrm{Pa} = \mathrm{N/m^2}$ (kraft per areal).
:::::::::::::::



:::::::::::::::{summary} Definisjon: Massetetthet
Dersom et legeme har masse $m$ og volum $V$, så er massetettheten $\rho$ definert som

$$
\rho = \dfrac{m}{V}
$$

Massetetthet er målt i $\mathrm{kg/m^3}$ (masse per volum). Nedenfor vises noen kjente massetettheter som vi får bruk for i beregninger:


:::{table}
---
width: 50%
---
labels: Stoff, $\rho~[\mathrm{kg}/m^3]$
Vann, 1000
Luft, 1.225
:::



:::::::::::::::


---


Definisjonen av trykk lar oss finne et uttrykk for hvor mye trykk man opplever når man er nedsenket en viss dybde i vann. Når vannet er i ro, så kaller vi dette trykket for **hydrostatisk trykk**.
 

:::::::::::::::{summary} Hydrostatisk trykk

:::{plot}
nocache:
fontsize: 24
width: 350px
xmin: -1.2
xmax: 1.2
ymin: -0.5
ymax: 2.5
align: right
axis: off
let: h = 2
let: b = 1
let: dy = 0.2
line-segment: (0, 0), (0, h + dy), solid, black
line-segment: (0, 0), (b, 0), solid, black
line-segment: (b, 0), (b, h + dy), solid, black
let: d = h
let: A = 1/100 * d
let: k = 4
let: omega = 2 * pi * k
let: phi = 0
function: A * cos(omega * x - phi) + d, (0, b)
def: f(x) = A * cos(omega * x - phi) + d
fill-between: f(x), 0, (0, b), blue, 0.2, where=above
text: 0.5 * b, h + dy, "$P_0$", center-center
text: 0.5 * b, 0, "$P$", top-center
bar: (b + 0.1, 0), h, vertical
text: b + 0.1, h/2, "$h$", center-right
:::



Trykket $P$ på en dybde $h$ i vann er gitt ved

$$
P = P_0 + \rho g h
$$

der 

* $P_0 = 101~325 \en{Pa}$ er lufttrykket ved havnivå. Vi skriver dette ofte som $P_0 = 1 \en{atm}$ (én atmosfære).
* $\rho$ er massetettheten til vann
* $g$ er tyngdeakselerasjonen
* $h$ er dybden under vannoverflaten




:::::{proof} Vis forklaring
Vi tenker oss at bunnen av en beholder som er fylt med vann har arealet $A$. Vannstanden er en høyde $h$ over bunnen. Da vil bunnen oppleve en kraft $F$ som skyldes den samlede vekten til både luften i atmosfæren og vannet over bunnen. Da har vi at 

$$
F = F_\mathrm{luft} + F_\mathrm{vann}
$$

Denne vekten vil svare til tyngden til både luften i atmosfæren og vannet over bunnen. Vi kan skrive dette som

$$
F = G_\mathrm{luft} + G_\mathrm{vann}
$$

Trykket på bunnen av beholderen finner vi ved å dele med arealet til bunnen:

$$
P = \dfrac{F}{A} = \dfrac{G_\mathrm{luft} + G_\mathrm{vann}}{A} = \dfrac{G_\mathrm{luft}}{A} + \dfrac{G_\mathrm{vann}}{A}
$$

Vi definerer lufttrykket på vannoverflaten som

$$
P_0 = \dfrac{F_\mathrm{luft}}{A}
$$

slik at 

$$
P = P_0 + \dfrac{G_\mathrm{vann}}{A}
$$

Dersom vannet i beholderen har en masse $m$, så vil tyngden av vannet være

$$
G_\mathrm{vann} = mg
$$

Volumet av vannet vil være arealet til bunnen ganget med høyden til vannstanden:

$$
V = A\cdot h
$$

Fra definisjonen av massetetthet har vi da at 

$$
\rho = \dfrac{m}{V} \liff m = \rho V = \rho A h
$$

Dermed kan vi skrive tyngden av vannet som

$$
G_\mathrm{vann} = \rho A h g
$$

Vi setter inn i formelen for trykket:

$$
P = P_0 + \dfrac{G_\mathrm{vann}}{A} = P_0 + \dfrac{\rho A h g}{A} = P_0 + \rho g h
$$

Dermed er trykket på bunnen av beholderen gitt ved 

$$
P = P_0 + \rho g h
$$

:::::


:::::::::::::::



---


Vi bruker et begrep som omfavner både væsker og gasser, og dette begrepet er en **fluid**. Både luft og vann er eksempler på fluider.


:::::::::::::::{summary} Oppdrift
Når et legeme med volum $V$ er nedsenket i en fluid (væske eller gass) med massetetthet $\rho$, virker det en kraft $\vec B$ fra fluiden på legemet som kalles for **oppdrift**. 

Styrken på denne kraften er gitt ved

$$
B = \rho V g
$$

:::::::::::::::







