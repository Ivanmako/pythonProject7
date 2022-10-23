word_l = input().split()
main_l = [[]]
for i in range(1, len(word_l) + 1):
    for j in range(len(word_l)):
        main_l.append(word_l[j:j + i])
print(main_l)