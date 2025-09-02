# Oppgaver: Programmering med posisjon, fart og akselerasjon



:::::::::::::::{exercise} Oppgave 1
Fartsfunksjonen (i m/s) til en gjenstand er gitt ved

$$
v(t) = 2t, \qder t \in [0, 5] \, \mathrm{s}.
$$

Her skal vi bygge opp et program og forstå hva hver kodelinje gjør underveis, mens vi stadig kommer nærmere et fullstendig program.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
I programmet nedenfor så ser du et program som definerer en variabel `t`{l=python} for tiden og en variabel `dt`{l=python} som skal brukes til å endre på tidsvariabelen underveis. 

Programmet skriver ut verdien til `t`{l=python} og `t + dt`{l=python} på hver runde i `while`{l=python}-løkka.

Kjør programmet og se på sammenhengen mellom utskriften til `t`{l=python} og `t + dt`{l=python}. Kan du forklare hva linja `t = t + dt`{l=python} gjør med verdien til `t`{l=python}? 


:::{interactive-code}
t = 0
dt = 0.5 
while t < 5:
    # Skriver ut verdien til t og t + dt
    print(f"{t = :.1f}         {t + dt = :.1f}")

    t = t + dt
:::


::::{solution}
Programmet gir utskriften:

:::{code-block} console
t = 0.0         t + dt = 0.5
t = 0.5         t + dt = 1.0
t = 1.0         t + dt = 1.5
t = 1.5         t + dt = 2.0
t = 2.0         t + dt = 2.5
t = 2.5         t + dt = 3.0
t = 3.0         t + dt = 3.5
t = 3.5         t + dt = 4.0
t = 4.0         t + dt = 4.5
t = 4.5         t + dt = 5.0
:::

Vi ser at `t + dt`{l=python} er `0.5`{l=python} større enn `t`{l=python} på hver runde i løkka. På neste runde (som blir neste rad), så er `t`{l=python} sin nye verdi lik `t + dt`{l=python} sin verdi på forrige runde som forteller oss at linja `t = t + dt`{l=python} øker verdien til `t`{l=python} med verdien til `dt`{l=python} på hver runde i løkka.


::::

:::::::::::::




:::::::::::::{tab-item} b
Nå legger vi til en linje i programmet der vi regner ut farten `v`{l=python} med formelen til fartsfunksjonen for hver verdi av `t`{l=python}. 

Kjør programmet og sjekk om du ser en sammenheng mellom utskriften og verdiene for farten `v`{l=python} for hvert tidspunkt `t`{l=python}.

Tegn punktene fra utskriften i et koordinatssystem og sjekk at det blir slik du forventer fra funksjonsuttrykket $v(t)$. 


:::{interactive-code}
t = 0
dt = 0.5 
while t < 5:
    v = 2 * t

    # Skriver ut verdien til `t` og `v`
    print(f"{t = }       {v = }")

    t = t + dt



:::



:::::::::::::


:::::::::::::{tab-item} c
Nå legger vi til en linje `s = 0`{l=python} på starten av programmet som gir variablen som holder styr på posisjonen over tid. I tillegg legger vi til en linje `s = s + v * dt`{l=python} i `while`{l=python}-løkka. I løkka skriver vi ut fire verdier på hver runde:
1. Verdien til `t`{l=python}
2. Verdien til `v * dt`{l=python}
3. Verdien til `s`{l=python}
4. Verdien til `s + v * dt`{l=python}


Se på utskriften og se på sammenhengen mellom kolonnene for `v * dt`{l=python}, `s`{l=python} og `s + v * dt`{l=python}.
1. Ser du en sammenheng mellom verdiene på hver rad?
2. Der du en sammenheng mellom verdiene til `s`{l=python} og `s + v*dt`{l=python} på to rader som er rett ovenfor hverandre?


Forklar hva linja `s = s + v * dt`{l=python} gjør for noe ut ifra det du har sett.

:::{interactive-code}
s = 0
t = 0
dt = 0.5 
while t < 5:
    v = 2 * t

    # Skriver ut verdiene til `t`, `v * dt`, `s` og `s + v * dt`. 
    print(f"{t = }    {v * dt = }     {s = }     {s + v * dt = }")

    s = s + v * dt

    t = t + dt



:::

:::::::::::::


::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 2
En ball blir kastet rett opp i luften og bevegelsen til ballen har fartsfunksjonen (i m/s)

$$
v(t) = -9.81\cdot t + 30
$$


Vi antar at posisjonen er målt i meter, farten i meter per sekund og tiden i sekunder.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Nedenfor vises et program som regner ut hvor lang tid det tar før ballen treffer bakken, men programmet er plassert i tilfeldig rekkefølge.

