import csv
from datetime import datetime

def load_data():
    """
    Load the csv data into a list with fields as correct type
    """
    file = open('mobile-phone-masts-uk.csv')
    reader = csv.reader(file)
    header = next(reader)
    print(header)

    mast_data =[]

    for row in reader:
        print(row)
        mast_data.append([
        row[0],
        row[1],
        row[2],
        row[3],  
        row[4],
        row[5],
        row[6],
        datetime.strptime(row[7], '%d %b %Y'), 
        datetime.strptime(row[8], '%d %b %Y'),
        int(row[9]),
        float(row[10])])
        
        # mast_data.append()
        print(mast_data)

    print(mast_data)
    return(mast_data, header)

def sort_data(data, header):
    print('The field headings are:')

    for h in header:
        print(h)
        
    sort_by = input("Enter the heading you wish to sort by here: ")
    
    i = header.index(sort_by)
    data.sort(key=lambda x:x[i])
    return data

def get_sort_criteria(header):
    
    
    return header(sort_by)

def main():
    
    mast_data_list, headings = load_data()

    print("This is the first 5 items from the csv file after loading into a list:")
    print(mast_data_list[:5])
    
    sorted_list = sort_data(mast_data_list, headings)
    print("This are the first 5 items from the sorted list:")
    print(sorted_list[:5])


main()