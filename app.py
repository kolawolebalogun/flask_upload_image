"""
This simple flask apps accepts images from users,
and displays the image to the user without saving it to the location on the server.
"""
import io
from flask import Flask, request, render_template, send_file, abort

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def hello_world():
    # Render the upload for if request is a GET Request
    if request.method == "GET":
        return render_template("index.html")
    # Process the from data if request is a POST Request
    elif request.method == 'POST':
        # Check if "image" key is in the form files; if false return message to user
        if "image" in request.files:
            image = request.files.get('image')
            # Define the only accepted image extension required
            allowed_extension = {'jpg', 'jpeg', 'png', 'gif'}
            # Get full filename and extract extension
            filename = image.filename
            extension = filename.rsplit('.', 1)[1].lower()

            # Check if file extension is a permitted extension
            if extension in allowed_extension:
                image_binary = image.read()
                return send_file(io.BytesIO(image_binary), mimetype="image/{}".format(extension),
                                 attachment_filename='image.pdf')

        abort(403)
