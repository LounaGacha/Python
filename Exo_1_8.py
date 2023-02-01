a=0
b=0
c=0
d=0
liste = [a,b,c,d]



for liste[0] in range(1,10):
    for liste[1] in range(1, 10):
        for liste[2] in range(1, 10):
            for liste[3] in range(1, 10):
                if liste[:2] + liste[3:] == liste[2:4]:
                    print("Les nombre vérifiant la propriété : ab + cd = bc" )
                    print("Sont : ", str(a),str(b),str(c),str(d))



