from Assignment import *


def check_towns(towns):
	towns_data = ['TOA PAYOH', 'CHOA CHU KANG', 'BUKIT TIMAH', 'YISHUN', 'QUEENSTOWN', 'HOUGANG', 'JURONG WEST', 'WOODLANDS', 'CLEMENTI', 'PUNGGOL', 'BEDOK', 'PASIR RIS', 'BUKIT MERAH', 'SERANGOON', 'MARINE PARADE', 'ANG MO KIO', 'BUKIT PANJANG', 'BUKIT BATOK', 'KALLANG/WHAMPOA', 'BISHAN', 'CENTRAL AREA', 'SEMBAWANG', 'GEYLANG', 'TAMPINES', 'SENGKANG', 'JURONG EAST']
	towns_data = set(towns_data)
	towns = set(towns)
	return towns == towns_data


def check_flat_types(flat_types):
	flat_types_data = ['2 ROOM', '1 ROOM', '4 ROOM', '3 ROOM', '5 ROOM', 'EXECUTIVE', 'MULTI-GENERATION']
	flat_types_data = set(flat_types_data)
	flat_types = set(flat_types)
	return flat_types == flat_types_data


def check_flat_models(flat_models):
	flat_models_data = ['TYPE S2', 'MODEL A2', '3GEN', 'IMPROVED', 'STANDARD', 'APARTMENT', '2-ROOM', 'MAISONETTE', 'MODEL A-MAISONETTE', 'TYPE S1', 'TERRACE', 'MULTI GENERATION', 'NEW GENERATION', 'PREMIUM APARTMENT LOFT', 'MODEL A', 'SIMPLIFIED', 'DBSS', 'PREMIUM APARTMENT', 'ADJOINED FLAT']
	flat_models_data = set(flat_models)
	flat_models = set(flat_models)
	return flat_models == flat_models_data


def main():
	counter = 0
	app = HDB_Resale_Admin()
	app.load()
	print("Test get_town():")
	if(check_towns(app.get_town())):
		counter += 1
	print("Test get_flat_type():")
	if(check_flat_types(app.get_flat_type())):
		counter += 1
	print("Test get_flat_model():")
	if(check_flat_models(app.get_flat_model())):
		counter += 1

	print("Test search with different combinations - single value each:")
	print("Town - QUEENSTOWN")
	r = app.search(town=["QUEENSTOWN"])
	if(len(r) == 220):
		counter += 1

	print("Town - QUEENSTOWN flat_type=4 ROOM")
	r = app.search(town=["QUEENSTOWN"], flat_type=["4 ROOM"])
	if(len(r) == 83):
		counter += 1

	print("Town - QUEENSTOWN flat_model=MODEL A")
	r = app.search(town=["QUEENSTOWN"], flat_model=["MODEL A"])
	if(len(r) == 87):
		counter += 1

	print("Town - QUEENSTOWN price_psf=500")
	r = app.search(town=["QUEENSTOWN"], price_psf=500)
	if(len(r) == 202):
		counter += 1

	print("Town - QUEENSTOWN flat_type=4 ROOM flat_model=MODEL A")
	r = app.search(town=["QUEENSTOWN"], flat_type=["4 ROOM"], flat_model=["MODEL A"])
	if(len(r) == 61):
		counter += 1

	print("Town - QUEENSTOWN  flat_type=4 ROOM price_psf=500")
	r = app.search(town=["QUEENSTOWN"], flat_type=["4 ROOM"], price_psf=500)
	if(len(r) == 82):
		counter += 1

	print("Town - QUEENSTOWN flat_model=MODEL A price_psf=500")
	r = app.search(town=["QUEENSTOWN"], flat_model=["MODEL A"], price_psf=500)
	if(len(r) == 87):
		counter += 1

	print("Town - QUEENSTOWN flat_type=4 ROOM flat_model=MODEL A price_psf=1000")
	r = app.search(town=["QUEENSTOWN"], flat_type=["4 ROOM"], flat_model=["MODEL A"], price_psf=1000)
	if(len(r) == 6):
		counter += 1

	print()
	print("#" * 30)
	print("Test search with different combinations - two values eac:")
	print("Town - QUEENSTOWN, BUKIT MERAH")
	r = app.search(town=["QUEENSTOWN", "BUKIT MERAH"])
	if(len(r) == 569):
		counter += 1

	print("Town - QUEENSTOWN,BUKIT MERAH  flat_type=4 ROOM, 5 ROOM")
	r = app.search(town=["QUEENSTOWN", "BUKIT MERAH"], flat_type=["4 ROOM", "5 ROOM"])
	if(len(r) == 316):
		counter += 1

	print("Town - QUEENSTOWN,BUKIT MERAH  flat_model=MODEL A,IMPROVED")
	r = app.search(town=["QUEENSTOWN", "BUKIT MERAH"], flat_model=["MODEL A", "IMPROVED"])
	if(len(r) == 440):
		counter += 1

	print("Town - QUEENSTOWN,BUKIT MERAH price_psf=900")
	r = app.search(town=["QUEENSTOWN", "BUKIT MERAH"], price_psf=900)
	if(len(r) == 174):
		counter += 1

	print("Town - QUEENSTOWN,BUKIT MERAH  flat_type=4 ROOM,5 ROOM flat_model=MODEL A,IMPROVED")
	r = app.search(town=["QUEENSTOWN", "BUKIT MERAH"], flat_type=["4 ROOM", "5 ROOM"], flat_model=["MODEL A", "IMPROVED"])
	if(len(r) == 266):
		counter += 1

	print("Town - QUEENSTOWN,BUKIT MERAH  flat_type=4 ROOM, 5 ROOM price_psf=900")
	r = app.search(town=["QUEENSTOWN", "BUKIT MERAH"], flat_type=["4 ROOM", "5 ROOM"], price_psf=900)
	if(len(r) == 124):
		counter += 1

	print("Town - QUEENSTOWN,BUKIT MERAH  flat_model=MODEL A,IMPROVED price_psf=500")
	r = app.search(town=["QUEENSTOWN", "BUKIT MERAH"], flat_model=["MODEL A", "IMPROVED"], price_psf=500)
	if(len(r) == 421):
		counter += 1

	print("Town - QUEENSTOWN,BUKIT MERAH  flat_type=4 ROOM, 5 ROOM flat_model=MODEL A,IMPROVED price_psf=1000")
	r = app.search(town=["QUEENSTOWN", "BUKIT MERAH"], flat_type=["4 ROOM", "5 ROOM"], flat_model=["MODEL A", "IMPROVED"], price_psf=1000)
	if(len(r) == 30):
		counter += 1

	#continue to built the test cases on your own.

	#different combination of search to test
	#town - done above
	#town, flat_type - done above
	#town, flat_model - done above
	#town, price_psf - done above

	#town, flat_type, flat_model - done above
	#town, flat_type, price_psf - done above
	#town, flat_model, price_psf - done above

	#town, flat_type, flat_model, price_psf - done above

	#flat_type
	#flat_type, flat_model
	#flat_type, price_psf
	#flat_type, flat_model, price_psf

	#flat_model
	#flat_model,price_psf

	#price_psf

	print("#" * 30)
	print("Test search with no results:")
	print("Town - ABC")
	r = app.search(town=["ABC"])
	if(len(r) == 0):
		counter += 1

	print("Town - QUEENSTOWN flat_type=10 ROOM")
	r = app.search(town=["QUEENSTOWN"], flat_type=["10 ROOM"])
	if(len(r) == 0):
		counter += 1

	print("Town - QUEENSTOWN flat_type=4 ROOM flat_model=MODEL D")
	r = app.search(town=["QUEENSTOWN"], flat_type=["4 ROOM"], flat_model=["MODEL D"])
	if(len(r) == 0):
		counter += 1

	print("Town - QUEENSTOWN  flat_type=4 ROOM flat_model=MODEL A price_psf=2000")
	r = app.search(town=["QUEENSTOWN"], flat_type=["4 ROOM"], flat_model=["MODEL A"], price_psf=2000)
	if(len(r) == 0):
		counter += 1

	print(f"Test cases passed:{counter}")


