#################################################################################
# @TheDoctorRAB
#################################################################################
#
#
# DESCRIPTION
#
#
#################################################################################
#
# Computes Fuzzy AHP utility set with trapezoid member functions.
# Can be easily modified for triangular membership functions. 
# Procedure is the same.
#
#################################################################################
#
# Source
#
# Redfoot, Emma K., Verner, Kelley M., Borrelli, R. A., 2021.
# Applying analytic hierarchy process to industrial process design in a nuclear renewable hybrid energy system.
# Progress in Nuclear Energy.
#
##################################################################################
#
# Code flow
#
# Input - tab delimited file containing crisp number pairwise comparisions
#       - one file each for criteria or alternatives per expert
#######
#
# Criteria
# 1. Convert crisp numbers to fuzzy numbers (l,m,n,s).
# 2. Compute geometric mean for each l,m,n,s per criteria per expert.
# 3. Compute geometric mean for each l,m,n,s per above per critera.
# 4. Sum each l,m,n,s.
# 5. Compute critera weights by 3l/4s, 3m/4n, 3n/4m, 3s/4l.
#    3 or 4 mean values from items 3 and 4 above not to multiply by those actual numbers
#
#######
#
# Alternatives
# Under each criteria, compute performance scores in the same way.
# It is the same math, but the result is named different.
#
#######
#
# Utility set
# 1. Compute the product of the weight of the critera per l,m,n,s, by the performance score under that criteria per l,m,n,s.
# 2. Sum the product per l,m,n,s per alternative.
#
#######
#
# See the calculation sheet on the github repository.
#
##################################################################################
#
# AHP pairwise comparison
#
# 1 - equal importance
# 2
# 3 - weak importance
# 4
# 5 - strong importance
# 6
# 7 - very strong importance
# 8
# 9 - absolutely strong importance
#
#######
#
# Experts will assign 1 - 9 when judging two criteria or alternatives under a criterion.
# Resulting matrix will always be n x n.
# (i,i) = 1
# (i,j) = (j,i)^(-1)
#
##################################################################################
#
# AHP fuzzy mapping
#
# 1 - (1,1,1,1)
# 2 - (1,1.5,2.5,3)
# 3 - (2,2.5,3.5,4)
# 4 - (3,3.5,4.5,5)
# 5 - (4,4.5,5.5,6)
# 6 - (5,5.5,6.5,7)
# 7 - (6,6.5,7.5,8)
# 8 - (7,7.5,8.5,9)
# 9 - (8,8.5,9,9)
#
# These are the l,m,n,s.
#
#######
#
# The matrix is still n x n with each (i,j) = l,m,n,s.
# (i,i) = 1,1,1,1
# (i,j) = l,m,n,s
# (j,i) = 1/s,1/n,1/m,1/l
# So the inverse is computed differently.
#
##################################################################################
#
#
# END DESCRIPTION
#
#
##################################################################################
#
#
#
#
#
#
##################################################################################
#
# PREAMBLE
#
#
#
####### imports
from sys import argv
import numpy
import sympy
#######
#
#
#
####### inputs
script,pairwise_input_criteria1,pairwise_input_criteria2,pairwise_input_criteria3,pairwise_input_criteria4,pairwise_input_criteria5=argv
#######
#
#
#
####### load data
#
# number is the label for the expert
# drawback that each have to be added through the code per expert
crisp_number_data_criteria1=numpy.genfromtxt(pairwise_input_criteria1,dtype=float)
crisp_number_data_criteria2=numpy.genfromtxt(pairwise_input_criteria2,dtype=float)
crisp_number_data_criteria3=numpy.genfromtxt(pairwise_input_criteria3,dtype=float)
crisp_number_data_criteria4=numpy.genfromtxt(pairwise_input_criteria4,dtype=float)
crisp_number_data_criteria5=numpy.genfromtxt(pairwise_input_criteria5,dtype=float)
#######
#
#
#
##################################################################################
# 
# FUNCTIONS
#
#
#
####### map pairwise comparision to fuzzy membership function for inverse
#
def InverseFuzzyMap(crisp_number_data,l):
    fuzzy_map=0
    inverse_pairwise_comparision=0
    inverse_pairwise_comparison=round((1)/(crisp_number_data))
    if (inverse_pairwise_comparison == 2):
        fuzzy_map=inverse_mid_equal[l]
    elif (inverse_pairwise_comparison == 3):
        fuzzy_map=inverse_weak[l]
    elif (inverse_pairwise_comparison == 4):
        fuzzy_map=inverse_mid_weak[l]
    elif (inverse_pairwise_comparison == 5):
        fuzzy_map=inverse_strong[l]
    elif (inverse_pairwise_comparison == 6):
        fuzzy_map=inverse_mid_strong[l]
    elif (inverse_pairwise_comparison == 7):
        fuzzy_map=inverse_very_strong[l]
    elif (inverse_pairwise_comparison == 8):
        fuzzy_map=inverse_mid_very_strong[l]
    elif (inverse_pairwise_comparison == 9):
        fuzzy_map=inverse_absolute[l]
    return (fuzzy_map)
