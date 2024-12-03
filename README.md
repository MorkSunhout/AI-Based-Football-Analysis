# Football Analysis Project
## Introduction
The objective of this project is to develop a system that can detect and track players, referees, and footballs in video footage using YOLO (You Only Look Once), a state-of-the-art object detection model.

In addition to object detection, the project will utilize K-means clustering for pixel segmentation, which will enable the automatic assignment of players to their respective teams based on the color of their shirts. This information will then allow us to calculate each team's ball possession percentage during a match.

The project will also incorporate optical flow techniques to track the movement of players by measuring camera motion between consecutive frames. To better quantify player movement in real-world terms, we will apply perspective transformation, converting the image’s coordinates from pixels to meters. This transformation will enable precise tracking of a player's speed and the distance they cover throughout the match.

![Screenshot](output_videos/screenshot.png)

## Modules Used

The following modules are used in this project:

- **YOLO**: AI object detection model
- **Kmeans**: Pixel segmentation and clustering to detect t-shirt color
- **Optical Flow**: Measure camera movement
- **Perspective Transformation**: Represent scene depth and perspective
- **Speed and distance calculation per player**: Measure player's speed and distance covered

## Trained models

- [Trained YOLO v5](https://drive.google.com/file/d/16IqbDw6ibE_-soz1vv1CzlfJpEKzFSpX/view?usp=sharing)

## Datasets

- [Roboflow Football Dataset](https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc/dataset/1)
- [Sample Input Video from kaggle Dataset](https://drive.google.com/file/d/1lcVC7bk8ErCURDbmS0vL3p22dcJSFO1-/view?usp=sharing)

## Requirements

To run this project, you need to have the following requirements installed:

- Python 3.x
- ultralytics
- supervision
- OpenCV
- NumPy
- Matplotlib
- Pandas
