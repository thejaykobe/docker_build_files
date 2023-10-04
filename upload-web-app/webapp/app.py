from flask import Flask, request, render_template
import os

app = Flask(__name__)

UPLOAD_FOLDER = os.path.abspath('/usr/share/webapp_uploaded')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
	xreal_ip = request.headers.get('X-Real-IP')
        if real_ip:
	    print(f"X-Real-IP: {real_ip}")
        file = request.files['file']
        if file:
            max_file_size = 512 * 512 * 512
            if file.content_length > max_file_size:
                return "File not accepted"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return "File Uploaded Successfully"
    return "Please contact support @ support@0mnihosting.org for help"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
