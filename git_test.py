
anmls = []
anmls.append('lion')
anmls.append('alligator')
anmls.append('bear')



areas = []
areas.append('wooded')
areas.append('rocky')
areas.append('watering hole')

options = []
options.append('pick')
options.append('send')


def lolo():
    if lo_lo.lower() == 'wooded':
        print(f'\n{option.title()} is walking through the woods.\n')
        
    if lo_lo.lower() == 'rocky':
        print(f'\n{option.title()} is climbing over the rocks.\n')
        
    if lo_lo.lower() == 'watering hole':
        print(f'\n{option.title()} is swimming across the watering hole.\n')
    
    

while True:
    Begin = input('Begin?\nYes or No\n\n')
    if Begin.lower() == 'yes':
        print('\n~~~~~~~~~~~~~~~~~~~~')
        print('\n\nTHE HUNT: Safari Survival\n\n')
        print('~~~~~~~~~~~~~~~~~~~~\n')
    elif Begin.lower() == 'no':
        quit()
    else:
        print('\nInvalid Response.\nTry Again\n')
        continue



    while True:       
        print('Lion\nBear\nAlligator')
        print('^^^^^^^^^^')
        option = input('\nPick Your Animal.\n\n')
        if option == 'back':
            break

        if option.lower() == anmls[0]:
            print('\nWooded\nRocky\nWatering Hole\n')            
            lo_lo = input('What map?\n')
            lolo()

        if option.lower() == anmls[1]:
            print('\nWooded\nRocky\nWatering Hole\n')
            lo_lo = input('\nWhat map?\n')
            lolo()

        if option.lower() == anmls[2]:
            print('\nWooded\nRocky\nWatering Hole\n')            
            lo_lo = input('\nWhat map?\n')
            lolo()

        else:
            lo_lo == 'back'
            quit()
        
        fin = input('\nDone?\n')
        if fin.lower() == 'yes':
            quit()
        else:
            break

       
            


               
        



    

