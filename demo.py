import requests 

print ('start program')
apiKey = 'your api key'
searchEngineId = 'your searchengine id'
searchText = 'president of india'

apiUrl1 = 'https://www.googleapis.com/customsearch/v1?key={apiKey}&cx={searchEngineId}&q={searchText}'
apiUrl = 'https://www.googleapis.com/customsearch/v1'

PARAMS = {
    'key' : apiKey,
    'cx' : searchEngineId,
    'q' : searchText
}
r = requests.get(url = apiUrl, params = PARAMS) 
data = r.json() 

print (data['items'][0]['snippet'])

print ('end program')
