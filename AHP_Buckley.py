import numpy
import sympy

#1 corresponds to Equally important
#2-3 correspond to weakly more important
#4-5 corresponds to strongly more important
#6-7 correspond to very strongly more important
#8-9 correspond to absolutely more important


Equal = (1.0,1.0,1.0,1.0)
EqI = (.5,1.0,1.0,1.5)
InvEqI=(2/3,1,1,2)
Weak = (1,1.5,1.5, 2)
InvWeak=(1/2,2/3,2/3,1)
Strong = (1.5,2,2,5/2)
InvStrong=(2/5,1/2,1/2,2/3)
Very = (2,5/2, 5/2,3)
InvVery=(1/3,2/5, 2/5, 1/2)
Abs=(5/2,3,3,7/2)
InvAbs=(2/7,1/3,1/3,2/5)

SafetyLine1=[Equal, Equal, Weak,Strong,Strong, Strong]
SafetyLine2=[InvWeak, InvStrong, Equal, Equal, EqI,EqI]
SafetyLine3=[InvStrong, InvStrong,InvEqI, InvEqI,Equal, Equal]

FluctuateLine1 = [Equal, Equal,EqI,EqI,Strong, Abs],
FluctuateLine2= [InvEqI, InvEqI, Equal, Equal, Abs, Abs]
FluctuateLine3= [InvStrong, InvAbs, InvAbs, InvAbs, Equal, Equal]

ProfitabilityLine1 = [Equal, Equal,InvVery,EqI,EqI, InvVery]
ProfitabilityLine2 = [Very, InvEqI, Equal, Equal, EqI, EqI]
ProfitabilityLine3 = [InvEqI, Very, InvEqI, InvEqI, Equal, Equal]

CharLine1=[Equal, Equal,Very,Abs,Abs, Abs]
CharLine2=[InvVery, InvAbs, Equal, Equal, Abs, Very]
CharLine3=[InvAbs, InvAbs, InvAbs, InvVery, Equal, Equal]

def GeometricMean(LineList, LineNumber):
    values = [x[LineNumber] for x in LineList]
    GeoMean=1
    for i in range(len(LineList)):
        GeoMean=GeoMean*values[i]
    return(GeoMean**(1/len(LineList)))

Safety1Mean = GeometricMean(SafetyLine1, 0) + GeometricMean(SafetyLine2, 0)+GeometricMean(SafetyLine3, 0)
Safety2Mean = GeometricMean(SafetyLine1, 1) + GeometricMean(SafetyLine2, 1)+GeometricMean(SafetyLine3, 1)
Safety3Mean = GeometricMean(SafetyLine1, 2) + GeometricMean(SafetyLine2, 2)+GeometricMean(SafetyLine3, 2)
Safety4Mean = GeometricMean(SafetyLine1, 3) + GeometricMean(SafetyLine2, 3)+GeometricMean(SafetyLine3, 3)

def PerformanceScores(LineList, LineNumber, MeanSum):
    r=GeometricMean(LineList, LineNumber)/MeanSum
    return(r)

R11=PerformanceScores(SafetyLine1,0, Safety4Mean)


# Safety1Mean = GeometricMean(SafetyLine1, 0) + GeometricMean(SafetyLine2, 0)+GeometricMean(SafetyLine3, 0)
# Safety2Mean = GeometricMean(SafetyLine1, 1) + GeometricMean(SafetyLine2, 1)+GeometricMean(SafetyLine3, 1)
# Safety3Mean = GeometricMean(SafetyLine1, 2) + GeometricMean(SafetyLine2, 2)+GeometricMean(SafetyLine3, 2)
# Safety4Mean = GeometricMean(SafetyLine1, 3) + GeometricMean(SafetyLine2, 3)+GeometricMean(SafetyLine3, 3)


#SafetyPS_11 = (GeometricMean(SafetyLine1,0)/Safety1Mean)

Fluctuate1Mean = GeometricMean(FluctuateLine1, 0) + GeometricMean(FluctuateLine2, 0)+GeometricMean(FluctuateLine3, 0)
Fluctuate2Mean = GeometricMean(FluctuateLine1, 1) + GeometricMean(FluctuateLine2, 1)+GeometricMean(FluctuateLine3, 1)
Fluctuate3Mean = GeometricMean(FluctuateLine1, 2) + GeometricMean(FluctuateLine2, 2)+GeometricMean(FluctuateLine3, 2)
Fluctuate4Mean = GeometricMean(FluctuateLine1, 3) + GeometricMean(FluctuateLine2, 3)+GeometricMean(FluctuateLine3, 3)
