bank1=['Tiger', 'Grass', 'Goat']
bank2=[]
bank1.remove('Goat')
bank2.append('Goat')
print("1st trip of farmer")
print(bank1,'|         |',bank2)
bank1.remove('Grass')
bank2.append('Grass')
print("\n2nd trip of farmer")
print(bank1,'|         |',bank2)
bank2.remove('Goat')
bank1.append('Goat')
print("\n3rd trip of farmer")
print(bank1,'|         |',bank2)
bank1.remove('Tiger')
bank2.append('Tiger')
print("\n4th trip of farmer")
print(bank1,'|         |',bank2)
bank1.remove('Goat')
bank2.append('Goat')
print(bank2)
