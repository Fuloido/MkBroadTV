try:
    import wx
except ImportError:
    raise ImportError,"The wxPython module is required to run this program"

try:
    import httplib
except ImportError:
    raise ImportError,"The httplib module is required to run this program"

try:
    import json
except ImportError:
    raise ImportError,"The json module is required to run this program"




channels= ['dragon', 'followgrubby', 'liquidret', 'mlgsc2', 'mtwdimaga', 'liquidtlo', 'ignproleague' ]


def check_twitch_lives(channels):
        print " - check_twitch_lives(channels): Checking live channels on twitch..."

	livechannels = []

        for channel in channels:
                con = httplib.HTTPConnection("api.justin.tv",80)
                con.request("GET","/api/stream/list.json?channel=" + channel)
                response = con.getresponse()

                if response.status == 200:
                    jsondata = response.read();

                    users = json.loads(jsondata)
                    for user in users:
                        print user['name'] + ' - ' + user['title'] + ' - ', user['channel_count'], " Viewers - " + user['channel']['channel_url']
                        print user['up_time'] + " - " + user['meta_game']
                        print user['channel']['image_url_huge']
		    livechannels.append(users)


        print "----------------------------------"


        return livechannels


lc = check_twitch_lives(channels)

for i in lc :
    print i
    print "------------------------------"

