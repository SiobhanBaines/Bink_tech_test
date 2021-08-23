import csv
from datetime import datetime


def load_data():
    """
    Load the csv data into a list with fields as correct type
    """
    file = open('mobile-phone-masts-uk.csv')
    reader = csv.reader(file)
    header = next(reader)

    mast_data =[]

    for row in reader:
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
    return lease_data
    
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
    """
    List tenants and the number of masts they have
    """
    input("\nPress Enter to display the number of masts each tenant has: ")
    tenants = [row[0] for row in data ]
    
    count = [[name, tenants.count(name)] for name in set(tenants)]
    return count


def lease_date(data):
    """
    List of all tenants within a specfic date range
    """
    from_date= input("\nPlease enter a lease from date in dd/mm/yyyy: ")
    to_date = input("\nPlease enter a lease to date in dd/mm/yyyy: ")
    f_date = datetime.strptime(from_date, '%d/%m/%Y')
    t_date = datetime.strptime(to_date, '%d/%m/%Y')
    for mast in data:
        if f_date <= mast[7] <= t_date:
            start_date = datetime.strftime(mast[7], "%d/%m/%Y")
            end_date = datetime.strftime(mast[8], "%d/%m/%Y")
            print('\nProperty Name:    ', mast[0],
                '\nProperty Address: ', mast[1], 
                '\n                  ', mast[2],
                '\n                  ', mast[3], 
                '\n                  ', mast[4], 
                '\nUnit Name:        ', mast[5], 
                '\nTenant Name:      ', mast[6], 
                '\nLease Date Start: ', start_date, 'End: ', end_date,  
                '\nLease Years:      ', mast[9], 
                '\nCurrent Rent:     ', mast[10])

def main():
    """
    this is where all the other functions are run
    """
    
    mast_data_list, headings = load_data()

    print("\nThis is the first 5 items from the csv file after loading into a list:")
    print(mast_data_list[:5])
    
    sorted_list = sort_data(mast_data_list, headings)
    print("This are the first 5 items from the sorted list:")
    print(sorted_list[:5])

    lease_list = leased_years(mast_data_list) 
    print("\nThis is a list of all the items for the above number of lease years")
    print(lease_list)

    total_rent = calc_rent(lease_list)
    print(f"\nThe total rent for these items is: £{total_rent:.2f}")

    mast_counts = count_masts(mast_data_list)
    print("\nThese are the number of masts for each tenant")
    for count in mast_counts:
        print(f'Property Name: {count[0]} has {str(count[1])} masts.')

    lease_date(mast_data_list)

main()