from flask import Flask,request,render_template
app = Flask(__name__)

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
@app.route('/ddd')
def upload_file():
   return render_template('index.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploads_file():
   if request.method == 'POST':
      f = request.files['file']
      #f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)