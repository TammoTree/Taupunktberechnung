import math

def Taupunkt(t, h):
    a1 = 7.45           #legt fest das die Temp über 0°C liegt
    b1 = 235
    temperatur = float(t)   #Die Temperatur als Gleitkommazahl ausgegeben z.b. 20 = 20.0
    luftfeuchtigkeit = float(h)     #Die Luftfeuchtigkeit als Gleitkommazahl ausgeben z.b. 60 = 60.0 (Sensoreingabe)

    #Saettigungsdampfdruck 
    x1=(a1*temperatur)/(b1+temperatur)
    saettigungsdampfdruck=(6.1*math.exp(x1*2.3025851))       #6.1 hoch ...
   

    #Dampfdruck
    e2=saettigungsdampfdruck*luftfeuchtigkeit/100
    x2=e2/6.1
    x3=0.434292289*math.log(x2)     #logorithmus naturales von x2
 

    #Taupunkttemperatur
    taupunkt=(235*x3)/(7.45-x3)*100
    taupunkt=math.floor(taupunkt)/100    #Abgerundete ganze Zahl vom Taupunkt 
    taupunkt =  "%02.2f" % (taupunkt)    #Gibt den Taupunkt mit 2 Kommazahlen an
    print(" Der Taupunkt befindet sich bei : "+taupunkt+" grad Celsius")
   
    return taupunkt     #schließt die Definition
Taupunkt(20, 45)





