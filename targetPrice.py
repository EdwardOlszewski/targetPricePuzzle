import itertools
import json
import os
from decimal import Decimal

def targetPriceFinder(jsonList, targetPrice):
    # Declare priceList list
    pricesList = []
    matchFound = False
    # Add the 'Items' from jsonList
    for item in jsonList['Items']:
        pricesList.append(Decimal(item['Price'][1:]))
    # Create sets of the different combination of prices
    for i in range (len(pricesList)):
        for subSet in itertools.combinations(pricesList, i,):
            if(sum(subSet) == targetPrice):
                matchFound = True
                dishFinder(jsonList, subSet, targetPrice)
            else:
                continue
    if not matchFound:
        print('\n   No combination of dishes equal $' + str(targetPrice))

def dishFinder(jsonList, targetPriceList, targetPrice):
    print('\n   The dishes that equal $' + str(targetPrice) + ' are ')
    # get every item in the jsonList
    for item in jsonList['Items']:
        # get every price in the pricesList
        for i in range ((len(targetPriceList))):
            # if the price in the jsonList is the same as a price from the targetPriceList print it
            if(Decimal(item['Price'][1:]) == targetPriceList[i]):
                # print the dish
               print('   ' ,str(i+1) + ')', item['Name'], item['Price'])
               break
            else:
                continue 

def main():
    jsonFileName = ''
    while jsonFileName != 'quit':
        # Ask user for file name
        jsonFileName = input("\n > Enter the json file name without extension or 'quit' to quit: ").lower()

        # Dictionary holding .json file values
        JSON_FILE = [] 
       
        # Path to the .json file
        CWD = os.getcwd() # returns current working directory
        JSON_FILE_PATH = '%s/%s' % (CWD, jsonFileName + '.json')

        # Open .json file, parse values and store them in the dictionary
        try: 
            with open(JSON_FILE_PATH) as data_file:
                JSON_FILE = json.load(data_file)
        except IOError:
            print ('\n   ERROR:',  jsonFileName + '.json', 'does not exist.')
            continue
        except ValueError:  
            print ('\n   ERROR:', jsonFileName + '.json', 'is an empty file.')
            continue
      
        # Get the target price from the .json file
        targetPrice = Decimal(JSON_FILE['Target Price'][1:])

        # Call targetPriceFinder function sending it the dictionary and the target price
        targetPriceFinder(JSON_FILE, targetPrice) 

if __name__ == "__main__": main()
# end of file    