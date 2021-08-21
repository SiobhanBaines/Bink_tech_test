import csv

with open('mobile-phone-masts-uk.csv') as file:
    mast_data = csv.DictReader(file)
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
