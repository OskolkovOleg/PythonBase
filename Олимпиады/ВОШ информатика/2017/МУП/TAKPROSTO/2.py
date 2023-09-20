with open('1.txt', 'r') as file:
    ArrText = file.readlines()

with open('Otvet.txt', 'a') as file:
    for text in ArrText:
        if '\n' in text:
            text = text.replace('\n', '')
        numbs = text.split(' ')
        numbs = [int(i)**3 for i in numbs]

        numbs = [str(i) for i in numbs]
        file.write(f'{" ".join(numbs)}\n')
        
