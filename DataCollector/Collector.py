import urllib2


class Collector:

	urlname=     #give the url of the website

	dollar_value=0
	ruppee_value=0
	sensex_value=0
	crudeOil_value=0
	gold_value=0

	def __init__(self):t
		global response  # for global variables to access across function 
		global html
		response=urllib2.urlopen(urlname)
		html=response.read()
	
	

		
