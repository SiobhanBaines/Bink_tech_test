import csv
from datetime import datetime

def load_data():
    """
    Load the csv data into a list with fields as correct type
    """
    file = open('uk-mast-data.csv')
    reader = csv.reader(file)

    header = next(reader)
    print(header)

    mast_data =[]

    for row in reader:
    property_name = row[0],
    property_address_1 = row[1],
    property_address_2 = row[2],
    property_address_3 = row[3],  
    property_address_4 = row[4],
    unit_name = row[5],
    tenant_name = row[6],
    lease_start_date = datetime.strptime(row[7], '%d %b %Y'), 
    lease_end_date = datetime.strptime(row[8], '%d %b %Y'),
    lease_years = int(row[9]),
    current_rent = float(row[10])
    
    mast_data.append([property_name, property_address_1, property_address_3, property_address_4, unit_name, tenant_name, lease_start_date, lease_end_date, lease_years, current_rent])

    print("This is the data from the csv file:")

    print(masts[0])


    sorted_mast = sorted(mast_data, key=lambda row: (row['Current Rent']))
    # print(sorted_mast)
    # print('line 12', list(sorted_mast))
    # Sorted except the last 2 records should be at the beginning


    # print first 5 records to console
    print('\nThis is the first 5 records of the list sorted by "Current Rent":\n')
    count=0
    for row in sorted_mast:
        count += 1
        if count <= 5:
            print(count, row)
    print('\nThese are the records where the lease is 25 years:\n')
    lease_data = [row for row in sorted_mast if row.get('Lease Years') =='25']
    print(lease_data)

    # total of rent for lease_data
    print(type(lease_data))
    total=0
    for row in lease_data:
        rent = row.get('Current Rent')

        total += float(rent)

    print(f'\nThe total value of rent where the lease is 25 years is £{total:.2f}')    
