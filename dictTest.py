mainDict = {'name': "Matt", 'age':48, 'eyes':'green'}

run = True
x = 1
while run:
    a_dict = {x:x}
    x=x+1
    # team = dict(team_a.items() + team_b.items())
    mainDict= dict(mainDict.items() + a_dict.items())
    print len(mainDict)
    userInput = raw_input("Keep going? ")
    if userInput == 'n':
        run = False
print mainDict

# Keep going? y
# 10
# Keep going? n
# {1: 1, 2: 2, 3: 3, 4: 4, 'name': 'Matt', 6: 6, 7: 7, 'age': 48, 'eyes': 'green', 5: 5}