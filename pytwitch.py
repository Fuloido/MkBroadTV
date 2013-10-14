import httplib
import json
con = httplib.HTTPConnection("api.justin.tv",80)
con.request("GET","/api/stream/list.json?limit=100&offset=0")
response = con.getresponse()

#print response.read()


if response.status == 200:
    jsondata = response.read();
	
    users = json.loads(jsondata)
    for user in users:
	#print user
	#print "-------------------------------------------------------------------------------------------------"
        #print user['channel']['login'] + ' - ' + user['stream_count'] + "Viewers"
	print user['name'] + ' - ' + user['title'] + ' - ', user['stream_count'], "Viewers - " + user['channel']['channel_url']


