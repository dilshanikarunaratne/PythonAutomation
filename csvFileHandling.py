import csv

#reading csv file data
with open('C:/Users/Dilshani/PycharmProjects/PythonFiles/SalesJan2009.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        #getting the column names
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[1]} had sales of {row[2]} dollars via {row[3]} payment method in {row[5]} city.')
            line_count += 1

#writing data to csv file
with open('C:/Users/Dilshani/PycharmProjects/PythonFiles/food.csv', mode='w') as food_file:
    food_writer = csv.writer(food_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    food_writer.writerow(['Food item', 'Qty', 'Unit price'])
    food_writer.writerow(['Pizza', '15', '$16'])
    food_writer.writerow(['Fried rice', '45', '$10'])
    food_writer.writerow(['Noodles', '12', '$12'])

with open('C:/Users/Dilshani/PycharmProjects/PythonFiles/food.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)



with open('C:/Users/Dilshani/PycharmProjects/PythonFiles/food1.csv', mode='w') as food_file:
    food_writer = csv.writer(food_file, dialect='excel', delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    food_writer.writerow(['Food item', 'Qty', 'Unit price'])
    food_writer.writerow(['Pizza', '15', '$16'])
    food_writer.writerow(['Fried rice', '45', '$10'])
    food_writer.writerow(['Noodles', '12', '$12'])


#write a csv file with a list
row_list = [["Food item", "Qty", "Unit price"],
             ["Pizza", "15", "$16"],
             ["Fried rice", "45", "$10"],
             ["Noodles", "12", "$12"]]

with open('food2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)

#write a csv file including quoted data
row_list1 = [
    ["row", "TV show", "Quote"],
    [1, "Friends", "We were on a break"],
    [2, "HIMYM", "Suit up!"],
    [3, "Big Bang Theory", "Bazinga"]
]
with open('quotes.csv', 'w', newline='') as file:
    writer1 = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=';')
    writer1.writerows(row_list1)

#Write a CSV files with custom quoting character
row_list2 = [
    ["row", "TV show", "Quote"],
    [1, "Friends", "We were on a break"],
    [2, "HIMYM", "Suit up!"],
    [3, "Big Bang Theory", "Bazinga"]
]
with open('quotes1.csv', 'w', newline='') as file:
    writer2 = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=',', quotechar='*')
    writer2.writerows(row_list2)

