#MUStudy.py
#########################################################################################################################
#This is a program written to assistant musicians in the Navy in studying for advancement exams.  This program simulates#
#the types of questions a musician might experience on the actual exams.  The program can be expanded by creating       #
#more lists and dictionaries (memorized music, transposition, etc.) and by using available data in new functions.       #
#########################################################################################################################


from random import *
#Except where noted, pitch "numbers" refer to either relationships between pitches or, in the case of specific note
#values, the numbers refer to a "fixed do" notion whereby 0 corresponds to the pitch "C", 1 to Db, etc.
#Define constants
#Scale Degrees Major
tonicMaj = {"pitch":0, "name":"Tonic", "mode": "Major"}
supertonicMaj = {"pitch":2, "name":"Supertonic", "mode": "Major"}
mediantMaj = {"pitch": 4, "name": "Mediant", "mode": "Major"}
subDomMaj = {"pitch": 5, "name": "Sub-Dominant", "mode": "Major"}
domMaj = {"pitch": 7, "name": "Dominant", "mode": "Major"}
subMedMaj = {"pitch": 9, "name": "Sub-Mediant", "mode": "Major"}
leadToneMaj = {"pitch": 11, "name": "Leading Tone", "mode": "Major"}

#Scale Degrees Dorian
tonicDor = {"pitch": 0, "name": "Tonic", "mode": "Dorian"}
supertonicDor ={"pitch": 2, "name": "Supertonic", "mode": "Dorian"}
mediantDor = {"pitch": 3, "name": "Mediant", "mode": "Dorian"}
subDomDor = {"pitch": 5, "name": "Sub-Dominant", "mode": "Dorian"}
domDor = {"pitch": 7, "name": "Dominant", "mode": "Dorian"}
subMedDor = {"pitch": 9, "name": "Sub-Mediant", "mode": "Dorian"}
subTonicDor = {"pitch": 10, "name": "Sub-Tonic", "mode": "Dorian"}

#Scale Degrees Phrygian
tonicPhr = {"pitch": 0, "name": "Tonic", "mode": "Phrygian"}
supertonicPhr = {"pitch": 1, "name": "Supertonic", "mode": "Phrygian"}
mediantPhr = {"pitch": 3, "name": "Mediant", "mode": "Phrygian"}
subDomPhr = {"pitch": 5, "name": "Sub-Dominant", "mode": "Phrygian"}
domPhr = {"pitch": 7, "name": "Dominant", "mode": "Phrygian"}
subMedPhr = {"pitch": 8, "name": "Sub-Mediant", "mode": "Phrygian"}
subTonicPhr = {"pitch": 10, "name": "Sub-Tonic", "mode": "Phrygian"}

#Scale Degrees Lydian
tonicLyd = {"pitch": 0, "name": "Tonic", "mode": "Lydian"}
supertonicLyd ={"pitch": 2, "name": "Supertonic", "mode": "Lydian"}
mediantLyd ={"pitch": 4, "name": "Mediant", "mode": "Lydian"}
subDomLyd = {"pitch": 6, "name": "Sub-Dominant", "mode": "Lydian"}
domLyd ={"pitch": 7, "name": "Dominant", "mode": "Lydian"}
subMedLyd = {"pitch": 9, "name": "Sub-Mediant", "mode": "Lydian"}
leadTonLyd ={"pitch": 11, "name": "Leading Tone", "mode": "Lydian"}

#Scale Degrees Mixolydian
tonicMixo = {"pitch": 0, "name": "Tonic", "mode": "Mixolydian"}
supertonMixo = {"pitch": 2, "name": "Supertonic", "mode": "Mixolydian"}
medMixo ={"pitch": 4, "name": "Mediant", "mode": "Mixolydian"}
subDomMixo ={"pitch": 5, "name": "Sub-Dominant", "mode": "Mixolydian"}
domMixo ={"pitch": 7, "name": "Dominant", "mode": "Mixolydian"}
subMedMixo = {"pitch": 9, "name": "Sub-Mediant", "mode": "Mixolydian"}
subTonMixo = {"pitch": 10, "name": "Sub-Tonic", "mode": "Mixolydian"}

#Scale Degrees for Aeolian
tonicAeo = {"pitch": 0, "name": "Tonic", "mode": "Aeolian"}
supertonAeo = {"pitch": 2, "name": "Supertonic", "mode": "Aeolian"}
mediantAeo = {"pitch": 3, "name": "Mediant", "mode": "Aeolian"}
subDomAeo = {"pitch": 5, "name": "Sub-Dominant", "mode": "Aeolian"}
domAeo ={"pitch": 7, "name": "Dominant", "mode": "Aeolian"}
subMedAeo = {"pitch": 8, "name": "Sub-Mediant", "mode": "Aeolian"}
subTonAeo = {"pitch": 10, "name": "Sub-Tonic", "mode": "Aeolian"}

#Scale Degrees for Locrian
tonicLoc ={"pitch": 0, "name": "Tonic", "mode": "Locrian"}
superTonLoc ={"pitch": 1, "name": "Supertonic", "mode": "Locrian"}
medLoc ={"pitch": 3, "name": "Mediant", "mode": "Locrian"}
subDomLoc ={"pitch": 5, "name": "Sub-Dominant", "mode": "Locrian"}
domLoc ={"pitch":6, "name": "Dominant", "mode": "Locrian"}
subMedLoc ={"pitch": 8, "name": "Sub-Mediant", "mode": "Locrian"}
subTonLoc ={"pitch": 10, "name": "Sub-Tonic", "mode": "Locrian"}