#
#######
#
#
#
####### map pairwise comparision to fuzzy membership function for inverse
#
def FuzzyMap(crisp_number_data,l):
    fuzzy_map=0
    pairwise_comparision=0
    pairwise_comparison=round(crisp_number_data)
    if (pairwise_comparison == 2):
        fuzzy_map=mid_equal[l]
    elif (pairwise_comparison == 3):
        fuzzy_map=weak[l]
    elif (pairwise_comparison == 4):
        fuzzy_map=mid_weak[l]
    elif (pairwise_comparison == 5):
        fuzzy_map=strong[l]
    elif (pairwise_comparison == 6):
        fuzzy_map=mid_strong[l]
    elif (pairwise_comparison == 7):
        fuzzy_map=very_strong[l]
    elif (pairwise_comparison == 8):
        fuzzy_map=mid_very_strong[l]
    elif (pairwise_comparison == 9):
        fuzzy_map=absolute[l]
    return (fuzzy_map)
#
#######
#
#
#
##################################################################################
#
# CONSTANTS
#
#
#
####### number of rows
crisp_number_data_row_criteria1=crisp_number_data_criteria1.shape[0]
crisp_number_data_column_criteria1=crisp_number_data_criteria1.shape[1]
#
crisp_number_data_row_criteria2=crisp_number_data_criteria2.shape[0]
crisp_number_data_column_criteria2=crisp_number_data_criteria2.shape[1]
#
crisp_number_data_row_criteria3=crisp_number_data_criteria3.shape[0]
crisp_number_data_column_criteria3=crisp_number_data_criteria3.shape[1]
#
crisp_number_data_row_criteria3=crisp_number_data_criteria3.shape[0]
crisp_number_data_column_criteria3=crisp_number_data_criteria3.shape[1]
#
crisp_number_data_row_criteria4=crisp_number_data_criteria4.shape[0]
crisp_number_data_column_criteria4=crisp_number_data_criteria4.shape[1]
#
crisp_number_data_row_criteria5=crisp_number_data_criteria5.shape[0]
crisp_number_data_column_criteria5=crisp_number_data_criteria5.shape[1]
#
###
#
# all pairwise matrices have to be n x n
# doing it all out because unit test can be made to verify later
#
crisp_number_row=crisp_number_data_row_criteria1
crisp_number_column=crisp_number_data_column_criteria1
#######
#
#
#
####### AHP mapping
#
### membership functions could be imported 
equal=numpy.array([1.0,1.0,1.0,1.0])         #1
mid_equal=numpy.array([1,1.5,2.5,3])         #2
weak=numpy.array([2,2.5,3.5,4])              #3
mid_weak=numpy.array([3,3.5,4.5,5])          #4 
strong=numpy.array([4,4.5,5.5,6])            #5
mid_strong=numpy.array([5,5.5,6.5,7])        #6
very_strong=numpy.array([6,6.5,7.5,8])       #7
mid_very_strong=numpy.array([7,7.5,8.5,9])   #8
absolute=numpy.array([8,8.5,9,9])            #9
#
#
#
####### membership function
fuzzy_membership=len(equal) # generalizes the fuzzy AHP membership functions 
#######
#
#
#
####### AHP inverse
#
### inverses will be calculated to generalize
inverse_equal=numpy.zeros(fuzzy_membership)
inverse_mid_equal=numpy.zeros(fuzzy_membership)
inverse_weak=numpy.zeros(fuzzy_membership)
inverse_mid_weak=numpy.zeros(fuzzy_membership)
inverse_strong=numpy.zeros(fuzzy_membership)
inverse_mid_strong=numpy.zeros(fuzzy_membership)
inverse_very_strong=numpy.zeros(fuzzy_membership)
inverse_mid_very_strong=numpy.zeros(fuzzy_membership)
inverse_absolute=numpy.zeros(fuzzy_membership)
#######
#
#
#
####### mapped pairwise comparisons per expert
#
# three dimensional matrix because calculations need to be done
# tuples cannot do calculations 
#
# dimensions are set, row, columns
# set = number of criteria/alternatives
# row = number of criteria/alternatives
# columns = membership function; e.g., trapezoid = 4
#
# convention is [set][row,column]
# not cumulative though
# set 0,[0,1] is the same position as set 1,[0,1], the [0,1] does not need to be added through sets
#
# in the calculation spread sheet, matrix dimensions are row-criteria,column-(criteria)(membership)
# could get unwieldy for a lot of criteria/alternatives
#
fuzzy_crisp_number_data_criteria1=numpy.zeros((crisp_number_data_row_criteria1,crisp_number_data_row_criteria1,fuzzy_membership))
fuzzy_crisp_number_data_criteria2=numpy.zeros((crisp_number_data_row_criteria2,crisp_number_data_row_criteria2,fuzzy_membership))
fuzzy_crisp_number_data_criteria3=numpy.zeros((crisp_number_data_row_criteria3,crisp_number_data_row_criteria3,fuzzy_membership))
fuzzy_crisp_number_data_criteria4=numpy.zeros((crisp_number_data_row_criteria4,crisp_number_data_row_criteria4,fuzzy_membership))
fuzzy_crisp_number_data_criteria5=numpy.zeros((crisp_number_data_row_criteria5,crisp_number_data_row_criteria5,fuzzy_membership))
#######
#
#
#
####### geometric means per expert
geometric_mean_criteria1=numpy.zeros((crisp_number_data_row_criteria1,fuzzy_membership))
geometric_mean_criteria2=numpy.zeros((crisp_number_data_row_criteria2,fuzzy_membership))
geometric_mean_criteria3=numpy.zeros((crisp_number_data_row_criteria3,fuzzy_membership))
geometric_mean_criteria4=numpy.zeros((crisp_number_data_row_criteria4,fuzzy_membership))
geometric_mean_criteria5=numpy.zeros((crisp_number_data_row_criteria5,fuzzy_membership))
#######
#
#
#
####### full geometric mean
# geometric mean of the geometric means
full_geometric_mean=numpy.zeros((crisp_number_row,fuzzy_membership))
#######
#
#
#
####### weighted criteria 
weighted_criteria=numpy.zeros((crisp_number_row,fuzzy_membership))
#######
#
#
#
####### remapped (normalized) crisp numbers for the final weights
remapped_crisp_numbers=numpy.zeros((crisp_number_row))
nmz_remapped_crisp_numbers=numpy.zeros((crisp_number_row))
#######
#
#
#
##################################################################################
#
# MEMBERSHIP FUNCTIONS 
#
#
#
####### AHP inverse mapping
#
### reverse the arrays first 
#
reverse_equal=equal[::-1]
reverse_mid_equal=mid_equal[::-1]
reverse_weak=weak[::-1]
reverse_mid_weak=mid_weak[::-1]
reverse_strong=strong[::-1]
reverse_mid_strong=mid_strong[::-1]
reverse_very_strong=very_strong[::-1]
reverse_mid_very_strong=mid_very_strong[::-1]
reverse_absolute=absolute[::-1]
#
###
#
#
#
### calculate the inverse of each
#
i=0 #row
for i in range (0,fuzzy_membership):
    inverse_equal[i]=(1)/(reverse_equal[i])
    inverse_mid_equal[i]=(1)/(reverse_mid_equal[i])
    inverse_weak[i]=(1)/(reverse_weak[i])
    inverse_mid_weak[i]=(1)/(reverse_mid_weak[i])
    inverse_strong[i]=(1)/(reverse_strong[i])
    inverse_mid_strong[i]=(1)/(reverse_mid_strong[i])
    inverse_very_strong[i]=(1)/(reverse_very_strong[i])
    inverse_mid_very_strong[i]=(1)/(reverse_mid_very_strong[i])
    inverse_absolute[i]=(1)/(reverse_absolute[i])