if __name__ == "__main__":
	main()

#Note I did not write the test case for log file:
#The expected output for the log file is
#Log file name: ErrorLog.txt
"""
File line 10: Invalid resale_price:-10.0
File line 11: Invalid floor_area_sqm:BIG
File line 14: Invalid floor_area_sqm:5X
File line 17: Invalid resale_price:-200000.0
File line 21: Invalid resale_price:Expensive
"""

#Note the floor_area in data file is sqm
#the price required is in sqf
#1 sqm = 10.76391041671 sqf

#Expected output
"""
Test get_town():
Test get_flat_type():
Test get_flat_model():
Test search with different combinations - single value each:
Town - QUEENSTOWN
Town - QUEENSTOWN flat_type=4 ROOM
Town - QUEENSTOWN flat_model=MODEL A
Town - QUEENSTOWN price_psf=500
Town - QUEENSTOWN flat_type=4 ROOM flat_model=MODEL A
Town - QUEENSTOWN  flat_type=4 ROOM price_psf=500
Town - QUEENSTOWN flat_model=MODEL A price_psf=500
Town - QUEENSTOWN flat_type=4 ROOM flat_model=MODEL A price_psf=1000

##############################
Test search with different combinations - two values eac:
Town - QUEENSTOWN, BUKIT MERAH
Town - QUEENSTOWN,BUKIT MERAH  flat_type=4 ROOM, 5 ROOM
Town - QUEENSTOWN,BUKIT MERAH  flat_model=MODEL A,IMPROVED
Town - QUEENSTOWN,BUKIT MERAH price_psf=900
Town - QUEENSTOWN,BUKIT MERAH  flat_type=4 ROOM,5 ROOM flat_model=MODEL A,IMPROVED
Town - QUEENSTOWN,BUKIT MERAH  flat_type=4 ROOM, 5 ROOM price_psf=900
Town - QUEENSTOWN,BUKIT MERAH  flat_model=MODEL A,IMPROVED price_psf=500
Town - QUEENSTOWN,BUKIT MERAH  flat_type=4 ROOM, 5 ROOM flat_model=MODEL A,IMPROVED price_psf=1000
##############################
Test search with no results:
Town - ABC
Town - QUEENSTOWN flat_type=10 ROOM
Town - QUEENSTOWN flat_type=4 ROOM flat_model=MODEL D
Town - QUEENSTOWN  flat_type=4 ROOM flat_model=MODEL A price_psf=2000
Test cases passed:23
"""
