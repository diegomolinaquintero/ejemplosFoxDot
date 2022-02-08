print(SynthDefs) 
print(Samples) 
print(FxList) 
print(Attributes)  
print(PatternMethods) 

#-------------------------------------------------------------------------

Clock.bpm = 60
Scale.default.set("minor")
Root.default.set("Bb")

p1 >> blip(var([0, 5, 3, 4], 8), dur=[4,4],room=3,chop=0.8,oct=3)# esta es la cuarta parte
p2 >> sinepad(var([0, 5, 4], 8), dur=[8],room=3,chop=0.5,oct=3) + (0, 3,4,6,11)
p3 >> keys(var([0, 5, 4], 8), dur=[2,2,2,2],room=4,chop=2,amp=[0.5,0.3,0.2,0.6]) + (0, 3,4,6,11)
p4 >> quin(var([0,3,11,6,7],2),dur=[1,1/2,1,1/2,2],oct=6,chop=[1,2,4,8,16,32],amp=[0.25,0.15,0.25,0.2,0.15,0.5]).every(6,"stutter", 2).every(8, "stutter", 4).every(12,"stutter",8).every(16,"stutter",3)
p5 >> bass(var([0, 5, 4], 8),room=2, dur=[1,1,0.75,0.25], oct=4, amp=0.8)
p6 >> sinepad(var([0, 5, 3, 4], 8),room=1, dur=[1,1,0.75,0.25], oct=3, amp=1)
d1 >> play(".o.o", dur=2,room=8).every(6,"stutter", 2).every(8, "stutter", 4).every(12,"stutter",8).every(16,"stutter",3)
d2 >> play("V.V.v", dur=[1,1,0.75,0.25]).every(6,"stutter", 2).every(16, "stutter", 4).every(12,"stutter",8).every(8,"stutter",3)
d3 >> play("rczC/%", dur=3,rate=[0.5,1,4,6,40],sample=[1,2,3],amp=0.3).every(8,"stutter", 8).every(16,"stutter",16) 


