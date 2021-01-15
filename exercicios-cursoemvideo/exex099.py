def maior(*args):
    mai = 0
    for num in args:
        if num > mai:
            mai = num
    print(f'O maior número entre \n{list(args)} é: {mai}')

maior(1, 3, 7, 4, 87, 323, 4, 12, 4354, 5)
maior(2, 4, 5, 6, 3, 4, 5, 9)