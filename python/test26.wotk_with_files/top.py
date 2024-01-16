import csv
from statistics import mean

my_list_2 = []
my_list_3 = []
my_list_4 = []

with open('doc.csv') as f:
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

print(paired_list)

with open('doc2.csv', 'w', newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerows(paired_list)

#############################################################################
input_file_path = 'doc2.csv'    # Specify the path to your input CSV file
output_file_path = 'ali2.csv'  # Specify the path to your output CSV file
with open(input_file_path, 'r') as input_file:
    # Create a CSV reader object
    reader = csv.reader(input_file)
    
    # Sort rows based on the second column (numeric values)
    sorted_rows = sorted(reader, key=lambda row: float(row[1]))

# Write sorted data to output CSV file
with open(output_file_path, 'w', newline='') as output_file:
    # Create a CSV writer object
    writer = csv.writer(output_file)
    
    # Write sorted rows
    writer.writerows(sorted_rows)

print(f"Data has been sorted and written to {output_file_path}.")