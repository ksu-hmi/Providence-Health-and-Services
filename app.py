from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def index():
    return """
<!DOCTYPE html>
<html>
<head>
    <style>
      body, html {
        height: 100%;
        margin: 0;
        background-color: green;
      }
       
      .bg {
       
        background-image: url("https://www.yourprovidencehealth.com/Content/Uploads/Providence%20Hospitals/images/Building%20Facilities%20Photos/Providence%20Health%20downtown%20hospital%20at%20night.jpg");

        height: 100%;

        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
      }
    </style>
   <title>My title</title>
   <link rel="stylesheet" href="http://stash.compjour.org/assets/css/foundation.css">
   
    <h1>Providence Health & Services </h1>
    <p>4805 NE Glisan St, Portland, OR 97213</p>
    <p>Phone: (503) 215-111 </p>
    <div class="bg">

    <form method="get" action="/patient-services">
        <p>
        <input type="submit" value="Next Page"/>
        </p>
    </form>

    <ul>
    <li>
    <a href="/patient-services">http://paitent-services.com</a>
    </li>
    </ul>
    
    </div>
       echo ("Rx Team");
        ?>
        <div>
            <img src="rxteam.jpg" alt="rxteam" />
			<iframe  width="570" height="300" src="https://www.ispot.tv/share/ACn4" frameborder="0" scrolling="no" allowfullscreen=""></iframe>
        </div>
        
    </body>
</html>
"""
 
@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/patient-services")
def patient():
    return """
<!DOCTYPE html>
<html>
<head>
    <style>
      body, html {
        height: 100%;
        margin: 0;
        background-color: lightseagreen;
      }
       
      .bg {
       
        background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQe3m51XbL6u4vyWuopj74KWR2J--W_muQ-75Iryiy28RH1HkBeeQ.jpg");

        height: 100%;

        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
      }
    </style>
   <title>My title</title>
   <link rel="stylesheet" href="http://stash.compjour.org/assets/css/foundation.css">
   
    <h1>Providence Health & Services </h1>
    <p>Info about hospital</p>
    <p>And here's an image:</p>
    <div class="bg">
    
    </div>
       echo ("Rx Team");
        ?>
        <div>
            <img src="rxteam.jpg" alt="rxteam" />
			<iframe  width="570" height="300" src="https://www.ispot.tv/share/ACn4" frameborder="0" scrolling="no" allowfullscreen=""></iframe>
        </div>
    </body>
</html>
"""
 
@app.route("/members")
def members():
    return "Members"
 
@app.route("/members/<string:name>/")
def getMember(name):
    return name
 
if __name__ == "__main__":
    app.run()
