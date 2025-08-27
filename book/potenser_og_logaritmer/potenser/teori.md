# Potenser

:::{goals} Læringsmål
* Kunne bruke potensregler til å forenkle algebraisk uttrykk med potenser.
:::


## Hva er en potens?

En potens er et uttrykk som forteller oss hvor mange ganger vi skal gange et tall med seg selv. For eksempel er 

$$
2^3 = 2 \cdot 2 \cdot 2 = 8
$$

som forteller oss at vi skal gange $2$ med seg selv $3$ ganger. Vi har et spesielt navn for de ulike tallene i potensen: 

:::::::::::::::{summary} Potenser
En potens $x^a$ har et grunntall $x$ og en eksponent $a$. Eksponenten forteller oss hvor mange ganger vi skal gange grunntallet med seg selv.


:::::::::::::::


---

## Potensregler
Når vi jobber med algebraiske uttrykk, trenger vi ofte å bruke noen regneregler for potenser slik at vi kan forenkle uttrykkene. 



:::::::::::::::{summary} Potensregel 1
For to potenser $x^a$ og $x^b$ med samme grunntall $x$, har vi 

$$
x^a \cdot x^b = x^{a + b}
$$

Når vi ganger to potenser med samme grunntall, legger vi sammen eksponentene for å få eksponenten i den nye potensen.
:::::::::::::::

Vi kan først se at regneregelen gir mening når vi jobber med tall:

:::::::::::::::{theory} Begrunnelse 1 for Potensregel 1 

$$
2^3 \cdot 2^4 = \underbrace{2 \cdot 2 \cdot 2}_{\displaystyle \text{$3$ faktorer}} \cdot \underbrace{2 \cdot 2 \cdot 2 \cdot 2}_{\displaystyle \text{$4$ faktorer}} = \underbrace{2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2}_{\displaystyle \text{$3+4 = 7$ faktorer}} = 2^{3 + 4} = 2^7
$$

:::::::::::::::


La oss se hvordan vi kan bruke samme tankemåte, men med variabler:


:::::::::::::::{theory} Begrunnelse 2 for Potensregel 1 

Vi kan rettferdiggjøre regneregelen ovenfor ved å tenke oss følgende regnestykke:

$$
x^a \cdot x^b = \underbrace{x \cdot x \cdot \ldots \cdot x}_{\displaystyle \text{$a$ faktorer}} \cdot \underbrace{x \cdot x \cdot \ldots \cdot x}_{\displaystyle \text{$b$ faktorer}} = \underbrace{x \cdot x \cdot \ldots \cdot x}_{\displaystyle \text{$a + b$ faktorer}} = x^{a + b}
$$

:::::::::::::::


---

La oss se på et eksempel:

:::::::::::::::{example} Eksempel 1
Skriv uttrykket nedenfor så enkelt som mulig: 

$$
x^3 \cdot x^6
$$

::::{solution}
---
dropdown: 0
---

$$
x^3 \cdot x^6 = x^{3 + 6} = x^9
$$
::::

:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 1
Skriv uttrykket nedenfor så enkelt som mulig.

$$
x^2 \cdot x^4
$$


::::{answer}
$$
x^6 
$$
::::

::::{solution}
$$
x^2 \cdot x^4 = x^{2 + 4} = x^6
$$
::::

:::::::::::::::


---

:::::::::::::::{summary} Potensregel 2
For to potenser $x^a$ og $x^b$ med samme grunntall $x$, har vi 

$$
\dfrac{x^a}{x^b} = x^{a - b}
$$

Når vi deler to potenser, tar vi altså eksponenten til telleren minus eksponenten til nevneren.

:::::::::::::::

La oss se hvordan dette stemmer når vi jobber med tall: 