#Scale Degrees for Harmoic Minor
tonicHar ={"pitch": 0, "name": "Tonic", "mode": "Harmonic Minor"}
suptonHar ={"pitch": 2, "name": "Supertonic", "mode": "Harmonic Minor"}
medHar={"pitch": 3, "name": "Mediant", "mode": "Harmonic Minor"}
subDomHar={"pitch": 5, "name": "Sub-Dominant", "mode": "Harmonic Minor"}
domHar={"pitch": 7, "name": "Dominant", "mode": "Harmonic Minor"}
subMedHar ={"pitch": 8, "name": "Sub-Mediant", "mode": "Harmonic Minor"}
leadHar={"pitch": 11, "name": "Leading Tone", "mode": "Harmonic Minor"}

#Scale degrees for Melodic Minor (only the upper tetrachord)
subMedAscending = {"pitch": 9, "name": "Sub-Mediant(ascending)", "mode": "Melodic Minor"}
leadTonAscending ={"pitch": 11, "name": "Leading Tone(ascending)", "mode": "Melodic Minor"}
leadTonDescending ={"pitch": 10, "name": "Leading Tone(descending)", "mode": "Melodic Minor"}
subMedDescending ={"pitch": 8, "name": "Sub-Mediant(descending)", "mode": "Melodic Minor"}

#Pitch Directions
m2Down = {"distance": -1, "name":"minor second below"}
m2Up = {"distance": 1, "name": "minor second above"}
maj2Down = {"distance": -2, "name": "major second below"}
maj2Up = {"distance": 2, "name": "major second above"}
m3Down = {"distance": -3, "name": "minor third below"}
m3Up = {"distance": 3, "name": "minor third above"}
maj3Down = {"distance": -4, "name": "major third below"}
p4Down = {"distance": -5, "name": "perfect fifth below"}
p4Up = {"distance": 5, "name": "perfect fifth above"}
aug4Up = {"distance": 6, "name": "tritone above"}
aug4Down = {"distance": -6, "name": "tritone below"}
p5Down ={"distance": -7, "name": "perfect fifth below" }
p5Up = {"distance": 7, "name": "perfect fifth above"}
m6Down = {"distance": -8, "name": "minor sixth below"}
m6Up = {"distance": 8, "name": "minor sixth above"}
maj6Up = {"distance": 9, "name": "major sixth above"}
maj6Down = {"distance": -9, "name":"major sixth below"}
min7Up = {"distance": 10, "name": "minor seventh above"}
min7Down = {"distance": -10, "name": "minor seventh below"}
maj7Up = {"distance": 11, "name": "major seventh above"}
maj7Down = {"distance": -11, "name": "major seventh below"}

#Overtone Series
over1 = {"pitch": 0, "name": "First Overtone"}
over2 = {"pitch": 7, "name": "Second Overtone"}
over3 = {"pitch": 0+12, "name": "Third Overtone"}
over4 = {"pitch": 4+12, "name": "Fourth Overtone"}
over5 = {"pitch": 7+12, "name": "Fifth Overtone"}
over6 = {"pitch": 10+12, "name": "Sixth Overtone"}
over7 = {"pitch": 0+24, "name": "Seventh Overtone"}
over8 = {"pitch": 2 + 24, "name": "Eighth Overtone"}
over9 = {"pitch": 4 + 24, "name": "Ninth Overtone"}
over10 = {"pitch":6 + 24, "name": "Tenth Overtone"}
over11 = {"pitch": 7 + 24, "name": "Eleventh Overtone"}
over12 = {"pitch": 9 + 24, "name": "Twelfth Overtone"}
over13 ={"pitch": 10 + 24, "name": "Thirteenth Overtone"}
over14 ={"pitch": 11 + 24, "name": "Fourteenth Overtone"}
over15={"pitch": 0 + 36, "name": "Fifteenth Overtone"}


#partials
par1 = {"pitch": 0, "name": "First Partial"}
par2 = {"pitch": 0, "name": "Second Partial"}
par3= {"pitch": 7, "name": "Third Partial"}
par4 ={"pitch": 0, "name": "Fourth Partial"}
par5={"pitch": 4, "name": "Fifth Partial"}
par6={"pitch": 7, "name": "Sixth Partial"}
par7={"pitch": 10, "name": "Seventh Partial"}
par8={"pitch": 0, "name": "Eighth Partial"}
par9={"pitch": 2, "name":"Ninth Partial" }
par10={"pitch": 4, "name": "Tenth Partial"}
par11 ={"pitch": 6, "name": "Eleventh Partial"}
par12 ={"pitch": 7, "name": "Twelfth Partial"}
par13 ={"pitch": 9, "name": "Thirteenth Partial"}
par14 = {"pitch": 10, "name": "Fourteenth Partial"}
par15 = {"pitch": 11, "name": "Fifteenth Partial"}
par16 ={"pitch": 0, "name": "Sixteenth Partial"}

#Staffs (breakdown of the grandstaff into different clefs)
#12 is added to put those pitches into a the correct octave displacement relative to notes that come lower
#Bass Clef staff
bassLine1 = {"pitch": 7, "name": "G", "clef": "bass", "location": "first line"}
bassSpace1 = {"pitch": 9, "name": "A", "clef": "bass", "location": "first space"}
bassLine2 = {"pitch": 11, "name": "B", "clef": "bass", "location": "second line"}
#Add 12 to position the pitch octaves relative to place on staff
bassSpace2 = {"pitch": 0+12, "name": "C", "clef": "bass", "location": "second space"}
bassLine3 = {"pitch": 2+12, "name": "D", "clef": "bass", "location": "third line"}
bassSpace3 = {"pitch": 4+12, "name": "E", "clef": "bass", "location": "third space"}
bassLine4 = {"pitch": 6+12, "name": "F", "clef": "bass", "location": "fourth line"}
bassSpace4 = {"pitch": 7+12, "name": "G", "clef": "bass", "location": "fourth space"}
bassLine5 = {"pitch": 9+12, "name": "A", "clef": "bass", "location": "fifth line"}

