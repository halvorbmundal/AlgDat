#Oppgave#

I denne �vingen skal du flette sammen et sett med kortstokker. P� hvert av disse kortene st�r det ett tall og en bokstav. Hver enkelt stokk er allerede sortert p� tall. Oppgaven din er � flette stokkene sammen slik at resultatet fremdeles er riktig sortert. Det er mange forskjellige m�ter � l�se dette problemet p�, men det enkleste er nok � flette sammen stokkene som du gj�r i merge-sort. Se Cormen side 32.

Input til programmet er en stokk p� hver linje. Kortene i hver stokk har alltid samme bokstav. Hver linje begynner med bokstaven til stokken etterfulgt av kolon. Deretter kommer verdien til kortene, separert med komma, i sortert rekkef�lge. Det vil aldri finnes to kort med samme verdi. Du skal skrive ut ordet som bokstavene til de sorterte kortene danner (uten mellomrom).

Hvis du implementerer fornuftig, blir kj�retiden O(n log k), hvor k er antall stokker. Men mergingen av disses stokkene kan til og med bli mer enn O(n log n) hvis du merger dem i p� en dum m�te. Den kan bli s� mye som O(n2). Hvordan det? Sp�r en studass hvis du ikke finner det ut.

I denne �vingen er det ikke tillatt � bruke den innebygde list.sort(). Ikke lev�r slike l�sninger p� �vingssystemet. Det er ogs� juks � bruke modulen heapq og lignende. Moral: Alt som har med selve sorteringen � gj�re m� du gj�re selv.

##Input-eksempel##

i:1,3,5,8  
n:2  
t:4,7  
a:6  
v:9  

##Tilh�rende output##

initiativ

Du kan teste programmet med kommandoen:

    python program.py < input.txt