Sett sammen programmet slik at det står i riktig rekkefølge.
:::::::::::::


:::::::::::::{tab-item} b
Hva er starthøyden til ballen som er brukt i programmet?


:::::::::::::


:::::::::::::{tab-item} c
Hvordan kan du se fra programmet at det kjører bare frem til ballen treffer bakken? 

:::::::::::::


:::::::::::::{tab-item} d
Hva er startfarten til ballen? 


:::::::::::::


:::::::::::::{tab-item} e
Hvor lang tid tar det før ballen treffer bakken, ifølge programmet? (Kjør programmet!)




:::{cas-popup}
---
layout: sidebar
---
:::


Posisjonsfunksjonen vil være gitt ved 

$$
s(t) = -\dfrac{9.81}{2}t^2 + 30t + 2
$$

Bruk CAS til å sjekke om svaret du får fra programmet stemmer overens med når $s(t) = 0$.



:::::::::::::


::::::::::::::


:::{parsons-puzzle}
s = 2 ;t = 0 ;dt = 0.001

while s > 0:
    v = -9.81 * t + 30
    s = s + v * dt

    t = t + dt

print(f"Ballen treffer bakken etter {t = :0.2f} s.")
:::



:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 3
> Her skal du endelig få se på en posisjonsgraf ut ifra beregning, og vi skal ta utgangspunkt i bevegelsen fra oppgave 2. 
> Programmet nedenfor legger til noen nye kodelinjer som du ikke trenger å forstå stort av, men her er en kort forklaring av hensikten deres.
> 1. Det legges til to tomme lister `tid = []`{l=python} og `posisjon = []`{l=python} som skal brukes til å lagre tidspunktene og posisjonene underveis i løkka.
> 2. Det legges til to linjer `tid.append(t)`{l=python} og `posisjon.append(s)`{l=python} som legger til verdiene til `t`{l=python} og `s`{l=python} i listene `tid`{l=python} og `posisjon`{l=python} på hver runde i løkka slik at vi kan tegne punktene i et koordinatssystem.
> 3. Helt på slutten av programmet legges det til noen kodelinjer som tegner grafen ut ifra verdiene i listene `tid`{l=python} og `posisjon`{l=python}. 


En ball blir kastet rett opp i luften og bevegelsen til ballen har fartsfunksjonen (i m/s)

$$
v(t) = -9.81\cdot t + 30
$$


Vi antar at posisjonen er målt i meter, farten i meter per sekund og tiden i sekunder.


Kjør programmet og se på posisjonsgrafen. Beskriv bevegelsen med utgangspunkt i følgende spørsmål:
1. Når er farten til ballen størst?
2. Når er farten til ballen lik null?
3. Hvor høyt over bakken kommer ballen (omtrent)?
4. Når er farten positiv, og når er farten negativ?


:::{interactive-code}
tid = []
posisjon = []

s = 2
t = 0
dt = 0.001

while s > 0:
    tid.append(t)
    posisjon.append(s)

    v = -9.81 * t + 30
    s = s + v * dt

    t = t + dt

print(f"Ballen treffer bakken etter {t = :0.2f} s.")


# Tegner posisjonsgrafen
import plotmath
plotmath.plot(xdata=tid, ydata=posisjon, xlabel="$t$ / s", ylabel="$s$ / m")
plotmath.show()
plotmath.close()
:::



:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 4
Anna og Rotem jobber med fartsfunksjonen fra oppgave 2 og 3, og snakker om hvordan de kan få programmet til å bestemme når ballen er på sitt høyeste punkt.


:::{dialogue}
---
name1: Anna
name2: Rotem
speaker1: left
speaker2: right
---
Anna: Er det ikke sånn at farten til ballen er null når den er på sitt høyeste?
Rotem: Jo, men jeg har hørt at vi ikke bare kan skrive `v == 0`{l=python} for å sjekke om farten er null siden vi kanskje ikke akkurat treffer den riktige verdien for tiden `t`{l=python} som gjør at farten blir null.
Anna: Men vi har jo sett på posisjonsgrafen, så vi vet jo når farten er positiv og når den er negativ.
Rotem: Sant det! Da kan vi jo bare kjøre programmet til farten bytter fortegn, kan vi ikke?
:::

<br>


Ta utgangspunkt i dialogen til Anna og Rotem, og sett en betingelse i `while`{l=python}-løkka slik at programmet finner ut når ballen er på sitt høyeste punkt. 

Bestem også hvor høyt over bakken ballen kommer.


:::{interactive-code}
s = 2
t = 0
dt = 0.001

while ????:
    v = -9.81 * t + 30
    s = s + v * dt

    t = t + dt

# Skriv ut når og hvor høyt ballen er over bakken på sitt høyeste
:::


:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 5
Anna og Rotem skal kaste en stein fra en bro som er 150 m over en elv. De lurer på om de kan forutsi hvor lang tid det tar før steinen treffer vannet.


:::{dialogue}
---
name1: Anna 
name2: Rotem 
speaker1: left
speaker2: right
---
Anna: Jeg har hørt at hvis vi ser bort i fra luften, så vil alle gjenstander falle med en konstant akselerasjon på $a = -9.81 \, \mathrm{m/s^2}$. 
Rotem: Kult det, men hva hjelper det oss? Vi vet jo bare hvordan vi bestemmer posisjonen ut ifra fart. 
Anna: Men fart er jo bare endring av posisjon, og akselerasjon er endring av fart. Burde ikke akselerasjon og fart ha en sammenheng som er akkurat som for fart og posisjon da?
Rotem: Jo det bør de! Spesielt hvis vi tenker på at vi bare ganger enhetene til akselerasjon med enheten til tid. Da får vi jo enheten til fart!
Anna: Men da må vi vel først bruke akselerasjon til å regne ut fart, og deretter farten til å regne ut posisjonen da?
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---


:::::::::::::{tab-item} a
Forklar hva Rotem mener med at det sammenhengen mellom akselerasjon og fart, og sammenhengen mellom fart og posisjon bør være lik ut ifra enhetene. 


:::::::::::::


:::::::::::::{tab-item} b
Anna og Rotem har skrevet et program som de så klippet ut for å teste hverandre på hvilken rekkefølge programmet må skrives i for å regne ut farten og posisjonen over tid. Men de har helt glemt hvilken rekkefølge det skal stå i.

Sett sammen programmet til Anna og Rotem så det regner ut farten og posisjonen til steinen over tid.



:::::::::::::


:::::::::::::{tab-item} c
Se på hvordan farten og posisjonen i programmet regnes ut.

Kan du forklare hva Anna og Rotem mener med at sammenhengen mellom akselerasjon og fart er den samme som sammenhengen mellom fart og posisjon?


:::::::::::::


::::::::::::::



:::{parsons-puzzle}
t = 0 ;v = 0 ;s = 150 ;dt = 0.01

while s > 0:
    a = -9.81
    v = v + a * dt
    s = s + v * dt

    t = t + dt

print(f"Det tar {t = :0.2f} s før steinen treffer vannet")
:::

:::::::::::::::



---




:::::::::::::::{exercise} Oppgave 6
Siden akselerasjonen til en gjenstand forteller oss hvordan farten endrer seg, og farten forteller oss hvordan posisjonen til en gjenstand endrer seg, er det naturlig å både tegne fartsgrafen og posisjonsgrafen til gjenstanden.

Fyll ut programmet nedenfor der det står `# FYLL INN`{l=python}. Alle andre kodelinjer skal du la stå som de er. 

Vi minner om disse opplysningene for steinen som blir sluppet fra broen:
* Steinen faller fra 150 m høyde.
* Steinen starter i ro (hva er startfarten da?)
* Akselerasjonen til steinen er konstant lik $a = -9.81 \, \mathrm{m/s^2}$.


> Du kan scrolle i vinduet som gir en utskrift der figurene kommer slik at du får se både fartsgrafen og posisjonsgrafen!

:::{interactive-code}
tid = []
fart = []
posisjon = []


t = 0
v = ???? # FYLL INN
s = ???? # FYLL INN
dt = 0.0001

while ????: # FYLL INN betingelse for bevegelsen
    tid.append(t)
    fart.append(v)
    posisjon.append(s)


    a = ???? # FYLL INN akselerasjonen
    v = ???? # FYLL INN formelen for å regne ut fart fra akselerasjon
    s = ???? # FYLL INN formelen for å regne ut posisjon fra fart

    t = t + dt




import plotmath
plotmath.plot(xdata=tid, ydata=fart, xlabel="$t$ / s", ylabel="$v$ / (m/s)")
plotmath.show()
plotmath.close()

plotmath.plot(xdata=tid, ydata=posisjon, xlabel="$t$ / s", ylabel="$s$ / m")
plotmath.show()
plotmath.close()
:::





:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 7
Fester vi en kloss til en fjær og lar den ligge i ro, så vil ikke klossen bevege seg. Vi lar $s = 0 \, \mathrm{m}$ svare til posisjonen klossen har når dette er tilfellet. 

Vi tenker oss at fjæra er festet til en betongvegg og så drar vi i klossen før vi slipper den. For klossen vi ser på, er akselerasjonen gitt ved

$$
a(t) = -2 \cdot s(t)
$$


der $s(t)$ er posisjonen til klossen etter $t$ sekunder og $a(t)$ er akselerasjonen i $\mathrm{m/s^2}$} til klossen etter $t$ sekunder.



