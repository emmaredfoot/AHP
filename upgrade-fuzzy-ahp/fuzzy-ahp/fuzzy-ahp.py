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
script,pairwise_input=argv #for now, input only one at a time; automate for N experts later
#######
#
#
#
####### load data
crisp_number_data=numpy.genfromtxt(pairwise_input,dtype=float) #just add crisp_number_data1,crisp_number_data2, etc.
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
####### membership function
trapezoid_membership=4
#######
#
#
#
####### number of rows
crisp_number_data_row=crisp_number_data.shape[0]
crisp_number_data_column=crisp_number_data.shape[1]
#######
#
#
#
##################################################################################
#
# COMPUTATIONS
#
#
#
####### AHP mapping
equal=(1.0,1.0,1.0,1.0)
mid_equal=(1,1.5,2.5,3)
weak=(2,2.5,3.5,4)
mid_weak=(3,3.5,4.5,5)
strong=(4,4.5,5.5,6)
mid_strong=(5,5.5,6.5,7)
very_strong=(6,6.5,7.5,8)
mid_very_strong=(7,7.5,8.5,9)
absolute=(8,8.5,9,9)
#######
#
#
#
####### AHP inverse mapping
inverse_equal=(1.0,1.0,1.0,1.0)
#
for i in range (0,trapezoid_membership):
# see tuple math - reverse and then inverse
#
# (j,i) = 1/s,1/n,1/m,1/l
##################################################################################
##
# FLAGS
#
print(crisp_number_data)
print(crisp_number_data_row,crisp_number_data_column)
print(equal,mid_equal,absolute)
print(tuple(reversed(strong)))
##################################################################################
