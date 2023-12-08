import csv

def open_csv_file(file_name) -> []:
    print("Opened a new csv file: " + str(file_name))
    # initializing the titles and rows list
    fields = []
    rows = []
    
    # reading csv file
    with open(file_name, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        
        # extracting field names through first row
        fields = next(csvreader)
    
        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
    
        # get total number of rows
        print("Total no. of rows: %d"%(csvreader.line_num))
    
    # printing the field names
    print('Field names are:' + ', '.join(field for field in fields))
    print('\n')
    return [fields, rows]