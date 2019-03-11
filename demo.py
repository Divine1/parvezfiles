import requests 

print ('start program')
apiKey = 'AIzaSyC1wjySMVuQxfl81yYtKaOq7mjtWEwOuGI'
searchEngineId = '008380015428355614352:wjfzvuqa4zy'
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
