# Thermographic Data Analysis

## Data

Data comes from a thermal camera which was used to analyze milling of bovine bone. Goal of this project was to understand patterns of the temperature generated from the milling. Easy analysis is to first track max and mean temperature over every frame of the video. Additionally, we can identify the maximum temperature during an experiment, and record the temperature of other 'hot' pixels as designated by some threshold

![image](https://github.com/monkeygobah/bone_milling/assets/117255104/23a07a27-63a0-40a6-8b6a-f6f81a0eeae8)

![image](https://github.com/monkeygobah/bone_milling/assets/117255104/b86b6895-9911-4490-bbba-dea0a245ce5e)


More interesting analysis is to plot the temperature of every pixel over the course of the experiment (color coded by temperature) and then add a slider so one can visualize the 'structure' of the temperature

![image](https://github.com/monkeygobah/bone_milling/assets/117255104/a66e5d0c-e2f2-44a6-869a-21960ab577de)


To analyze the structure further, can perform DBSCAN to identify clusters of pixels at different temperature thresholds. DBSCAN parameters determined by elbow plots.

![image](https://github.com/monkeygobah/bone_milling/assets/117255104/1238cf40-ffc0-458d-9265-a0206d360a86)


