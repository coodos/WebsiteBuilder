# importing dependencies
from flask import *
import os

# instantiating a flask app
app = Flask(__name__, static_folder='static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#Preset Elements and CSS
elements = {
    'topBar': '''
<div class="topBar">
    {}
</div>
    ''',
    'main': '''
<div class="main">
    <h1>
        {}
    </h1>
</div>
    ''',
    'about': '''
<div class="about">
    <h1>
        About Us
    </h1>
    <p>
        {}
    </p>
</div>
    ''',
    'features': '''
<div class="features">
    <div class="feature">
        {}
    </div>
    <div class="feature">
        {}
    </div>
    <div class="feature">
        {}
    </div>
</div>
    ''',
    'contact': '''
<div class="contact">
    <h1>
        Contact Us
    </h1>
    <form action"mailto:{}">
        <input type="text" name="name" placeholder="your name">
        <br>
        <input type="text" name="name" placeholder="email address">
        <br>
        <input type="text" name="name" placeholder="Phone Number">
        <br>
        <textarea placeholder="Your message" rows="4" cols="50"></textarea>
        <br>
        <input type="submit" value"Send Message" class="btn">
    </form>
</div>
    ''',
    'footer': '''
<div class="footer">
    {}
</div>
    '''
}

styles = {
    'topBar': '''

.topBar {
    width: 100%;
    height: 30px;
    padding: 15px;
    background-image: linear-gradient(to bottom right, #3d3d3d, #5d5d5d);
    text-align: center;
    color: white;
    font-size: 23px;
}
    ''',
    'main': '''

.main {
    width: 100%;
    margin: 0;
    padding: 0;
    height: 800px;
    background: url('../imgs/header.jpg');
    background-repeat: no-repeat;
    background-size: cover;
}

.main h1 {
    padding-top: 330px;
    margin-top: 0;
    text-align: center;
    width: 60%;
    font-size: 100px;
    margin-left: 20%;
    object-fit: cover;
    color: white;
}
''',
    'about': '''

.about {
    padding: 40px;
    background-color: #f5f5f5;
    width: 100%;
}

.about p {
    width: 70%;
    text-align: justify;
    margin-left: 15%;
}

.about h1 {
    width: 80%;
    margin-left: 15%;
    font-size: 60px;
}    

''',
    'features': '''
.features {
    width: 100%;
    padding: 40px 1%;
    height: 95vh;
    background-color: #d3d3d3;
}

.feature {
    width: 21.5%;
    float: left;
    margin: 30px 0.5%;
    background-color: #fff;
    border-radius: 10px;
    text-align: center;
    height: 70vh;
    padding: 4% 5%;
}

    ''',
    'contact': '''
.contact {
    width: 100%;
    padding: 50px;
    background-color: #fff;
    margin-top: 20px;
}

.contact input[type=text] {
    width: 70%;
    padding: 8px;
    margin: 5px;
    margin-left: 10%;
}

.contact textarea {
    width: 70%;
    padding: 8px;
    margin: 5px;
    margin-left: 10%;
}

.contact h1 {
    font-size: 80px;
    margin-left: 10%;
}

.btn {
    width: 71.5%;
    margin: 15px 10%;
    padding: 20px;
    font-size: 20px;
    color: white;
    background-image: linear-gradient(to bottom right, rgb(0, 168, 235), rgb(99, 99, 250));
    border: none;
    border-radius: 5px;
}
    ''',
    'footer': '''
.footer {
    width: 100%;
    height: 30px;
    padding: 15px;
    background-image: linear-gradient(to bottom right, #3d3d3d, #5d5d5d);
    text-align: center;
    color: white;
    font-size: 23px;
}

@media only screen and (max-width: 1000px) {
    .feature {
        width: 90%;
        margin-left: 5%;
    }
}
    '''
}

# this is the index route to the application
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addElement', methods=['POST'])
def addElement():
    # receiving the data from POST 
    queryData = request.form['queryData']
    elemType = request.form['type']
    # Adding returned data to html file 
    with open('static/output/index.html', 'a+') as html:
        if elemType == 'topBar':
            html.write(f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="css/body.css">
    <link rel="stylesheet" href="css/main.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{queryData}</title>
</head>
<body>''')
            html.write(elements[elemType].format(queryData))
        elif elemType == 'footer':
            html.write(elements[elemType].format(queryData))
            html.write('''
</body>
</html>
            ''')
        else: 
            html.write(elements[elemType].format(queryData))
    with open('static/output/css/main.css', 'a+') as css:
        css.write(styles[elemType])
    return 'none'

@app.route('/features', methods=['POST'])
def addThreeStuffDiv():
    # get stuff of divs
    elemType = request.form['type']
    one = request.form['one']
    two = request.form['two']
    three = request.form['three']
    with open('static/output/index.html', 'a+') as html:
        html.write(elements[elemType].format(one, two, three))
    with open('static/output/css/main.css', 'a+') as css:
        css.write(styles[elemType])

@app.route('/delete')
def deleteWebsite():
    try:
        os.remove('static/output/index.html')
    except FileNotFoundError:
        pass
    try:
        os.remove('static/output/css/main.css')
    except FileNotFoundError:
        pass
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
