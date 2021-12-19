import numpy
import sympy

#1 corresponds to Equally important
#2-3 correspond to weakly more important
#4-5 corresponds to strongly more important
#6-7 correspond to very strongly more important
#8-9 correspond to absolutely more important


Equal = (1.0,1.0,1.0)
EqI = (.5,1.0,1.5)
InvEqI=(2/3,1.0,2.0)
Weak = (1,1.5,2)
InvWeak=(1/2,2/3,1)
Strong = (1.5,2,5/2)
InvStrong=(2/5,1/2,2/3)
Very = (2,5/2,3)
InvVery=(1/3,2/5,1/2)
Abs=(5/2,3,7/2)
InvAbs=(2/7,1/3,2/5)

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


#Find the first (0th) value in each tuple in the first 6 spots,
#take the natural log and add them together
#Since ln(1)=0, it is ok to include the Equal point
def LnSumCalculator(LineList, LineNumber):
    values = [x[LineNumber] for x in LineList]
    LnList = [0]*len(LineList)
    for i in range(len(LineList)):
        LnList.append(numpy.log(values[i]))
    return(sum(LnList))

NumDeciders = len(SafetyLine1)/3.0
NumDecisions = len(SafetyLine1)-NumDeciders

SafeAns1=LnSumCalculator(SafetyLine1, 0)
SafeAns2=LnSumCalculator(SafetyLine2, 0)
SafeAns3=LnSumCalculator(SafetyLine3, 0)
SafeAns4=LnSumCalculator(SafetyLine1, 1)
SafeAns5=LnSumCalculator(SafetyLine2, 1)
SafeAns6=LnSumCalculator(SafetyLine3, 1)
SafeAns7=LnSumCalculator(SafetyLine1, 2)
SafeAns8=LnSumCalculator(SafetyLine2, 2)
SafeAns9=LnSumCalculator(SafetyLine3, 2)

FlucAns1=LnSumCalculator(FluctuateLine1, 0)
FlucAns2=LnSumCalculator(FluctuateLine2, 0)
FlucAns3=LnSumCalculator(FluctuateLine3, 0)
FlucAns4=LnSumCalculator(FluctuateLine1, 1)
FlucAns5=LnSumCalculator(FluctuateLine2, 1)
FlucAns6=LnSumCalculator(FluctuateLine3, 1)
FlucAns7=LnSumCalculator(FluctuateLine1, 2)
FlucAns8=LnSumCalculator(FluctuateLine2, 2)
FlucAns9=LnSumCalculator(FluctuateLine3, 2)


#Generate a matrix with all of the l and u values
#FirstAns, SecondAns, ThirdAns,
#SeventhAns, EigthAns, NinthAns
def MiddleMatrix(NumDecisions, NumDeciders, ForthAns, FifthAns, SixthAns):
    M=sympy.Matrix([[NumDecisions, -NumDeciders, -NumDeciders, ForthAns],
                    [NumDeciders, -NumDecisions, -NumDeciders, FifthAns],
                    [NumDeciders, -NumDeciders, -NumDecisions, SixthAns]]).rref()
    print(M)

def Matrix(NumDecisions, NumDeciders, FirstAns, SecondAns, ThirdAns,SeventhAns, EigthAns, NinthAns):
    A=sympy.Matrix([[NumDecisions,0, 0, 0, -NumDeciders, -NumDeciders, FirstAns],
                    [0, NumDecisions, 0, -NumDeciders, 0, -NumDeciders, SecondAns],
                    [0, 0, NumDecisions, -NumDeciders, -NumDeciders, 0, ThirdAns],
                    [0, -NumDeciders, -NumDeciders, NumDecisions, 0, 0, SeventhAns],
                    [-NumDeciders, 0, -NumDeciders, 0, NumDecisions,0, EigthAns],
                    [-NumDeciders, -NumDeciders, 0, 0, 0, NumDecisions, NinthAns]]).rref()
    print(A)

MiddleMatrix(NumDecisions, NumDeciders, SafeAns4, SafeAns5, SafeAns6)
Matrix(NumDecisions, NumDeciders, SafeAns1, SafeAns2, SafeAns3, SafeAns7, SafeAns8, SafeAns9)
Matrix(NumDecisions, NumDeciders, FlucAns1, FlucAns2, FlucAns3, FlucAns7, FlucAns8, FlucAns9)


# print("Safety Line 1 Spot 1: ", LnSumCalculator(SafetyLine1, 0))
# print("Safety Line 1 Spot 2: ", LnSumCalculator(SafetyLine1, 1))
# print("Safety Line 2 Spot 1: ", LnSumCalculator(SafetyLine2, 0))
# print("Safety Line 3 Spot 1: ", LnSumCalculator(SafetyLine3, 0))
