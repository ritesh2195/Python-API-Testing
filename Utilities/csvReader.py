import csv

with open('D:\\PYTHON\\API_Testing\\Utilities\\CSVFile.csv') as file:

    readers = csv.reader(file, delimiter=',')

    print(list(readers))

    list_reader = list(readers)

with open('D:\\PYTHON\\API_Testing\\Utilities\\CSVFile.csv', 'a') as wFile:
    write = csv.writer(wFile)

    write.writerow(['rajiv', 'rejected'])
