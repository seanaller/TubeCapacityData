# %% main.py
# Description:
# > Main python script for the data processing and plotting of tube data


# %% Python Depdendencies
import 	os
import 	re
import	pandas as pd 
import 	numpy as np
import 	matplotlib.pyplot as plt

# %% Function Definitions
def loadData(file):
	# Load the data from supplied CSV file and transform columns into appropriate time axes
	df 			= pd.read_csv(file)
	timePoints 	= list(df.columns[1:])
	# Isolate the individual start and end for each time point
	newPoints 	= []
	newPoints.append('Line')
	for point in timePoints:
		if '0000-' in point:
			t1 	= int(24)
		else:
			t1 	= int(re.search(r'(?!0)(.*)(?=00-)',point).group())
		#if '-0000' in point:
		#	t2 	= int(24)
		#else:
		#	t2 	= int(re.search(r'(?<=-)(.*)(?<!0)',point).group().lstrip("0"))
		newPoints.append(t1)
	# Edit frame
	newFrame = df
	newFrame.columns = newPoints
	newFrame.iloc[1:,1:] = newFrame.iloc[1:,1:] * 100
	# Return the frame
	return newFrame

def summaryLinePlot(frame):
	# Create a line plot, with time as x-axis, for the capacity of all lines
	
	
# def individualLinePlot(frame):
	# Create line plots, with time as x-azis, for the capacity of each individual line	

# %% Run Workflow
frame 	= loadData('MQ2019_19838_TubeCapacity.csv')
print(frame.head())