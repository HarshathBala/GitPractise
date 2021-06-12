from nsetools import Nse

nse=Nse()

x=nse.get_quote("BATAINDIA")

print(x['open'])
