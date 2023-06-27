# Military-Object-Detection
This project utilised Python programming, specifically the yolov5 package to detect military assets such as soldiers, supply trucks and assult vehicles. It is trained on infra-red imagery of simulated objects from drone video footage. 

In this github it has the google collab file used to train the object detection program and the flask gui built for the application.

A presentation of the entire project can be summarised in the youtube video below. 

<p align="center">
  <a href="https://www.youtube.com/watch?v=hLSiAEOvlas&t=1s&ab_channel=RizwanYe">
    <img src="https://github.com/Rizwanye/Military-Object-Detection/raw/main/youtube_thumbnail.jpg" width="50%" alt="Alt Text">
  </a>
</p>

# Output of sample object classifications
Below are sample images of the classified objects from the output of this project. Please allow 1 - 2 minutes for the gifs to load as it is quite large. 
<div style="display: flex;">
  <img src="https://github.com/Rizwanye/Military-Object-Detection/blob/main/example1.gif" width="256" style="margin-right: 10px;" />
  <img src="https://github.com/Rizwanye/Military-Object-Detection/blob/main/example2.gif" width="256" style="margin-right: 10px;" />
  <img src="https://github.com/Rizwanye/Military-Object-Detection/blob/main/example3.gif" width="256" />
</div>

# Flask GUI built for the program
The final project was finalised together using flask, the backend used yolov5 object classifcation with yolo5x for its backbone. In the website, users can upload an infra-red video (drone video) and the program will classify and maintain bounding boxes on these objects.
<a href="https://github.com/Rizwanye/Military-Object-Detection">
  <img src="https://github.com/Rizwanye/rizwanye/blob/main/project1.gif" width="456" />
</a>
