from flask import Flask, render_template, request, send_from_directory
from MukeshAPI import api
import os
import datetime

app = Flask(__name__)

UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        response = api.ai_image(prompt)
        
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'mukesh{timestamp}.jpg'
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        with open(filepath, 'wb') as f:
            f.write(response)

        return render_template('index.html', filename=filename)
    return render_template('index.html', filename=None)

@app.route('/static/images/<filename>')
def display_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)