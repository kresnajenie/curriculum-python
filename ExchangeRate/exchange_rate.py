# Python program to get the real-time 
# currency exchange rate 
import exchange as exc
import pytz
import requests, json 
import datetime
# Function to get real time currency exchange 

def utc_to_local(utc_dt):
	local_tz = pytz.timezone('Asia/Jakarta') #timezone jakarta
	local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz) #function to change timezone
	return local_tz.normalize(local_dt) # .normalize might be unnecessary

def aslocaltimestr(utc_dt):
    return utc_to_local(utc_dt).strftime('%H:%M:%S WIB') #format the output strucutre of the date

def RealTimeCurrencyExchangeRate(from_currency) : 
	# importing required libraries 
	to_currency = "IDR"

	# base_url variable store base url 
	base_url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE' # cara menggunakan api

	api_key = "RCBPGO0BOZ6KLM1Q"
	# main_url variable store complete url 
	main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key # query dari api pake api key

	# get method of requests module 
	# return response object 
	req_ob = requests.get(main_url) # di query pake function requests

	req_ob

	# json method return json format 
	# data into python dictionary data type. 
	
	# result contains list of nested dictionaries 
	result = req_ob.json() # hasil dari query diformat ke bentuk json
	a = result['Realtime Currency Exchange Rate'] #get the result dictionary
	froms = a['1. From_Currency Code'] #outputs the from currency code from the 'a' dictionary
	to = a['3. To_Currency Code'] #outputs the to currency code from the 'a' dictionary
	times = a['6. Last Refreshed'] #outputs when the last time it refreshed from the 'a' dictionary
	price_decimal = a['8. Bid Price'] #outputs bid price from the 'a' dictionary

	precision = 3 #how many decimal number
	price = str(
		("{:.{}f}".format( float(price_decimal), precision ))
	) #convert from many decimals to normal 

	formatfrom="%Y-%m-%d %H:%M:%S" #format date from this structure
	formatto="%H:%M:%S UTC"	#to this structure 
	time_utc = datetime.datetime.strptime(times,formatfrom) #using this function

	time_wib = (aslocaltimestr(time_utc)) # convert using the fuction aslocaltimestr form utc to wib


	ech = exc.Exchange(froms, to, time_wib, price) #inputs the parameters to the class
	return ech



