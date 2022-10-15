from django.shortcuts import render


def home(request):
	import json
	import requests

	if request.method == 'POST':
		zipcode = request.POST['zipcode']
		
		api_request = requests.get(f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zipcode}&distance=5&API_KEY=9D91C779-69BB-4159-AEAE-4AB61D19DE2F")

		try:
			# see if api_request was successful and holds valid info
			api = json.loads(api_request.content)
		except Exception as e:
			api = 'Error...'

		if api[0]['Category']['Name'] == 'Good':
			category_description = '0-50 Air quality is considered satisfactory, and air polution poses little or no risk'
			category_color = 'good'
		elif api[0]['Category']['Name'] == 'Moderate':
			category_description = "51-100 Air qualiti is acceptable, however, for some polutants" 
			category_color = 'moderate'
		elif api[0]['Category']['Name'] == 'USG':
			category_description = 'Air is somewhat poluted'
			category_color = 'usg'
		elif api[0]['Category']['Name'] == 'Unhealthy':
			category_description = 'The air is unhealthy'
			category_color = 'unhealthy'
		elif api[0]['Category']['Name'] == 'Very Unhealthy':
			category_description = 'Very Unhealthy!'
			category_color = 'veryunhealthy'
		elif api[0]['Category']['Name'] == 'Hazardous':
			category_description = 'Hazardous!!!!!!'
			category_color = 'hazardours'

		return render(request, 'home.html', {'api': api,
			'category_description': category_description,
			'category_color': category_color})


	elif request.method == "GET":
		
		api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=9D91C779-69BB-4159-AEAE-4AB61D19DE2F")
		try:
			# Json to parse the received info into json
			api = json.loads(api_request.content)
		except Exception as e:
			api = 'Error...'


		if api[0]['Category']['Name'] == 'Good':
			category_description = '0-50 Air quality is considered satisfactory, and air polution poses little or no risk'
			category_color = 'good'
		elif api[0]['Category']['Name'] == 'Moderate':
			category_description = "51-100 Air qualiti is acceptable, however, for some polutants" 
			category_color = 'moderate'
		elif api[0]['Category']['Name'] == 'USG':
			category_description = 'Air is somewhat poluted'
			category_color = 'usg'
		elif api[0]['Category']['Name'] == 'Unhealthy':
			category_description = 'The air is unhealthy'
			category_color = 'unhealthy'
		elif api[0]['Category']['Name'] == 'Very Unhealthy':
			category_description = 'Very Unhealthy!'
			category_color = 'veryunhealthy'
		elif api[0]['Category']['Name'] == 'Hazardous':
			category_description = 'Hazardous!!!!!!'
			category_color = 'hazardours'
	    		

		return render(request, 'home.html', {'api': api,
			'category_description': category_description,
			'category_color': category_color})

def about(request):
	return render(request, 'about.html', {})