#
###
#
#
#
##################################################################################
#
# MAP PAIRWISE COMPARISONS TO FUZZY MEMBERSHIP
#
#
#
### each set in the mapped matrix corresponds to a column in the pairwise comparision matrix
#
i=0 #row
j=0 #column
k=0 #set
l=0 #membership
###
#
#
#
### map diagonal of pairwise matrix because always 1
# find any other 1 comparisions
#
for k in range(0,crisp_number_row):
    for i in range(0,crisp_number_row):
        for l in range(0,fuzzy_membership):
            if (crisp_number_data_criteria1[i,k] == 1):
                fuzzy_crisp_number_data_criteria1[k][i,l]=equal[l]
            if (crisp_number_data_criteria2[i,k] == 1):
                fuzzy_crisp_number_data_criteria2[k][i,l]=equal[l]
            if (crisp_number_data_criteria3[i,k] == 1):
                fuzzy_crisp_number_data_criteria3[k][i,l]=equal[l]
            if (crisp_number_data_criteria4[i,k] == 1):
                fuzzy_crisp_number_data_criteria4[k][i,l]=equal[l]
            if (crisp_number_data_criteria5[i,k] == 1):
                fuzzy_crisp_number_data_criteria5[k][i,l]=equal[l]
#
###
#
#
#
### map by column in the pairwise comparison matrix
# not really any elegant way to map
# 
for k in range(0,crisp_number_row):
    for i in range(0,crisp_number_row):
        for l in range(0,fuzzy_membership):
            if (crisp_number_data_criteria1[i,k] < 1):
                fuzzy_crisp_number_data_criteria1[k][i,l]=InverseFuzzyMap(crisp_number_data_criteria1[i,k],l)
            elif (crisp_number_data_criteria1[i,k] > 1):
                fuzzy_crisp_number_data_criteria1[k][i,l]=FuzzyMap(crisp_number_data_criteria1[i,k],l)
