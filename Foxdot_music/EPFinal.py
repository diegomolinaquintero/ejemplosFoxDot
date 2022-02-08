print(SynthDefs) 
print(Samples) 
print(FxList) 
print(Attributes)  
print(PatternMethods)
print(Scale.names()) 

#-------------------------------------------------------------------------


Clock.bpm = 65
Scale.default.set("major")
Root.default.set("F")

def verse1():
    a1 >> sinepad([(0,6,9,11),(5,7,11,13),(1,7,10,12),(4,6,10,12)],dur=4,glide=3,oct=3,vib=1,swell=1/16,amp=0.8) 
    Clock.future(32, verse2)
def verse2():
    a1 >> sinepad([(0,6,9,11),(5,7,11,13),(1,7,10,12),(4,6,10,12)],dur=4,glide=0.5,oct=3,vib=4,amp=0.5) 
    d1 >> play("V", dur=PDur(2,8),amp=0.08,lpf=600).every(8,"stutter", 4)   
    Clock.future(32, verse3)
def verse3():
    a1 >> sinepad([(0,6,9,11)],dur=4,glide=0.5,oct=3,vib=0,amp=0.5) 
    d1 >> play("V", dur=4,amp=0.08,lpf=600)
    f1 >> bug(dur=1,sus=3,amp=0.2)
    Clock.future(4, chorus1)
def chorus1():
    f1.stop()
    a1 >> sinepad([(0,6,9,11),(5,7,11,13),(1,7,10,12),(4,6,10,12)],dur=2,glide=0.5,oct=3,vib=4,amp=0.5) 
    d1 >> play("V", dur=PDur(3,8),amp=0.08,lpf=600).every(7,"stutter", 3)
    d2 >> play("o", dur=PDur(2,8),amp=0.08,lpf=2000).every(9,"stutter", 3)
    d3 >> play("--(-=):", dur=PDur(5,8),amp=0.2).every(11,"stutter", 3)  
    Clock.future(32, chorus2)
def chorus2():
    a1 >> sinepad([(0,6,9,11),(5,7,11,13),(1,7,10,12),(4,6,10,12)],dur=4,glide=0.5,oct=3,vib=4,amp=0.5) 
    a2 >> soprano([0,5,1,4],dur=PDur(2,6),amp=0.2,oct=3)
    d3 >> play("--(-=):", dur=PDur(3,5),amp=0.2).every(7,"stutter", 3)
    d1.stop()
    d2.stop()
    Clock.future(16, chorus3)
def chorus3():
    a1 >> sinepad([(0,6,9,11),(5,7,11,13),(1,7,10,12),(4,6,10,12)],dur=2,glide=0.5,oct=3,vib=4,amp=0.5)
    a2 >> soprano([5,8,10,7,11,16],dur=PDur(2,5),amp=0.2,oct=3)
    a3 >> bell([1,10,12,4,10,12,0,6,11],dur=PDur(3,4),oct=5,amp=0.02).every(4,"stutter", 3).every(3,"stutter", 2).every(2,"stutter", 6) 
    a4 >> star([1,4,0],dur=PDur(3,6),oct=5,amp=0.05,tremolo=1).every(4,"stutter", 3).every(3,"stutter", 2).every(2,"stutter", 6) 
    d1 >> play("V", dur=PDur(3,8),amp=0.08,lpf=600).every(7,"stutter", 3)
    d2 >> play("o", dur=PDur(2,8),amp=0.08,lpf=2000).every(9,"stutter", 3)
    d3 >> play("--(-=):", dur=PDur(3,5),amp=0.2).every(11,"stutter", 3) 
    Clock.future(64, chorus4)
def chorus4():
    a3.stop()
    d1.stop()
    d2.stop()
    d3.stop()
    Clock.future(32, final)
def final():
    a2.stop()
    Clock.future(16, cierre)
def cierre():
    a1.stop()
    a4.stop()
verse1()  

print(SynthDefs) 
print(Samples) 
print(FxList) 
print(Attributes)  
print(PatternMethods)
print(Scale.names()) 

