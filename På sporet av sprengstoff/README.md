#Oppgave#

Du skal lære å traversere (se på alle elementene) en lenket liste. I det utleverte rammeverket er det skrevet kode for å lage en lenket liste. Det viktige i denne øvingen er å forstå hvordan du kan lenke sammen elementer ved hjelp av referanser. Dette er veldig vanlig i objektorientert programmering. Trikset når du lager en lenket liste, er å koble sammen flere objekter av samme klasse, slik at hvert objekt har en referanse (lenke) til ett annet objekt (det 'neste' objektet'). Hvis du så et eller annet sted tar vare på en referanse til det første objektet i lenkingen (det eneste objektet som ikke blir lenket til av noen andre objekter), har du et utgangspunkt for å traverse hele listen av objekter.

Input består av heltall separert av linjeskift. Programmet ditt skal legge inn disse i en lenket liste, traversere den lenkete listen, og skrive ut det høyeste tallet. Du kan tenke på tallene som vekter på dynamittkubber og lenkene du lager mellom kubbene som lunter koblet sammen.

##Input-eksempel##

54  
37  
100  
123  
1  
54  

##Tilhørende output##

123