#treble clef staff
#Add 24 to the pitches to place them in the proper octave on the grand staff (i.e., higher than the bass clef notes)
trebLine1 = {"pitch": 4+24, "name": "E", "location": "first line", "clef": "treble"}
trebSpace1 = {"pitch": 5+24, "name": "F", "location": "first space", "clef": "treble"}
trebLine2 = {"pitch": 7+24, "name": "G", "location": "second line", "clef": "treble"}
trebSpace2 = {"pitch": 9+24, "name": "A", "location": "second space", "clef": "treble"}
trebLine3 = {"pitch": 11+24, "name": "B", "location": "third line", "clef": "treble"}
trebSpace3 = {"pitch": 0+36, "name": "C", "location": "third space", "clef": "treble"}
trebLine4 = {"pitch": 2+36, "name": "D", "location": "fourth line", "clef": "treble"}
trebSpace4 = {"pitch": 4+36, "name": "E", "location": "fourth space", "clef": "treble"}
trebLine5 = {"pitch": 5+36, "name": "F", "location": "fifth line", "clef": "treble"}

#tenor clef
tenLine1 = {"pitch": 2, "name": "D", "location": "first line", "clef": "tenor"}
tenSpace1 = {"pitch": 4, "name": "E", "location": "first space", "clef": "tenor"}
tenLine2 = {"pitch": 5, "name": "F", "location": "second line", "clef": "tenor"}
tenSpace2 = {"pitch": 7, "name": "G", "location": "second space", "clef": "tenor"}
tenLine3 = {"pitch": 9, "name": "A", "location": "third line", "clef": "tenor"}
tenSpace3 = {"pitch": 11, "name": "B", "location": "third space", "clef": "tenor"}
tenLine4 = {"pitch": 0+12, "name": "C", "location": "fourth line", "clef": "tenor"}
tenSpace4 = {"pitch": 2+12, "name": "D", "location": "fourth space", "clef": "tenor"}
tenLine5 = {"pitch": 4+12, "name": "E", "location": "fifth line", "clef": "tenor"}


#Alto clef
altoLine1 = {"pitch": 5, "name": "F", "location": "first line", "clef": "alto"}
altoSpace1 = {"pitch": 7, "name": "G", "location":"first space", "clef": "alto"}
altoLine2 = {"pitch": 9, "name": "A", "location": "second line", "clef": "alto"}
altoSpace2 = {"pitch": 11, "name": "B", "location": "second space", "clef": "alto"}
altoLine3 = {"pitch": 0+12, "name": "C", "location": "third line", "clef": "alto"}
altoSpace3 = {"pitch": 2+12, "name": "D", "location": "third space", "clef": "alto"}
altoLine4 = {"pitch": 4+12, "name": "E", "location": "fourth line", "clef": "alto"}
altoSapce4 = {"pitch": 5+12, "name": "F", "location": "fourth space", "clef": "alto"}
altoLine5 = {"pitch": 7+12, "name": "G", "location": "fifth line", "clef": "alto"}

#Pitch names mapped to numbers
bs = {"pitch": 0, "name": "B#", "nameMajor": "B major", "nameDor": "B# Dorian", "namePhr": "B# Phrygian",
      "nameLyd":"B# Lydian", "nameMixo": "B# Mixolydian", "nameAeo": "B# Aeolian", "nameLoc": "B# Locrian",
      "nameHar": "B# Harmonic Minor", "nameMel": "B# Melodic Minor"}
c ={"pitch":0, "name": "C", "nameMajor": "C Major", "nameDor": "C Dorian", "namePhr": "C Phrygian",
    "nameLyd": "C Lydian", "nameMixo": "C Mixolydian", "nameAeo": "C Aeolian", "nameLoc": "C Locrian",
    "nameHar": "C Harmonic Minor", "nameMel": "C Melodic Minor"}
cs ={"pitch":1, "name": "C#", "nameMajor": "C# Major", "nameDor": "C# Dorian", "namePhr": "C# Phrygian",
     "nameLyd": "C# Lydian", "nameMixo":"C# Mixolydian", "nameAeo": "C# Aeolian", "nameLoc": "C# Locrian",
     "nameHar": "C# Harmonic Minor", "nameMel": "C# Melodic Minor"}
db ={"pitch": 1, "name": "Db", "nameMajor": "Db Major", "nameDor": "Db Dorian", "namePhr": "Db Phrygian",
     "nameLyd": "Db Lydian", "nameMixo": "Db Mixolydian", "nameAeo": "Db Aeolian", "nameLoc": "Db Locrian",
     "nameHar": "Db Harmonic Minor", "nameMel": "Db Melodic Minor"}
d = {"pitch": 2, "name": "D", "nameMajor": "D Major", "nameDor": "D Dorian", "namePhr": "D Phrygian",
     "nameLyd": "D Lydian", "nameMixo": "D Mixolydian", "nameAeo": "D Aeolian", "nameLoc": "D Locrian",
     "nameHar": "D Harmonic Minor", "nameMel": "D Melodic Minor"}
ds = {"pitch": 3, "name": "D#", "nameMajor": "D# Major", "nameDor": "D# Dorian", "namePhr": "D# Phrygian",
      "nameLyd": "D# Lydian", "nameMixo": "D# Mixolydian", "nameAeo": "D# Aeolian", "nameLoc": "D# Locrian",
      "nameMel": "D# Melodic Minor"}