#-------------------------------------------------------------------------


Clock.bpm = 70
Scale.default.set("phrygian")
Root.default.set("F")

def verso1():
    a1 >> razz([0,2,4,6,8,10,11,13],dur=4,amp=0.5,oct=3)
    Clock.future(32, verso2)
def verso2():
    a1 >> razz([0,2,4,6,8,10,11,13],dur=8,amp=0.5,oct=3) 
    a2 >> swell([0,2,4,6,8,10,11,13],dur=8,amp=0.5,oct=3,sus=18) 
    Clock.future(32, verso3)
def verso3():
    a1 >> razz([0,2,4,6,8,10,11,13],dur=16,amp=0.5,oct=3) 
    a2 >> swell([0,2,4,6,8,10,11,13],dur=16,amp=0.5,oct=3,sus=18) 
    a3 >> charm([0,2,4,6,8,10,11],dur=PDur(3,16),amp=[0.2,0.3,0.1,0.4,0.2],oct=5)
    a4 >> snick([0,2,4,6,8,10,11,13],dur=PDur(3,5),amp=[0.5,0.2,0.4,0.1,0.4],oct=5) 
    Clock.future(32, choros1)
def choros1():
    a1 >> razz([0,2,4,6,8,10,11,13],dur=16,amp=0.5,oct=3) 
    a2 >> swell([0,2,4,6,8,10,11,13],dur=16,amp=0.5,oct=3,sus=18) 
    a3 >> charm([0,2,4,6,8,10,11],dur=PDur(3,16),amp=[0.2,0.3,0.1,0.4,0.2],oct=5)
    a4 >> snick([0,2,4,6,8,10,11,13],dur=PDur(3,5),amp=[0.5,0.2,0.4,0.1,0.4],oct=5) 
    a5 >> spark([0,2,4,6,8,10,11,13],dur=PDur(5,6),amp=[0.05,0.09,0.07,0.09,0.06],oct=5)
    a6 >> arpy([0,2,4,6,8,10,11,13],dur=PDur(3,6),amp=[0.4,0.2,0.3,0.9,0.1],oct=2).every(4,"stutter", 3)
    a7 >> gong([0,2,4,6,8,10,11,13],dur=PDur(2,5),amp=[0.4,0.2,0.3,0.9,0.1],oct=4).every(4,"stutter", 2)
    Clock.future(32, choros2)
def choros2():
    d1 >> play("qn", dur=PDur(3,7),amp=0.07,sample=[1,2,3,4,5]).every(11,"stutter", 3)
    d2 >> play("nq", dur=PDur(4,7),amp=0.08,sample=[1,2,3,4,5]).every(13,"stutter", 6)
    d3 >> play("u@", dur=PDur(5,7),amp=0.08,sample=[1,2,3,4,5]).every(15,"stutter", 3)
    d4 >> play("j", dur=PDur(4,6),amp=0.03,sample=[1,2,3,4,5,6,7]).every(13,"stutter", 6)
    Clock.future(32, choros3)
def choros3():
    d3 >> play("V", dur=1,amp=0.1,sample=[1,2,3,4,5]).every(4,"stutter", 3)
    Clock.future(32, choros4)
def choros4():
    d1 >> play("qn", dur=PDur(3,5),amp=0.07,sample=[1,2,3,4,5]).every(11,"stutter", 3)
    d2 >> play("nq", dur=PDur(4,6),amp=0.08,sample=[1,2,3,4,5]).every(13,"stutter", 6)
    d3 >> play("u@", dur=PDur(5,8),amp=0.08,sample=[1,2,3,4,5]).every(15,"stutter", 3)
    d4 >> play("j", dur=PDur(4,5),amp=0.03,sample=[1,2,3,4,5,6,7]).every(13,"stutter", 6)
    d3 >> play("V", dur=PDur(3,6),amp=0.1,sample=[1,2,3,4,5]).every(4,"stutter", 3)
    Clock.future(32, finol)
