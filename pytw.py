#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

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

title="pylive"
desc="Show current live on Twitch.tv"
version="0.1.0"


def init(title, desc, version):
        print "[-] " + title + " v" + version + " - " + desc



def check_twitch_lives(channels):
	print " - check_twitch_lives(channels): Checking live channels on twitch..."
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

        print "----------------------------------"
	return jsondata




class simpleapp_wx(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title)
        self.parent = parent
        self.initialize()

    def initialize(self):
        sizer = wx.GridBagSizer()

	self.conteneur = wx.Panel(self, 1, size = self.GetClientSize())

        for channel in channels:
                con = httplib.HTTPConnection("api.justin.tv",80)
                con.request("GET","/api/stream/list.json?channel=" + channel)
                response = con.getresponse()

		self.conteneur = wx.Panel(self, 1, size = self.GetClientSize())

                if response.status == 200:
                    jsondata = response.read();

                    users = json.loads(jsondata)
                    for user in users:
			Text = user['name'] + ' - ' + user['title'] + ' - ' + str(user['channel_count']) + " Viewers - " + user['channel']['channel_url']
			self.etiquette = wx.StaticText(self.conteneur, 1, Text)
			Text = user['up_time'] + " - " + user['meta_game']
			self.etiquette = wx.StaticText(self.conteneur, 1, Text)
                        print user['channel']['image_url_huge']


#        sizer.AddGrowableCol(0)
#        self.SetSizerAndFit(sizer)
#        self.SetSizeHints(-1,self.GetSize().y,-1,self.GetSize().y );

	self.StatusBar = wx.StatusBar(self, 1)
	self.StatusBar.SetFieldsCount(2)
	self.StatusBar.SetStatusWidths([1,1])
	self.SetStatusBar(self.StatusBar)

	self.StatusBar.SetStatusText("We all live in America", 1)

	self.Show(True)


    def OnButtonClick(self,event):
        self.label.SetLabel( self.entry.GetValue() + " (You clicked the button)" )
        self.entry.SetFocus()
        self.entry.SetSelection(-1,-1)

    def OnPressEnter(self,event):
        self.label.SetLabel( self.entry.GetValue() + " (You pressed ENTER)" )
        self.entry.SetFocus()
        self.entry.SetSelection(-1,-1)

if __name__ == "__main__":
    init(title, desc, version)
    jsondata = check_twitch_lives(channels)
    app = wx.App()
    frame = simpleapp_wx(None,-1,desc)
    app.MainLoop()

