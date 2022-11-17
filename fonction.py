def process(data):
    data[1]=2
    return data[-2]
measurements=[0 for i in range (3)]
print(measurements)
process(measurements)
print(measurements)
