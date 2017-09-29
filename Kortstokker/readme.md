#Oppgave#

I denne øvingen skal du flette sammen et sett med kortstokker. På hvert av disse kortene står det ett tall og en bokstav. Hver enkelt stokk er allerede sortert på tall. Oppgaven din er å flette stokkene sammen slik at resultatet fremdeles er riktig sortert. Det er mange forskjellige måter å løse dette problemet på, men det enkleste er nok å flette sammen stokkene som du gjør i merge-sort. Se Cormen side 32.

Input til programmet er en stokk på hver linje. Kortene i hver stokk har alltid samme bokstav. Hver linje begynner med bokstaven til stokken etterfulgt av kolon. Deretter kommer verdien til kortene, separert med komma, i sortert rekkefølge. Det vil aldri finnes to kort med samme verdi. Du skal skrive ut ordet som bokstavene til de sorterte kortene danner (uten mellomrom).

Hvis du implementerer fornuftig, blir kjøretiden O(n log k), hvor k er antall stokker. Men mergingen av disses stokkene kan til og med bli mer enn O(n log n) hvis du merger dem i på en dum måte. Den kan bli så mye som O(n2). Hvordan det? Spør en studass hvis du ikke finner det ut.

I denne øvingen er det ikke tillatt å bruke den innebygde list.sort(). Ikke levér slike løsninger på øvingssystemet. Det er også juks å bruke modulen heapq og lignende. Moral: Alt som har med selve sorteringen å gjøre må du gjøre selv.

##Input-eksempel##

i:1,3,5,8  
n:2  
t:4,7  
a:6  
v:9  

##Tilhørende output##

initiativ

Du kan teste programmet med kommandoen:

    python program.py < input.txt