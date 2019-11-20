# Tube Capacity Data - Analysis

#### Description

Analysis of the Tube Capacity Data obatined 20th October 2019. Time series data exploring the per-line capactiy of the London Tube lines on a "typical weekday"

#### Data Information

| Title       | Tube Capacity (1)                                            |
| ----------- | ------------------------------------------------------------ |
| Link        | https://www.london.gov.uk/questions/2019/19838               |
| Date        | 22 10 2019                                                   |
| Description | Please see attached to this answer the capacity utilisation level of each Tube line by hour on a typical weekday. <br/>A second table tallies whether this value is over 50 per cent and a third estimates whether all seats are taken. <br/>Please note Transport for London (TfL) does not have a way to monitor train loadings accurately in real time. <br/>Although it holds ticketing data, this only indicates where customers entered and exited the network, not which route they took within it. <br/>This analysis is based on the typical weekday TfL uses for planning purposes, where a combination of survey data and assignment modelling are used to determine the combination of routes passengers are likely to have taken through the network. |
| File        | MQ2019_19838 - Tube Capacity (1).xlsx                        |

#### Tube Summary

Summary, for all tube lines, of the average weekday capacity. Data resolution is collected in hour time spans (i.e. 06:00 to 07:00) and so the data is plotted at the median of these (i.e. 06:30) for that time span. 

Note that times between 01:00 and 05:00 are absent as the tubes do not run through this time (weekdays).

Peak times (as defined by TFL) are shown using grey-blue hatching. Peak times are defined as:

* AM: 06:30 to 09:30
* PM: 16:00 to 19:00

![Summary Tube Capacity](figures/allTubeSummary.pdf)  

Note: Individual line summaries are avaliable in the "/figures" folder.
