##### PARAMETERS
# Input file
input_csv_file = 'C:/Users/GalliM29530/Downloads/Export.csv'
# Output file
output_csv_file = 'C:/Users/GalliM29530/Downloads/Conversion map.csv'
# Columns to preserve
columns_to_preserve_headers = ['ART_Key', 'ID']
#columns_to_preserve_excel_indices = ['I, C']





##### SCRIPT
# Import libraries
import csv
# Open the CSV file
with open(input_csv_file, 'r', encoding='utf-8') as input_file:
    # Initialise output variable
    output_csv_file_content = []
    # Read content
    csv_file_content = list(csv.reader(input_file))
    # Extract header (and discard it from the content)
    csv_header = csv_file_content[0]
    csv_file_content.remove(csv_header)
    # See the column positions of interest
    column_indices_to_preserve = []
    csv_header_columns_to_preserve = []
    for cp in columns_to_preserve_headers:
        for hd in range(len(csv_header)):
            if cp.lower() == csv_header[hd].lower():
               column_indices_to_preserve.append(hd) 
               csv_header_columns_to_preserve.append(csv_header[hd])
    # Go through the rows and select only the desired content (checking the columns to preserve)
    for row in csv_file_content:
        row_to_preserve = []
        for col in column_indices_to_preserve:
            for cl in range(len(row)):
                if cl == col:
                    row_to_preserve.append(row[cl])
        output_csv_file_content.append(row_to_preserve)
# Close the input file
input_file.close()
# Write the output file
with open(output_csv_file, 'w', encoding='utf-8', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(csv_header_columns_to_preserve)
    for row in output_csv_file_content:
        csv_writer.writerow(row)
# Close the output file
output_file.close()