ef = {"pitch": 3, "name":"Eb", "nameMajor": "Eb Major", "nameDor": "Eb Dorian", "namePhr": "Eb Phrygian",
      "nameLyd": "Eb Lydian", "nameMixo": "Eb Mixolydian", "nameAeo": "Eb Aeolian", "nameLoc": "Eb Locrian",
      "nameHar": "Eb Harmonic Minor", "nameMel": "Eb Melodic Minor"}
e = {"pitch": 4, "name": "E", "nameMajor": "E Major", "nameDor": "E Dorian", "namePhr": "E Phrygian",
     "nameLyd": "E Lydian", "nameMixo": "E Mixolydian", "nameAeo": "E Aeolian", "nameLoc": "E Locrian",
     "nameHar": "E Harmonic Minor", "nameMel": "E Melodic Minor"}
f = {"pitch": 5, "name": "F", "nameMajor": "F Major", "nameDor": "F Dorian", "namePhr": "F Phrygian",
     "nameLyd": "F Lydian", "nameMixo": "F Mixolydian", "nameAeo": "F Aeolian", "nameLoc": "F Locrian",
     "nameHar": "F Harmonic Minor", "nameMel": "F Melodic Minor"}
es = {"pitch": 5, "name": "E#", "nameMajor": "E# Major", "nameDor": "E# Dorian", "namePhr": "E# Phrygian",
      "nameLyd": "E# Lydian", "nameMixo": "E# Mixolydian", "nameAeo": "E# Aeolian", "nameLoc": "E# Locrian",
      "nameHar": "E# Harmonic Minor", "nameMel": "E# Harmonic Minor"}
fs = {"pitch": 6, "name": "F#", "nameMajor": "F# Major", "nameDor": "F# Dorian", "namePhr": "F# Phrygian",
      "nameLyd": "F# Lydian", "nameMixo": "F# Mixolydian", "nameAeo": "F# Aeolian", "nameLoc": "F# Locrian",
      "nameHar": "F# Harmonic Minor", "nameMel": "F# Melodic Minor"}
gf = {"pitch": 6, "name": "Gb", "nameMajor": "Gb Major", "nameDor": "Gb Dorian", "namePhr": "Gb Phrygian",
      "nameLyd": "Gb Lydian", "nameMixo": "Gb Mixolydian", "nameAeo": "Gb Aeolian", "nameLoc": "Gb Locrian",
      "nameHar": "Gb Harmonic Minor", "nameMel": "Gb Melodic Minor"}
g = {"pitch": 7, "name": "G", "nameMajor": "G Major", "nameDor": "G Dorian", "namePhr": "G Phrygian",
     "nameLyd": "G Lydian", "nameMixo": "G Mixolydian", "nameAeo": "G Aeolian", "nameLoc": "G Locrian",
     "nameHar": "G Harmonic Minor", "nameMel": "G Melodic Minor"}
gs ={"pitch": 8, "name": "G#", "nameMajor": "G# Major", "nameDor": "G# Dorian", "namePhr": "G# Phrygian",
     "nameLyd": "G# Lydian", "nameMixo": "G# Mixolydian", "nameAeo": "G# Aeolian", "nameLoc": "G# Locrian",
     "nameHar": "G# Harmonic Minor", "nameMel": "G# Melodic Minor"}
af ={"pitch": 8, "name": "Ab", "nameMajor": "Ab Major", "nameDor": "Ab Dorian", "namePhr": "Ab Phrygian",
     "nameLyd": "Ab Lydian", "nameMixo": "Ab Mixolydian", "nameAeo": "Ab Aeolian", "nameLoc": "Ab Locrian",
     "nameHar": "Ab Harmonic Minor", "nameMel": "Ab Melodic Minor"}
a = {"pitch": 9, "name": "A", "nameMajor": "A Major", "nameDor": "A Dorian", "namePhr": "A Phrygian",
     "nameLyd": "A Lydian", "nameMixo": "A Mixolydian", "nameAeo": "A Aeolian", "nameLoc": "A Locrian",
     "nameHar": "A Harmonic Minor", "nameMel": "A Melodic Minor"}
aSharp = {"pitch": 10, "name":"A#", "nameMajor": "A# Major", "nameDor": "A# Dorian", "namePhr": "A# Phrygian",
          "nameLyd": "A# Lydian", "nameMixo": "A# Mixolydian", "nameAeo": "A# Aeolian", "nameLoc": "A# Locrian",
          "nameHar": "A# Harmonic Minor", "nameMel": "A# Melodic Minor"}
bf ={"pitch": 10, "name": "Bb", "nameMajor": "Bb Major", "nameDor": "Bb Dorian","namePhr": "Bb Phrygian",
     "nameLyd": "Bb Lydian", "nameMixo": "Bb MixoLydian", "nameAeo": "Bb Aeolian", "nameLoc": "Bb Locrian",
     "nameHar": "Bb Harmonic Minor", "nameMel": "Bb Melodic Minor"}
b = {"pitch": 11, "name": "B", "nameMajor": "B Major", "nameDor": "B Dorian", "namePhr": "B Phrygian",
     "nameLyd": "B Lydian", "nameMixo": "B Mixolydian", "nameAeo":"B Aeolian", "nameLoc": "B Locrian",
     "nameHar": "B Harmonic Minor", "nameMel": "B Melodic Minor"}
cf ={"pitch": 11, "name": "Cb", "nameMajor": "Cb Major", "nameDor": "C Dorian", "namePhr": "C Phrygian",
     "nameLyd": "Cb Lydian", "nameMixo": "Cb Mixolydian", "nameAeo": "Cb Aeolian", "nameLoc": "Cb Locrian",
     "nameHar": "Cb Harmonic Minor", "nameMel": "Cb Melodic Minor"}

