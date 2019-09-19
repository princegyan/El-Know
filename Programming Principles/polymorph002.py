class Ghana(): 
	def capital(self): 
		print("Accra is the capital of Ghana.") 

	def language(self): 
		print("English the primary language of Ghana.") 

	def type(self): 
		print("Ghana is a developing country.") 

class USA(): 
	def capital(self): 
		print("Washington, D.C. is the capital of USA.") 

	def language(self): 
		print("English is the primary language of USA.") 

	def type(self): 
		print("USA is a developed country.") 

objectGhana = Ghana()
objectUSA = USA()
for country in (objectGhana, objectUSA): 
	country.capital() 
	country.language() 
	country.type() 
