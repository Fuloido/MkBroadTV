import httplib
import json



channels= ['dragon', 'followgrubby', 'liquidret', 'mlgsc2', 'mtwdimaga', 'liquidtlo', 'ignproleague' ]

for channel in channels:
	con = httplib.HTTPConnection("api.justin.tv",80)
	con.request("GET","/api/stream/list.json?channel=" + channel)
	response = con.getresponse()

	if response.status == 200:
	    jsondata = response.read();
	
	    users = json.loads(jsondata)
	    for user in users:
		#print user
		#print "-------------------------------------------------------------------------------------------------"
	        #print user['channel']['login'] + ' - ' + user['stream_count'] + "Viewers"
		print user['name'] + ' - ' + user['title'] + ' - ', user['channel_count'], "Viewers - " + user['channel']['channel_url']
		print user['up_time'] + " - " + user['meta_game']
		print user['channel']['image_url_huge']