#Lists of variables for indexing
#Major Scale
majorScaleDegrees = [tonicMaj, supertonicMaj, mediantMaj, subDomMaj, domMaj, subMedMaj, leadToneMaj]
#Dorian Scale
dorianScaleDegrees = [tonicDor, supertonicDor, mediantDor, subDomDor, domDor, subMedDor, subTonicDor]
#Phrygian Scale
phrygianScaleDegrees = [tonicPhr, supertonicPhr, mediantPhr, subDomPhr, domPhr, subMedPhr, subTonicPhr]
#Lydian Scale
lydianScaleDegrees = [tonicLyd, supertonicLyd, mediantLyd, subDomLyd, domLyd, subMedLyd, leadTonLyd]
#Mixolydian Scale Degrees
mixoScaleDegrees = [tonicMixo, supertonMixo, medMixo, subDomMixo, domMixo, subMedMixo, subTonMixo]
#Aeolian Scale Degrees
aeoScaleDegrees = [tonicAeo, supertonAeo, mediantAeo, subDomAeo, domAeo, subMedAeo, subTonAeo]
#Locrian Scale Degrees
locScaleDegrees = [tonicLoc, superTonLoc, medLoc, subDomLoc, domLoc, subMedLoc, subTonLoc]
#All of the pitches and their enharmonic spellings
harScaleDegrees = [tonicHar, suptonHar, medHar, subDomHar, domHar, subMedHar, leadHar]
#Melodic Minor Scale
melMinScaleDegrees = [subMedAscending, subMedDescending, leadTonAscending, leadTonDescending]
#Chromatic pitches(chromatic scale with enharmonics)
chromaticPitches = [c, cs, db, d, ds, ef, e, f, es, fs, gf, g, gs, af, a, aSharp, bf, b, cf]
#Interval directions
directions = [m2Down, m2Up, maj2Down, maj2Up, m3Down, m3Up, maj3Down, p4Down, p4Up, aug4Up, aug4Down, p5Down, p5Up, m6Down,
              m6Up, maj6Up, maj6Down, maj7Up, maj7Down, m6Down, m6Up]
#Overtones and partials
overtones = [over1, over2, over3, over4, over5, over6, over7, over8, over9, over10, over11, over12, over13,
             over14, over15]
partials = [par1, par2, par3, par4, par5, par6, par7, par8, par9, par10, par11, par12, par13, par14, par15,
            par16]
#Clefs
bassClef = [bassLine1, bassLine2, bassLine3, bassLine4, bassLine5, bassSpace1, bassSpace2, bassSpace3, bassSpace4]
trebleClef = [trebLine1, trebLine2, trebLine3, trebLine4, trebLine5, trebSpace1, trebSpace2, trebSpace3, trebSpace4]
tenorClef = [tenLine1, tenLine2, tenLine3, tenLine4, tenLine5, tenSpace1, tenSpace2, tenSpace3, tenSpace4]
altoClef = [altoLine1, altoLine2, altoLine3, altoLine4, altoLine5, altoSpace1, altoSpace2, altoSpace3, altoSapce4]
#Random selection from lists to be used as parameters when calling functions
randMajorScaleDegree = choice(majorScaleDegrees)
randDorScaleDegree = choice(dorianScaleDegrees)
randPhrScaleDegree = choice(phrygianScaleDegrees)
randLydScaleDegree = choice(lydianScaleDegrees)
randMixoScaleDegree = choice(mixoScaleDegrees)
randAeoScaleDegree = choice(aeoScaleDegrees)
randLocScaleDegree = choice(locScaleDegrees)
randHarScaleDegree = choice(harScaleDegrees)
randMelScaleDegree = choice(melMinScaleDegrees)
randChromaticPitches = choice(chromaticPitches)
randDirections = choice(directions)
randOvertones = choice(overtones)
randPartials = choice(partials)
randBassClef = choice(bassClef)
randTrebleClef = choice(trebleClef)
randTenorClef = choice(tenorClef)
randAltoClef = choice(altoClef)

#Functions
#Converts a given number of half steps into an interval name
def intervalToName(halfSteps):
    if halfSteps == 0:
        halfSteps = "perfect unison"
    elif halfSteps == 1:
        halfSteps = "minor second"
    elif halfSteps == 2:
        halfSteps = "major second"
    elif halfSteps == 3:
        halfSteps = "minor third"
    elif halfSteps == 4:
        halfSteps = "major third"
    elif halfSteps == 5:
        halfSteps = "perfect fourth"
    elif halfSteps == 6:
        halfSteps = "tritone"
    elif halfSteps == 7:
        halfSteps = "perfect fifth"
    elif halfSteps == 8:
        halfSteps = "minor sixth"
    elif halfSteps == 9:
        halfSteps = "major sixth"
    elif halfSteps == 10:
        halfSteps = "minor seventh"
    elif halfSteps == 11:
        halfSteps ="major seventh"
    return halfSteps
def intervalNameToHalfSteps(name):
    if name == "P1":
        name = 0
    elif name == "m2":
        name = 1
    elif name == "M2":
        name = 2
    elif name == "m3":
        name = 3
    elif name == "M3":
        name = 4
    elif name == "P4":
        name = 5
    elif name == "A4":
        name = 6
    elif name == "d4":
        name = 6
    elif name == "P5":
        name = 7
    elif name == "m6":
        name = 8
    elif name == "M6":
        name = 9
    elif name == "m7":
        name = 10
    elif name == "M7":
        name = 11
    return name
