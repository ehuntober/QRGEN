from flask import Flask 
import os


app = Flask(__name__)

dir_path=os.path.dirname(os.path.realpath(__file__))

app.config.update(
    UPLOAD_PATH=os.path.join(dir_path,"static")
)

app.config['SECRET_KEY'] = 'bdb21f595598ab4780155f48ea1c1add8ef3efdd'


from application import routes
