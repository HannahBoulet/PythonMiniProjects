
def calcrealestate(size, type):
    propval = 0;
    if type == "city":
        propval = size * 250
        print(f'The estimated price for a {size}sq ft property in the {type} is: ${propval}')
    elif type == "suburb":
        propval = size * 150
        print(f'The estimated price for a {size}sq ft property in the {type} is: ${propval}')
    else:
        print("Error with type, only 2 valid types city and suburb")

if __name__ == '__main__':
    print("Welcome to the Real Estate Price Estimator")
    size = int(input("Enter the size of the property in square feet: "))
    type = input("Enter the location (city or suburb): ")
    calcrealestate(size, type)