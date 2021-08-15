'''from flask import Flask, render_template, request,flash
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)
UPLOAD_FOLDER = './upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.secret_key = 'many random bytes'
@app.route('/upload')
def upload_file():
   return render_template('upload.html')
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file1():
   if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',filename=filename))
   return render_template('upload.html')
if __name__ == '__main__':
   app.run(debug = True)'''
import os
from flask import Flask, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename
#from waitress import serve
UPLOAD_FOLDER = './static/myfiles'
GALLERY_FOLDER='./gallery'
#ALLOWED_EXTENSIONS = set(['txt','pdf','mkv','mp4'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['GALLERY_FOLDER'] = GALLERY_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/u", methods=['GET', 'POST'])
def index1():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect('/u')
    return render_template('upload1.html')
@app.route('/gallery')
def get_gallery():
    image_names = os.listdir(app.config['UPLOAD_FOLDER'])
    print(image_names)
    return render_template("gallery1.html", image_names=image_names)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001,debug=True)
