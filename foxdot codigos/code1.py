print(SynthDefs) 
print(Samples) 
print(FxList) 
print(Attributes)  
print(PatternMethods) 

#-------------------------------------------------------------------------

Clock.bpm = 60
Scale.default.set("minor")
Root.default.set("D")




#Primera parte una vuelta sin nada
p1 >> blip(var([0, 5, 3, 4], 8), dur=[4,4],room=3,chop=0.8,oct=3)
p2 >> soprano(var([0, 5, 3, 4], 8), dur=[8],room=3,chop=0.5,oct=4, amp=0.6) + (0, 2,4,6,7,11)#volumen desacio
d4 >> play("n", amp=2, dur=1) 

#una vuelta con redo
p1 >> blip(var([0, 5, 3, 4], 8), dur=[4,4],room=3,chop=0.8,oct=3)
p2 >> soprano(var([0, 5, 3, 4], 8), dur=[8],room=3,chop=0.5,oct=4, amp=0.4) + (0, 2,4,6,7,11)#volumen desacio
d1 >> play(".o.o", dur=1)
d4 >> play("n", amp=2, dur=1) 

#una vuelta redo Bajo
p1 >> blip(var([0, 5, 3, 4], 8), dur=[4,4],room=3,chop=0.8,oct=3)
p2 >> soprano(var([0, 5, 3, 4], 8), dur=[8],room=3,chop=0.5,oct=4, amp=0.4) + (0, 2,4,6,7,11)#volumen desacio
p3 >> bass(var([0, 5, 3, 4], 8),room=2, dur=[1,1,0.75,0.25], oct=4, amp=0.6)
p4 >> sinepad(var([0, 5, 3, 4], 8),room=1, dur=[1,1,0.75,0.25], oct=3, amp=1)
d1 >> play(".o.o", dur=1)
d4 >> play("n", amp=2, dur=1) 


p1 >> blip(var([0, 5, 3, 4], 8), dur=[4,4],room=3,chop=0.8,oct=3)
p2 >> sinepad(var([0, 5, 3, 4], 8), dur=[8],room=3,chop=0.5,oct=3) + (0, 2,4,6,7,11)
p3 >> keys(var([0, 5, 3, 4], 8), dur=[2,2,2,2],room=4,chop=2,amp=[0.5,0.3,0.2,0.6]) + (0, 2,4,6,11)
p4 >> bass(var([0, 5, 3, 4], 8),room=2, dur=[1,1,0.75,0.25], oct=4, amp=0.6)
p5 >> sinepad(var([0, 5, 3, 4], 8),room=1, dur=[1,1,0.75,0.25], oct=3, amp=1)
d1 >> play(".o.oo", dur=[1,1,1,0.75,0.25])
d2 >> play("V.v.v", dur=[1,1,0.75,0.25])

p1 >> blip(var([0, 5, 3, 4], 8), dur=[4,4],room=3,chop=0.8,oct=3)# esta es la cuarta parte
p2 >> sinepad(var([0, 5, 3, 4], 8), dur=[8],room=3,chop=0.5,oct=3) + (0, 2,4,6,7)
p3 >> keys(var([0, 5, 3, 4], 8), dur=[2,2,2,2],room=4,chop=2,amp=[0.5,0.3,0.2,0.6]) + (0, 2,4,6,11)
p4 >> bell(var([0,2,4,6,7],2),dur=[1/2,1/4,1,1/4,4],oct=6,chop=[1,2,4],rate=[1,23,3],amp=[0.5,1,0.2,0.4,1,0.5])
p5 >> bass(var([0, 5, 3, 4], 8),room=2, dur=[1,1,0.75,0.25], oct=4, amp=0.6)
p6 >> sinepad(var([0, 5, 3, 4], 8),room=1, dur=[1,1,0.75,0.25], oct=3, amp=1)
d1 >> play(".o.o", dur=2,room=8).every(6,"stutter", 2).every(8, "stutter", 4).every(12,"stutter",8).every(16,"stutter",3)
d2 >> play("V.V.v", dur=[1,1,0.75,0.25]).every(6,"stutter", 2).every(16, "stutter", 4).every(12,"stutter",8).every(8,"stutter",3)