def finol():
    a3 >> charm([0,2,4,6,8,10,11],dur=PDur(3,6),amp=[0.2,0.3,0.1,0.4,0.2],oct=5)
    a4 >> snick([0,2,4,6,8,10,11,13],dur=PDur(4,5),amp=[0.5,0.2,0.4,0.1,0.4],oct=5) 
    a5 >> spark([0,2,4,6,8,10,11,13],dur=PDur(3,8),amp=[0.05,0.09,0.07,0.09,0.06],oct=5)
    a6 >> arpy([0,2,4,6,8,10,11,13],dur=PDur(3,5),amp=[0.4,0.2,0.3,0.9,0.1],oct=2).every(4,"stutter", 3)
    a7 >> gong([0,2,4,6,8,10,11,13],dur=PDur(3,7),amp=[0.4,0.2,0.3,0.9,0.1],oct=4).every(4,"stutter", 2)
    d3 >> play("V", dur=PDur(3,8),amp=0.1,sample=[1,2,3,4,5]).every(4,"stutter", 3)    
    Clock.future(32, cierro)
def cierro():
    a1.stop()
    a2.stop()
    a3.stop()
    a4.stop()
    a5.stop()
    a6.stop()
    a7.stop()
    d1.stop()
    d2.stop()
    d3.stop()
    d4.stop()
    Clock.future(16, cierro)
verso1()

print(SynthDefs) 
print(Samples) 
print(FxList) 
print(Attributes)  
print(PatternMethods)
print(Scale.names()) 

#-------------------------------------------------------------------------


Clock.bpm = 85
Scale.default.set("minMaj")
Root.default.set("D")

def versa1():
    a1 >> pads([(0,6,9,11),(5,7,11,13),(1,7,10,12),(4,6,10,12)],dur=4,glide=2,oct=3,chop=8,vib=1,amp=0.3)
    d1 >> play("V", dur=PDur(1,8),amp=0.08,lpf=600)
    d2 >> play("o", dur=PDur(2,8),amp=0.08,lpf=2000)
    d3 >> play("--(-=):", dur=PDur(5,7),amp=0.2).every(11,"stutter", 3)   
    Clock.future(32, versa2)
def versa2():
    a1 >> pads([(0,6,9,11),(5,7,11,13),(1,7,10,12),(4,6,10,12)],dur=4,glide=2,oct=3,chop=2,vib=1,amp=0.3)
    d1 >> play("V", dur=PDur(3,8),amp=0.08,lpf=600).every(8,"stutter", 4)
    d2 >> play("o", dur=PDur(6,8),amp=0.08,lpf=2000)   
    Clock.future(32, versa3)
def versa3():
    d2.stop()
    d3.stop()
    a1 >> pads([(0,6,9,11),(5,7,11,13),(1,7,10,12),(4,6,10,12)],dur=4,glide=2,oct=3,chop=1,vib=2,amp=0.3)
    d1 >> play("V", dur=1/3,amp=0.08,lpf=600)
    f1 >> ambi(dur=1,sus=3,amp=0.2)
    Clock.future(4, choras1)
def choras1():
    f1.stop()
    a1 >> pads([(0,6,9,11),(5,7,11,13),(1,7,10,12),(4,6,10,12)],dur=2,glide=0.5,oct=3,vib=16,amp=0.5,lpf=4000) 
    d1 >> play("V", dur=PDur(3,8),amp=0.08,lpf=600).every(7,"stutter", 3)
    d2 >> play("o", dur=PDur(2,8),amp=0.08,lpf=2000).every(9,"stutter", 3)
    d3 >> play("--(-=):", dur=PDur(5,8),amp=0.2).every(11,"stutter", 3)  
    Clock.future(32, choras2)
def choras2():
    a1 >> sinepad([(0,6,9,11),(5,7,11,13),(1,7,10,12),(4,6,10,12)],dur=4,glide=0.5,oct=3,vib=4,amp=0.5,lpf=4000) 
    a2 >> soprano([0,5,1,4],dur=PDur(2,6),amp=0.2,oct=3)
    d3 >> play("--(-=):", dur=PDur(3,5),amp=0.2).every(11,"stutter", 3)
    d1.stop()
    d2.stop()
    Clock.future(16, choras3)
