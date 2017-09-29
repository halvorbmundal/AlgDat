#Oppgave#

Du skal lage et program for å finne ord i en tekst. For å gjøre dette, kan du lage en funksjon som bygger et tre og en funksjon som bruker treet til å søke. Første linje av input til programmet er en streng som består av tegnene [a-z] og mellomrom. Dette representerer dokumentet det skal søkes i. De neste linjene i input er spørringer etter ord. Programmet skal søke etter disse ordene i teksten, og returnere hvilke posisjoner ordet finnes på. Tegnet ? brukes til å angi at her kan det stå en hvilket som helst bokstav fra alfabetet [a-z].

En måte å løse denne oppgaven på er å putte ordene inn i et tre, hvor hver bokstav i ordet tilsvarer en peker til neste node. Nedenfor ser du treet for setningen ha ha mons har en hund med moms hun er en hunn. Legg merke til at noen av nodene inne i treet tilsvarer slutten på ord, mens andre ikke gjør det. Legg også merke til at noen ord finnes på flere steder i dokumentet.

Funksjonen posisjoner(ord, indeks, node) som skal returnerer posisjonene til alle treff på ord i trestrukturen med rot node. indeks sier hvor langt i ordet vi har kommet. For å finne disse posisjonene kan den bruke rekursjon. Å bruke rekursjon vil si å utføre rekursive kall. Et kall til funksjonen selv er et rekursivt kall. Rekursjon brukes som regel til å dele opp et problem i mindre deler, for deretter å sette sammen løsningene. I dette problemet er det ordene som inneholder ? som kan gi flere delproblemer. Når du ser ? skal du kalle posisjoner én gang for alle mulige erstatninger for ? med de tilhørende delene av treet.

##Input-eksempel##

ha ha mons har en hund med moms hun er en hunn  
ha  
mjau  
m?d  
e? 

##Tilhørende output##

ha: 0 3  
mjau:  
m?d: 23  
e?: 15 36 39  

Du kan teste programmet med kommandoen:

    python program.py < input.txt