########################################################################
# @TheDoctorRAB
########################################################################
#
# Plot fuzzy numbers for analytic heirarchy procedure (AHP)
# Uses trapezoidal membership functions
# Import data file for each set of fuzzy numbers
#
# First column of data file is y-axis (0,1,1,0)
# Second column is Criteria 1, etc.
#
########################################################################
#
#
#
#######
#
# imports
#
# plot
#
import numpy
import matplotlib
import matplotlib.pyplot as plot
from matplotlib.ticker import MultipleLocator
#
#######
#
# command line
#
from sys import argv
script,plot_datafile=argv
#
#######
#
# screen resolution
#
import tkinter
root=tkinter.Tk()
#
########################################################################
#
#
#
#######
#
# screen resolution
#
###
#
# pixels
#
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
#
###
#
# mm
#
width_mm=root.winfo_screenmmwidth()
height_mm=root.winfo_screenmmheight()
#
###
#
# in
#
width_in=width_mm/25.4
height_in=height_mm/25.4
#
###
#
# dpi
#
width_dpi=width/width_in
height_dpi=height/height_in
#
dpi_values=(96,120,144,168,192)
current_dpi=width_dpi
minimum=1000
#
for dval in dpi_values:
  difference=abs(dval-width_dpi)
  if difference<minimum:
    minimum=difference
    current_dpi=dval
#
#######
#
# output to screen
#
print('width: %i px, height: %i px'%(width,height))
print('width: %i mm, height: %i mm'%(width_mm,height_mm))
print('width: %0.f in, height: %0.f in'%(width_in,height_in))
print('width: %0.f dpi, height: %0.f dpi'%(width_dpi,height_dpi))
print('size is %0.f %0.f'%(width,height))
print('current DPI is %0.f' % (current_dpi))
#
#######
#
# open the plot data file(s)
# add plot_dataN for each plot_datafileN
#
plot_data=numpy.loadtxt(plot_datafile,dtype=float)
#
#######
#
# graph parameters
#
###
#
# font sizes
#
matplotlib.rcParams.update({'font.size': 36}) #axis numbers
#
title_fontsize=54 #plot title
axis_fontsize=48 #axis labels
annotate_fontsize=48 #annotation
#
###
#
# set up for two y axis
#
fig,left_axis=plot.subplots()
# right_axis=left_axis.twinx()
#
###
#
# plot text
#
title='Fuzzy weights'
xtitle='Fuzzy number $\chi$ [-]'
ytitle='Membership function $\mu(\chi)$ [-]'
#
###
#
# legend
# add linecolorN for each plot_dataN
# add curve_textN for each plot_dataN
#
line_color0='blue' #color
line_color1='orange' #color
line_color2='red' #color
#line_color3='green' #color
#line_color4='cyan' #color
#
curve_text0='Safety'           #legend text
curve_text1='Flexibility'      #legend text
curve_text2='Profitability'    #legend text
#curve_text3=''	               #legend text
#curve_text4=''	               #legend text
#
legend_location='upper center' #location of legend on grid
legend_font=42
#
###
#
# annotate
# position of the annotation dependent on axis domain and range
#
annotate_title='Criteria'
annotate_x=0.87
annotate_y=0.95
#
#annotate_title2=''
#annotate_x2=
#annotate_y2=
#
#annotate_title3=''
#annotate_x3=
#annotate_y3=
#
###
#
# axis domain and range
#
xmin=0
xmax=1
#
ymin=-0.01
ymax=1.04
#
###
#
# axis ticks
#
xmajortick=0.25
ymajortick=0.25
#
xminortick=0.05
yminortick=0.05
#
###
#
# grid linewidth
#
major_grid_linewidth=2.5
minor_grid_linewidth=2.1
#
major_grid_tick_length=7
minor_grid_tick_length=5
#
###
#
# curve linewidth
#
curve_linewidth=4.0
#
#######
#
# set plot diagnostics
#
###
#
# titles
#
plot.title(title,fontsize=title_fontsize)
left_axis.set_xlabel(xtitle,fontsize=axis_fontsize)
left_axis.set_ylabel(ytitle,fontsize=axis_fontsize)
# right_axis.set_ylabel()
#
###
#
# grid
#
left_axis.grid(which='major',axis='both',linewidth=major_grid_linewidth)
left_axis.grid(which='minor',axis='both',linewidth=minor_grid_linewidth)
#
left_axis.tick_params(axis='both',which='major',direction='inout',length=major_grid_tick_length)
left_axis.tick_params(axis='both',which='minor',direction='inout',length=minor_grid_tick_length)
#
###
#
# axis domain and range
#
plot.xlim(xmin,xmax)
left_axis.axis(ymin=ymin,ymax=ymax)
###
#
# axis ticks
#
left_axis.xaxis.set_major_locator(MultipleLocator(xmajortick))
left_axis.xaxis.set_minor_locator(MultipleLocator(xminortick))
left_axis.yaxis.set_major_locator(MultipleLocator(ymajortick))
left_axis.yaxis.set_minor_locator(MultipleLocator(yminortick))
#
###
#
# log scale option
# xmin,ymin !=0 for log scale
#
#left_axis.set_xscale('log')
#left_axis.set_yscale('log')
#
###
#
# annotation
# comment out if not needed
#
left_axis.annotate(annotate_title,xy=(annotate_x,annotate_y),xytext=(annotate_x,annotate_y),fontsize=annotate_fontsize)
#left_axis.annotate(annotate_title2,xy=(annotate_x2,annotate_y2),xytext=(annotate_x2,annotate_y2),fontsize=annotate_fontsize)
#left_axis.annotate(annotate_title3,xy=(annotate_x3,annotate_y3),xytext=(annotate_x3,annotate_y3),fontsize=annotate_fontsize)
#
#######
#
# plot data
#
left_axis.plot(plot_data[:,1],plot_data[:,0],marker='o',color=line_color0,label=curve_text0,linewidth=curve_linewidth,markersize=20)
left_axis.plot(plot_data[:,2],plot_data[:,0],marker='o',color=line_color1,label=curve_text1,linewidth=curve_linewidth,markersize=20)
left_axis.plot(plot_data[:,3],plot_data[:,0],marker='o',color=line_color2,label=curve_text2,linewidth=curve_linewidth,markersize=20)
left_axis.legend(loc=legend_location,fontsize=legend_font) #legend needs to be after all the plot data
plot.get_current_fig_manager().resize(width,height)
plot.gcf().set_size_inches((0.01*width),(0.01*height))
#
#######
#
# save
#
plot.savefig(title,dpi=current_dpi)
#
#######
#
# plot to screen
#
plot.show()
#
########################################################################
#
# EOF
#
########################################################################