p1 >> blip(var([0, 5, 3, 4], 8), dur=[4,4],room=3,chop=0.8,oct=3)
p2 >> sinepad(var([0, 5, 3, 4], 8), dur=[8],room=3,chop=0.5,oct=3) + (0, 2,4,6,7)
p3 >> keys(var([0, 5, 3, 4], 8), dur=[2,2,2,2],room=4,chop=2,amp=[0.5,0.3,0.2,0.6]) + (0, 2,4,6,11)
p4 >> bell(var([0,2,4,6,7],2),dur=[1/2,1/4,1,1/4,4],oct=6,chop=[1,2,4],rate=[1,23,3],amp=[0.3,0.1,0.2,0.4,0.7,0.3])
p5 >> bass(var([0, 5, 3, 4], 8),room=2, dur=[1,1,0.75,0.25], oct=4, amp=0.6)
p4 >> sinepad(var([0, 5, 3, 4], 8),room=1, dur=[1,1,0.75,0.25], oct=3, amp=1)
d1 >> play(".o.oo", dur=[1,1,1,0.75,0.25]).every(6,"stutter", 2).every(8, "stutter", 4).every(12,"stutter",8).every(16,"stutter",3)
d2 >> play("V.v.v", dur=[1,1,0.75,0.25]).every(6,"stutter", 2).every(16, "stutter", 4).every(12,"stutter",8).every(8,"stutter",3)







p1 >> blip(var([0, 5, 3, 4], 8), dur=[2,1,2,3],room=3,chop=0.8,oct=3)#poner abajo
p2 >> sinepad(var([0, 5, 3, 4], 8), dur=[2,4,2],room=3,chop=0.5,oct=3) + (0, 2,4,6,7)
p3 >> pads(var([0, 5, 3, 4], 8), dur=[8],room=4,chop=2,amp=[0.5,0.6],oct=4) + (0, 2,4,6)
p4.stop()
p5.stop()
d1 >> play(".o.oo", dur=[1,1,1,0.75,0.25]).every(6,"stutter", 2).every(8, "stutter", 4).every(12,"stutter",8).every(16,"stutter",3)
d2 >> play("cC123j", dur=3,rate=[0.5,1,4,6,40],sample=[1,2,3,4],amp=[0.3,0.2]).every(8,"stutter", 8)
d3 >> play("V", dur=2).every(16, "stutter", 4) .every(12,"stutter",8)


p1 >> ambi(var([0, 5, 3, 4], 8), dur=[8],room=3,chop=0.8,oct=3)
p2 >> sinepad(var([0, 5, 3, 4], 8), dur=[8],room=3,chop=0.5,oct=4) + (0, 2,4,6,7)
p3 >> space(var([0, 5, 3, 4], 8), dur=[2,1,2,3],room=4,chop=2,amp=[0.3,0.2],oct=3) + (0, 2,4,6)
p4.stop()
p5.stop()
d1.stop()
d2.stop()
d3 >> play("V", dur=2).every(8, "stutter", 3) 


p1 >> soprano(var([0], 32), dur=[32],room=13,chop=0.8,oct=4)
p2 >> sinepad(var([0,], 32), dur=[32],room=18,chop=0.5,oct=4) + (0, 2,4,6,7)
p3.stop()
p4.stop()
p5.stop()
d1.stop()
d2.stop()
d3.stop()
d4.stop()

#------------------------------------------------------------------------------------------------


#p1 >> blip(var([0, 5, 3, 4], 8), dur=[1.5,2,2,1.5],room=3,chop=0.5,oct=3)
#p2 >> soprano(var([0], 32), dur=[32],room=13,chop=4,oct=4)
#d4 >> play("n", amp=4, dur=1)

