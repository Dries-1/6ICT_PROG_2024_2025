""" Vraag aan een gebruiker hoeveel 2+2 is.
    
    Blijf deze vraag herhalen tot het correcte 
    antwoord gegeven wordt. Print "dat klopt".
    Stop hierna het programma.
    
    >>> Hoeveel is 2+2: 8
    >>> Hoeveel is 2+2: 3
    >>> Hoeveel is 2+2: 5
    >>> Hoeveel is 2+2: 4
    dat klopt
"""

while True:
    antwoord = int(input("Hoeveel is 2+2: "))
    
    if antwoord == 4:
        print("dat klopt")
        break  
