import requests
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option("max_colwidth", None)


url = #Rapid API url here#

querystring = {"location":"long beach, ca",
			   "home_type":"Houses",
			   "minPrice":"100000",
			   "maxPrice":"1000000"}

headers = {
	#rapid api header here#
	#rapid api key here#
}

detail_cols = ['address',
			   'price',
			   'imgSrc']

for_sale_response = requests.request("GET", url, headers=headers, params=querystring)

for_sale_response = for_sale_response.json()
data_for_sale = pd.json_normalize(data=for_sale_response['props'])
app_data_for_sale = data_for_sale[detail_cols]
app_data_for_sale.to_csv("house_data.csv")

#print("num of rows: ", len(data_for_sale))
#print("num of cols: ", len(data_for_sale.columns))
#print(app_data_for_sale.head())
