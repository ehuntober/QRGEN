from flask import Flask 
from flask import render_template , request , redirect ,url_for
import os
import qrcode
# import cv2

import secrets

app = Flask(__name__)

dir_path=os.path.dirname(os.path.realpath(__file__))

app.config.update(
    UPLOAD_PATH=os.path.join(dir_path,"static")
)

app.config['SECRET_KEY'] = 'bdb21f595598ab4780155f48ea1c1add8ef3efdd'






@app.route('/',methods=['GET','POST'])
def index_page():
    return render_template('generate_qrcode.html', title="index Page")

@app.route('/generate',methods=['POST'])
def generate_url():
    
    return redirect(url_for('index_generated'))


@app.route('/generated')
def index_generated():
    data = request.form.get('url')
    image_name = f"{secrets.token_hex(10)}.png"
    qrcode_location = f"{app.config['UPLOAD_PATH']}/{image_name}"
    my_qrcode = qrcode.make(str(data))
    my_qrcode.save(qrcode_location)

    return render_template('generated_qrcode.html',image = image_name)


@app.route('/decode',methods=['POST','GET'])
def decode_url():
    if request.method == 'POST':
        file = request.files['file']

        # file_path = os.path.abspath(str(file))

        # img = cv2.imread(file_path)

        # detector = cv2.QRCodeDetector()

        # data,bbox, straight_qrcode = detector.detectAndDecode(img)

        return redirect(url_for( 'wait'))

    return render_template('decode.html')
 

@app.route('/waitlist',methods=['POST','GET'])
def wait():
    return render_template('coming.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500



if __name__ == '__main__':
    app.run()