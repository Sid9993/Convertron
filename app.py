from flask import Flask,session,request,render_template,flash,redirect,send_from_directory,abort,send_file
import os
#to give secure filename
from werkzeug.utils import secure_filename
#tesseract import
import pytesseract as tess
tess.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
from PyPDF2 import PdfFileMerger
from flask_session import Session

SESSION_TYPE="memcache"

app = Flask(__name__)
app.secret_key = 'super secret key'
sess=Session()

#upload folder details
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#app.config['SESSION_TYPE'] = 'filesystem'

#FILE CONFIG INSTRUCTIONS#
#providing a path to where we want to temperorily save the image
app.config["IMAGE_UPLOADS"]="static/uploads"
app.config["allowed_image_extensions"]=["JPG","PNG","JPEG"]

def allowed_ext(filename):
   if "." not in filename:
      return False
   else:
      s=filename.split(".")
      if s[1].upper() in app.config["allowed_image_extensions"]:
         return True
      else:
         return False

### TEXT EXTRACTION USING TESSERACT ###
def image_ocr(image_path, output_txt_file_name):
  image_text = tess.image_to_string(image_path, lang='eng+ces', config='--psm 1')
  with open(output_txt_file_name, 'w+', encoding='utf-8') as f:
    f.write(image_text)

########################################

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/contact')
def contact():
   return render_template('contact.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/convert')
def convert():
   return render_template('convert.html')

@app.route('/download-image')
   
#upload function need completion
@app.route('/upload-image',methods=['GET','POST'])
def upload_file():
   if request.method=='POST':
      if request.files:
         image=request.files['name']
         if image.filename=="":
            print("image should have a file name")
            return redirect(request.url)

         if allowed_ext(image.filename)== False:
            print("image extension is invalid")
            return redirect(request.url)
         
         else:
            #giving secure filename
            filename=secure_filename(image.filename)
            #saving the image
            image.save(os.path.join(app.config["IMAGE_UPLOADS"],filename))
            image_ocr
            
         return redirect(request.url)
   #if 'file1' not in request.files:
    #  flash('no file part') 
     # return redirect (request.url)
   return render_template('convert.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploads_file():
   if request.method == 'POST':
      f = request.files['file']
      #f.save(secure_filename(f.filename))
      return 'file uploaded successfully'


#portion to merge the pdf
@app.route('/upload-pdf', methods=['GET', 'POST'])
def upload_file_pdf():
    if request.method=='POST':
        if 'test' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        files = request.files.getlist('test')
        merger = PdfFileMerger()
        for file in files:
            if file.filename != '':
                merger.append(file)
        merger.write("final.pdf")
        merger.close
        return send_file("final.pdf")

        #uploaded_file = request.files['test']
        #if uploaded_file.filename != '':

            #uploaded_file.save(uploaded_file.filename)
         #   uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename))
            #return send_file()
    return render_template('convert.html')
		
if __name__ == '__main__':
   
   app.config['SESSION_TYPE'] = 'filesystem'

   sess.init_app(app)
   app.run(debug = True)