print(SynthDefs) 
print(Samples) 
print(FxList) 
print(Attributes)  
print(PatternMethods) 



Clock.bpm = 240
Scale.default.set("minorPentatonic")
Root.default.set("A")

a1 >> sinepad(dur=8)

a1 >> pads([0,1,4,3],mix=PRange(5,8), dur= 2,rate=PRange(-10,10),drive=2,chop=16)

a2 >> space([0,2,4],dur=4,room=5,amp=0.9,mix=10,chop=8)

a3 >> keys([0,2,(0,2)], dur=4,chop=[12,16,20,24,32],echotime=[2,4,8])

a4 >> zap([0,2,4,8],dur=2,oct=3,amp=0.9,spin=8,chop=8)

a5 >> soprano([0,1,4,3,2],chop=[32,64,16,3,2,4], dur= 2,rate=PRange(-10,10),amp=0.1,drive=[2,5,1,8],echotime=4,room=20)

a6 >> feel([0,1,4,3,2],chop=1, dur= 4,rate=1,amp=4)
a7.stop()

a7 >> bell([0,1,4,3,2],mix=PRange(8,18), dur= PDur(3,8),rate=1)

a8 >> marimba([0,2,4],oct=3,amp=5, dur=PDur(3,8))

d1 >> play("x", dur=PDur(3,8))
hh >> play("Vn", pan=0.5, dur=PDur(3,8))



p1 >> MidiOut([1,2,3,4],dur=PDur(3,8), amp=0.5)
p6 >> MidiOut([0,1],oct=2,amp=0.4)
p5 >> MidiOut([5,6,7,8,9],dur=PDur(7,8),oct=6, amp=0.3)
a3 >> rave([1,2,3,4], dur=PDur(3,8))
a4 >> keys([5,6,7,8,9], dur=PDur(7,8),oct=7)
a5 >> keys([0,1,2,3,4,5,6,7,8,9], dur=PDur(3,8))
p2 >> play("x * ")
 
# Value is usually between 0.15 and 0.25
Clock.midi_nudge = 0.2

hh.stop()
