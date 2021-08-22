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

    return(mast_data)

def main():
    print('line 34')
    mast_data_list = load_data()
    print("This is the data from the csv file:")
    print(mast_data_list[:5])

main()