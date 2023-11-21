# Import Libraries below
import os
from flask import  Flask, request, redirect, url_for, render_template
#import cv2 as Opencv 
from werkzeug.utils import secure_filename 
# Define flask 
app = Flask(__name__)
@app.route('/' ) 
# Define upload_form() and route the webapp 
def upload_form():
	return render_template('upload.html')

@app.route('/' , methods=['POST'])


# Define upload_video() to get video in defined folder and route the webapp  
def upload_video():
	file = request.files['file']
	filename = secure_filename(file.filename)
	file.save(os.path.join('static/' , filename))

	return render_template("upload.html" , filename = filename)




# Define display_video() to Display video in defined folder and route the webapp  
@app.route('/display/<filename>')
def display_video(filename):
	return(redirect(url_for('static' , filename = filename)))





if __name__ == "__main__":
    app.run(debug=True)