#
            if (crisp_number_data_criteria2[i,k] < 1):
                fuzzy_crisp_number_data_criteria2[k][i,l]=InverseFuzzyMap(crisp_number_data_criteria2[i,k],l)
            elif (crisp_number_data_criteria2[i,k] > 1):
                fuzzy_crisp_number_data_criteria2[k][i,l]=FuzzyMap(crisp_number_data_criteria2[i,k],l)
#
            if (crisp_number_data_criteria3[i,k] < 1):
                fuzzy_crisp_number_data_criteria3[k][i,l]=InverseFuzzyMap(crisp_number_data_criteria3[i,k],l)
            elif (crisp_number_data_criteria3[i,k] > 1):
                fuzzy_crisp_number_data_criteria3[k][i,l]=FuzzyMap(crisp_number_data_criteria3[i,k],l)
#
            if (crisp_number_data_criteria4[i,k] < 1):
                fuzzy_crisp_number_data_criteria4[k][i,l]=InverseFuzzyMap(crisp_number_data_criteria4[i,k],l)
            elif (crisp_number_data_criteria4[i,k] > 1):
                fuzzy_crisp_number_data_criteria4[k][i,l]=FuzzyMap(crisp_number_data_criteria4[i,k],l)
#
            if (crisp_number_data_criteria5[i,k] < 1):
                fuzzy_crisp_number_data_criteria5[k][i,l]=InverseFuzzyMap(crisp_number_data_criteria5[i,k],l)
            elif (crisp_number_data_criteria5[i,k] > 1):
                fuzzy_crisp_number_data_criteria5[k][i,l]=FuzzyMap(crisp_number_data_criteria5[i,k],l)
