import csv
# For the average
from statistics import mean 

def calculate_averages(input_file_name, output_file_name):
    
    my_list_2 = []
    my_list_3 = []
    my_list_4 = []

    with open(input_file_name) as f:
        reader = csv.reader(f)
        for row in reader:
            my_list = row[1:]
            my_list_3.append(row[0])
            total = sum(map(float, my_list))
            average = total / len(my_list)
            my_list_2.append(str(average))

    for j in range(0, len(my_list_2)):
        my_list_4.append(str(my_list_3[j]))
        my_list_4.append(str(my_list_2[j]))

# Reshape the list to pair elements for writing to CSV
    paired_list = list(zip(my_list_4[::2], my_list_4[1::2]))

#    print(paired_list)

    with open(output_file_name, 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(paired_list)

def calculate_sorted_averages(input_file_name, output_file_name):

    with open(input_file_name, 'r') as input_file:
# Create a CSV reader object
        reader = csv.reader(input_file)
    
# Sort rows based on the second column (numeric values)
        sorted_rows = sorted(reader, key=lambda row: float(row[1]))

# Write sorted data to output CSV file
    with open(output_file_name, 'w', newline='') as output_file:
# Create a CSV writer object
        writer = csv.writer(output_file)
    
# Write sorted rows
        writer.writerows(sorted_rows)

#print(f"Data has been sorted and written to {output_file_path}.")    


def calculate_three_best(input_file_name, output_file_name):
    


#def calculate_three_worst(input_file_name, output_file_name):
    


#def calculate_average_of_averages(input_file_name, output_file_name):


calculate_averages('doc.csv','ali.csv')    
calculate_sorted_averages('ali.csv','ali2.csv')