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
script,weighted_criteria,performance_score_criteria1,performance_score_criteria2,performance_score_criteria3=argv
#######
#
#
#
####### load data
#
# number is the label for the expert
# drawback that each have to be added through the code per expert
weighted_criteria_data=numpy.genfromtxt(weighted_criteria,dtype=float)
performance_score_criteria1_data=numpy.genfromtxt(performance_score_criteria1,dtype=float)
performance_score_criteria2_data=numpy.genfromtxt(performance_score_criteria2,dtype=float)
performance_score_criteria3_data=numpy.genfromtxt(performance_score_criteria3,dtype=float)
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
weighted_criteria_row=weighted_criteria_data.shape[0]
weighted_criteria_column=weighted_criteria_data.shape[1]
#
performance_score_criteria1_row=performance_score_criteria1_data.shape[0]
performance_score_criteria1_column=performance_score_criteria1_data.shape[1]
#
performance_score_criteria2_row=performance_score_criteria2_data.shape[0]
performance_score_criteria2_column=performance_score_criteria2_data.shape[1]
#
performance_score_criteria3_row=performance_score_criteria3_data.shape[0]
performance_score_criteria3_column=performance_score_criteria3_data.shape[1]
#
###
#
# all pairwise matrices have to be n x n
# doing it all out because unit test can be made to verify later
#
row=weighted_criteria_row
column=weighted_criteria_column
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
####### utility set
utility_set=numpy.zeros((row,fuzzy_membership))
utility_set_criteria1=numpy.zeros((row,fuzzy_membership))
utility_set_criteria2=numpy.zeros((row,fuzzy_membership))
utility_set_criteria3=numpy.zeros((row,fuzzy_membership))
#######
#
#
#
####### remapped (normalized) crisp numbers for the final utility set
remapped_crisp_numbers=numpy.zeros((row))
nmz_remapped_crisp_numbers=numpy.zeros((row))
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
# UTILITY SET 
#
#
#
###
i=0 #row
j=0 #column
k=0 #set
l=0 #membership
addition_holder=0
###
#
#
#
#
### merge the performance scores into a 3D matrix
# each set is a criteria
#
weighted_performance_scores=numpy.vstack([performance_score_criteria1_data,performance_score_criteria2_data,performance_score_criteria3_data]).reshape(row,row,fuzzy_membership)
#
###
#
#
###
# multiply weight per criteria matrix(set)
for k in range(0,row):
    for j in range(0,fuzzy_membership):
        for i in range(0,row):
            weighted_performance_scores[k][i,j]=weighted_criteria_data[k,j]*weighted_performance_scores[k][i,j]
#
###
#
#
#
### add weighted peformance scores
#
for i in range(0,row):
    for j in range(0,fuzzy_membership):
        for k in range (0,row):
            utility_set[i,j]=utility_set[i,j]+weighted_performance_scores[k][i,j]
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
for i in range(0,row):
    remapped_crisp_numbers[i]=(utility_set[i,0]+2*utility_set[i,1]+2*utility_set[i,2]+utility_set[i,3])/(6)
#
remapped_sum=numpy.sum(remapped_crisp_numbers)
###
#
#
#
###
#
for i in range(0,row):
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
### transpose weighted alternative 
utility_set_transpose=numpy.transpose(utility_set)
###
#
#
#
### make graphing file
utility_set_graph=numpy.concatenate((membership_function_ordinate,utility_set_transpose),axis=1)
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
numpy.savetxt('utility-set.out',utility_set,fmt='%.4f')
numpy.savetxt('utility-set-graph.out',utility_set_graph,fmt='%.4f')
numpy.savetxt('nmz-remapped-crisp-numbers-utility-set.out',nmz_remapped_crisp_numbers,fmt='%.4f')
#
#
#
##################################################################################
#
# FLAGS AND UNIT TESTS
#
#
#
#print('pairwise comparison example matrix 1','\n',crisp_number_data_alternative1,'\n')
#print('pairwise comparison example matrix 2','\n',crisp_number_data_alternative2,'\n')
#print('pairwise comparison example matrix 3','\n',crisp_number_data_alternative3,'\n')
#print('pairwise comparison example matrix 4','\n',crisp_number_data_alternative4,'\n')
#print('pairwise comparison example matrix 5','\n',crisp_number_data_alternative5,'\n')
#print('rows and columns',crisp_number_data_row_alternative1,crisp_number_data_column_alternative1,crisp_number_data_row_alternative2,crisp_number_data_column_alternative2,'\n')
#print('length of membership function',fuzzy_membership,'\n')
#print('weak',weak,'\n')
#print('reverse weak',reverse_weak,'\n')
#print('mid strong',mid_strong,'\n')
#print('inverse mid strong',inverse_mid_strong,'\n')
#print('fuzzy map 1','\n',fuzzy_crisp_number_data_alternative1,'\n')
#print('fuzzy map 2','\n',fuzzy_crisp_number_data_alternative2,'\n')
#print('fuzzy map 3','\n',fuzzy_crisp_number_data_alternative3,'\n')
#print('fuzzy map 4','\n',fuzzy_crisp_number_data_alternative4,'\n')
#print('fuzzy map 5','\n',fuzzy_crisp_number_data_alternative5,'\n')
#print('geometric mean 1','\n',geometric_mean_alternative1,'\n')
#print('geometric mean 2','\n',geometric_mean_alternative2,'\n')
#print('geometric mean 3','\n',geometric_mean_alternative3,'\n')
#print('geometric mean 4','\n',geometric_mean_alternative4,'\n')
#print('geometric mean 5','\n',geometric_mean_alternative5,'\n')
#print('full geometric mean','\n',full_geometric_mean,'\n')
#print('weighted alternative','\n',weighted_alternative,'\n')
#print('remapped crisp numbers',remapped_crisp_numbers,'\n')
#print('single weighted performance','\n',weighted_performance_scores,'\n')
#print('utility set','\n',utility_set,'\n')
#
#
#
##################################################################################
