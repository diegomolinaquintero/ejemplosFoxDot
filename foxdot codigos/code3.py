print(SynthDefs) 
print(Samples) 
print(FxList) 
print(Attributes)  
print(PatternMethods) 

#-------------------------------------------------------------------------

Clock.bpm = 90
Scale.default.set("minor")
Root.default.set("A")



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



