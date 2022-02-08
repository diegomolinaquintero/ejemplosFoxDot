print(SynthDefs) 
print(Samples) 
print(FxList) 
print(Attributes)  
print(PatternMethods) 

#-------------------------------------------------------------------------

Clock.bpm = 60
Scale.default.set("minorPentatonic")
Root.default.set("A")

b1 >> sinepad(dur=[16],beat_dur=1)
b2 >> noise(dur=[0.25],amp=0.6,echo=1)
b3 >> scratch(dur=[1],amp=1,coarse=2)

#---------------------------------------------------------------------------

c1 >> bell([0,2,4,6,8,1,3,5],dur=[2,3,4,1,0.5,0.25,0.25],chop=[2,4,32,16,12],mix=18,room=18,sus=18,drive=[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],amp=0.1)


a7 >> bell([0,1,4,3,2],mix=PRange(8,18), dur= 0.5,oct=2,rate=PRange(-1,1),chop=[16,32,48,1],cut=1/4)

a1 >> pads([0,1,4,3],mix=PRange(5,8), dur= 4,rate=PRange(1,2),drive=0,chop=[16,32,48,1],cut=1/4)

a5 >> soprano([0,1,4,3,2],chop=[32,64,16,3,2,4,1], dur= 0.25,rate=PRange(1,10),amp=0.6,drive=[2,5,1,8],echotime=4,room=20,cut=1/4)

#-------------------------------------------------------------------------
Clock.bpm = 60
Scale.default.set("minorPentatonic")
Root.default.set("C")

#Galaxia
t1 >> klank(dur=16,oct=5)
t2 >> klank(dur=16,oct=2,amp=0.5)
t3 >> klank(dur=16, oct=1, amp=1)
g1 >> space(dur=32,oct=5)
g2 >> feel(dur=16,oct=2,amp=0.5)
g3 >> space(dur=16, oct=1,amp=0.5)
s1.stop()
s2.stop()
s3.stop()
s4.stop()

s1 >> space([0,2,4],dur=[8,4,16], oct=5,amp=1,room=3,chop=6)
s2 >> ambi([0,2,4],dur=32, oct=5,amp=0.7,room=3,chop=4)

s3 >> space([0,2,4],dur=16, oct=5,amp=0.8,room=10,chop=4)


s3 >> space([0,2,4],dur=[8,4,16], oct=7,amp=0.5,room=3,chop=[1,3,6,9,12],echotime=[0.5,0.25,1,2],beat_dur=[2,4]).every(2,"stutter",6).every(8,"stutter",8)


s5 >> soprano([0,2,4],dur=[8,4,16], oct=4,amp=0.5,room=3,chop=[1,3,6,9,12],echotime=[0.5,0.25,1,2],beat_dur=[2,4]).every(2,"stutter",6).every(8,"stutter",8)


s4 >> arpy([0,2,4],dur=[8,4,16], oct=7,amp=0.5,room=3,chop=[1,3,6,9,12],echotime=[0.5,0.25,1,2],beat_dur=[2,4]).every(2,"stutter",6).every(8,"stutter",8)

Clock.bpm = 80
Scale.default.set("minorPentatonic")
Root.default.set("C")

e1 >> sinepad([0,7],dur=12,sus=14,oct=2)
e2 >> sinepad(dur=12,sus=14,oct=5,chop=48)

e3 >> soprano(dur=12,sus=14,oct=[3,4,5,7],chop=[2,4,8,3,6,12])

e4 >> glass(dur=12,sus=14,oct=[3,4,5,7], chop=[2,4,8,3,6,12])

e4 >> ambi([0,7],dur=12,sus=14,oct=[3,4,5,7],chop=[2,4,8,3,6,12])

#-------------------------------------------------------------------------
Clock.bpm = 60
Scale.default.set("minorPentatonic")
Root.default.set("A")


t1 >> klank(dur=16,oct=5)
t2 >> klank(dur=16,oct=2,amp=0.5)
t3 >> klank(dur=16, oct=1, amp=1)
g1 >> space(dur=32,oct=5)
g5 >> space(dur=32,oct=1)
g2 >> feel(dur=16,oct=2,amp=0.5)
g3 >> space(dur=16, oct=1,amp=0.5)
s1.stop()
s2.stop()
s3.stop()
s4.stop()
e3 >> sinepad(dur=32,sus=14,oct=3,chop=48)
e2 >> sinepad(dur=32,sus=14,oct=1)

