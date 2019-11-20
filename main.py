# %% main.py
# Description:
# > Main python script for the data processing and plotting of tube data


# %% Python Depdendencies
import 	os
from 	os.path import join
import 	re
import 	math
import	pandas as pd 
import 	numpy as np
import 	matplotlib.pyplot as plt

# %% Tube Line Colours
# > Note: Hammersmith & City and Circle are a double colour due to being combined
tubeColours 	= {
	'Jubilee': 			"#A0A5A9",
	'Northern': 		"#000000",
	'Piccadilly': 		"#003688",
	'Bakerloo': 		"#B36305",
	'Metropolitan': 	"#9B0056",
	'Victoria': 		"#0098D4",
	'Central': 			"#E32017",
	'District': 		"#00782A",
	'Waterloo & City': 	"#95CDBA"	,
	'Hammersmith & City and Circle': "#F3A9BB" #FFD300
}

# %% Peak time definitions
peakTimes 	= {
	'amStart':	3,	# 06:30
	'amStop': 	5,	# 09:30
	'pmStart': 	12,	# 16:00
	'pmStop': 	15	# 19:00
}

# %% Function Definitions

def roundTen(n):
	# Round up number to the nearest multiple of 10
	return int(math.ceil(n / 10.0)) * 10

def loadData(file):
	# > Load the data from supplied CSV file and transform columns into appropriate time axes
	df 			= pd.read_csv(file)
	timePoints 	= list(df.columns[1:])
	# > Isolate the individual start and end for each time point
	newPoints 		= []
	formattedTime 	= []
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
		if len(str(t1)) == 1:
			formattedTime.append('0'+str(t1)+':00')
		else:
			formattedTime.append(str(t1)+':00')
	# > Additional time to account for day shift
	formattedTime.append("(+1) 01:00")
	# > Edit frame
	newFrame 			= df
	newCol 				= newPoints
	newCol 				= [float(x)-3.5 for x in newCol]
	colList 			= ['Line']
	colList.extend(newCol)
	newFrame.columns 	= colList
	newFrame.iloc[:,1:] = newFrame.iloc[:,1:] * 100
	# > Return the frame
	return newFrame, formattedTime

def individualLinePlot(frame, peakTimes, xLabels, line):
	# Create line plot, with time as x-azis, for a specific line
	# > Load the tube information
	tubeFrame 	= frame[frame['Line'] == line]
	tubeColor 	= tubeColours[line]
	tubeX 		= tubeFrame.columns[1:]
	tubeY 		= tubeFrame.iloc[0,1:]
	# > Create the plot
	plt.plot(tubeX,tubeY, 
		color 			= tubeColor, 
		linewidth 		= 3,
		marker 			= 'o',
		markeredgecolor = tubeColor,
		markeredgewidth = 2,
		markerfacecolor = 'white',
	)
	# > X Tick Labels
	plt.xticks(range(1,len(xLabels)+1,1), xLabels, rotation = "vertical")
	# > Ensure correct scaling of y axis limits
	if roundTen(max(tubeY)) < 100:
		yMax 	= 100
	else:
		yMax = roundTen(max(tubeY))
	# > Plot limit and margin adjustments
	plt.ylim((0,yMax))
	plt.subplots_adjust(bottom=0.2)
	# > Create highlighted regions for peak times
	plt.axvspan(
		peakTimes['amStart'], 
		peakTimes['amStop'],
		color 	= 'red',
		alpha 	= 0.25) 	# AM Peak
	plt.axvspan(
		peakTimes['pmStart'], 
		peakTimes['pmStop'],
		color 	= 'red',
		alpha 	= 0.25) 	# PM Peak
	# > Capture figure and set figure size
	fig 		= plt.gcf()
	fig.set_size_inches(10,5)
	# > Convert tube line into filename-safe string and save into figures
	saveName 	= re.sub(r'\W+', '', line)
	fig.savefig(join('figures',saveName+'.pdf', dpi=600))

def multipleLinePlots(frame, peakTimes, xLabels):
	# Create line plots, with time as x-azis, for the capacity of each individual line
	# > Create and save a plot for each tube line
	for tube in tubeLines:
		# > Run individual figure creation
		individualLinePlot(frame, peakTimes, xlabels, line)

def summaryLinePlot(frame):
	# Create a line plot, with time as x-axis, for the capacity of all lines
	# > Identify all the lines
	tubeLines 	= list(set(frame['Line']))
	# > Record max values
	maxValues 	= []
	# > Create and save a plot for each tube line
	for tube in tubeLines:
		# > Load the tube information
		tubeFrame 	= frame[frame['Line'] == tube]
		tubeColor 	= tubeColours[tube]
		tubeX 		= tubeFrame.columns[1:]
		tubeY 		= tubeFrame.iloc[0,1:]
		maxValues.append(max(tubeY))
		# > Create the plot
		plt.plot(tubeX,tubeY, 
			color 			= tubeColor, 
			linewidth 		= 3,
			marker 			= 'o',
			markeredgecolor = tubeColor,
			markeredgewidth = 2,
			markerfacecolor = 'white',
		)
	# > X Tick Labels
	plt.xticks(range(1,len(xLabels)+1,1), xLabels, rotation = "vertical")
	# > Ensure correct scaling of y axis limits
	if roundTen(max(maxValues)) < 100:
		yMax 	= 100
	else:
		yMax = roundTen(max(maxValues))
	# > Plot limit and margin adjustments
	plt.ylim((0,yMax))
	plt.subplots_adjust(bottom=0.2)
	# > Create highlighted regions for peak times
	plt.axvspan(
		peakTimes['amStart'], 
		peakTimes['amStop'],
		color 	= 'red',
		alpha 	= 0.25) 	# AM Peak
	plt.axvspan(
		peakTimes['pmStart'], 
		peakTimes['pmStop'],
		color 	= 'red',
		alpha 	= 0.25) 	# PM Peak
	# > Capture figure and set figure size
	fig 		= plt.gcf()
	fig.set_size_inches(15,10)
	# > Convert tube line into filename-safe string and save into figures
	fig.savefig(join('figures','allTubeSummary.pdf', dpi=600))

# %% Run Workflow
# > Isolate frame and xTick Labels
frame, xLabels = loadData('MQ2019_19838_TubeCapacity.csv')
individualLinePlot(frame, peakTimes, xLabels, 'Northern')