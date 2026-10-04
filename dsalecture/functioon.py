def sumofeven(n: list)->int:

    sum = 0

    # for i in range(len(n)):
    #     if i % 2 == 0:
    #      sum += n[i]
    #     print(sum)

    for i in range(0, len(n), 3):
        sum += n[i]
    print(sum)

sumofeven([1, 5, 2,6,7,10,12])