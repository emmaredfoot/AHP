import numpy
import csv

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

#Weight all of the performance score values
#Add all of the values in the individual locations together
#Return the utility function for safety, ability to fluctuate, and profitability
def WeightPS(r_ij, weight_i):
    weightedPS=[0]*len(r_ij)
    for i in range(len(r_ij)):
        weightedPS[i]=[a*b for a,b in zip(r_ij[i],weight_i[i])]
    A=weightedPS[0]
    B=weightedPS[1]
    C=weightedPS[2]
    utility=[0]*len(C)
    for x in range(len(C)):
        utility[x] = A[x]+B[x]+C[x]
    return(utility)


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

SafetyLine1=[Equal, Equal, Equal, Equal, Weak,Strong, EqI, Strong, Strong, Strong, EqI, Strong]
SafetyLine2=[InvWeak, InvStrong, InvEqI, InvStrong, Equal, Equal, Equal, Equal, EqI, EqI,EqI, EqI]
SafetyLine3=[InvStrong, InvStrong, InvEqI, InvStrong, InvEqI, InvEqI, InvEqI, InvEqI, Equal, Equal, Equal, Equal]

FluctuateLine1 = [Equal, Equal, Equal, Equal, EqI, EqI, EqI, Abs, Strong, Abs, EqI, Strong]
FluctuateLine2= [InvEqI, InvEqI, InvEqI, InvAbs, Equal, Equal, Equal, Equal, Abs, Abs, EqI, InvWeak]
FluctuateLine3= [InvStrong, InvAbs, InvEqI, InvStrong, InvAbs, InvAbs, InvEqI, Weak, Equal, Equal, Equal, Equal]

ProfitabilityLine1 = [Equal, Equal, Equal, Equal, InvVery, EqI, Very, InvStrong, EqI, InvVery, InvAbs, InvStrong]
ProfitabilityLine2 = [Very, InvEqI, InvVery, Strong, Equal, Equal, Equal, Equal, EqI, EqI, InvAbs, EqI]
ProfitabilityLine3 = [InvEqI, Very, Abs, Strong, InvEqI, InvEqI, Abs, InvEqI, Equal, Equal, Equal, Equal]

CharLine1=[Equal, Equal, Equal, Equal, Very, Abs, Abs, Very, Abs, Abs, Abs, EqI]
CharLine2=[InvVery, InvAbs, InvAbs, InvVery, Equal, Equal, Equal, Equal, InvAbs, InvVery, EqI, InvAbs]
CharLine3=[InvAbs, InvAbs, InvAbs, InvEqI, Abs, Very, InvEqI, Abs,  Equal, Equal, Equal, Equal]

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

#Save the Performance Score values
SafetyPS = PerformanceScores(SafeSpot0, SafeSpot1, SafeSpot2, SafeSpot3)
FlucPS = PerformanceScores(FlucSpot0, FlucSpot1, FlucSpot2, FlucSpot3)
ProfitPS = PerformanceScores(ProfitSpot0, ProfitSpot1, ProfitSpot2, ProfitSpot3)
Weights = PerformanceScores(CharSpot0, CharSpot1, CharSpot2, CharSpot3)



#I am passing in the performance scores and returning the summed up utility values
SafetyUtility = WeightPS(SafetyPS, Weights)
FlucUtility = WeightPS(FlucPS, Weights)
ProfitUtility = WeightPS(ProfitPS, Weights)

#Save the PerformanceScores to a file
with open('PerformanceScores.csv', 'w') as myfile:
    out=csv.writer(myfile)
    out.writerow('Safety')
    out.writerow(SafetyPS[0])
    out.writerow(SafetyPS[1])
    out.writerow(SafetyPS[2])
    out.writerow('\nFluctuate')
    out.writerow(FlucPS[0])
    out.writerow(FlucPS[1])
    out.writerow(FlucPS[2])
    out.writerow('\nProfitability')
    out.writerow(ProfitPS[0])
    out.writerow(ProfitPS[1])
    out.writerow(ProfitPS[2])
    out.writerow('\nFuzzy Weights')
    out.writerow(Weights[0])
    out.writerow(Weights[1])
    out.writerow(Weights[2])
myfile.close()

with open('Utility.csv', 'w') as ufile:
    output = csv.writer(ufile)
    output.writerow('Safety')
    output.writerow(SafetyUtility)
    output.writerow("Fluctuate")
    output.writerow(FlucUtility)
    output.writerow("Profitability")
    output.writerow(ProfitUtility)

ufile.close()