#
###
#
#
#
##################################################################################
#
# GEOMETRIC MEANS
#
#
#
###
i=0 #row
j=0 #column
k=0 #set
l=0 #membership
###
#
#
#
###
multiplier_holder1=1
geometric_mean_holder1=1
#
multiplier_holder2=1
geometric_mean_holder2=1
#
multiplier_holder3=1
geometric_mean_holder3=1
#
multiplier_holder4=1
geometric_mean_holder4=1
#
multiplier_holder5=1
geometric_mean_holder5=1
###
#
#
#
for l in range(0,fuzzy_membership):
    for i in range(0,crisp_number_row):
        for k in range(0,crisp_number_row):
            multiplier_holder1=multiplier_holder1*fuzzy_crisp_number_data_criteria1[k][i,l]
            multiplier_holder2=multiplier_holder2*fuzzy_crisp_number_data_criteria2[k][i,l]
            multiplier_holder3=multiplier_holder3*fuzzy_crisp_number_data_criteria3[k][i,l]
            multiplier_holder4=multiplier_holder4*fuzzy_crisp_number_data_criteria4[k][i,l]
            multiplier_holder5=multiplier_holder5*fuzzy_crisp_number_data_criteria5[k][i,l]
#
        geometric_mean_holder1=multiplier_holder1**((1)/(crisp_number_row))
        geometric_mean_holder2=multiplier_holder2**((1)/(crisp_number_row))
        geometric_mean_holder3=multiplier_holder3**((1)/(crisp_number_row))
        geometric_mean_holder4=multiplier_holder4**((1)/(crisp_number_row))
        geometric_mean_holder5=multiplier_holder5**((1)/(crisp_number_row))
#
        geometric_mean_criteria1[i,l]=geometric_mean_holder1
        geometric_mean_criteria2[i,l]=geometric_mean_holder2
        geometric_mean_criteria3[i,l]=geometric_mean_holder3
        geometric_mean_criteria4[i,l]=geometric_mean_holder4
        geometric_mean_criteria5[i,l]=geometric_mean_holder5
#
        multiplier_holder1=1
        geometric_mean_holder1=1
#
        multiplier_holder2=1
        geometric_mean_holder2=1
#
        multiplier_holder3=1
        geometric_mean_holder3=1
#
        multiplier_holder4=1
        geometric_mean_holder4=1
#
        multiplier_holder5=1
        geometric_mean_holder5=1
#
###
#
#
#
##################################################################################
#
# FULL GEOMETRIC MEAN
#
#
#
###
i=0 #row
j=0 #column
k=0 #set
l=0 #membership
###
#
#
#
###
multiplier_holder=1
geometric_mean_holder=1
###
#
#
#
### concatenate geometric mean matrices
# stacks the geometric mean matrices on top
# rows = experts*criteria (or alternatives)
# columns = membership functions
#
concatenated_geometric_mean=numpy.concatenate((geometric_mean_criteria1,geometric_mean_criteria2,geometric_mean_criteria3,geometric_mean_criteria4,geometric_mean_criteria5),axis=0)
#
### get rows
concatenated_geometric_mean_row=concatenated_geometric_mean.shape[0]
###
#
#
#
### compute experts
# experts is the exponent to use in the full geometric mean
#
experts=round(concatenated_geometric_mean_row/crisp_number_row)
#
###
#
#
#
### compute by column
#
for l in range(0,fuzzy_membership):
    for i in range(0,crisp_number_row):
        for k in range(0,experts):
            multiplier_holder=multiplier_holder*concatenated_geometric_mean[k*crisp_number_row+i,l]
        geometric_mean_holder=multiplier_holder**((1)/(experts))
        full_geometric_mean[i,l]=geometric_mean_holder
        multiplier_holder=1
        geometric_mean_holder=1
#
###
#
#
#
##################################################################################
#
# WEIGHTED CRITERIA 
#
#
#
###
i=0 #row
j=0 #column
k=0 #set
l=0 #membership
###
#
#
#
### sum columns of full geometric mean
# ridiculous after all that the sum is only one line
column_sum=full_geometric_mean.sum(axis=0)
###
#
#
#
### compute weights
for l in range(0,fuzzy_membership):
    for i in range(crisp_number_row):
        weighted_criteria[i,l]=(full_geometric_mean[i,l])/(column_sum[(fuzzy_membership-1)-l])
