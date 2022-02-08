print(SynthDefs) 
print(Samples) 
print(FxList) 
print(Attributes)  
print(PatternMethods) 

#-------------------------------------------------------------------------


Clock.bpm = 70
Scale.default.set("majorPentatonic")
Root.default.set("C")


def verse1():
    v1 >> MidiOut([0,2,4,6,0,2,4,6,1,3,5,8,1,3,4,6],dur=1,oct=[5,3,7],amp=1.2)
    p1 >> keys([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=[4],room=3,oct=5, amp=0.3,glide=0.3)
    p2 >> blip([0, 1], dur=8,room=3,oct=3,amp=0.1)
    p3 >> jbass([0,1], dur=8,room=3,oct=2, amp=0.1)
    Clock.future(32, verse2)
def verse2():
    v1 >> MidiOut([0,2,4,6,0,2,4,6,1,3,5,8,1,3,4,6],dur=1,oct=[5,3,7],amp=1.2)
    p1 >> keys([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=4,room=3,oct=5,amp=0.3,glide=0.1)
    p2 >> dab([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=4,oct=8,chop=[16,8,4,32,3,5,2,1],amp=[0.09,0.02,0.05,0.03])
    p3 >> blip([0, 0, 1, 1],amp=0.1, dur=4,room=3,oct=3).every(16,"stutter", 16)
    p4 >> jbass([0, 0, 1, 1], dur=4,room=3,oct=3, amp=0.1) 
    d4 >> play("n", amp=0.03, dur=1).every(16,"stutter", 8) 
    Clock.future(32, verse3)
def verse3():
    v1 >> MidiOut([0,2,4,6,0,2,4,6,1,3,5,8,1,3,4,6],dur=1,oct=[5,3,7],amp=1.2)
    p1 >> keys([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=[4],room=3,oct=5,amp=0.3,glide=0.1)
    p2 >> dab([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=[4],oct=8,chop=[16,8,4,32,3,5,2,1],amp=[0.09,0.02,0.05,0.02])
    p3 >> blip([0, 1], dur=[8],room=3,amp=0.1,oct=3).every(16,"stutter", 8) 
    p4 >> jbass([0,1], dur=[8],room=3,oct=3, amp=0.1) 
    d4 >> play("n", amp=0.04, dur=0.5).every(8,"stutter", 3) 
    d1 >> play(".o.oo", dur=[1,1,1,0.75,0.25],amp=0.08).every(6,"stutter", 3)
    d2 >> play("V.v.", dur=1,amp=0.08).every(16,"stutter", 3).every(24,"stutter", 8)
    Clock.future(32, chorus1)
def chorus1():
    v1 >> MidiOut([0,1,0,4,2,1,0,1,0],dur=[1,2,0.75,0.25,1,0.75,0.25,1,0.75,0.25],oct=7,amp=1,vib=4)
    p1 >> keys([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=[4],room=3,oct=5,amp=0.5,glide=0.1)
    p2 >> dab([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=[4],oct=8,chop=[16,8,4,32,3,5,2,1],amp=[0.09,0.02,0.05,0.04])
    p3 >> blip([0, 0, 1, 1], dur=[4],room=3,chop=0.1,oct=3).every(16,"stutter", 8) 
    p4 >> jbass([0, 0, 1, 1], dur=[4],room=3,oct=3, amp=0.1) 
    d4 >> play("n", amp=0.04, dur=0.5) 
    d1 >> play(".o.oo", dur=[1,1,1,0.75,0.25],amp=0.08).every(6,"stutter", 3)
    d2 >> play("V.vv", dur=[1],amp=0.08).every(16,"stutter", 3).every(12,"stutter", 8)
    m1 >> twang([0,1,0,4,2,1,0,1,0],dur=[1,2,0.75,0.25,1,0.75,0.25,1,0.75,0.25],oct=7,amp=0.021,vib=4).every(8,"stutter", 2)
    m3 >> sinepad([0,4], dur=1/2,oct=7,amp=0.072,vib=4).every(8,"stutter", 3)
    Clock.future(16, chorus2)
def chorus2():
    v1 >> MidiOut([0,2,4,6,0,2,4,6,1,3,5,8,1,3,4,6], dur=[1/2,1,1/2,1/4,1/2,1/4,1],oct=8,amp=1.2)
    p1 >> keys([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=[4],room=3,oct=5,glide=0.1,amp=0.3)
    p2 >> dab([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=[4],oct=8,chop=[16,8,4,32,3,5,2,1],amp=[0.01,0.02,0.05,0.09])
    p3 >> blip([0,0,1, 1], dur=[4],room=3,chop=0.8,oct=3).every(16,"stutter", 8) 
    p4 >> jbass([0, 0, 1, 1], dur=[4],room=3,oct=3, amp=0.1) 
    d4 >> play("n", amp=0.05, dur=0.5) 
    d1 >> play(".o.oo", dur=[1,1,1,0.75,0.25],amp=0.08).every(6,"stutter", 3)
    d2 >> play("V.v.", dur=[1],amp=0.08).every(16,"stutter", 3)
    d3 >> play("rczC/%", dur=3,rate=[0.5,1,4,6,40],sample=[1,2,3],amp=0.03).every(8,"stutter", 8).every(16,"stutter",16) 
    m1 >> twang([0,1,0,4,2,1,0,1,0],dur=[1,2,0.75,0.25,1,0.75,0.25,1,0.75,0.25],oct=7,amp=0.021,vib=4).every(8,"stutter", 2)
    m3 >> sinepad([0,4], dur=1/2,oct=7,amp=0.051,vib=4).every(8,"stutter", 2)
    m4 >> marimba([0,2,4,6,0,2,4,6,1,3,5,8,1,3,4,6], dur=[1/2,1,1/2,1/4,1/2,1/4,1],oct=8,amp=0.8).every(8,"stutter", 3)
    Clock.future(16, chorus3)
def chorus3():
    p1 >> keys([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=[4],room=3,oct=5,glide=0.1,amp=0.4)
    p2 >> dab([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=[4],oct=8,chop=[16,8,4,32,3,5,2,1],amp=[0.01,0.05,0.07,0.03])
    p3 >> blip([0, 0, 1, 1], dur=[4],room=3,chop=0.8,oct=3).every(16,"stutter", 8) 
    p4 >> jbass([0,0, 1, 1], dur=[4],room=3,oct=3, amp=0.1) #volumen desacio
    d4 >> play("n", amp=0.05, dur=0.5).every(8,"stutter", 13) 
    d1 >> play(".o.oo", dur=[1,1,1,0.75,0.25],amp=0.08).every(6,"stutter", 3).every(8, "stutter", 4).every(12,"stutter",8).every(16,"stutter",3)
    d2 >> play("V.v.", dur=[1],amp=0.08).every(4,"stutter", 3).every(16, "stutter", 4).every(12,"stutter",8).every(8,"stutter",3)
    d3 >> play("rczC/%", dur=3,rate=[0.5,1,4,6,40],sample=[1,2,3],amp=0.03).every(8,"stutter", 8).every(16,"stutter",16) 
    m1 >> twang([0,1,0,4,2,1,0,1,0],dur=[1,2,0.75,0.25,1,0.75,0.25,1,0.75,0.25],oct=7,amp=0.021,vib=4).every(8,"stutter", 2).every(6,"stutter", 3).every(16, "stutter", 4).every(12,"stutter",8).every(8,"stutter",3)
    m3 >> sinepad([0,4], dur=[1/2,1/4,1/4,1/2,1],oct=7,amp=0.051,vib=4).every(8,"stutter", 2)
    m4 >> marimba([0,2,4,6,0,2,4,6,1,3,5,8,1,3,4,6], dur=[1/2,1,1/2,1/4,1/2,1/4,1],oct=8,amp=0.9,room=5).every(2,"stutter", 3).every(4, "stutter", 4).every(8,"stutter",8).every(12,"stutter",3)
    Clock.future(32, chorus4)
def chorus4():
    p1 >> keys([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=[4],room=3,oct=5,amp=0.4)
    p2 >> dab([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=[4],oct=8,chop=[16,8,4,32,3,5,2,1],amp=[0.03,0.02,0.05,0.07])
    p3 >> blip([0,0, 1, 1], dur=[4],room=3,chop=0.8,oct=3).every(16,"stutter", 8)
    p4 >> jbass([0, 0,1, 1], dur=[4],room=3,oct=3, amp=0.1) #volumen desacio
    d4 >> play("n", amp=0.05, dur=0.5).every(3,"stutter", 3).every(2,"stutter", 8) 
    d3 >> play("rczC/%", dur=3,rate=[0.5,1,4,6,40],sample=[1,2,3],amp=0.07).every(8,"stutter", 3).every(16,"stutter",16) 
    m1 >> twang([0,1,0,4,2,1,0,1,0],dur=[1,2,0.75,0.25,1,0.75,0.25,1,0.75,0.25],oct=7,amp=0.03,vib=4).every(8,"stutter", 2).every(3,"stutter", 8)
    m3 >> sinepad([0,4], dur=1/2,oct=7,amp=0.06,vib=4).every(8,"stutter", 2)
    d1.stop()
    d2.stop()  
    Clock.future(32, final)
def final():
    p1 >> keys([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=[4],room=3,oct=5,glide=0.5,amp=0.4)
    p2 >> dab([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=[4],oct=8,chop=[16,8,4,32,3,5,2,1],amp=[0.01,0.02,0.05,0.02])
    p3 >> blip([0, 1, 4, 0], dur=[4],room=3,chop=0.8,oct=3).every(16,"stutter", 8)
    p4 >> jbass([0, 1, 4, 0], dur=[4],room=3,oct=3, amp=0.1) #volumen desacio
    d4 >> play("n", amp=0.03, dur=1).every(3,"stutter", 8).every(2,"stutter", 3)
    v1.stop()
    d3.stop()
    m1.stop()
    m3.stop()
    Clock.future(16, cierre)
def cierre():
    p1 >> keys([(0,2,4,6)], dur=[16],room=3,oct=5,glide=1,amp=0.3)
    d3.stop()
    m1.stop()
    m3.stop()
    p2.stop() 
    p3.stop()
    p4.stop()
    d4.stop()
    Clock.future(16, cierre1)
def cierre1():
    m4.stop()
    p1.stop() 
    p2.stop() 
    p3.stop()
    p4.stop()
    d4.stop()
    #Clock.future(16, cierre)
verse1()


#-------------------------------------------------------------------------

Clock.bpm = 65
Scale.default.set("minorPentatonic")
Root.default.set("A")
print(SynthDefs) 

def versa1():
    p1 >> klank([0], dur=16,room=3,oct=3,glide=3)
    p2 >> glass([0,4], dur=4,room=3,oct=4,amp=0.5,glide=1)
    p3 >> feel([0,7], dur=8,room=3,oct=4, amp=0.6,glide=3)
    Clock.future(48, versa2)
def versa2():
    p4 >> sinepad([0, 0, 4, 7], dur=4,room=3,oct=5, amp=0.1,glide=1) 
    d4 >> play("U", amp=0.02, dur=[1/2,1,1/2], sample=[1,2,3,4,5]).every(6,"stutter", 3).every(3,"stutter", 8)
    Clock.future(16, versa3)
def versa3():
    p4 >> sinepad([0, 0, 4, 6,4,5,0,1,2,2,1,0], dur=1,room=3,oct=[3,4,5,4,3,2], amp=0.1).every(3,"stutter", 3).every(3,"stutter", 8)
    d1 >> play(".l.(lb)", dur=[1,1,1,0.75,0.25],amp=0.01).every(3,"stutter", 3).every(3,"stutter", 8)
    d2 >> play("f.f.", dur=[1],amp=0.02).every(2,"stutter", 3).every(3,"stutter", 8)
    Clock.future(16, choras1)
def choras1():
    m1 >> soprano([0,1,0,6,6,1,0,1,0],dur=[1/2,1/3,1/3,1/3,1/2,2],oct=3,amp=0.4,glide=0.01).every(8,"stutter", 2)
    m3 >> soprano([0,4], dur=[1/4,1/2,1/4],oct=5,amp=0.2,vib=4,glide=0.03).every(8,"stutter", 3)
    p1.stop()
    p3.stop()
    p2.stop()
    Clock.future(16, choras2)
def choras2():
    p4 >> sinepad([0, 0, 4, 6,4,5,0,1,2,2,1,0], dur=[1,1/2,1/4,1/8],room=3,oct=[3,4,5,4,3,2], amp=0.2).every(3,"stutter", 3).every(3,"stutter", 8)  
    d3 >> play("r.c.z.C./.%.l.u.", dur=1/3,rate=[0.5,1,4,6,40],sample=[1,2,3],amp=0.05).every(8,"stutter", 8).every(16,"stutter",16) 
    m4 >> prophet([0,6,4,0], dur=[1/2,1,1/2,1/4,1/2,1/4,1],oct=[3,4,5,4,3,2],amp=0.3,rate=[0.5,1,4,6,40],glide=1).every(8,"stutter", 3)
    p1.stop()
    p3.stop()
    p2.stop()
    Clock.future(16, choras4)
def choras4():
    p5 >> pads([(0,6,2,4)], dur=[8],room=3,oct=[4,6],chop=4,amp=[0.2,0.08],glide=1)
    p1.stop()
    p3.stop()
    p4.stop()
    p2.stop()
    Clock.future(24, cierra1)
def cierra1():
    m4.stop()
    p1.stop() 
    p2.stop() 
    p3.stop()
    p4.stop()
    p5.stop()
    d4.stop()
    d1.stop()
    d2.stop()
    Clock.future(2, cierra)
def cierra():
    d1.stop() 
    d2.stop() 
    d3.stop()
    m3.stop()
    m1.stop()
    m2.stop()
    #Clock.future(2, cierra)
versa1()




print(SynthDefs) 
print(Samples) 
print(FxList) 
print(Attributes)  
print(PatternMethods) 

#-------------------------------------------------------------------------

Clock.bpm = 70
Scale.default.set("minorPentatonic")
Root.default.set("E")


def verso1():
    p1 >> pads([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)],amp=0.3 ,dur=4,room=3,oct=3,sus=4)
    p2 >> sinepad([0, 1], dur=8,room=3,chop=0.8,oct=3,amp=0.1)
    p3 >> soft([0,1], dur=8,room=3,oct=2, amp=0.8,amp=0.1)
    Clock.future(32, verso2)
def verso2():
    p1 >> pads([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=[4],room=3,oct=3)
    p2 >> soft([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=[4],oct=8,chop=[16,8,4,32,3,5,2,1],amp=[0.1,0.2,0.15,0.2])
    p3 >> sinepad([0, 0, 1, 1], dur=[4],room=3,chop=0.8,oct=3).every(16,"stutter", 8)
    p4 >> jbass([0, 0, 1, 1], dur=[4],room=3,oct=3, amp=0.8) 
    d4 >> play(":", amp=0.4, dur=1) 
    Clock.future(32, verso3)
def verso3():
    p1 >> pads([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=[4],room=3,oct=3)
    p2 >> soft([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=[4],oct=8,chop=[16,8,4,32,3,5,2,1],amp=[0.1,0.2,0.15,0.2])
    p3 >> sinepad([0, 1], dur=[8],room=3,chop=0.8,oct=3).every(16,"stutter", 8) 
    p4 >> jbass([0,1], dur=[8],room=3,oct=3, amp=0.8) 
    d4 >> play(":", amp=0.4, dur=0.5) 
    d1 >> play(".h.hh", dur=[1,1,1,0.75,0.25],amp=0.5).every(6,"stutter", 3)
    d2 >> play("X", dur=PDur(3,8),amp=0.6).every(6,"stutter", 6)
    Clock.future(32, choros1)
def choros1():
    p1 >> pads([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=[4],room=3,oct=3)
    p2 >> soft([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=[4],oct=8,chop=[16,8,4,32,3,5,2,1],amp=[0.1,0.2,0.15,0.09])
    p3 >> sinepad([0, 0, 1, 1], dur=[4],room=3,chop=0.8,oct=3).every(16,"stutter", 8) 
    p4 >> jbass([0, 0, 1, 1], dur=[4],room=3,oct=3, amp=0.8) 
    d4 >> play(":", amp=0.4, dur=0.5) 
    d1 >> play(".h.hh", dur=[1,1,1,0.75,0.25],amp=0.5).every(6,"stutter", 3)
    d2 >> play("X", dur=PDur(3,8),amp=0.6).every(6,"stutter", 4)
    m1 >> pluck([0,1,0,4,2,1,0,1,0],dur=[1,2,0.75,0.25,1,0.75,0.25,1,0.75,0.25],oct=7,amp=0.3,vib=4).every(8,"stutter", 2)
    m3 >> sitar([0,4], dur=PDur(2,8),oct=5,amp=0.2,vib=4).every(8,"stutter", 3)
    Clock.future(16, choros2)
def choros2():
    p1 >> pads([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=[4],room=3,oct=3)
    p2 >> soft([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=[4],oct=8,chop=[16,8,4,32,3,5,2,1],amp=[0.1,0.2,0.15,0.09])
    p3 >> sinepad([0,0,1, 1], dur=[4],room=3,chop=0.8,oct=3).every(16,"stutter", 8) 
    p4 >> jbass([0, 0, 1, 1], dur=[4],room=3,oct=3, amp=0.4,rate=[0.5,1,4,6,40]) 
    d4 >> play(":", amp=0.4, dur=0.5) 
    d1 >> play(".o.hH", dur=[1,1,1,0.75,0.25],amp=0.5,rate=[0.5,1,4,6,40]).every(6,"stutter", 3)
    d2 >> play("Xx", dur=PDur(3,8),amp=0.6).every(6,"stutter", 3)
    d3 >> play("rczC/%:h", dur=3,rate=[0.5,1,4,6,40],sample=[1,2,3],amp=0.07).every(8,"stutter", 8).every(16,"stutter",16) 
    m1 >> pluck([0,1,0,4,2,1,0,1,0],dur=PDur(3,7),oct=7,amp=0.4,vib=4,rate=[0.5,1,4,6,40]).every(8,"stutter", 2)
    m3 >> sitar([0,4], dur=PDur(4,9),oct=5,amp=0.4,vib=4).every(8,"stutter", 2)
    m4 >> viola([0,2,4,6,0,2,4,6,1,3,5,8,1,3,4,6], dur=1,oct=4,amp=0.5,rate=[0.5,1,4,6,40]).every(8,"stutter", 3)
    Clock.future(16, choros4)
def choros3():
    p1 >> pads([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=[4],room=3,oct=3)
    p2 >> soft([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=[4],oct=8,chop=[16,8,4,32,3,5,2,1],amp=[0.1,0.2,0.15,0.09])
    p3 >> sinepad([0, 0, 1, 1], dur=[4],room=3,chop=0.8,oct=3).every(16,"stutter", 8) 
    p4 >> jbass([0,0, 1, 1], dur=[4],room=3,oct=3, amp=0.8) #volumen desacio
    d4 >> play(":", amp=0.5, dur=0.5) 
    d1 >> play(".h.oh", dur=[1,1,1,0.75,0.25]).every(6,"stutter", 3).every(8, "stutter", 4).every(12,"stutter",8).every(16,"stutter",3)
    d2 >> play("X",dur=PDur(3,8)).every(6,"stutter", 3).every(16, "stutter", 4).every(12,"stutter",8).every(8,"stutter",3)
    d3 >> play("rczC/%", dur=PDur(3,8),rate=[0.5,1,4,6,40],sample=[1,2,3],amp=0.09).every(8,"stutter", 8).every(16,"stutter",16) 
    m1 >> pluck([0,1,0,4,2,1,0,1,0],dur=1,oct=7,amp=0.1,vib=4).every(8,"stutter", 2).every(6,"stutter", 3).every(16, "stutter", 4).every(12,"stutter",8).every(8,"stutter",3)
    m3 >> sitar([0,4], dur=PDur(3,6),oct=5,amp=0.1,vib=4).every(8,"stutter", 2)
    m4 >> viola([0,2,4,6,0,2,4,6,1,3,5,8,1,3,4,6], dur=PDur(3,7),oct=4,amp=2,room=5).every(2,"stutter", 3).every(4, "stutter", 4).every(8,"stutter",8).every(12,"stutter",3)
    Clock.future(32, choros4)
def choros4():
    p1 >> pads([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=[4],room=3,oct=3)
    p2 >> soft([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=[4],oct=8,chop=[16,8,4,32,3,5,2,1],amp=[0.1,0.2,0.15,0.2])
    p3 >> sinepad([0,0, 1, 1], dur=[4],room=3,chop=0.8,oct=3).every(16,"stutter", 8)
    p4 >> jbass([0, 0,1, 1], dur=PDur(3,8),room=3,oct=3, amp=0.8) #volumen desacio
    d4 >> play(":", amp=0.5, dur=1) 
    d3 >> play("rczC/%::",dur=PDur(3,8),rate=[0.5,1,4,6,40],sample=[1,2,3],amp=0.07).every(8,"stutter", 8).every(16,"stutter",16) 
    m1 >> pluck([0,1,0,4,2,1,0,1,0],dur=PDur(3,8),oct=7,amp=0.1,vib=4).every(8,"stutter", 2)
    m3 >> sitar([0,4], dur=PDur(3,7),oct=5,amp=0.1,vib=4).every(8,"stutter", 2)
    d1.stop()
    d2.stop()  
    Clock.future(32, finol)
def finol():
    p1 >> pads([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=[4],room=3,oct=3)
    p2 >> soft([(0,2,4,6),(0,2,4,6),(1,3,5,8),(1,3,4,6)], dur=[4],oct=8,chop=[16,8,4,32,3,5,2,1],amp=[0.1,0.2,0.15,0.2])
    p3 >> sinepad([0, 1, 4, 0], dur=PDur(3,8),room=3,chop=0.8,oct=3).every(16,"stutter", 8)
    p4 >> jbass([0, 1, 4, 0], dur=[4],room=3,oct=3, amp=0.8) #volumen desacio
    d4 >> play(":", dur=1)
    d3.stop()
    m1.stop()
    m3.stop()
    Clock.future(16, cierro)
def cierro():
    p1 >> pads([(0,2,4,6)], dur=[16],room=3,oct=2)
    d3.stop()
    m1.stop()
    m3.stop()
    p2.stop() 
    p3.stop()
    p4.stop()
    d4.stop()
    Clock.future(16, cierro1)
def cierro1():
    m4.stop()
    p1.stop() 
    p2.stop() 
    p3.stop()
    p4.stop()
    d4.stop()
verso1()

choros2()
-----------------------------------------
print(SynthDefs) 
print(Samples) 
print(FxList) 
print(Attributes)  
print(PatternMethods) 

#-------------------------------------------------------------------------

Clock.bpm = 80
Scale.default.set("minor")
Root.default.set("D")



def primera():
    p1 >> blip(var([0, 5, 3, 4], 8), dur=[4,4],room=3,chop=0.8,oct=3,amp=0.2)
    p2 >> soprano(var([0, 5, 3, 4], 8), dur=[8],room=3,chop=0.5,oct=4, amp=0.2) + (0, 2,4,6,7,11)#volumen desacio
    d4 >> play("n", amp=0.06, dur=1) 
    Clock.future(32, redo)
def redo():
    p1 >> blip(var([0, 5, 3, 4], 8), dur=[4,4],room=3,chop=0.8,oct=3,amp=0.2)
    p2 >> soprano(var([0, 5, 3, 4], 8), dur=[8],room=3,chop=0.5,oct=4, amp=0.2) + (0, 2,4,6,7,11)#volumen desacio
    d1 >> play(".o.o", dur=1,amp=0.07)
    d4 >> play("n", amp=0.06, dur=1)
    Clock.future(32, bajos) 
def bajos():
    p1 >> blip(var([0, 5, 3, 4], 8), dur=[4,4],room=3,chop=0.8,oct=3,amp=0.2)
    p2 >> soprano(var([0, 5, 3, 4], 8), dur=[8],room=3,chop=0.5,oct=4, amp=0.2) + (0, 2,4,6,7,11)#volumen desacio
    p3 >> bass(var([0, 5, 3, 4], 8),room=2, dur=[1,1,0.75,0.25], oct=4, amp=0.15)
    p4 >> sinepad(var([0, 5, 3, 4], 8),room=1, dur=[1,1,0.75,0.25], oct=3, amp=0.1)
    d1 >> play(".o.o",dur=1, amp=0.07)
    d4 >> play("n", amp=0.05, dur=[0.5,1,0.5]).every(8,"stutter",3) 
    Clock.future(32, inter) 
def inter():
    p1 >> blip(var([0, 5, 3, 4], 8), dur=[4,4],room=3,chop=0.8,oct=3,amp=0.2)# esta es la cuarta parte
    p2 >> sinepad(var([0, 5, 3, 4], 8), dur=[8],room=3,chop=0.5,oct=3,amp=0.1) + (0, 2,4,6,7)
    p3 >> keys(var([0, 5, 3, 4], 8), dur=[2,2,2,2],room=4,chop=2,amp=[0.05,0.03,0.02,0.06]) + (0, 2,4,6,11)
    p4 >> bell(var([0,2,4,6],2),dur=[1/2,1/4,1,1/4,4],oct=6,chop=[1,2,4],rate=[1,23,3],amp=[0.05,0.03,0.02,0.04,0.02,0.05])
    p5 >> bass(var([0, 5, 3, 4], 8),room=2, dur=[1,1,0.75,0.25], oct=4, amp=0.15)
    p6 >> sinepad(var([0, 5, 3, 4], 8),room=1, dur=[1,1,0.75,0.25], oct=3, amp=0.07)
    d1 >> play(".o.o", dur=2,room=8,amp=0.06).every(6,"stutter", 2).every(8, "stutter", 4).every(12,"stutter",8).every(16,"stutter",3)
    d2 >> play("V.V.v", dur=[1,1,0.75,0.25],amp=0.07).every(6,"stutter", 2).every(16, "stutter", 4).every(12,"stutter",8).every(8,"stutter",3)
    d3 >> play("rczC/%", dur=3,rate=[0.5,1,4,6,40],sample=[1,2,3],amp=0.02).every(8,"stutter", 8).every(16,"stutter",16)
    Clock.future(32, kicks) 
def kicks():  
    p1 >> blip(var([0, 5, 3, 4], 8), dur=[4,4],room=3,chop=0.8,oct=3,amp=0.2)
    p2 >> sinepad(var([0, 5, 3, 4], 8), dur=[8],room=3,chop=0.5,oct=3,amp=0.1) + (0, 2,4,6,7,11)
    p3 >> keys(var([0, 5, 3, 4], 8), dur=[2,2,2,2],room=4,chop=2,amp=[0.05,0.03,0.02,0.06]) + (0, 2,4,6,11)
    p4 >> bass(var([0, 5, 3, 4], 8),room=2, dur=[1,1,0.75,0.25], oct=4, amp=0.15).every(6,"stutter", 2).every(8, "stutter", 4).every(12,"stutter",8).every(16,"stutter",3)
    p5 >> sinepad(var([0, 5, 3, 4], 8),room=1, dur=[1,1,0.75,0.25], oct=3, amp=0.07)
    d1 >> play(".o.oo", dur=[1,1,1,0.75,0.25],amp=0.06).every(6,"stutter", 2).every(8, "stutter", 4).every(12,"stutter",8).every(16,"stutter",3)
    d2 >> play("V.v.v", dur=[1,1,0.75,0.25],amp=0.07).every(6,"stutter", 2).every(16, "stutter", 4).every(12,"stutter",8).every(8,"stutter",3)
    d3 >> play("rczC/%", dur=3,rate=[0.5,1,4,6,40],sample=[1,2,3],amp=0.02).every(8,"stutter", 8).every(16,"stutter",16).every(8,"stutter",3) 
    Clock.future(64, voxx) 
def voxx():
    p1 >> blip(var([0, 5, 3, 4], 8), dur=[2,1,2,3],room=3,chop=0.8,oct=3,amp=0.2)#poner abajo
    p2 >> sinepad(var([0, 5, 3, 4], 8), dur=[2,4,2],room=3,chop=0.5,oct=30,amp=0.1) + (0, 2,4,6,7)
    p3 >> pads(var([0, 5, 3, 4], 8), dur=[8],room=4,chop=2,amp=[0.09,0.08],oct=4) + (0, 2,4,6)
    p4.stop()
    p5.stop()
    d1 >> play(".o.oo", dur=[1,1,1,0.75,0.25],amp=0.06).every(6,"stutter", 2).every(8, "stutter", 4).every(12,"stutter",8).every(16,"stutter",3)
    d2 >> play("cC123j", dur=3,rate=[0.5,1,4,6,40],sample=[1,2,3,4],amp=[0.02,0.01]).every(8,"stutter", 8)
    d3 >> play("V", dur=2,amp=0.08).every(16, "stutter", 3)
    Clock.future(97, finn)
def finn():
    p1 >> ambi(var([0, 5, 3, 4], 8), dur=[8],room=3,chop=0.8,oct=3,amp=0.2)
    p2 >> sinepad(var([0, 5, 3, 4], 8), dur=[8],room=3,chop=0.5,oct=4,amp=0.1) + (0, 2,4,6,7)
    p3 >> space(var([0, 5, 3, 4], 8), dur=[2,1,2,3],room=4,chop=2,amp=[0.04,0.02],oct=3) + (0, 2,4,6)
    p4.stop()
    p5.stop()
    d1.stop()
    d2.stop()
    d3 >> play("V", dur=2,amp=0.07).every(8, "stutter", 3)
    Clock.future(32, closes)
def closes():
    p1 >> soprano(var([0], 32), dur=[32],room=13,chop=0.8,oct=4,amp=0.4,glide=1)
    p2 >> sinepad(var([0,], 32), dur=[32],room=18,chop=0.5,oct=4,amp=0.3,glide=2) + (0, 2,4,6,7)
    p4.stop()
    p5.stop()
    d1.stop()
    d2.stop()
    d3.stop()
    d4.stop()
    Clock.future(32, closes1)
def closes1():
    p1.stop()
    p2.stop()
    p3.stop()
    p4.stop()
    p5.stop()
    d1.stop()
    d2.stop()
    d3.stop()
    d4.stop()
primera()

closes()
#------------------------------------------------------------------------------------------------
