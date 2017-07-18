# should this be called diatonic.py ?
# are there 7 notes in a diatonic scale?

#diatonic_scale_count = 7
#blues_scale_count = ...

majorintervals = [0, 2, 4, 5, 7, 9, 11]

notes = [['C'], ['C#', ]

class Scale(object):

    def __init__(self, intervals, alias=""):
        self.aliases = []
        self.intervals = intervals
        if len(alias) > 0:
            self.add(alias)

    def add(self, alias):
        self.aliases.append(alias)

    
    






chromatic = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] # short hand way of doing this???

# Returns a new Scale object, rebased on a given one
# Returns 'None' on error
def getRebasedScale(scale, index):
    newintervals = []
    i1 = 0
    val = -1
    newval = -1
    i2 = index 
    maxindex = len(scale.intervals) - 1
    while i1 <= maxindex:
        try:
            prev = val
            prevnew = newval
            val = scale.intervals[i2]        
            if i1 > i2:
                # Wrapping around               
                if prev > val:
                    # First time
                    newval = prevnew + (len(chromatic) - prev)  
                else:
                    newval = prevnew + (val - prev)
            else:
                if i1 == 0:
                    n = val
                newval = val - n
            newintervals.append(newval)
        except IndexError:
            return None
        i1 += 1
        if i2 == maxindex:
            i2 = 0
        else:
            i2 += 1
   # print newintervals
    return Scale(newintervals)

major = Scale(majorintervals, "Major")
dorian = getRebasedScale(major, 1)
dorian.add("Dorian")
phyrgian = getRebasedScale(major, 2)
phyrgian.add("Phyrgian")
lydian = getRebasedScale(major, 3)
lydian.add("Lydian")
mixolydian = getRebasedScale(major, 4)
mixolydian.add("Mixolydian")
aeolian = getRebasedScale(major, 5)
aeolian.add("Aeolian")
aeolian.add("Minor")
locrian = getRebasedScale(major, 6)
locrian.add("Locrian")

#print major.intervals
print dorian.intervals
#print phyrgian
 

