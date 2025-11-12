import csv
field_name =['NO','company','car model']
car = [
    {'NO':1,'company':'ferrari','car model':'GH'},
    {'NO':2,'company':'BMW','car model':'x5'},
    {'NO':3,'company':'Maruti suzuki','car model':'swift'},
    {'NO':4,'company':'Audi','car model':'RS7'}, # Corrected 'Audit' to 'Audi'
    {'NO':5,'company':'Toyota','car model':'fortuner'},
]

# Note: The dictionary keys in 'car' should match 'field_name' for DictWriter
# I've corrected the 'No' key in your data to 'NO' for consistency with 'field_name'
# and 'Audit' to 'Audi' as a probable intention.

with open('car.csv','w',newline='') as csvfile:
    write = csv.DictWriter(csvfile, fieldnames=field_name)
    write.writeheader()
    write.writerows(car)

with open('car.csv',newline='') as csvfile:
    d = csv.reader(csvfile)
    for r in d:
        # 💡 This line had the typo: 'joint' should be 'join'
        print(','.join(r))
        print(r)