#Converts the name of a pitch (a string) into the corresponding note int (for the purposes of pitch calculation)
def convertToPitchNumber(pitchNumber):
    if pitchNumber == "C" or pitchNumber == "B#":
        pitchNumber = 0
    elif pitchNumber == "C#" or pitchNumber =="Db":
        pitchNumber = 1
    elif pitchNumber == "D":
        pitchNumber = 2
    elif pitchNumber == "D#" or pitchNumber == "Eb":
        pitchNumber = 3
    elif pitchNumber == "E":
        pitchNumber = 4
    elif pitchNumber == "E#" or pitchNumber == "F":
        pitchNumber =5
    elif pitchNumber == "F#" or pitchNumber == "Gb":
        pitchNumber = 6
    elif pitchNumber == "G":
        pitchNumber = 7
    elif pitchNumber == "G#" or pitchNumber == "Ab":
        pitchNumber =8
    elif pitchNumber == "A":
        pitchNumber = 9
    elif pitchNumber == "A#" or pitchNumber == "Bb":
        pitchNumber = 10
    elif pitchNumber == "B":
        pitchNumber = 11
    return pitchNumber
#Converts a numbered pitch to a letter name
def convertToNoteName(pitchNumber):
    if pitchNumber== 0:
        pitchNumber = "C/B#"
    elif pitchNumber == 1:
        pitchNumber = "Db/C#"
    elif pitchNumber == 2:
        pitchNumber = "D"
    elif pitchNumber == 3:
        pitchNumber = "Eb/D#"
    elif pitchNumber == 4:
        pitchNumber = "E/Fb"
    elif pitchNumber == 5:
        pitchNumber = "F/E#"
    elif pitchNumber == 6:
        pitchNumber = "F#/Gb"
    elif pitchNumber == 7:
        pitchNumber = "G"
    elif pitchNumber == 8:
        pitchNumber = "Ab/G#"
    elif pitchNumber == 9:
        pitchNumber = "A"
    elif pitchNumber == 10:
        pitchNumber = "Bb"
    elif pitchNumber == 11:
        pitchNumber = "B/Cb"
    return pitchNumber



def clefMath(clefLoc1, clefName1, clefLoc2, clefName2, clef1Number, clef2Number ):
    print("What is the interval between", clefLoc1, "of the", clefName1, "clef staff and the", clefLoc2,
          "of the", clefName2, "clef staff if you reduce the interval? (P4, m2, M3, etc)")
    answer = abs(clef2Number - clef1Number)%12
    userAnswer = input()
    userAnswer = intervalNameToHalfSteps(userAnswer)
    if answer == userAnswer:
        print("Your answer was correct")
    else:
        print("Your answer was incorrect")
    print("The answer was", intervalToName(answer))

#bass and treble math

def overMath(distanceName, overName, rootName, distanceNumber, overNumber, rootNumber):
    global convertToNoteName
    print("What is a", distanceName, "the", overName, "with a fundamental of", rootName,"?")
    answer = (distanceNumber + overNumber+ rootNumber)%12
    userAnswer = input()
    userAnswer = userAnswer.capitalize()
    convertedUserAnswer = convertToPitchNumber(userAnswer)
    if answer == convertedUserAnswer:
        print("Your answer is correct")
    else:
        print("Your answer is incorrect")
    #convertedAnswer = convertToNoteName(answer)
    print("The answer was:", convertToNoteName(answer))

def parMath(distanceName, partialName, rootName, distance, partialNumber, rootNumber):
    print("A", distanceName,"the", partialName, "of", rootName)
    answer = (distance + partialNumber+rootNumber)%12
    userAnswer = input()
    userAnswer = userAnswer.capitalize()
    convertedUserAnswer = convertToPitchNumber(userAnswer)
    if answer == convertedUserAnswer:
        print("Your answer is correct")
    else:
        print("Your answer is incorrect")
    #convertedAnswer = convertToNoteName(answer)
    print("The answer was:", convertToNoteName(answer))


#Tests the user on their knowledge of scale degrees for different scales
def layeredScaleBlitz(distance, scaleDegree, root, quality, distanceNumber, degreeMode, rootNumber):
    print("The note a",distance, "the", scaleDegree, "of", root, quality)
    answer = (distanceNumber + degreeMode + rootNumber)%12
    userAnswer = input()
    userAnswer = userAnswer.capitalize()
    convertedUser = convertToPitchNumber(userAnswer)
    if answer == convertedUser:
        print("Your answer is correct")
    else:
        print("Your answer is incorrect")
    print("The answer was:", convertToNoteName(answer))
#Similar to layeredScaleBlitz, but easier.
def scaleBlitz(scaleDegree, root, scaleDegreeName, rootPitch):
    global convertToPitchNumber

    print("The", scaleDegreeName, "of", root) #The question
    answer = (scaleDegree + rootPitch)%12 #The answer is a simple addition of the two intergers.  The % contains the
                                            #answer to one octave.
    #convertedAnswer = convertToPitchNumber(answer)
    userAnswer = input()
    userAnswer = userAnswer.capitalize()#capitalize just the first letter of the user input because the second letter (b or #) should remain "lowered"
    convertedUser = convertToPitchNumber(userAnswer)

    if answer == convertedUser:
        print("Your answer is correct")
    else:
        print("Your answer is incorrect")
    print("The answer was:", convertToNoteName(answer))

def layeredScaleOvertone(distance, overDegreeName, root, distanceNumber, overDegreeNumber, rootNumber):
    print("The note a",distance, "the", overDegreeName, "of", root,)
    answer = (distanceNumber + overDegreeNumber + rootNumber)%12
    userAnswer = input()
    userAnswer = userAnswer.capitalize()
    convertedUser = convertToPitchNumber(userAnswer)
    if answer == convertedUser:
        print("Your answer is correct")
    else:
        print("Your answer is incorrect")
    print("The answer was:", convertToNoteName(answer))

