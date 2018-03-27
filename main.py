from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>



<html>

    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}

        </style>
    </head>

    <body>
      <!-- create your form here -->
        <form method="post">
            <label for='rot'>Rotate by:</label>
            <input type='text' name='rot' value='0'/>
            <input type="submit" value="Submit"/>
            <textarea name='text' >{0}</textarea>
        </form>
    </body>
</html>
"""
@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    rot_int = int(rot)
    text = request.form['text']
    text_str = str(text)
    new_string = rotate_string(text_str, rot_int)
    return form.format(new_string)



app.run()