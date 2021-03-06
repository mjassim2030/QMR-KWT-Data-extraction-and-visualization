# QMR-KWT-Data-extraction-and-visualization


Design an algorithm that will be uploaded to the CubeSat to collect sensors data and store them in a log file, then it will send those data to the ground station to be visualized on a dashboard where the data could be manipulated further more. 
Principle
1-	On-board Code
-	This code will be written in Python which will interface with the OBC hardware and extract the data for accelerometers, digital compasses, temperature sensor, real time  clock, battery level…etc.

- The data then be stored in a comma separated values file (CSV) as the following schema with an example:

DATA_ID	ACC_X	ACC_Y	ACC_Z	CMP	TMP	BAT	RTC
0	12	-21	23	-16	-50	40	13:20:30

2-	Data Analysis Platform (Ground)
Once the data are collected and sent to the ground the station it will be accessed using an API (Will be developed) to visualize the data on a front end dashboard that could be easily accessed by anyone.
The platform will not only view the data but it will do the following:
-	Predict the CubeSat current location and view it on a map. 
-	Smooth interpolation of each of collected parameter so the data will be viewed on curve graph showing values fluctuation.
-	Allow the user to set range of acceptable values for each parameter and alert the user when the any value exceeded the range. (minimum and maximum)

Screen shots of the dashbaord:

![GitHub Logo](https://github.com/Athary/QMR-KWT-Data-extraction-and-visualization/raw/master/static/img/dashboard01.jpg)

![GitHub Logo](https://github.com/Athary/QMR-KWT-Data-extraction-and-visualization/raw/master/static/img/dashboard02.jpg)

![GitHub Logo](https://github.com/Athary/QMR-KWT-Data-extraction-and-visualization/raw/master/static/img/dashboard03.jpg)

# Software and Programing language
-	Python 3.5 for the code that will be on-board
-	Python 3.5 using flask framework for the dashboard
-	Bootstrap 4.0 and jQuery for front of the dashboard
-	Github to store the source code of the project
-	heroku Cloud Platform to upload the python project code to be accessed online

# Install
- To Start the data logger, run the code: [python log.py]
- To Start the user interface, run the code: [python ground.py]
- 
# Contributions
- Code written by - Eng. Mohammed Jassim
- Supervised by Dr. Abdulmonem Alshino (University of Bahrain) 

for the Code in Space Challenge 2021 by <a style="color: aqua;" href="https://orbital-space.com">Orbital Space</a> and <a style="color: aqua;" href="https://www.nssa.gov.bh/">NSSA Bahrain</a>