#Asks for a note a specific interval above or below a note located on a given clef
def intervalClef(distance, lineSpaceName, clefName, distanceNumber, clefNumber):
    print("The note a",distance, "the", lineSpaceName, "of the", clefName, "clef")
    answer = (distanceNumber + clefNumber)%12
    userAnswer = input()
    userAnswer = userAnswer.capitalize()
    convertedUser = convertToPitchNumber(userAnswer)
    if answer == convertedUser:
        print("Your answer is correct")
    else:
        print("Your answer is incorrect")
    print("The answer was:", convertToNoteName(answer))

#Asks for the interval between a note on a given clef and an overtone above a given note.
def clefOvertoneInterval(clefLoc1, clefName1, overName, root, clef1Number, overNumber, rootNumber):
    print("What is the interval between", clefLoc1, "of the", clefName1, "clef and the",overName,
          "above the fundamental",root, "if you reduce the interval? (P4, m2, M3, etc)")
    answer = abs((overNumber+rootNumber) - clef1Number)%12
    userAnswer = input()
    userAnswer = intervalNameToHalfSteps(userAnswer)
    if answer == userAnswer:
        print("Your answer was correct")
    else:
        print("Your answer was incorrect")
    print("The answer was", intervalToName(answer))



#Set up a call for the question, randomly selected. THE VALUE OF THE SECOND NUMBER PARAMETER NEEDS TO BE UPDATED WITH EACH NEW QUESTION
randomQuestion = randint(0, 35)


#scale blitz on major scale
if randomQuestion == 0:
     scaleBlitz(randMajorScaleDegree["pitch"], randChromaticPitches["nameMajor"], randMajorScaleDegree["name"], randChromaticPitches["pitch"])
#scale blitz on dorian minor scale
elif randomQuestion == 1:
    scaleBlitz(randDorScaleDegree["pitch"], randChromaticPitches["nameDor"], randDorScaleDegree["name"], randChromaticPitches["pitch"])
#scale blitz on phrygian minor scale
elif randomQuestion == 2:
    scaleBlitz(randPhrScaleDegree["pitch"], randChromaticPitches["namePhr"], randPhrScaleDegree["name"], randChromaticPitches["pitch"])
#scale blitz on lydian major scale
elif randomQuestion == 3:
    scaleBlitz(randLydScaleDegree["pitch"], randChromaticPitches["nameLyd"], randLydScaleDegree["name"], randChromaticPitches["pitch"])
#scale blitz for mixolydian scale
elif randomQuestion == 4:
    scaleBlitz(randMixoScaleDegree["pitch"], randChromaticPitches["nameMixo"], randMixoScaleDegree["name"], randChromaticPitches["pitch"])
#scale blitz for aeolian scale
elif randomQuestion ==5:
    scaleBlitz(randAeoScaleDegree["pitch"], randChromaticPitches["nameAeo"], randAeoScaleDegree["name"], randChromaticPitches["pitch"])
#scale blitz for locrian scale
elif randomQuestion == 6:
    scaleBlitz(randLocScaleDegree["pitch"], randChromaticPitches["nameLoc"], randLocScaleDegree["name"], randChromaticPitches["pitch"])
#scale blitz for harmonic minor
elif randomQuestion == 7:
    scaleBlitz(randHarScaleDegree["pitch"], randChromaticPitches["nameHar"], randHarScaleDegree["name"], randChromaticPitches['pitch'])
#scale blitz for the melodic minor scale
elif randomQuestion == 8:
    scaleBlitz(randMelScaleDegree["pitch"], randChromaticPitches["nameMel"], randMelScaleDegree["name"], randChromaticPitches["pitch"])
#layerd scale blitz for major scale
elif randomQuestion == 9:
  layeredScaleBlitz(randDirections["name"],randMajorScaleDegree["name"], randChromaticPitches["name"], randMajorScaleDegree["mode"],
                  randDirections["distance"], randMajorScaleDegree["pitch"], randChromaticPitches["pitch"])
#layered scale blitz for aeolian mode (natural minor scale)
elif randomQuestion == 10:
    layeredScaleBlitz(randDirections["name"], randAeoScaleDegree["name"], randChromaticPitches["name"], randAeoScaleDegree["mode"],
                      randDirections["distance"], randAeoScaleDegree["pitch"], randChromaticPitches["pitch"])
#Layered scale blitz for dorian.
elif randomQuestion == 11:
    layeredScaleBlitz(randDirections["name"], randDorScaleDegree["name"], randChromaticPitches["name"], randDorScaleDegree["mode"],
                      randDirections["distance"], randDorScaleDegree["pitch"], randChromaticPitches["pitch"])
elif randomQuestion == 12:
    layeredScaleBlitz(randDirections["name"], randDorScaleDegree["name"], randChromaticPitches["name"], randDorScaleDegree["mode"],
                      randDirections["distance"], randDorScaleDegree["pitch"], randChromaticPitches["pitch"])
#Layered scale blitz for phrygian
elif randomQuestion == 13:
    layeredScaleBlitz(randDirections["name"], randPhrScaleDegree["name"], randChromaticPitches["name"], randPhrScaleDegree["mode"],
                      randDirections["distance"], randPhrScaleDegree["pitch"], randChromaticPitches["pitch"])
#Layered scale blitz for lydian
elif randomQuestion == 14:
    layeredScaleBlitz(randDirections["name"], randLydScaleDegree["name"], randChromaticPitches["name"], randLydScaleDegree["mode"],
                      randDirections["distance"], randLydScaleDegree["pitch"], randChromaticPitches["pitch"])
