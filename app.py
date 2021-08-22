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
    """
    Sort list data by requested column
    """
    print('\nThe field headings are:')

    for h in header:
        print(h)

    sort_by = input("\nEnter the heading you wish to sort by here: ")
    
    i = header.index(sort_by)
    data.sort(key=lambda x:x[i])
    return data

def leased_years(data):
    """
    Select list data for specific lease length
    """
    term = input("\nEnter the number of lease years: ")
    lease_data = [row for row in data if row[9] == int(term)]
    return 
    
def calc_rent(data):
    """
    Calculate the total rent for all list data for  
    specfic lease length
    """
    total=0
    for row in data:
        total += float(row[10])

    return total


def count_masts(data):
    tenants = [row[0] for row in data ]
    
    count = [[name, tenants.count(name)] for name in set(tenants)]
    return count
    # print(tenants)


def main():
    
    mast_data_list, headings = load_data()

    # print("\nThis is the first 5 items from the csv file after loading into a list:")
    # print(mast_data_list[:5])
    
    # sorted_list = sort_data(mast_data_list, headings)
    # print("This are the first 5 items from the sorted list:")
    # print(sorted_list[:5])

    # lease_list = leased_years(mast_data_list) 
    # print("\nThis is a list of all the items for the above number of lease years")
    # print(lease_list)

    # total_rent = calc_rent(lease_list)
    # print(f"\nThe total rent for these items is: £{total_rent:.2f}")

    mast_counts = count_masts(mast_data_list)
    print("\nThese are the number of masts for each tenant")
    for count in mast_counts:
        print(count[0] + 'has ' + str(count[1]) + ' masts.')

    



main()