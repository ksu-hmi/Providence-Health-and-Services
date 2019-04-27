from flask import Flask ,flash,session,render_template,redirect,escape, url_for,request, send_from_directory
from string import Template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('main.html')

@app.route("/patient-services")
def patient():
    return render_template('patientservices.html')

@app.route("/patient-education")
def education():
    return render_template('pteducation.html')

@app.route("/patient-mediaplayer")
def media():
    return render_template('header.html')

@app.route("/patient-musicplayer")
def music():
    return render_template('ptmusicplayer.html')

@app.route('/videos/<vid>')
def videos(vid):
    vidtemplate = Template("""
      <h2>
        YouTube video link: 
        <a href="https://www.youtube.com/watch?v=${youtube_id}">
          ${youtube_id}
        </a>
      </h2>
    
      <iframe src="https://www.youtube.com/embed/${youtube_id}" width="853" height="480" frameborder="0" allowfullscreen></iframe>
    """)

    return vidtemplate.substitute(youtube_id=vid)

@app.route("/patient-games")
def games():
    return render_template('ptgames.html')

@app.route("/hello")
def hello():
    return "Hello World!"
 
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)