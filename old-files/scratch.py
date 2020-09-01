total = dict()
counter=0
randset = {'test', 'words', 'test', 'Test'}
for word in randset:
    counter+=1
    if word in total:
        total[word] += 1
    elif word not in total:
        total.update({f'{counter}' : f'{word}'})
print(total)
