import exchange_rate as exch

country_list = ['USD','JPY','EUR','SGD','GBP']

for country in country_list:
app = exch.RealTimeCurrencyExchangeRate(country)

print('\nFrom: %s, To: %s, Bid Price: %s, Last Refreshed at %s' 
        % (app.getFrom(), app.getTo(), app.getPrice(), app.getTime()))