#
###
#
#
#
##################################################################################
#
# REMAP TO CRISP NUMBERS
#
# change based on membership functions
#
#
#
###
i=0
###
#
#
#
### remap uses trapezoid rule
#
for i in range(0,crisp_number_row):
    remapped_crisp_numbers[i]=(weighted_criteria[i,0]+2*weighted_criteria[i,1]+2*weighted_criteria[i,2]+weighted_criteria[i,3])/(6)
#
remapped_sum=numpy.sum(remapped_crisp_numbers)
###
#
#
#
###
#
for i in range(0,crisp_number_row):
    nmz_remapped_crisp_numbers[i]=remapped_crisp_numbers[i]/remapped_sum
#
nmz_remapped_crisp_numbers=numpy.vstack(nmz_remapped_crisp_numbers)
###
#
#
#
##################################################################################
#
# PREPARE FOR GRAPHING
#
#
#
### fuzzy graphs are always the same for the same membership functions
# change if using triangular
# ordinates are the same for each membership function
#
membership_function_ordinate=([0,1,1,0])
membership_function_ordinate=numpy.vstack(membership_function_ordinate)
#
###
#
#
#
### transpose weighted criteria 
weighted_criteria_transpose=numpy.transpose(weighted_criteria)
###
#
#
#
### make graphing file
weighted_criteria_graph=numpy.concatenate((membership_function_ordinate,weighted_criteria_transpose),axis=1)
###
#
#
#
##################################################################################
#
# EXPORT DATA
#
#
#
numpy.savetxt('weighted-criteria.out',weighted_criteria,fmt='%.4f')
numpy.savetxt('weighted-criteria-graph.out',weighted_criteria_graph,fmt='%.4f')
numpy.savetxt('nmz-remapped-crisp-numbers-criteria.out',nmz_remapped_crisp_numbers,fmt='%.4f')
#
#
#
##################################################################################
#
# FLAGS AND UNIT TESTS
#
#
#
#print('pairwise comparison example matrix 1','\n',crisp_number_data_criteria1,'\n')
#print('pairwise comparison example matrix 2','\n',crisp_number_data_criteria2,'\n')
#print('pairwise comparison example matrix 3','\n',crisp_number_data_criteria3,'\n')
#print('pairwise comparison example matrix 4','\n',crisp_number_data_criteria4,'\n')
#print('pairwise comparison example matrix 5','\n',crisp_number_data_criteria5,'\n')
#print('rows and columns',crisp_number_data_row_criteria1,crisp_number_data_column_criteria1,crisp_number_data_row_criteria2,crisp_number_data_column_criteria2,'\n')
#print('length of membership function',fuzzy_membership,'\n')
#print('weak',weak,'\n')
#print('reverse weak',reverse_weak,'\n')
#print('mid strong',mid_strong,'\n')
#print('inverse mid strong',inverse_mid_strong,'\n')
#print('fuzzy map 1','\n',fuzzy_crisp_number_data_criteria1,'\n')
#print('fuzzy map 2','\n',fuzzy_crisp_number_data_criteria2,'\n')
#print('fuzzy map 3','\n',fuzzy_crisp_number_data_criteria3,'\n')
#print('fuzzy map 4','\n',fuzzy_crisp_number_data_criteria4,'\n')
#print('fuzzy map 5','\n',fuzzy_crisp_number_data_criteria5,'\n')
#print('geometric mean 1','\n',geometric_mean_criteria1,'\n')
#print('geometric mean 2','\n',geometric_mean_criteria2,'\n')
#print('geometric mean 3','\n',geometric_mean_criteria3,'\n')
#print('geometric mean 4','\n',geometric_mean_criteria4,'\n')
#print('geometric mean 5','\n',geometric_mean_criteria5,'\n')
#print('full geometric mean','\n',full_geometric_mean,'\n')
#print('weighted criteria','\n',weighted_criteria,'\n')
#print('remapped crisp numbers',remapped_crisp_numbers,'\n')
#
#
#
##################################################################################