def choras3():
    a1 >> sinepad([(0,6,9,11),(5,7,11,13),(1,7,10,12),(4,6,10,12)],dur=2,glide=0.5,oct=3,vib=4,amp=0.5)
    a2 >> soprano([0,5,1,4],dur=PDur(2,5),amp=0.2,oct=3).every(11,"stutter", 3)
    a3 >> bell([1,10,12,4,10,12,0,6,11],dur=PDur(3,4),oct=5,amp=0.02).every(4,"stutter", 3).every(3,"stutter", 2).every(2,"stutter", 6) 
    a4 >> star([1,4,0],dur=PDur(3,4),oct=5,amp=0.05,tremolo=1).every(4,"stutter", 3).every(3,"stutter", 2).every(2,"stutter", 6) 
    d1 >> play("V", dur=PDur(3,8),amp=0.08,lpf=600).every(7,"stutter", 3)
    d2 >> play("o", dur=PDur(2,8),amp=0.08,lpf=2000).every(9,"stutter", 3)
    d3 >> play("--(-=):", dur=PDur(3,5),amp=0.2).every(11,"stutter", 3) 
    Clock.future(64, choras4)
def choras4():
    d2.stop()
    d3.stop()
    a1 >> pads([(0,6,9,11),(5,7,11,13),(1,7,10,12),(4,6,10,12)],dur=4,glide=2,oct=3,chop=1,vib=2,amp=0.3)
    d1 >> play("V", dur=1/3,amp=0.08,lpf=600)
    f1 >> ambi(dur=1,sus=3,amp=0.2)
    Clock.future(8, finaal)
def finaal():
    a3.stop()
    d1.stop()
    d2.stop()
    d3.stop()
    a2.stop()
    Clock.future(16, cierra1)
def cierra1():
    d2.stop()
    d3.stop()
    a1.stop()
    a4.stop()
    a1 >> pads([(0,6,9,11),(5,7,11,13),(1,7,10,12),(4,6,10,12)],dur=4,glide=2,oct=3,chop=1,vib=2,amp=0.3)
    d1 >> play("V", dur=1/3,amp=0.08,lpf=600)
    f1 >> ambi(dur=1,sus=3,amp=0.2)
    Clock.future(8, cierra)
def cierra():
    a1.stop()
    a4.stop()
    f1.stop()
    d1.stop()
versa1()




print(SynthDefs) 
print(Samples) 
print(FxList) 
print(Attributes)  
print(PatternMethods)
print(Scale.names()) 
#-------------------------------------------------------------------------


Clock.bpm = 90
Scale.default.set("lydianAug")
Root.default.set("A")

def versi1():
    a1 >> growl([0,2,4,6,8,10,11,13],dur=4,amp=0.2,oct=3)
    Clock.future(32, versi2)
def versi2():
    a2 >> space([0,2,4,6,8,10,11,13],dur=8,amp=0.1,oct=3,sus=18,vib=3) 
    Clock.future(32, versi3)
def versi3():
    a3 >> bell([0,2,4,6,8,10,11],dur=PDur(3,16),amp=[0.08,0.07,0.05,0.06,0.04],oct=5)
    a4 >> space([0,2,4,6,8,10,11,13],dur=PDur(3,5),amp=[0.05,0.02,0.04,0.01,0.04],oct=8) 
    Clock.future(32, choris1)
