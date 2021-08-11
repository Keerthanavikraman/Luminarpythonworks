

class Computer:     #superclasss
    def cdetails(self,getspecs,displayspecs):     #methods-->getspecs,displayspecs
        self.getspecs=getspecs
        self.displayspecs=displayspecs
        print(self.getspecs,self.displayspecs)

class Desktop(Computer):   #subclass
    def edetails(self,weight,storage,memory,display):   #methods-->weight,storage,memory,display
        self.weight=weight   #weight is a special specification in both desktop and laptop
        self.storage=storage
        self.memory=memory
        self.display=display
        print(self,weight,storage,memory,display)

class Laptop(Computer):    #subclass
    def ldetails(self,weight,color,os,ssd):   #methods-->weight,color,os,ssd
        self.weight=weight     #weight is a special specification in both desktop and laptop
        self.color=color
        self.os=os
        self.ssd=ssd
        print(self,weight,color,os,ssd)

de=Desktop()
de.edetails("5kg",500,"8gb","13lcdmonitor")
de.cdetails("hardware","software")

la=Laptop()
la.ldetails("4kg","black","windows",256)
la.cdetails("graphicscard","storage")