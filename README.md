# Military-Object-Detection
This project utilised Python programming, specifically the yolov5 package to detect military assets such as soldiers, supply trucks and assult vehicles. It is trained on infra-red imagery of simulated objects from drone video footage. 

In this github it has the google collab file used to train the object detection program and the flask gui built for the application.

A presentation of the entire project can be summarised in the youtube video below. 

<div style="display: flex;">
  <div style="margin-right: 10px;">
    <a href="https://www.youtube.com/watch?v=hLSiAEOvlas&t=1s&ab_channel=RizwanYe">
      <img src="https://github.com/Rizwanye/Military-Object-Detection/raw/main/youtube_thumbnail.jpg" width="50%" alt="Alt Text">
    </a>
    <p style="text-align: center;">Power Point Presentation</p>
  </div>
  
  <div style="display: flex;">
    <a href="https://www.youtube.com/watch?v=I2R6yuKW-l4&ab_channel=RizwanYe">
      <img src="https://github.com/Rizwanye/Military-Object-Detection/raw/main/youtube_thumbnail_2.jpg" width="50%" alt="Alt Text">
    </a>
    <p style="text-align: center;">Video Trailer Presentation with Demonstration</p>

</div>



# Output of sample object classifications
Below are sample images of the classified objects from the output of this project. Please allow 1 - 2 minutes for the gifs to load as it is quite large. 
<div style="display: flex; justify-content: center;">
  <img src="https://github.com/Rizwanye/Military-Object-Detection/blob/main/example1.gif" width="256" style="margin-right: 10px;" />
  <img src="https://github.com/Rizwanye/Military-Object-Detection/blob/main/example2.gif" width="256" style="margin-right: 10px;" />
  <img src="https://github.com/Rizwanye/Military-Object-Detection/blob/main/example3.gif" width="256" />
</div>

# Flask GUI built for the program
The final project was finalised together using flask, the backend used yolov5 object classifcation with yolo5x for its backbone. In the website, users can upload an infra-red video (drone video) and the program will classify and maintain bounding boxes on these objects.
<div style="text-align: center;">
  <a href="https://github.com/Rizwanye/Military-Object-Detection">
    <img src="https://github.com/Rizwanye/rizwanye/blob/main/project1.gif" width="456" />
  </a>
</div>

## Error handling added on GUI

1. Error handling for missing file upload:
The code checks if the 'file' key is not present in request.files and returns the string "No file uploaded". This handles the case when the user submits the form without selecting any file.

2. Error handling for empty file selection:
The code checks if the filename of the uploaded file is empty and returns the string "No file selected". This handles the case when the user selects a file but its filename is empty.

3. Error handling for missing detection results:
The code checks if the list of exp_dirs is empty, indicating that no detection results were found. It returns the string "No detection results found, check the program output, most likely missing packages/modules." This handles the case when the object detection process does not generate any results.
