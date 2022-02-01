import requests
import json
import pandas as pd
import openpyxl

# 1. create url using app id and app key
# 2. request the created url
# 3. retrieve the recipe data json

def recipe_search(ingredient):
    app_id1 = "enter app id"                              
    app_key1 = "enter app key"     
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'
            .format( ingredient, app_id1, app_key1))
    data = result.json()
    return data['hits']


#Getting started with API data
#input ingredient
ingredient = input('Enter ingredients:')

#call recipe_search()
results = recipe_search(ingredient)

#loop retrieved data and extract label,url,totalWeight
for result in results:
    recipe = result['recipe']

    # print the Recipe title
    print(recipe['label'])
    # print the Original recipe URL
    print(recipe['url'])
    # print the Total weight, g
    print(recipe['totalWeight'])


#normalize json data into a flat table
df=pd.json_normalize(results)

#save data
df.to_excel('chefable.xlsx')