#Layered scale blitz for mixolydian
elif randomQuestion == 15:
    layeredScaleBlitz(randDirections["name"], randMixoScaleDegree["name"], randChromaticPitches["name"], randMixoScaleDegree["mode"],
                      randDirections["distance"], randMixoScaleDegree["pitch"], randChromaticPitches["pitch"])
#Layered scale blitz for locrian
elif randomQuestion == 16:
    layeredScaleBlitz(randDirections["name"], randLocScaleDegree["name"], randChromaticPitches['name'], randLocScaleDegree["mode"],
                      randDirections["distance"], randLocScaleDegree["pitch"], randChromaticPitches["pitch"])
#Layered scale blitz for harmonic minor
elif randomQuestion == 17:
    layeredScaleBlitz(randDirections["name"], randHarScaleDegree["name"], randChromaticPitches["name"], randHarScaleDegree["mode"],
                      randDirections["distance"], randHarScaleDegree["pitch"], randChromaticPitches["pitch"])
#layered scale blitz for meloidc minor
elif randomQuestion == 18:
    layeredScaleBlitz(randDirections["name"], randMelScaleDegree["name"], randChromaticPitches["name"], randMelScaleDegree["mode"],
                      randDirections["distance"], randMelScaleDegree["pitch"], randChromaticPitches["pitch"])
#Overtone math
elif randomQuestion == 19:
    overMath(randDirections["name"], randOvertones["name"], randChromaticPitches["name"], randDirections["distance"],
         randOvertones["pitch"], randChromaticPitches["pitch"])
#Partial math
elif randomQuestion == 20:
    parMath(randDirections["name"], randPartials["name"], randChromaticPitches["name"],
        randDirections["distance"], randPartials["pitch"], randChromaticPitches["pitch"])
#Clef math bass and treble
elif randomQuestion == 21:
    clefMath(randBassClef["location"], randBassClef["clef"], randTrebleClef["location"], randTrebleClef["clef"],
         randBassClef["pitch"], randTrebleClef["pitch"])
#clef math bass and tenor
elif randomQuestion == 22:
    clefMath(randBassClef["location"], randBassClef["clef"], randTenorClef["location"], randTenorClef["clef"],
             randBassClef["pitch"], randTenorClef["pitch"])
#clef math bass and alto
elif randomQuestion == 23:
    clefMath(randBassClef["location"], randBassClef["clef"], randAltoClef["location"], randAltoClef["clef"],
             randBassClef["pitch"], randAltoClef["pitch"])
#clef math treble and tenor
elif randomQuestion == 24:
    clefMath(randTenorClef["location"], randTenorClef["clef"], randTrebleClef["location"], randTrebleClef["clef"],
             randTenorClef["pitch"], randTrebleClef["pitch"])
#clef math treble and alto
elif randomQuestion == 25:
    clefMath(randAltoClef["location"], randAltoClef["clef"], randTrebleClef["location"], randTrebleClef["clef"],
             randAltoClef["pitch"], randTrebleClef["pitch"])
#clef math alto and tenor
elif randomQuestion == 26:
    clefMath(randTenorClef["location"], randTenorClef["clef"], randAltoClef["location"], randAltoClef["clef"],
             randTenorClef["pitch"], randAltoClef["pitch"])
#layered scale and overtone math
elif randomQuestion == 27:
    layeredScaleOvertone(randDirections["name"], randOvertones["name"], randChromaticPitches["name"], randDirections["distance"],
                        randOvertones["pitch"], randChromaticPitches["pitch"])
#intervals from bass clef
elif randomQuestion == 28:
    intervalClef(randDirections["name"], randBassClef["location"], randBassClef["clef"], randDirections["distance"], randBassClef["pitch"])

#intervals from treble clef
elif randomQuestion == 29:
    intervalClef(randDirections["name"], randTrebleClef["location"], randTrebleClef["clef"], randDirections["distance"], randTrebleClef["pitch"])
#intervals from alto clef
elif randomQuestion == 30:
    intervalClef(randDirections["name"], randAltoClef["location"],randAltoClef["clef"], randDirections["distance"], randAltoClef["pitch"])

#intervals from the tenor clef
elif randomQuestion == 31:
    intervalClef(randDirections["name"], randTenorClef["location"], randTenorClef["clef"], randDirections["distance"], randTenorClef["pitch"])

#Interval between bass clef and a note in the overtone series
elif randomQuestion == 32:
    clefOvertoneInterval(randBassClef["location"],randBassClef["clef"], randOvertones["name"],randChromaticPitches["name"], randBassClef["pitch"],
                         randOvertones["pitch"], randChromaticPitches["pitch"] )

#Interval between treble clef and a note in the overtone series
elif randomQuestion == 33:
    clefOvertoneInterval(randTrebleClef["location"], randTrebleClef["clef"], randOvertones["name"], randChromaticPitches["name"], randTrebleClef["pitch"],
                         randOvertones["pitch"], randChromaticPitches["pitch"])

#Interval between alto clef and a note in the overtone series
elif randomQuestion == 34:
    clefOvertoneInterval(randAltoClef["location"], randAltoClef["clef"], randOvertones["name"], randChromaticPitches["name"], randAltoClef["pitch"],
                         randOvertones["pitch"], randChromaticPitches["pitch"])

#Interval between tenor clef note and a note in the overtone series
elif randomQuestion == 35:
    clefOvertoneInterval(randTenorClef["location"], randTenorClef["clef"], randOvertones["name"], randChromaticPitches["name"], randTenorClef["pitch"],
                         randOvertones["pitch"], randChromaticPitches["pitch"])