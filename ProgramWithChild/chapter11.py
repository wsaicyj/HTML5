import easygui

# numBlocks = easygui.integerbox('你想要多少块?')
# numLines = easygui.integerbox('你想要打印多少行?')
# numStars = easygui.integerbox('你想要多少颗星星?')

# for block in range(0,numBlocks):
#     for line in range(0,numLines):
#         for start in range(0,numStars):
#             print('*',end=' ')
#         print()
#     print()

# for block in range(1,numBlocks + 1):
#     for line in range(1,block * 2):
#         for star in range(1,(block + line) * 2):
#             print('*',end=' ')
#         print()
#     print()

count = 1
dog_cal = 140
bun_cal = 120
ket_cal = 80
mus_cal = 20
onion_cal = 40
print('\t\tDog\tBun\tKetchup\tMustard\tonions\tCalories')
for dog in [0,1]:
    for bun in [0,1]:
        for ketchup in [0,1]:
            for mustard in [0,1]:
                for onion in [0,1]:
                    # print('#',count,'\t')
                    # print('\t\t', 'dog', '\t', 'bun', '\t', 'ketchup', '\t', 'mustard', '\t', 'onion')
                    total_cal = (bun * bun_cal) + (dog * dog_cal) + \
                                (ketchup * ket_cal) + (mustard * mus_cal) + \
                                (onion * onion_cal)
                    print('#',count,'\t',dog,'\t',bun,'\t',ketchup,'\t\t',mustard,'\t\t',onion,'\t\t',total_cal)
                    # print(mustard,'\t',onion)
                    count += 1