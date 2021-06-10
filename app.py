from flask import Flask,request,render_template,flash,redirect
import os
#to give secure filename
from werkzeug.utils import secure_filename


app = Flask(__name__)


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
		
if __name__ == '__main__':
   app.run(debug = True)