with open(file1, 'r') as a:
    data_a = a.read()
    with open(file1, 'w')as a:
        a.write(data_b)
