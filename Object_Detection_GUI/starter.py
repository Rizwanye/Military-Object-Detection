import argparse
import os
import subprocess
from subprocess import Popen
import time
from flask import Flask, render_template, request, send_from_directory, Response
from werkzeug.utils import secure_filename
import cv2
from moviepy.editor import VideoFileClip
import uuid

app = Flask(__name__)

# Set the upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
TEST_FOLDER = '/static'

YOLOV5_WEIGHTS = 'best.pt'

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/page2")
def page2():
    return render_template('page2.html')


@app.route("/analyze", methods=["POST"])
def analyze():
    if 'file' not in request.files:
        return "No file uploaded"

    file = request.files['file']
    if file.filename == '':
        return "No file selected"

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)


    process = Popen(["python", "detect.py", "--source", file_path, "--weights", YOLOV5_WEIGHTS], shell=True)
    process.wait()

    # Get the most recent directory in 'runs/detect/exp'
    exp_dirs = os.listdir('runs/detect')
    exp_dirs.sort(reverse=True)  # Sort in reverse order

    if not exp_dirs:  # Check if the list is empty
        return "No detection results found, check the program output, most likely missing packages/modules."

    recent_exp_dir = exp_dirs[0]

    detected_filename = "detected_" + str(uuid.uuid4()) + ".mp4"  # Generate a unique filename
    detected_file_path = os.path.join('static', detected_filename)  # Save in static folder

    # Move the detected video file to the static folder
    detected_temp_file_path = os.path.join('runs', 'detect', recent_exp_dir, filename)
    os.rename(detected_temp_file_path, detected_file_path)

    # Convert the video to WebM format using moviepy
    webm_filename = "detected_" + os.path.splitext(filename)[0] + ".webm"
    webm_file_path = os.path.join('static', webm_filename)
    clip = VideoFileClip(detected_file_path)
    clip.write_videofile(webm_file_path, codec='libvpx-vp9')

    return render_template('page2.html', detected_file=webm_filename)



@app.route("/static/<path:filename>")
def display_video(filename):
    file_path = os.path.join(app.root_path, 'static', filename)
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, mimetype='video/webm', conditional=True)


def get_frame(filename):
    file_path = os.path.join('static', filename)  # Access from static folder
    video = cv2.VideoCapture(file_path)

    while True:
        success, image = video.read()
        if not success:
            break
        ret, jpeg = cv2.imencode('.jpg', image)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')
        time.sleep(0.1)


@app.route("/static/<path:filename>")
def video_feed(filename):
    return Response(get_frame(filename), mimetype='multipart/x-mixed-replace; boundary=frame')


# video
@app.route("/video")
def serve_video():
    message = "Video Route"
    return render_template('video.html', message=message)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask app for object detection")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    args = parser.parse_args()

    app.run(host="0.0.0.0", port=args.port, debug=True, threaded=True)
