# Luftmotstand: Oppgaver


:::::::::::::::{exercise} Oppgave 1

:::{plot}
width: 350px
axis: off
axis: equal
align: right
let: s = 1
line-segment: (-s, 0), (s, 0), solid, blue
let: phi = pi/4
let: Px = s + s * cos(phi)
let: Py = s * sin(phi)
let: Qx = - s - s * cos(phi)
let: Qy = s * sin(phi)
line-segment: (s, 0), (Px, Py), solid, blue
line-segment: (-s, 0), (Qx, Qy), solid, blue
line-segment: (Qx, Qy), (Px, Py), solid, blue
point: (0, 0.5 * s * sin(phi))
vector: (0, 0.5 * s * sin(phi)), 0, -1, red
text: 0, 0.5 * s * sin(phi) - 1, "$\vec G$", bottom-center
point: (0.5 * s, 0)
vector: (0.5 * s, 0), 0, 0.5 * s, red
text: 0.5 * s, 0.5 * s, "$\vec L$", bottom-right
text: 0, s * sin(phi) + 0.1 * s, "Kaffefilter", top-center
fontsize: 24
:::



Et kaffefilter slippes fra ro fra en høyde $h$ over bakken.

Mens det faller virker gravitasjon $\vec G$ og luftmotstand $\vec L$ på kaffefilteret fram til det treffer bakken.

Se fritt-legemediagrammet til høyre.


Skriv ferdig programmet nedenfor ved å bruke Euler-Cromers metode til å simulere hvor lang tid det tar før det treffer bakken. 

Dere må bytte ut `????`{l=python} med riktig kode.



:::{clear}
:::

:::{interactive-code}
# Disse verdiene får du oppgitt av Rotem eller René
h = ????         # meter over bakken
m = ????         # Massen til kaffefilteret/kaffefilterene

# Startbetingelser
s = h
v = 0
t = 0

# Fysiske konstanter
g = 9.82 # tyngdeakselerasjon i Oslo i m/s^2
k = ???? # Luftmotstandskoeffisient hvis du valgte L = kv^2


dt = 1e-3 # steglengde

while ????:
    # 1. Regn ut summen av kreftene
    G = ????
    L = ????

    sum_F = ????


    # 2. Regn ut akselerasjonen
    a = ????

    
    # 3. Simulerer bevegelsen med Euler-Cromer
    v = ????
    s = ????
    t = ????


print(t)
:::

:::::::::::::::