:::::::::::::::{theory} Begrunnelse 1 for Potensregel 2 
$$
\dfrac{2^5}{2^2} = \dfrac{\overbrace{2 \cdot 2 \cdot 2 \cdot 2 \cdot 2}^{\displaystyle \text{$5$ faktorer}}}{\underbrace{2 \cdot 2}_{\displaystyle \text{$2$ faktorer}}} = \dfrac{\overbrace{\cancel{2} \cdot \cancel{2}}^{\displaystyle \text{$2$ faktorer}} \cdot \overbrace{2 \cdot 2 \cdot 2}^{\displaystyle \text{$5 - 2$ faktorer}}}{\underbrace{\cancel{2} \cdot \cancel{2}}_{\displaystyle \text{$2$ faktorer}}} = \underbrace{2 \cdot 2 \cdot 2}_{\text{$5 - 2 = 3$ faktorer}} = 2^{5 - 2} = 2^3 
$$

:::::::::::::::


---

La oss se hvordan vi kan bruke samme tankemåte, men med variabler:

:::::::::::::::{theory} Begrunnelse 2 for Potensregel 2 
Vi tenker oss to potenser $x^a$ og $x^b$ der $a$ er større enn $b$. Da har vi at

$$
\dfrac{x^a}{x^b}
= \dfrac{\overbrace{x \cdot x \cdot \ldots \cdot x}^{\displaystyle \text{$a$ faktorer}}}{\underbrace{x \cdot x \cdot \ldots \cdot x}_{\displaystyle \text{$b$ faktorer}}}
= \dfrac{\overbrace{\cancel{x} \cdot \cancel{x} \cdot \ldots \cdot \cancel{x}}^{\displaystyle \text{$b$ faktorer}} \cdot \overbrace{x \cdot x \cdot \ldots \cdot x}^{\displaystyle \text{$a - b$ faktorer}}}{\underbrace{\cancel{x} \cdot \cancel{x} \cdot \ldots \cdot \cancel{x}}_{\displaystyle \text{$b$ faktorer}}}
= \underbrace{x \cdot x \cdot \ldots \cdot x}_{\displaystyle \text{$a - b$ faktorer}}
= x^{a - b}
$$

:::::::::::::::


---

La oss se på et eksempel:


:::::::::::::::{example} Eksempel 2
Skriv uttrykket nedenfor så enkelt som mulig: 

$$
\dfrac{x^7}{x^2}
$$

::::{solution}
---
dropdown: 0
---

$$
\dfrac{x^7}{x^2} = x^{7 - 2} = x^5
$$
::::

:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 2
Skriv uttrykket nedenfor så enkelt som mulig.

$$
\dfrac{x^8}{x^5}
$$


::::{answer}
$$
x^3
$$
::::

::::{solution}
$$
\dfrac{x^8}{x^5} = x^{8 - 5} = x^3
$$
::::

:::::::::::::::


---


:::::::::::::::{summary} Potensregel 3
For et grunntall $x$, så gjelder følgende regneregel

$$
(x^a)^b = x^{a \cdot b}
$$
:::::::::::::::


---

La oss først se at denne regelen gir mening med tall:


:::::::::::::::{theory} Begrunnelse 1 for Potensregel 3 
$$
(3^4)^2 = \underbrace{3^4 \cdot 3^4}_{\displaystyle \text{$2$ faktorer}} = \underbrace{\overbrace{(3 \cdot 3 \cdot 3 \cdot 3)}^{\text{$4$ faktorer}} \cdot \overbrace{(3 \cdot 3 \cdot 3 \cdot 3)}^{\text{$4$ faktorer}}}_{\displaystyle \text{$2$ faktorer av $(3 \cdot 3 \cdot 3 \cdot 3)$}} = \underbrace{3 \cdot 3 \cdot 3 \cdot 3 \cdot 3 \cdot 3 \cdot 3 \cdot 3}_{\displaystyle \text{$4 \cdot 2$ faktorer}} = 3^{4 \cdot 2} = 3^8
$$
:::::::::::::::