::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Fyll ut programmet nedenfor og kjør programmet for å tegne fartsgrafen og posisjonsgrafen til klossen.



:::::::::::::


:::::::::::::{tab-item} b
Se på posisjonsgrafen (husk på se på aksene for å se hvilken graf du ser på!)

Gi en beskrivelse av klossens bevegelse ut ifra posisjonsgrafen.
:::::::::::::


:::::::::::::{tab-item} c
Se på fartsgrafen til klossen.

Gi en beskrivelse av klossens bevegelse ut ifra fartsgrafen.

:::::::::::::


:::::::::::::{tab-item} d
Kan du gi en beskrivelse av sammenhengen mellom posisjonsgrafen og fartsgrafen til klossen?


::::{hints}
Vi har ikke enda vektlagt denne ideen, men kanskje har du oppdaget at "stigningstallet" til posisjonsgrafen gir oss farten til grafen. Mer presist vil den momentane vekstfarten til posisjonsgrafen være lik farten til klossen. Se på de grafene og sjekk om dette stemmer.
::::


:::::::::::::


::::::::::::::



:::{interactive-code}
tid = []
fart = []
posisjon = []


t = 0
v = ???? # FYLL INN
s = ???? # FYLL INN
dt = 0.0001

while ????: # FYLL INN betingelse for bevegelsen
    tid.append(t)
    fart.append(v)
    posisjon.append(s)


    a = ???? # FYLL INN akselerasjonen
    v = ???? # FYLL INN formelen for å regne ut fart fra akselerasjon
    s = ???? # FYLL INN formelen for å regne ut posisjon fra fart

    t = t + dt




import plotmath
plotmath.plot(xdata=tid, ydata=fart, xlabel="$t$ / s", ylabel="$v$ / (m/s)")
plotmath.show()
plotmath.close()

plotmath.plot(xdata=tid, ydata=posisjon, xlabel="$t$ / s", ylabel="$s$ / m")
plotmath.show()
plotmath.close()
:::




:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 8
En fallskjermhopper hopper ut av et fly fra 3000 m høyde. Under fallet, opplever en motstand fra luften og en tiltrekning til bakken fra tyngdefeltet. Dermed har fallskjermhopperen en akselerasjon som er gitt ved

$$
a(t) = -9.81 + 0.0025 \cdot v(t)^2
$$

der $a(t)$ er målt i $\mathrm{m/s^2}$ og $v(t)$ er farten i $\mathrm{m/s}$ til fallskjermhopperen etter $t$ sekunder. Akselerasjonen er altså avhengig av farten til fallskjermhopperen.

Vi tenker oss at startfarten til fallskjermhopperen er $v = 0 \, \mathrm{m/s}$. Posisjonen til fallskjermhopperen er målt i meter.



::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Fyll ut programmet nedenfor og kjør programmet for å tegne fartsgrafen og posisjonsgrafen til fallskjermhopperen.


:::::::::::::


:::::::::::::{tab-item} b
Bruk fartsgrafen til å beskrive hvordan bevegelsen til fallskjermhopperen utvikler seg over tid.

Kan du forklare hva som skjer med fallskjermhopperens fart når tiden blir stor? Hva tror du er grunnen til at farten oppfører seg slik?


:::::::::::::


:::::::::::::{tab-item} c
Kan du beskrive sammenhengen mellom fartsgrafen og posisjonsgrafen? 


::::{hints}
Tenk på at "stigningstallet" til posisjonsgrafen gir oss farten til fallskjermhopperen. 
::::


:::::::::::::


:::::::::::::{tab-item} d
Hvor lang tid tar det før fallskjermhopperen lander på bakken? 

Er det noe urealistisk med bevegelsen til fallskjermhopperen ved landingen? 

:::::::::::::







::::::::::::::



:::{interactive-code}
tid = []
fart = []
posisjon = []


t = 0
v = ???? # FYLL INN
s = ???? # FYLL INN
dt = 0.0001

while ????: # FYLL INN betingelse for bevegelsen
    tid.append(t)
    fart.append(v)
    posisjon.append(s)


    a = ???? # FYLL INN akselerasjonen
    v = ???? # FYLL INN formelen for å regne ut fart fra akselerasjon
    s = ???? # FYLL INN formelen for å regne ut posisjon fra fart

    t = t + dt




import plotmath
plotmath.plot(xdata=tid, ydata=fart, xlabel="$t$ / s", ylabel="$v$ / (m/s)")
plotmath.show()
plotmath.close()

plotmath.plot(xdata=tid, ydata=posisjon, xlabel="$t$ / s", ylabel="$s$ / m")
plotmath.show()
plotmath.close()
:::

:::::::::::::::


