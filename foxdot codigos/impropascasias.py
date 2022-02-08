print(SynthDefs) 
print(Samples) 
print(FxList) 
print(Attributes)  
print(PatternMethods) 
print(Scale.names()) 

#-------------------------------------------------------------------------

Clock.bpm = 100
Scale.default.set("chromatic")
Root.default.set("C")


a1 >> space([0,7,16],dur=[1],oct=3,amp=[6])

a1 >> space([4,7,6,11],dur=1,oct=3,amp=[7])

a1 >> space([7,11,18,14,21],dur=1,oct=3,amp=[7])

a1 >> space([19,18,16,12,11,9],dur=1,oct=3,amp=[7])

a1 >> space([7,4,12,9,14,6,11],dur=1,oct=3,amp=[7])

a1 >> space([12,14,16,19,12,14,16,18],dur=1,oct=3,amp=[7])

a1 >> space([12,11,9,12,16,14,12,11,9],dur=16,oct=2,amp=[7])

a1 >> space([16,18,19,18,16,12,14,16,19,18],dur=16,oct=3,amp=[2])

a2 >> pads(amp=0.2)

a1 >> ripple([18],dur=1,oct=4,amp=4,rate=[40,50,60],glide=[60])


p6 >> play("---(-=)%/qwertgfhncsC",rate=[40,12,200,5,440,1],amp=4,dur=0.01).every(4,"stutter",16).every(4,"stutter",8)


a2 >> sinepad([0,5,3,4],dur=8,oct=4, amp=0.5)
a3 >> sinepad([0,5,3,4],dur=8,oct=8, amp=0.2)



p1 >> blip(var([0, 5, 3, 4], 0.5), dur=[2,1,0.5],room=3,chop=0.5).every(4,"stutter",3).every(4,"stutter",4)
p2 >> bug(amp=0.4).follow(p1) + [0,2,4]
p3 >> snick(amp=0.4).follow(p2) + [0,2]
p4 >> razz().follow(p3) + [2,4]
p5 >> play("X/o/").every(4,"stutter",8).every(4,"stutter",4)
p6 >> play("---(-=)").every(4,"stutter",16).every(4,"stutter",8)



p1 >> blip(var([0, 5, 3, 4], 0.5), dur=[2,1,0.5],room=3,chop=0.25).every(4,"stutter",3).every(4,"stutter",4)
p2 >> bug(amp=0.4).follow(p1) + [0,2,4]
p3 >> snick(amp=0.4).follow(p2) + [0,2]
p4 >> razz().follow(p3) + [2,4]
p5 >> play("X/o/").every(4,"stutter",8).every(4,"stutter",4)
p6 >> play("---(-=)").every(4,"stutter",16).every(4,"stutter",8)


p1 >> blip(var([0, 5, 3, 4], 0.25), dur=[2,1,0.5],room=3,chop=0.25).every(4,"stutter",3).every(4,"stutter",4)
p2 >> bug(amp=0.4).follow(p1) + [0,2,4]
p3 >> snick(amp=0.4).follow(p2) + [0,2]
p4 >> razz().follow(p3) + [2,4]
p5 >> play("X/o/")#.every(4,"stutter",8).every(4,"stutter",4)
p6 >> play("---(-=)")#.every(4,"stutter",16).every(4,"stutter",8)

p1 >> blip(var([0, 5, 3, 4], 8), dur=[4],room=3,chop=0.25).every(4,"stutter",3).every(4,"stutter",4)
p2 >> bug(amp=0.4).follow(p1) + [0,2,4]
p3 >> snick(amp=0.4).follow(p2) + [0,2]
p4 >> razz().follow(p3) + [2,4]
p5.stop()
p6.stop()


p1 >> blip(var([0, 5, 3, 4], 16), dur=[32],room=3,chop=0.25).every(4,"stutter",3).every(4,"stutter",4)
p2.stop()
p3.stop()
p4 >> razz().follow(p3) + [(0,2,4)]
p5.stop()
p6.stop()