La oss ta utgangspunkt i tankegangen ovenfor og vise det mer generelt med variabler:

:::::::::::::::{theory} Begrunnelse 2 for Potensregel 3
Vi skal vise at $(x^a)^b = x^{a \cdot b}$. Hver faktor $x^a$ bringer med seg $a$ faktorer av $x$. Vi har $b$ faktorer av $x^a$ som gir oss $a \cdot b$ faktorer av $x$: 

$$
(x^a)^b = \underbrace{x^a \cdot x^a \cdot \ldots \cdot x^a}_{\displaystyle b\ \text{faktorer}} 
= \underbrace{x \cdot x \cdot \ldots \cdot x}_{\displaystyle a \cdot b\ \text{faktorer}} 
= x^{a \cdot b}
$$
:::::::::::::::


---

La oss se på et eksempel:

:::::::::::::::{example} Eksempel 3
Skriv så enkelt som mulig:

$$
(x^3)^4
$$

::::{solution}
---
dropdown: 0
---

Vi bruker Potensregel 3 

$$
(x^3)^4 = x^{3 \cdot 4} = x^{12}
$$
::::

:::::::::::::::

---

:::::::::::::::{exercise} Underveisoppgave 3
Skriv så enkelt som mulig:

$$
(x^2)^3
$$



::::{answer}
$$
x^6
$$
::::

::::{solution}
Vi bruker Potensregel 3:

$$
(x^2)^3 = x^{2 \cdot 3} = x^6
$$

::::

:::::::::::::::


---


:::::::::::::::{summary} Potensregel 4
For to tall $x$ og $y$, og en eksponent $a$, har vi 

$$
(x \cdot y)^a = x^a \cdot y^a
$$
:::::::::::::::


---

La oss se på en begrunnelse for Potensregel 4 med tall: 


:::::::::::::::{theory} Begrunnelse 1 for Potensregel 4 

$$
(2 \cdot 4)^4 = \underbrace{(2 \cdot 4) \cdot (2 \cdot 4) \cdot (2 \cdot 4) \cdot (2 \cdot 4)}_{\displaystyle 4\ \text{faktorer}} = \underbrace{(2 \cdot 2 \cdot 2 \cdot 2)}_{\displaystyle 4\ \text{faktorer}} \cdot \underbrace{(4 \cdot 4 \cdot 4 \cdot 4)}_{\displaystyle 4\ \text{faktorer}} = 2^4 \cdot 4^4
$$

:::::::::::::::

---

Vi tar utgangspunkt i samme tankemåte og viser regneregelen mer generelt:


:::::::::::::::{theory} Begrunnelse 2 for Potensregel 4
Vi skal vise at $(x \cdot y)^a = x^a \cdot y^a$. Vi har $a$ faktorer av $(x \cdot y)$ som bringer med seg $a$ faktorer av $x$ og $a$ faktorer av $y$. Vi kan bytte rekkefølgen vi ganger tallene i som gir:

$$
(x \cdot y)^a = \underbrace{(x \cdot y) \cdot (x \cdot y) \cdot \ldots \cdot (x \cdot y)}_{\displaystyle \text{$a$ faktorer}}  = \underbrace{x \cdot x \cdot \ldots \cdot x}_{\displaystyle \text{$a$ faktorer}} \cdot \underbrace{y \cdot y \cdot \ldots \cdot y}_{\displaystyle \text{$a$ faktorer}} = x^a \cdot y^a
$$

:::::::::::::::



---

La oss se på et konkret eksempel:

:::::::::::::::{example} Eksempel 4
Skriv uttrykket nedenfor så enkelt som mulig: 

$$
(3x)^4
$$


::::{solution}
---
dropdown: 0
---
Vi bruker Potensregel 4: 

$$
(3x)^4 = (3 \cdot x)^4 = 3^4 \cdot x^4 = 81x^4 
$$

::::



:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 4
Utvid parentesen:

$$
(2x)^3
$$


::::{answer}
$$
8x^3
$$
::::

::::{solution}
$$
(2x)^3 = (2\cdot x)^3 = 2^3 \cdot x^3 = 8x^3
$$
::::

:::::::::::::::


---


:::::::::::::::{summary} Potensregel 5
For alle tall $x \neq 0$, har vi **definert** at 

$$
x^0 = 1
$$
:::::::::::::::


---


:::::::::::::::{theory} Begrunnelse for Potensregel 5 
Vi tenker oss følgende regnestykke:

$$
\dfrac{x^a}{x^a} = 1
$$

Så lenge $x \neq 0$, så må dette være lik $1$. Men Potensregel 2 forteller oss også at 

$$
\dfrac{x^a}{x^a} = x^{a - a} = x^0
$$

For at de to regnestykkene skal stemme overens, er vi nødt til å definere at $x^0 = 1$.
:::::::::::::::


---

La oss se på et eksempel:

:::::::::::::::{example} Eksempel 5
Regn ut $1000^0$

::::{solution}
---
dropdown: 0
---

For alle grunntall $x \neq 0$ har vi at $x^0 = 1$. Dermed er $1000^0 = 1$.
::::


:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 5
Regn ut

$$
72^0
$$


::::{answer}
$$
72^0 = 1
$$
::::


::::{solution}
For tall grunntall $x \neq 0$ har vi at $x^0 = 1$. Dermed er $72^0 = 1$.
::::
 

:::::::::::::::


---


:::::::::::::::{summary} Potensregel 6
For alle grunntall $x \neq 0$, så har vi **definert** at

$$
x^{-a} = \dfrac{1}{x^a}
$$
:::::::::::::::


---


:::::::::::::::{theory} Begrunnelse for Potensregel 6 
Dette følger som en konsekvens av Potensregel 5. For alle tall $a$, vil følgende være sant:

$$
x^{a - a} = x^0 
$$

Bruker vi potensregel 1 på venstre side og potensregel 5 på høyre side, får vi:

$$
x^a \cdot x^{-a} = 1
$$

Hvis vi deler med $x^a$ på hver side får vi:

$$
x^{-a} = \dfrac{1}{x^a}
$$
:::::::::::::::


---

La oss se på et eksempel med tall der vi bruker potensregel 6:


:::::::::::::::{example} Eksempel 6
Regn ut 

$$
5^{-2}
$$


::::{solution}
---
dropdown: 0
---
Vi bruker Potensregel 6:

$$
5^{-2} = \dfrac{1}{5^2} = \dfrac{1}{25}
$$
::::
:::::::::::::::

---


:::::::::::::::{exercise} Underveisoppgave 6
Regn ut 

$$
2^{-4}
$$


::::{answer}
$$
\dfrac{1}{16}
$$
::::

::::{solution}
Vi bruker Potensregel 6:

$$
2^{-4} = \dfrac{1}{2^4} = \dfrac{1}{16}
$$
::::

:::::::::::::::


---

## Potensregler og røtter

Vi har til nå bare jobbet med hele tall som eksponenter. Et naturlig spørsmål man kan stille seg er om vi kan bruke potensreglene uansett hva eksponenten er. 

La oss se hva som skjer dersom vi tillatter brøker som eksponenter ved å ta utgangspunkt i Potensregel 1 $x^a \cdot x^b = x^{a + b}$:

$$
x = x^1 = x^{\tfrac{1}{2} + \tfrac{1}{2}} = x^{\tfrac{1}{2}} \cdot x^{\tfrac{1}{2}}
$$

Vi ser altså at $x^{\frac{1}{2}}$ er det tallet vi må gange med seg selv for å få $x$. Men dette er jo definisjonen av kvadratroten av $x$, som må bety at hvis vi tillater at eksponentene ikke bare er hele tall, så kan vi definere:

$$
\sqrt{x} = x^{\tfrac{1}{2}}
$$