p1 >> blip(var([0, 5, 3, 4], 8), dur=[4,4],room=3,chop=0.8,oct=3)
p2 >> sinepad(var([0, 5, 3, 4], 8), dur=[8],room=3,chop=0.5,oct=3) + (0, 2,4,6,7)
p3 >> pads(var([0, 5, 3, 4], 8), dur=[2,1,2,3],room=4,chop=2,amp=[0.3,0.2],oct=3) + (0, 2,4,6)
p4 >> pads(var([0,2,4,6,7],2),dur=[1/2,1/4,1,1/4,4],oct=6,chop=[1,2,4],rate=[1,23,3],amp=[0.5,0.8])
p5 >> viola(var([0,2,3,6,4],4),dur=[1/4,1/3,1/3,1/4,2],oct=6,chop=[4,2,8],rate=[1,23,3],amp=[0.5,1,0.2,0.4,1,0.5])
d1 >> play(".o.oo", dur=[1,1,1,0.75,0.25]).every(6,"stutter", 2).every(8, "stutter", 4).every(12,"stutter",8).every(16,"stutter",3)
d2 >> play("1rcz2/3%cC", dur=3,rate=[0.5,1,4,6,40],sample=[1,2,3,4],amp=[0.3,0.2],room=10).every(8,"stutter", 8) 
d3 >> play("V.V.v", dur=[1,1,0.75,0.25]).every(16,"stutter",3)

p1.stop()
p2.stop()
p3 >> keys(var([0, 5, 3, 4], 8), dur=[2,1,2,3],room=4,chop=2,amp=[0.3,0.2]) + (0, 2,4,6)
p4 >> bell(var([0,2,4,6,7],2),dur=[1/2,1/4,1,1/4,4],oct=6,chop=[1,2,4],rate=[1,23,3],amp=[0.5,1,0.2,0.4,1,0.5])
p5 >> pluck(var([0,2,3,6,4],4),dur=[1/4,1/3,1/3,1/4,2],oct=6,chop=[4,2,8],rate=[1,23,3],amp=[0.5,0.7,0.2,0.4,0.7,0.5])
d1 >> play(".o.oo", dur=[1,1,1,0.75,0.25]).every(6,"stutter", 2).every(8, "stutter", 4).every(12,"stutter",8).every(16,"stutter",3)
d2 >> play("V.V.v", dur=[1,1,0.75,0.25]).every(6,"stutter", 2).every(16, "stutter", 4).every(12,"stutter",8).every(8,"stutter",3)
d3 >> play("rczC/%", dur=3,rate=[0.5,1,4,6,40],sample=[1,2,3],amp=0.5).every(8,"stutter", 8).every(16,"stutter",16) 


p1 >> ambi(var([0, 5, 3, 4], 8), dur=[8],room=3,chop=0.8,oct=3)#voz otr VEW
p2 >> sinepad(var([0, 5, 3, 4], 8), dur=[8],room=3,chop=0.5,oct=3) + (0, 2,4,6,7)
p3 >> space(var([0, 5, 3, 4], 8), dur=[2,1,2,3],room=4,chop=2,amp=[0.3,0.2],oct=3) + (0, 2,4,6)
p4.stop()
p5.stop()
d1 >> play(".o.o", dur=1).every(3,"stutter", 3).every(6,"stutter", 2).every(8, "stutter", 4).every(12,"stutter",8).every(16,"stutter",3) 
d2.stop()
d3 >> play("V", dur=2).every(4, "stutter", 4).every(6,"stutter", 2).every(8, "stutter", 4).every(12,"stutter",8).every(16,"stutter",3) 

p1 >> ambi(var([0, 5, 3, 4], 8), dur=[8],room=3,chop=0.8,oct=3)
p2 >> sinepad(var([0, 5, 3, 4], 8), dur=[8],room=3,chop=0.5,oct=4) + (0, 2,4,6,7)
p3 >> space(var([0, 5, 3, 4], 8), dur=[2,1,2,3],room=4,chop=2,amp=[0.3,0.2],oct=3) + (0, 2,4,6)
p4.stop()
p5.stop()
d1.stop()
d2.stop()
d3 >> play("V", dur=2).every(8, "stutter", 3) 


p1 >> ambi(var([0, 5, 3, 4], 8), dur=[8],room=3,chop=0.8,oct=3)
p2 >> sinepad(var([0, 5, 3, 4], 8), dur=[8],room=3,chop=0.5,oct=4) + (0, 2,4,6,7)
p3.stop()
p4.stop()
p5.stop()
d1.stop()
d2.stop()
d3.stop()



p1 >> soprano(var([0], 32), dur=[32],room=13,chop=0.8,oct=4)
p2 >> sinepad(var([0,], 32), dur=[32],room=18,chop=0.5,oct=4) + (0, 2,4,6,7)
p3.stop()
p4.stop()
p5.stop()
d1.stop()
d2.stop()
d3.stop()
