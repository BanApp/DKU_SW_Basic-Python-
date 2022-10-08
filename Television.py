class Television:
    def __init__(self, channel =11, volume =9, onoff = True ):
        self.channel = channel
        self.volume = volume
        self.onoff = onoff

    def show(self):
        print(self.channel,self.volume,self.onoff)

    def setChannel(self,channel):
        self.channel = channel

    def getChannel(self):
        return self.channel

t = Television(9,10,True)
t.show()
t.setChannel(11)
t.show()