c1 >> play("xn",amp=1, sample=[0,PRand(7)]).every(6,"stutter",4,dur=3).every(12, "amen")

c2 >> play("Xo",dur=PDur(1,8))

c3 >> play("y  Cc  [qwert]   [cq/w/e/r] [fgghdjs-l]",sample=[0,PRand(7)],chop=[1,4,8,16],room=[1,10,20]).every(4,"stutter",4).every(2,"stutter",8).every(2,"stutter",32)
b3 >> scratch(dur=PDur(3,8),amp=1,coarse=2).every(4,"stutter",4).every(2,"stutter",8).every(2,"stutter",32)
b2 >> noise(dur=PDur(2,8),amp=[0.01,0.03,0.05,0.07,0.1],echo=1).every(4,"stutter",4).every(2,"stutter",8).every(2,"stutter",32)


t1 >> bass(dur=PDur(3,8),oct=3,drive=4,amp=0.5)
t2 >> soprano(dur=4,oct=2,amp=0.5)
t3 >> charm(dur=2, oct=1, amp=1)
g1 >> dab(dur=PDur(3,8),oct=5)
g5 >> dab(dur=2,oct=1)
g2 >> varsaw(dur=6,oct=2,amp=0.5)
g3 >> jbass(dur=PDur(5,8), oct=1,amp=0.5)
s1.stop()
s2.stop()
s3.stop()
s4.stop()
e3 >> ripple(dur=1,sus=14,oct=3,chop=48)
e2 >> razz(dur=32,sus=14,oct=1)



c4 >> play("Vn n", dur=PDur(3,8), amp=1)
#-------------------------------------------------------------------------

a1 >> sinepad(dur=8,amp=0.5,chop=1)

a1 >> pads([0,1,4,3],mix=PRange(5,8), dur= 2,rate=PRange(-10,10),drive=2,chop=16)

a2 >> viola([0,2,4],dur=PDur(3,8),room=1,amp=10,mix=1,chop=8)

a3 >> keys([0,2,(0,2)], dur=4,chop=[12,16,20,24,32],echotime=[2,4,8])

a5 >> keys([1,2,3,4,5,6,7,11], dur=PDur(2,8))

a4 >> zap([0,2,4,8],dur=2,oct=3,amp=0.9,spin=8,chop=8)

a5 >> soprano([0,1,4,3,2],chop=[32,64,16,3,2,4,1], dur= 0.25,rate=PRange(-10,10),amp=0.6,drive=[2,5,1,8],echotime=4,room=20)

a6 >> feel([0,1,4,3,2],chop=1, dur= 4,rate=1,amp=4)
a7.stop()



a8 >> marimba([0,2,4],oct=2,amp=0.7, dur=PRange(3,8))

every


d1 >> play("x", dur=PDur(3,8),striate=PRange(60,100),pshift=PRange(0,100),rate=PRange(-10,10))

hh >> play("Vn n", pan=0.5, dur=PDur(3,8))



p1 >> MidiOut([1,2,3,4],dur=PDur(3,8), amp=0.5)
p6 >> MidiOut([0,1],oct=2,amp=0.4)
p5 >> MidiOut([5,6,7,8,9],dur=PDur(7,8),oct=6, amp=0.3)
a3 >> rave([1,2,3,4], dur=PDur(3,32))
a4 >> keys([5,6,7,8,9], dur=PDur(7,8),oct=7)
a5 >> keys([0,1,2,3,4,5,6,7,8,9], dur=PDur(3,8))
p2 >> play("x * ")
 
# Value is usually between 0.15 and 0.25
Clock.midi_nudge = 0.2

hh.stop()



Replace the pattern
print(P[0, 1, 2, 3].alt([4, 5]))
P[4, 5]
# Useful when used with a Player
p1 >> keys([0, 1, 2, 3], oct=5,dur=(2,1,6.1,3.8,1.8)).every(3, "alt", P[4, 5, 6, 7])

p1 >> pads([0, 1, 2, 3],oct=3, dur=(2,1,6.1,3.8,1.8)).every(3, "mirror")

p1 >> pads([0, 1, 2, 3], dur=(2.3,1.8,3.3)).every(3, "alt", P[4, 5, 6, 7]
