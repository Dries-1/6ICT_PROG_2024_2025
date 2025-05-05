## Opdracht 16
Je begint je eigen coder dojo! In dit project zul je object georiënteerd programmeren gebruiken om een `Lid`, `Student`, `Instructeur` en `Workshop` klasse te maken in **dojo.py**. De `Student` en `Instructeur` klasse moeten een kind zijn van de klasse `Lid`. In het bestand **test.py** zijn testen te vinden om de correcte werking van iedere klasse na te gaan.

### Lid klasse
Er komen twee soorten mensen langs bij Codebar. Degene die workshops willen volgen (`Student`) en zij die ze willen geven (`Instructeur`). Deze twee klassen hebben echter een hoop gemeen. Maak daarom een klasse `Lid` aan waarvan `Student` & `Instructeur` zullen erven.

Een object van `Lid` moet worden aangemaakt met als enige waarde de volledige naam. Deze wordt in de klasse opgesplitst naar de eigenschappen `voornaam` en `achternaam` De klasse moet hiernaast de volgende methoden bevatten.
* `voorstellen`: geeft een string terug met een introductie (VB. "Hey, mijn naam is Marc!").
* `beschrijving`: deze functie moet None teruggeven (wordt gebruikt in de Student en Instructeur klassen).

```
Test de werking door de code onder "Testen van klasse Lid" uit commentaar te halen. Zet deze na het testen terug in commentaar.
```

### Student klasse 
`Student` is een kind van de klasse `Lid`, en neemt dus alle eigenschappen en methoden van deze klasse over.

Een `Student` heeft twee extra eigenschappen.
* `reden`: waarom persoon naar de dojo komt (VB. "Ik heb altijd al websites willen maken!"). 
* `interesses`: een lijst met wat de persoon interesseert (VB. ["C#", "Java", "Javascript"]). De lijst begint altijd leeg.

Een `Student` heeft ook twee extra methoden.
* `interesse_toevoegen`: voeg een interesse toe aan de lijst met `interesses`. Als de interesse reeds in de lijst staat, voeg je deze niet opnieuw toe. Print in dit geval dat de interesse reeds aanwezig is.
* `interesse_verwijderen`: verwijder een interesse uit de lijst met `interesses`. Als de opgegeven interesse niet in de lijst staat, print dan dat de student hier nooit interesse in had.

Overschrijf tenslotte de methode `beschrijving` uit de klasse `Lid`. Oproepen van de methode print de `reden` die de persoon heeft om deel te nemen.

```
Test de werking door de code onder "Testen van klasse Student" uit commentaar te halen. Zet deze na het testen terug in commentaar.
```

### Instructeur klasse
`Instructeur` is een kind van de klasse `Lid`, en neemt dus alle eigenschappen en methoden van deze klasse over.

Een `Instructeur` heeft twee extra eigenschappen.
* `bio`: een korte besschrijving van hun ervaring (VB. "Ik ben een professionele website-ontwikkelaar!").
* `skills`: een lijst met de vaardigheden die de persoon kent (VB. ["C#", "Python", "Javascript"]). Deze lijst begint altijd leeg. 

Een `Instructeur` heeft ook een extra methode.
* `skill_toevoegen`: voeg een skill toe aan de lijst met `skills`. Als de skill reeds in de lijst staat, voeg je deze niet opnieuw toe. Print in dit geval dat de skill reeds aanwezig is.

Overschrijf tenslotte de methode `beschrijving` uit de klasse `Lid`. Oproepen van de methode print de `bio` van de persoon.

```
Test de werking door de code onder "Testen van klasse Student" uit commentaar te halen. Zet deze na het testen terug in commentaar.
```

### Workshop klasse

Je dojo bestaat uit workshops. Iedere workshop heeft volgende eigenschappen:
* `datum`: wanneer workshop plaatsvindt.
* `onderwerp`: onderwerp van de workshop.
* Een lijst met `instructeurs`. Begint leeg.
* Een lijst met `studenten`. Begint leeg.

Hiernaast heeft de dojo 3 methoden.
* `deelnemer_toevoegen`: geef aan deze methode een object van `Student` of `Instructeur` mee. Het voegt het object vervolgens toe aan de overeenkomstige lijst (`instructeurs` of `studenten`). Dit gebeurt echter enkel als het `onderwerp` in de workshop overeenkomt met de `interesses` of `skills` van deze persoon. Indien dit niet het geval is, print de methode een bericht dat aangeeft dat de persoon niet geinteresseerd is. Een persoon kan zich ook maar eenmaal voor een workshop inschrijven. Indien deze nogmaals ingeschreven wordt, print dan dat dit niet mogelijk is.
* `update`: verwijder `Studenten` en `Instructeurs` uit de workshop als hun `interesses` of `skills` niet langer overeenkomen met het `onderwerp` van de workshop.
* `info`: print de algemene info van de workshop. Voor een voorbeeld zie **Voorbeeld info**.

```
Test de werking door de code onder "Testen van klasse Workshop" uit commentaar te halen.
```

### Voorbeeld info
```
Workshop - 12/03/2024 - HTML

Totaal aantal deelnemers: 4

Studenten
 1. Jane Doe - Python, HTML
 2. Lena Smith - HTML, C#

Instructors
 1. Vicky Ruby - HTML, JavaScript
 2. Nicole McMillan - HTML, Cobal
```

