# Football Analysis Project
## Introduction
The objective of this project is to develop a system that can detect and track players, referees, and footballs in video footage using YOLO (You Only Look Once), a state-of-the-art object detection model.

In addition to object detection, the project will utilize K-means clustering for pixel segmentation, which will enable the automatic assignment of players to their respective teams based on the color of their shirts. This information will then allow us to calculate each team's ball possession percentage during a match.

The project will also incorporate optical flow techniques to track the movement of players by measuring camera motion between consecutive frames. To better quantify player movement in real-world terms, we will apply perspective transformation, converting the image’s coordinates from pixels to meters. This transformation will enable precise tracking of a player's speed and the distance they cover throughout the match.

