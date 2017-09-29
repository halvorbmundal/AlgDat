#Oppgave#

Du skal lage et program for � finne ord i en tekst. For � gj�re dette, kan du lage en funksjon som bygger et tre og en funksjon som bruker treet til � s�ke. F�rste linje av input til programmet er en streng som best�r av tegnene [a-z] og mellomrom. Dette representerer dokumentet det skal s�kes i. De neste linjene i input er sp�rringer etter ord. Programmet skal s�ke etter disse ordene i teksten, og returnere hvilke posisjoner ordet finnes p�. Tegnet ? brukes til � angi at her kan det st� en hvilket som helst bokstav fra alfabetet [a-z].

En m�te � l�se denne oppgaven p� er � putte ordene inn i et tre, hvor hver bokstav i ordet tilsvarer en peker til neste node. Nedenfor ser du treet for setningen ha ha mons har en hund med moms hun er en hunn. Legg merke til at noen av nodene inne i treet tilsvarer slutten p� ord, mens andre ikke gj�r det. Legg ogs� merke til at noen ord finnes p� flere steder i dokumentet.

Funksjonen posisjoner(ord, indeks, node) som skal returnerer posisjonene til alle treff p� ord i trestrukturen med rot node. indeks sier hvor langt i ordet vi har kommet. For � finne disse posisjonene kan den bruke rekursjon. � bruke rekursjon vil si � utf�re rekursive kall. Et kall til funksjonen selv er et rekursivt kall. Rekursjon brukes som regel til � dele opp et problem i mindre deler, for deretter � sette sammen l�sningene. I dette problemet er det ordene som inneholder ? som kan gi flere delproblemer. N�r du ser ? skal du kalle posisjoner �n gang for alle mulige erstatninger for ? med de tilh�rende delene av treet.

##Input-eksempel##

ha ha mons har en hund med moms hun er en hunn  
ha  
mjau  
m?d  
e? 

##Tilh�rende output##

ha: 0 3  
mjau:  
m?d: 23  
e?: 15 36 39  

Du kan teste programmet med kommandoen:

    python program.py < input.txt