Når vi opphøyer et tall i $\dfrac{1}{2}$ mener vi altså at vi skal ta kvadratroten av tallet! 

> Merk: Eksponenten $\dfrac{1}{2}$ i $x^\tfrac{1}{2}$ er ikke det samme som å dele $x$ med $2$. Husk at det handler om å ta kvadratroten.



La oss se på et konkret eksempel der vi bruker potensreglene til å vise at dette funker:


:::::::::::::::{example} Eksempel 7
Regn ut 

$$
9^\tfrac{1}{2}
$$

::::{solution}
---
dropdown: 0
---
Først kan vi merke oss at $9 = 3^2$ som betyr at vi kan skrive

$$
9^\tfrac{1}{2} = (3^2)^\tfrac{1}{2}
$$

Hvis vi nå bruker Potensregel 3 som sa at $(x^a)^b = x^{a \cdot b}$, så får vi 

$$
(3^2)^\frac{1}{2} = 3^{2 \cdot \tfrac{1}{2}} = 3^1 = 3
$$

Men dette er jo det samme som $\sqrt{9}$ så vi ser at regelen fungerer i praksis.
::::
:::::::::::::::


:::::::::::::::{summary} Kvadratrot som potens
Kvadratroten av et tall $x$ er det samme som å opphøye tallet i $\dfrac{1}{2}$, altså


$$
\sqrt{x} = x^{\tfrac{1}{2}}
$$
:::::::::::::::


### $n$-te røtter

Men hva om vi i stedet velger å dele opp potensen flere ganger som dette:

$$
x^1 = x^{\tfrac{1}{3} + \tfrac{1}{3} + \tfrac{1}{3}} = x^{\tfrac{1}{3} \cdot 3} = (x^{\tfrac{1}{3}})^3
$$

Da ser vi at $x^{\tfrac{1}{3}}$ er det tallet som må opphøyes i $3$ for å få $x$. På tilsvarende måte som at kvadratroten av $x$ er tallet som må opphøyes i $2$ for å få $x$, så vil tredjeroten av $x$ være tallet som må opphøyes i $3$ for å få $x$. Det betyr at 

:::{margin}
$\sqrt[3]{x}$ kalles noen ganger for **kubikkroten** fordi det er sidelengdene til en kube med volum $x$.
:::

$$
x^{\tfrac{1}{3}} = \sqrt[3]{x}
$$


Vi kan generalisere dette enda lenger til å definere sammenhengen mellom en $n$-te rot og potenser:


:::::::::::::::{summary} $n$-te røtter
$n$-te roten av et tall $x$ skriver vi som $\sqrt[n]{x}$ og er definert som hvilket tall vi må opphøye i $n$ for å få $x$. Sammenhengen mellom $n$-te roten og potenser er

$$
\sqrt[n]{x} = x^{\tfrac{1}{n}}
$$

:::::::::::::::

Med notasjonen vi har introdusert ovenfor, så kan vi også skrive kvadratroten av $x$ som $\sqrt[2]{x}$, men det er ikke så vanlig å gjøre i praksis. Men det kan være nyttig når vi skal huske på hvordan vi skriver om mellom potenser og kvadratrøtter.


La oss se på et eksempel der vi skriver om et sammensatte uttrykk så enkelt som mulig med potenser: 


:::::::::::::::{example} Eksempel 8
Skriv så enkelt som mulig.

$$
(\sqrt[3]{x})^2 \cdot x^2
$$


::::{solution}
---
dropdown: 0
---

$$
(\sqrt[3]{x})^2 \cdot x^2 = (x^{\tfrac{1}{3}})^2 \cdot x^2 = x^{\tfrac{2}{3}} \cdot x^2 = x^{\tfrac{2}{3}} \cdot x^{\tfrac{6}{3}} = x^{\tfrac{8}{3}}
$$

::::

:::::::::::::::