#HotDog
dog_cal = 140
bun_cal = 120
mus_cal = 20
ket_cal = 80
onion_cal = 40

print('\tСосиски \tБулочка \tКетчуп \tГорчица \tЛук \tКалории')
count = 1
for dog in [0, 1]:
    for bun in [0, 1]:
        for ketchup in [0, 1]:
            for mustard in [0, 1]:
                for onion in [0, 1]:
                    tot_cal = (dog * dog_cal) + (bun * bun_cal) + \
                              (mustard * mus_cal) + (ketchup * ket_cal) + \
                              (onion * onion_cal)
                    print('#', count, '\t'),
                    print(dog, '\t', bun, '\t', ketchup, '\t'),
                    print(mustard, '\t', onion),
                    print('\t', tot_cal)
                    count += 1