def choris1():
    a1 >> growl([0,2,4,6,8,10,11,13],dur=PDur(3,6),amp=0.2,oct=3) 
    a2 >> space([0,2,4,6,8,10,11,13],dur=4,amp=0.2,oct=3,sus=18) 
    a3 >> bell([0,2,4,6,8,10,11],dur=PDur(3,16),amp=[0.05,0.09,0.07,0.09,0.06],oct=5)
    a4 >> space([0,2,4,6,8,10,11,13],dur=PDur(3,8),amp=[0.08,0.07,0.05,0.06,0.04],oct=8) 
    a5 >> bell([0,2,4,6,8,10,11,13],dur=PDur(5,6),amp=[0.05,0.09,0.07,0.09,0.06],oct=5)
    a6 >> bell([0,2,4,6,8,10,11,13],dur=PDur(3,6),amp=[0.04,0.02,0.03,0.09,0.1],oct=2).every(4,"stutter", 3)
    a7 >> space([0,2,4,6,8,10,11,13],dur=PDur(2,5),amp=[0.05,0.09,0.07,0.09,0.06],oct=4).every(4,"stutter", 2)
    Clock.future(32, choris2)
def choris2():
    d1 >> play("---(==-)", dur=PDur(6,8),amp=0.07,sample=[1,2,3,4,5]).every(11,"stutter", 16)
    d2 >> play("o.o.", dur=PDur(3,4),amp=0.08,sample=[1,2,3,4,5]).every(13,"stutter", 6)
    d3 >> play("cc$%&", dur=PDur(2,8),amp=0.08,sample=[1,2,3,4,5]).every(15,"stutter", 3)
    d4 >> play("V", dur=PDur(3,8),amp=0.1,sample=[1,2,3,4,5,6,7]).every(8,"stutter", 3)
    Clock.future(32, choris3)
def choris3():
    d4 >> play("V", dur=1/3,amp=0.1,sample=[1,2,3,4,5]).every(4,"stutter", 3)
    Clock.future(16, choris4)
def choris4():
    d1 >> play("---(==-)", dur=PDur(3,8),amp=0.07,sample=[1,2,3,4,5]).every(8,"stutter", 12)
    d2 >> play("o.o.", dur=PDur(3,4),amp=0.08,sample=[1,2,3,4,5]).every(13,"stutter", 6)
    d3 >> play("cc$%&", dur=PDur(3,8),amp=0.08,sample=[1,2,3,4,5]).every(15,"stutter", 3)
    d4 >> play("V", dur=PDur(3,8),amp=0.1,sample=[1,2,3,4,5,6,7]).every(4,"stutter", 4)
    Clock.future(32, finil)
def finil():
    a1 >> growl([0,2,4,6,8,10,11,13],dur=PDur(3,8),amp=0.2,oct=3) 
    a2 >> space([0,2,4,6,8,10,11,13],dur=4,amp=0.2,oct=3,sus=18) 
    a3 >> bell([0,2,4,6,8,10,11],dur=PDur(6,12),amp=[0.05,0.09,0.07,0.09,0.06],oct=5)
    a4 >> space([0,2,4,6,8,10,11,13],dur=PDur(3,8),amp=[0.08,0.07,0.05,0.06,0.04],oct=8) 
    a5 >> bell([0,2,4,6,8,10,11,13],dur=PDur(6,8),amp=[0.05,0.09,0.07,0.09,0.06],oct=5)
    a6 >> ambi([0,2,4,6,8,10,11,13],dur=PDur(3,8),amp=[0.04,0.02,0.03,0.09,0.1],oct=2).every(4,"stutter", 3)
    a7 >> space([0,2,4,6,8,10,11,13],dur=PDur(2,8),amp=[0.05,0.09,0.07,0.09,0.06],oct=4).every(4,"stutter", 2)
    d4 >> play("V", dur=PDur(3,8),amp=0.1,sample=[1,2,3,4,5]).every(4,"stutter", 3)    
    Clock.future(32, cierri)
def cierri():
    a1 >> growl([0,2,4,6,8,10,11,13],dur=4,amp=0.2,oct=3)
    a2 >> space([0,2,4,6,8,10,11,13],dur=8,amp=0.1,oct=3,sus=18,vib=3) 
    a3.stop()
    a4.stop()
    a5.stop()
    a6.stop()
    a7.stop()
    d1.stop()
    d2.stop()
    d3.stop()
    d5.stop()
    d4.stop()
    Clock.future(16, cierri2)
def cierri2():
    a1.stop()
    a2.stop()
versi1()
