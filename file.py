with open('./sample.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line)