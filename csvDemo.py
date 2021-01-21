import csv

with open('D:\\PYTHON\\API_Testing\\Utilities\\CSVFile.csv') as file:

    readers = csv.reader(file, delimiter=',')

    #print(list(readers))

    #list_reader = list(readers)

    name = []

    Status = []

    for row in readers:

        name.append(row[0])

        Status.append(row[1])

print(name)
print(Status)

with open('D:\\PYTHON\\API_Testing\\Utilities\\CSVFile.csv', 'a') as wFile:

    write = csv.writer(wFile)

    write.writerow(['sameer', 'rejected'])
