print(SynthDefs) 
print(Samples) 
print(FxList) 
print(Attributes)  
print(PatternMethods) 


Clock.bpm = 90
Scale.default.set("minor")
Root.default.set("A")

q1 >> play(" o",dur=3,room=2).every(8,"stutter",room=10,mix=10)

q8 >> play("(lt) ",dur=2,room=5)

q9 >> play("(elb) (zpf) ",dur=0.5,sample=[0,1,2,3,4,5])

q3 >> feel([0,4,5],dur=8,amp=3)

q2 >> glass([4,11,12],dur=8, amp=3)

q9 >> pads([(4,11,12),(0,4,5)],dur=8, amp=0.5, chop=58,echo=4,cut=1/4)

q5 >> quin([0,4],dur=[0.25,0.5],amp=0.5,cut=1/4)

q6 >> dirt([0,4,5,7],dur=[0.25],amp=0.5,cut=1/4)

q4 >> growl([0,4,5],dur=8, amp=0.5,oct=3)

q7 >> pasha([0,4,5],dur=8, amp=0.2,oct=7,slide=4,slidedelay=3,bend=6)

q3.stop()
q4.stop()
q5.stop()
q6.stop()
q7.stop()
q8.stop()


Clock.bpm = 80
Scale.default.set("minorPentatonic")
Root.default.set("E")
    
e1 >> space([0,2,7,8,12],dur=[2,4,1,0.5,0.5],amp=0.5 ,room=4, chop=15,spin=1)#.every(8,"stutter",8,chop=32)
e2 >> sawbass([0,4,3],dur=[4,8,2],echotime=4,vib=4,beat_dur=4, amp=0.8)
e3 >> ripple([2,4,2,4],dur=[0.5,2,0.5,1],chop=12,vib=4,beat_dur=4)
e7 >> keys([(0,2,4),(4,6,8),(3,5,7)],dur=[4,8,2])#.every(4,"amen").every(8,"stutter",2,chop=32)


e4 >> snick([0,2,7,8,12],dur=PDur(3,8),amp=2)
e5 >> play("Xo ", dur = PDur(3,8)).every(12,"amen").every(8,"stutter",2,chop=32)
e6 >> play("f  U", dur = PDur(3,8),sample=[0,1,2,3,4],amp=0.5).every(4,"amen").every(8,"stutter",2,chop=32)


Clock.bpm = 90
Scale.default.set("major")
Root.default.set("G")

a1 >> pads([4,5,4,2,8,8,6,6,7,7,4],dur=[12] ,oct=5 , amp = 0.3)
b1 >> bell([4,5,4,2,8,8,6,6,7,7,4],dur=[12] ,oct=5, amp=0.2)
c1 >> play("x n",dur=3, amp=2)

a1 >> pads([4,5,4,2,8,8,6,6,7,7,4],dur=[6] ,oct=5 , amp = 0.3)
b1 >> bell([4,5,4,2,8,8,6,6,7,7,4],dur=[6] ,oct=5, amp=0.2)
a2 >> pads([2,4,6,6,8,8,4,4,2],dur=[6] ,oct=4, amp = 0.3)
b2 >> bell([2,4,6,6,8,8,4,4,2],dur=[6] ,oct=3, amp= 0.2)
c2 >> play(PZip("Vs"," n"),dur=3, amp=1)


a1 >> soprano([4,5,4,2,8,8,6,6,7,7,4],dur=[1.5,0.5,1,3,2,1,2,1,2,1,3] ,oct=5)
a2 >> soprano([2,4,6,6,8,8,4,4,2],dur=[3,3,2,1,2,1,2,1,3] ,oct=4)

a3 >> soprano([0,2,3,3,6,6,2,2,7],dur=[3,3,2,1,2,1,2,1,3] ,oct=3)
b1 >> pads([4,5,4,2,8,8,6,6,7,7,4],dur=[1.5,0.5,1,3,2,1,2,1,2,1,3] ,oct=5, amp=0.2)
b2 >> pads([2,4,6,6,8,8,4,4,2],dur=[3,3,2,1,2,1,2,1,3] ,oct=3, amp= 0.2)
b3 >> pads([0,2,3,3,6,6,2,2,7],dur=[3,3,2,1,2,1,2,1,3] ,oct=1, amp=0.3)
c1 >> play("[oo]",dur=PDur(3,12), amp=0.4).every(4,"amen")


a1 >> soprano([4,5,4,2,8,8,6,6,7,7,4],dur=[1.5,0.5,1,3,2,1,2,1,2,1,3] ,oct=4)
a2 >> soprano([2,4,6,6,8,8,4,4,2],dur=[3,3,2,1,2,1,2,1,3] ,oct=5)
a3 >> soprano([0,2,3,3,6,6,2,2,7],dur=[3,3,2,1,2,1,2,1,3] ,oct=3)
b1 >> pads([4,5,4,2,8,8,6,6,7,7,4],dur=[1.5,0.5,1,3,2,1,2,1,2,1,3] ,oct=3, amp=0.2)
b2 >> pads([2,4,6,6,8,8,4,4,2],dur=[3,3,2,1,2,1,2,1,3] ,oct=5, amp= 0.2)
b3 >> pads([0,2,3,3,6,6,2,2,7],dur=[3,3,2,1,2,1,2,1,3] ,oct=1, amp=0.3) 
c1 >> play("[oo]",dur=PDur(3,12), amp=0.4)
c2 >> play("Xon",dur=PDur(3,12), amp=1)


