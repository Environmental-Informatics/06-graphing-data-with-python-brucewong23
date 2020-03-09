#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 20:18:18 2020
This script generate a simple figure with required plots of streamflow, tqmean
and R-B index on the same figure when user provide a valid input file 

@author: wang2846
"""

import numpy as np
import matplotlib.pyplot as plt
import re
import os.path

# prompt user for file input
in_file = input("Provide input file: ")
# check if input file exist, if so, proceed, otherwise print (bottom) file does
# not exist. we can also add another condition to see if the file is what we
# need, i.e. name check but we need to know the filename beforehand it would 
# be useful for this assignment alone, but may not for general usage
if os.path.exists(in_file):
    base_filename = re.sub("\.txt", "", in_file) # for figure output naming
    # in_file = "Tippecanoe_River_at_Ora.Annual_Metrics.txt" # for testing
    # names in genfromtxt can be specified with the headers list below with
    # other names desired or just set to true
    headers = ["Year", "Mean", "Max", "Min", "StdDev", "Tqmean", "RBindex"]
    data = np.genfromtxt(in_file, names=True)
    
    # generate 3 subplot, since all three use year as x-axis, axis are shared among
    # all 3 plots
    f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)
    # subplot 1 of streamflow
    ax1.plot(data["Year"], data["Mean"], color="black", label="Mean")
    ax1.plot(data["Year"], data["Max"], color="red", label="Max")
    ax1.plot(data["Year"], data["Min"], color="blue", label="Min")
    ax1.set_ylabel("Streamflow (cfs)") # name y label
    # Legend box is set outside for legibility
    ax1.legend(loc="best", frameon=False, ncol=3, bbox_to_anchor=(0.4, 0.9))
    
    ax2.plot(data["Year"], data["Tqmean"]*100, "D") # disconnected symbol
    ax2.set_ylabel("Tqmean (%)")
    
    ax3.bar(data["Year"], data["RBindex"]) # bar chart
    ax3.set_ylabel("R-B index (ratio)")
    ax3.set_xlabel("Year") # name x label
    
    ## method 2
    #plt.subplot(3,1,1)
    #plt.plot(data["Year"], data["Mean"], color="black", label="Mean")
    #plt.plot(data["Year"], data["Max"], color="red", label="Max")
    #plt.plot(data["Year"], data["Min"], color="blue", label="Min")
    #plt.xlabel("Year")
    #plt.ylabel("Streamflow (cfs)")
    #plt.xticks([min(data["Year"], max(data["Year"]))])
    #plt.yticks([min(data["Min"], max(data["Max"]))])
    #plt.legend(loc="best", frameon=False, ncol=3, bbox_to_anchor=(0.4, 0.9))
    
    #plt.subplot(3,1,2)
    #plt.plot(data["Year"], data["Tqmean"]*100, "D")
    #plt.xlabel("Year")
    #plt.ylabel("Tqmean (%)")
    
    #plt.subplot(3,1,3)
    #plt.bar(data["Year"], data["RBindex"])
    #plt.xlabel("Year")
    #plt.ylabel("R-B index (ratio)")
    
    plt.savefig(base_filename + "_fig.pdf")
else:
    print("input file does not exist")