from flask import Flask, render_template, request, redirect, jsonify, send_from_directory, url_for, send_file
from werkzeug.utils import secure_filename

import os
import asyncio
from moviepy.editor import VideoFileClip, clips_array, vfx
import moviepy.editor as me


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('dashboard.html')

video_name = ''
@app.route('/create', methods=['POST', 'GET'])
def create():
    global video_name
    if request.method == 'POST':
        data = request.json
        video_name = str(data['bg'] + 1) + str(data['ef'] + 1)

    return render_template('create.html', video_name=video_name)

@app.route('/dowload/<name>', methods=['GET'])
def dowload(name):
    if request.method == 'GET':
        return send_from_directory(directory='static', path=f"video/{name}.mp4", as_attachment=True)



# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True)

# UPLOAD_FOLDER = 'static/uploads/'
# @app.route('/upload', methods=['POST', 'GET'])
# def upload():
#    file = request.files['file']
#    file.save('static/uploads/' + file.filename)
#    return 'File uploaded and saved.'

# async def create_video(data):
#     output_path="static/output.mp4"
#     video_clip = VideoFileClip(("static/bg/" + data['bg'] + ".mp4"), target_resolution=(1080, 1080)) #b .mp4 file
#     overlay_clip = VideoFileClip(("static/ef/" + data['ef'] + ".mov"), has_mask=True, target_resolution=(1080, 1080)) #.mov file with alpha channel

#     final_video = me.CompositeVideoClip([video_clip, overlay_clip])  
#     final_video.write_videofile(
#         output_path,
#         fps=30,
#         remove_temp=True,
#         codec="libx264",
#         audio_codec="aac",
#         threads = 6,
#     )

# @app.route('/create', methods=['POST', 'GET'])
# async def create():
#     if request.method == 'POST':
#         data = request.json
#         await create_video(data)
#         print(1)

#     return render_template('dashboard.html')


# async def async_get_data():
#     await asyncio.sleep(1)
#     return 'Done!'


# @app.route("/data")
# async def get_data():
#     data = await async_get_data()
#     return data