a1 >> soprano([4,5,4,2,8,8,6,6,7,7,4],dur=[1.5,0.5,1,3,2,1,2,1,2,1,3] ,oct=4)
a2 >> soprano([2,4,6,6,8,8,4,4,2],dur=[3,3,2,1,2,1,2,1,3] ,oct=3)
a3 >> soprano([0,2,3,3,6,6,2,2,7],dur=[3,3,2,1,2,1,2,1,3] ,oct=5)
b1 >> pads([4,5,4,2,8,8,6,6,7,7,4],dur=[1.5,0.5,1,3,2,1,2,1,2,1,3] ,oct=3, amp=0.2)
b2 >> pads([2,4,6,6,8,8,4,4,2],dur=[3,3,2,1,2,1,2,1,3] ,oct=1, amp= 0.2)
b3 >> pads([0,2,3,3,6,6,2,2,7],dur=[3,3,2,1,2,1,2,1,3] ,oct=5, amp=0.3)
c1 >> play("[oo]",dur=PDur(3,12), amp=0.4)
c2 >> play("Xon",dur=PDur(3,12), amp=1)
c3 >> play("#",dur=6, amp=2, room=2)
c4 >> play("xn",amp=3, sample=[0,PRand(7)]).every(6,"stutter",4,dur=3).every(12, "amen")



a1 >> soprano([4,5,4,2,8,8,6,6,7,7,4],dur=[1.5,0.5,1,3,2,1,2,1,2,1,3] ,oct=3)
a2 >> soprano([2,4,6,6,8,8,4,4,2],dur=[3,3,2,1,2,1,2,1,3] ,oct=4)
a3 >> soprano([0,2,3,3,6,6,2,2,7],dur=[3,3,2,1,2,1,2,1,3] ,oct=5)
b1 >> pads([4,5,4,2,8,8,6,6,7,7,4],dur=[1.5,0.5,1,3,2,1,2,1,2,1,3] ,oct=1, amp=0.2)
b2 >> pads([2,4,6,6,8,8,4,4,2],dur=[3,3,2,1,2,1,2,1,3] ,oct=3, amp= 0.2)
b3 >> pads([0,2,3,3,6,6,2,2,7],dur=[3,3,2,1,2,1,2,1,3] ,oct=5, amp=0.3)
c1 >> play("[oo]",dur=PDur(5,12), amp=0.4)
c2 >> play("Xon",dur=PDur(5,12), amp=1)
c3 >> play("#",dur=3, amp=2, room=2)
c4 >> play("xn",amp=3, sample=[0,PRand(7)]).every(6,"stutter",4,dur=3).every(12, "amen")

a1 >> glass([4,5,4,2,8,8,6,6,7,7,4],dur=[1.5,0.5,1,3,2,1,2,1,2,1,3] ,oct=5)
a2 >> feel([2,4,6,6,8,8,4,4,2],dur=[3,3,2,1,2,1,2,1,3] ,oct=4)
a3 >> ambi([0,2,3,3,6,6,2,2,7],dur=[3,3,2,1,2,1,2,1,3] ,oct=3)
b1 >> bell([4,5,4,2,8,8,6,6,7,7,4],dur=[1.5,0.5,1,3,2,1,2,1,2,1,3] ,oct=5, amp=0.2)
b2 >> bell([2,4,6,6,8,8,4,4,2],dur=[3,3,2,1,2,1,2,1,3] ,oct=3, amp= 0.2)
b3 >> bell([0,2,3,3,6,6,2,2,7],dur=[3,3,2,1,2,1,2,1,3] ,oct=1, amp=0.3)
c1 >> play("[oo]",dur=PDur(7,12), amp=0.4)
c2 >> play("Xon",dur=PDur(8,12), amp=1)
c3 >> play("#",dur=1, amp=2, room=2, chop=3)
c4 >> play("xn",amp=3, sample=[0,PRand(7)]).every(6,"stutter",4,dur=3).every(12, "amen")


a1 >> pads([4,5,4,2,8,8,6,6,7,7,4],dur=[8] ,oct=5 , amp = 0.3)
b1 >> bell([4,5,4,2,8,8,6,6,7,7,4],dur=[8] ,oct=5, amp=0.2)
a2.stop()
b2.stop()
a3.stop()
b3.stop()
c1.stop()
c2.stop()
c3.stop()
c4.stop()

Clock.bpm = 120
Scale.default.set("major")
Root.default.set("F")


p2 >> pluck([0, 1, 2, 3, 4, 5, 6, 7],dur=PDur(2,8)).penta().every(8,"trim",6)
p1 >> saw([7, 0, 3, 1, 7, 4, 5, 2], dur=1/4, oct=[4,3,5]).slider()
d1 >> play("x-o-").every(6.5, "jump", cycle=8)
d1 >> play("x-o-", dur=1/2).every(6, "stutter", 4, dur=3)
d1 >> play("x-o-").every(4, "stutter", 4, dur=1, pan=(-1,1), rate=(4, 1/2))
d1 >> play("x-o-", dur=1/4).every(6, "stutter", dur=3, n=4)
d1 >> play("x-o-").every(4, "trim", 3)
