import numpy

#Functions
def GeometricMean(LineList, Spot):
    values = [x[Spot] for x in LineList]
    GeoMean=1
    for i in range(len(LineList)):
        GeoMean=GeoMean*values[i]
    return(GeoMean**(1/len(LineList)))

def PerformanceScores(a, b, c, d):
    # The number of rows in each matrix will always be three, so I am hard coding it in
    PS=[0]*3
    for x in range(3):
        PS[x]=[a[x]/sum(d), b[x]/sum(c), c[x]/sum(b), d[x]/sum(a)]
    return(PS)


#CONSTANTS AND INPUT
#1 corresponds to equally important
#2-3 correspond to weakly more important
#4-5 corresponds to strongly more important
#6-7 correspond to very strongly more important
#8-9 correspond to absolutely more important

Equal = (1.0,1.0,1.0,1.0)
EqI = (1/2,1.0,1.0,3/2)
InvEqI=(2/3,1,1,2)
Weak = (1,2,2,3)
InvWeak=(1/3,1/2,1/2,1)
Strong = (2,3,3,4)
InvStrong=(1/4,1/3,1/3,1/2)
Very = (5,6,6,7)
InvVery=(1/7,1/6,1/6,1/5)
Abs=(7,8,8,9)
InvAbs=(1/9,1/8,1/8,1/7)

SafetyLine1=[Equal, Equal, Equal, Weak,Strong, EqI, Strong, Strong, EqI]
SafetyLine2=[InvWeak, InvStrong, InvEqI, Equal, Equal, Equal, EqI, EqI,EqI]
SafetyLine3=[InvStrong, InvStrong, InvEqI, InvEqI, InvEqI, InvEqI, Equal, Equal, Equal]

FluctuateLine1 = [Equal, Equal, Equal, EqI, EqI, EqI, Strong, Abs, EqI]
FluctuateLine2= [InvEqI, InvEqI, InvEqI, Equal, Equal, Equal, Abs, Abs, EqI]
FluctuateLine3= [InvStrong, InvAbs, InvEqI, InvAbs, InvAbs, InvEqI, Equal, Equal, Equal]

ProfitabilityLine1 = [Equal, Equal, Equal, InvVery, EqI, Very, EqI, InvVery, InvAbs]
ProfitabilityLine2 = [Very, InvEqI, InvVery, Equal, Equal, Equal, EqI, EqI, InvAbs]
ProfitabilityLine3 = [InvEqI, Very, Abs, InvEqI, InvEqI, Abs, Equal, Equal, Equal]

CharLine1=[Equal, Equal, Equal, Very, Abs, Abs, Abs, Abs, Abs]
CharLine2=[InvVery, InvAbs, InvAbs, Equal, Equal, Equal, Abs, Very, EqI]
CharLine3=[InvAbs, InvAbs, InvAbs, InvAbs, InvVery, InvEqI, Equal, Equal, Equal]

#Find the Geometric Mean for Each of the matrices and each location
SafeSpot0 = [GeometricMean(SafetyLine1, 0), GeometricMean(SafetyLine2, 0), GeometricMean(SafetyLine3, 0)]
SafeSpot1 = [GeometricMean(SafetyLine1, 1), GeometricMean(SafetyLine2, 1),GeometricMean(SafetyLine3, 1)]
SafeSpot2 = [GeometricMean(SafetyLine1, 2), GeometricMean(SafetyLine2, 2),GeometricMean(SafetyLine3, 2)]
SafeSpot3 = [GeometricMean(SafetyLine1, 3), GeometricMean(SafetyLine2, 3),GeometricMean(SafetyLine3, 3)]

FlucSpot0 =  [GeometricMean(FluctuateLine1, 0), GeometricMean(FluctuateLine2, 0), GeometricMean(FluctuateLine3, 0)]
FlucSpot1  = [GeometricMean(FluctuateLine1, 1), GeometricMean(FluctuateLine2, 1), GeometricMean(FluctuateLine3, 1)]
FlucSpot2  = [GeometricMean(FluctuateLine1, 2), GeometricMean(FluctuateLine2, 2), GeometricMean(FluctuateLine3, 2)]
FlucSpot3  = [GeometricMean(FluctuateLine1, 3), GeometricMean(FluctuateLine2, 3), GeometricMean(FluctuateLine3, 3)]

ProfitSpot0 =  [GeometricMean(ProfitabilityLine1, 0), GeometricMean(ProfitabilityLine2, 0), GeometricMean(ProfitabilityLine3, 0)]
ProfitSpot1  = [GeometricMean(ProfitabilityLine1, 1), GeometricMean(ProfitabilityLine2, 1), GeometricMean(ProfitabilityLine3, 1)]
ProfitSpot2  = [GeometricMean(ProfitabilityLine1, 2), GeometricMean(ProfitabilityLine2, 2), GeometricMean(ProfitabilityLine3, 2)]
ProfitSpot3  = [GeometricMean(ProfitabilityLine1, 3), GeometricMean(ProfitabilityLine2, 3), GeometricMean(ProfitabilityLine3, 3)]

CharSpot0 =  [GeometricMean(CharLine1, 0), GeometricMean(CharLine2, 0), GeometricMean(CharLine3, 0)]
CharSpot1  = [GeometricMean(CharLine1, 1), GeometricMean(CharLine2, 1), GeometricMean(CharLine3, 1)]
CharSpot2  = [GeometricMean(CharLine1, 2), GeometricMean(CharLine2, 2), GeometricMean(CharLine3, 2)]
CharSpot3  = [GeometricMean(CharLine1, 3), GeometricMean(CharLine2, 3), GeometricMean(CharLine3, 3)]


print("The Performance Scores indicate the relative strength of each pair of elements in the same hierarchy \n")
print("Safety Performance Scores: ", PerformanceScores(SafeSpot0, SafeSpot1, SafeSpot2, SafeSpot3))
print("\nFluctuation Performance Scores: ", PerformanceScores(FlucSpot0, FlucSpot1, FlucSpot2, FlucSpot3))
print("\nProfitability Performance Scores: ", PerformanceScores(ProfitSpot0, ProfitSpot1, ProfitSpot2, ProfitSpot3))
print("\n The Fuzzy Weights are: ", PerformanceScores(CharSpot0, CharSpot1, CharSpot2, CharSpot3))
