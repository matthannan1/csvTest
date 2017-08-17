mainDict = {"Matt": {'age':48, 'eyes':'green'},
            "Jenny": {'age':45, 'eyes':'hazel'},
            "Calin": {'age':5, 'eyes':'blue'}}

run = True

while run:
    userInput = raw_input("Press 1 for ages, 2 for eyes, 3 for all, or 4 to end: ")

    if userInput == '4':
        run = False

    else:
        print

        for k, v in mainDict.items():
            print k
            details = mainDict[k]
            if userInput == '1':
                print "Age:  ", details.get('age')

            if userInput == '2':
                print "Eyes: ", details.get('eyes')

            if userInput == '3':
                print "Age:  ", details.get('age')
                print "Eyes: ", details.get('eyes')

            print
