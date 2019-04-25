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
       echo ("Patient Services");
        ?>
                                                                                                                                                                                
        <img src="http://images.gmanews.tv/webpics/2017/04/640_Ken_and_Chris_at_PGH_(Photo_from_Kim_Verly_G_Santiago)_2017_04_04_15_58_03.jpg"alt="Coldplay at Providence"   <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQe3m51XbL6u4vyWuopj74KWR2J--W_muQ-75Iryiy28RH1HkBeeQ"alt="rxteam"/>
         
        <div>
         <iframe width="800" height="300" src="https://www.ispot.tv/share/ACn4" frameborder="0" scrolling="no" allowfullscreen=""></iframe>

         <iframe width="560" height="315" src="https://www.youtube.com/embed/qM5Ells0ii0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        <html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>About Flask</title>
  </head>
  <body>
    {% extends "template.html" %}
    {% block content %}

    <h1> About Flask </h1>
    <p> Flask is a micro web framework written in Python.</p>
    <p> Applications that use the Flask framework include Pinterest,
      LinkedIn, and the community web page for Flask itself.</p>

  <html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Flask Tutorial</title>
  </head>
  <body>
    {% extends "template.html" %}
    {% block content %}

    <h1> My First Try Using Flask </h1>
    <p> Flask is Fun </p>
    <html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Flask Parent Template</title>

    <link rel="stylesheet" href="{{ url_for('static', filename='css/template.css') }}">

  </head>
  <body>
    <header>
      <div class="container">
        <h1 class="logo">First Web App</h1>
        <strong><nav>
          <ul class="menu">
            <li><a href="{{ url_for('home') }}">Home</a></li>
            <li><a href="{{ url_for('about') }}">About</a></li>
          </ul>
        </nav></strong>
      </div>
    </header>

    {% endblock %}
 
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
           
       
         background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtN_MYpa7g103fEU3o_hA3Ccim2EyYw4ryWce53MbP7DWUDuzP");
        height: 100%;

        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
      }
    </style>
   <title>My title</title>
   <link rel="stylesheet" href="http://stash.compjour.org/assets/css/foundation.css">
   
    <h1>Providence Health & Services </h1>
    <p>Family Medicine</p>
    <p>And here's our services:</p>
    <div class="bg">
       

    <form method="get" action="/patient-education">
        <p>
        <input type="submit" value="Next Page"/>
        </p>
    </form>

    <ul>
    <li>
    <a href="/patient-education">http://paitent-education.com</a>
    </li>
    </ul>
    
    </div>
       echo ("Rx Team");
        ?>


        
            <img src="https://bisnow.files.wordpress.com/2011/09/maroon5gwst3.jpg" alt="rxteam" />
        <div>
                <iframe width="580" height="315" src="https://www.youtube.com/embed/6-pou5z5Q2w" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

                 

<blockquote>Achieving the best clinical outcomes requires commitment and passion to transform care for future generations. Through our research programs, clinical trials and strategic initiatives, Providence identifies and implements clinical innovations to enhance patient care.

While we pursue long-term clinical innovations, we also devote time to more immediate initiatives. For instance, our ministries share best practices for reducing hospital-acquired infections and cultivating safer environments that eliminate preventable injuries and deaths. Providence is dedicated to pioneering improvements in health care and changing lives.="cite">Providence</div>

blockquote {
  background-color: white;
  color: yellow;
  padding: 10px;
}

.cite {
  text-align: right;
  font-weight: bold;
  font-size: x-large;
}


function partypartyparty() {
    var quotes = document.getElementsByClassName('fancyquote');
    for(var i=0; i<quotes.length; i++) {
        var r = Math.floor(Math.random()*255);
        var g = Math.floor(Math.random()*255);
        var b = Math.floor(Math.random()*255);
        var q = quotes[i];
        q.style.setProperty('color', 'rgb('+ r +','+ g +',' + b + ')');
    }
}

window.setInterval(partypartyparty, 500);


<h1>Hello stanford!</h1>

      <img src="https://www.providencecare.ca/wp-content/uploads/2018/04/PRO0055-Welcome-Sheet-EN-WEB.pdf">
  
      <img src="https://maps.googleapis.com/maps/api/streetview?size=700x300&location=stanford" alt="street view of stanford">
    

        </div>
    </body>
</html>
"""



@app.route("/patient-education")
def education():
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
           
       
         background-image: url("https://www.travelnursing.com/uploadedImages/StaffCare/Content/Resource_Center/Ethnic_nurse_listening_senior_patient_in_wheelchair.jpg");
        height: 100%;

        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
      }
    </style>
   <title>My title</title>
   <link rel="stylesheet" href="http://stash.compjour.org/assets/css/foundation.css">
   
    <h1>Providence Health & Services </h1>
    <p>Family Medicine</p>
    <p>And here's our services:</p>
    <div class="bg">
   

    <form method="get" action="/patient-entertainment">
        <p>
        <input type="submit" value="Next Page"/>
        </p>
    </form>

    <ul>
    <li>
    <a href="/patient-education">http://paitent-entertainment.com</a>
    </li>
    </ul>
    
    </div>
       echo ("Rx Team");
        ?>

        <div>
                <iframe width="580" height="315" src="https://www.youtube.com/embed/6-pou5z5Q2w" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

                 

<blockquote>Nerds like us are allowed to be unironically enthusiastic about stuff. Nerds are allowed to love stuff - like, jump-up-and-down-in-your-chair-can't-control-yourself love it. When people call other people nerds, mostly what they're saying is "You like stuff", which is not a good insult at all. Like, "You are too enthusiastic about the miracle of human consciousness".</blockquote>
<div class="cite">John Green</div>

blockquote {
  background-color: white;
  color: yellow;
  padding: 10px;
}

.cite {
  text-align: right;
  font-weight: bold;
  font-size: x-large;
}


function partypartyparty() {
    var quotes = document.getElementsByClassName('fancyquote');
    for(var i=0; i<quotes.length; i++) {
        var r = Math.floor(Math.random()*255);
        var g = Math.floor(Math.random()*255);
        var b = Math.floor(Math.random()*255);
        var q = quotes[i];
        q.style.setProperty('color', 'rgb('+ r +','+ g +',' + b + ')');
    }
}

window.setInterval(partypartyparty, 500);


<h1>Hello stanford!</h1>

      <img src="https://www.providencecare.ca/wp-content/uploads/2018/04/PRO0055-Welcome-Sheet-EN-WEB.pdf">
  
      <img src="https://maps.googleapis.com/maps/api/streetview?size=700x300&location=stanford" alt="street view of stanford">

        </div>
    </body>
</html>
"""

@app.route("/patient-entertainment")
def entertainment():
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
           
       
         background-image: url("https://bisnow.files.wordpress.com/2011/09/maroon5gwst3.jpg");
        height: 200%;

        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
      }
    </style>
   <title>My title</title>
   <link rel="stylesheet" href="http://stash.compjour.org/assets/css/foundation.css">
   
    <h1>Providence Health & Services </h1>
    <p>Family Medicine</p>
    <p>And here's our services:</p>
    <div class="bg">
   

    <form method="get" action="/patient-games">
        <p>
        <input type="submit" value="Next Page"/>
        </p>
    </form>

    <ul>
    <li>
    <a href="/patient-education">http://paitent-games.com</a>
    </li>
    </ul>
    
    </div>
       echo ("Rx Team");
        ?>
<!-- Wikplayer https://www.wikplayer.com -->

<script type="text/javascript" src="https://www.wikplayer.com/code.js"

data-config="{'skin':'skins/wikfull/funkyDeepOcean/skin.css','volume':95,'autoplay':true,'shuffle':true,'repeat':2,'showcomment':false,'marqueetexton':true,'placement':'top','showplaylist':false,'playlist':[{'title':'Girls%20Like%20You%20ft.%20Cardi%20B','url':'https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DaJOTlE1K90k'}]}" ></script>

<!-- Wikplayer code end -->
        
        <div>
                <iframe width="580" height="315" src="https://www.youtube.com/embed/6-pou5z5Q2w" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

                 

<blockquote>Nerds like us are allowed to be unironically enthusiastic about stuff. Nerds are allowed to love stuff - like, jump-up-and-down-in-your-chair-can't-control-yourself love it. When people call other people nerds, mostly what they're saying is "You like stuff", which is not a good insult at all. Like, "You are too enthusiastic about the miracle of human consciousness".</blockquote>
<div class="cite">John Green</div>

blockquote {
  background-color: white;
  color: yellow;
  padding: 10px;
}

.cite {
  text-align: right;
  font-weight: bold;
  font-size: x-large;
}


function partypartyparty() {
    var quotes = document.getElementsByClassName('fancyquote');
    for(var i=0; i<quotes.length; i++) {
        var r = Math.floor(Math.random()*255);
        var g = Math.floor(Math.random()*255);
        var b = Math.floor(Math.random()*255);
        var q = quotes[i];
        q.style.setProperty('color', 'rgb('+ r +','+ g +',' + b + ')');
    }
}

window.setInterval(partypartyparty, 500);


<h1>Hello stanford!</h1>

      <img src="https://www.providencecare.ca/wp-content/uploads/2018/04/PRO0055-Welcome-Sheet-EN-WEB.pdf">
  
      <img src="https://maps.googleapis.com/maps/api/streetview?size=700x300&location=stanford" alt="street view of stanford">
    

        </div>
    </body>
</html>
"""

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

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)



@app.route("/patient-games")
def games():
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
           
       
         background-image: url("https://img-s-msn-com.akamaized.net/tenant/amp/entityid/BBUwT7W.img?h=768&w=1366&m=6&q=60&o=f&l=f&x=488&y=302");
        height: 100%;

        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
      }
    </style>
   <title>My title</title>
   <link rel="stylesheet" href="http://stash.compjour.org/assets/css/foundation.css">
   
    <h1>Providence Health & Services </h1>
    <p>Family Medicine</p>
    <p>And here's our services:</p>
    <div class="bg">
   

    <form method="get" action="/providence-profile">
        <p>
        <input type="submit" value="Next Page"/>
        </p>
    </form>

    <ul>
    <li>
    <a href="/providence-profile">http://providence-profile.com</a>
    </li>
    </ul>
    
    </div>
       echo ("Rx Team");
        ?>

        <div>
                <iframe width="580" height="315" src="https://www.youtube.com/embed/6-pou5z5Q2w" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

                 

<blockquote>Nerds like us are allowed to be unironically enthusiastic about stuff. Nerds are allowed to love stuff - like, jump-up-and-down-in-your-chair-can't-control-yourself love it. When people call other people nerds, mostly what they're saying is "You like stuff", which is not a good insult at all. Like, "You are too enthusiastic about the miracle of human consciousness".</blockquote>
<div class="cite">John Green</div>

blockquote {
  background-color: white;
  color: yellow;
  padding: 10px;
}

.cite {
  text-align: right;
  font-weight: bold;
  font-size: x-large;
}


function partypartyparty() {
    var quotes = document.getElementsByClassName('fancyquote');
    for(var i=0; i<quotes.length; i++) {
        var r = Math.floor(Math.random()*255);
        var g = Math.floor(Math.random()*255);
        var b = Math.floor(Math.random()*255);
        var q = quotes[i];
        q.style.setProperty('color', 'rgb('+ r +','+ g +',' + b + ')');
    }
}

window.setInterval(partypartyparty, 500);


<h1>Hello stanford!</h1>

      <img src="https://www.providencecare.ca/wp-content/uploads/2018/04/PRO0055-Welcome-Sheet-EN-WEB.pdf">
  
      <img src="https://maps.googleapis.com/maps/api/streetview?size=700x300&location=stanford" alt="street view of stanford">


       

        </div>
    </body>
</html>
"""
@app.route("/providence-profile")
def profile():
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
           
      
         background-image: url("https://img-s-msn-com.akamaized.net/tenant/amp/entityid/BBUwT7W.img?h=768&w=1366&m=6&q=60&o=f&l=f&x=488&y=302");
        height: 100%;

        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
      }
    </style>
   <title>My title</title>
   <link rel="stylesheet" href="http://stash.compjour.org/assets/css/foundation.css">
   
    <h1>Providence Health & Services </h1>
    <p>Family Medicine</p>
    <p>And here's our services:</p>
    <div class="bg">

      

    <form method="get" action="/providence-vid">
        <p>
        <input type="submit" value="Next Page"/>
        </p>
    </form>

    <ul>
    <li>
    <a href="/providence-vid">http://providence-vid.com</a>
    </li>
    </ul>
    
    </div>
       echo ("Rx Team");
        ?>
        
        <div>
                <iframe width="580" height="315" src="https://www.youtube.com/embed/6-pou5z5Q2w" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

                 

<blockquote>Nerds like us are allowed to be unironically enthusiastic about stuff. Nerds are allowed to love stuff - like, jump-up-and-down-in-your-chair-can't-control-yourself love it. When people call other people nerds, mostly what they're saying is "You like stuff", which is not a good insult at all. Like, "You are too enthusiastic about the miracle of human consciousness".</blockquote>
<div class="cite">John Green</div>

blockquote {
  background-color: white;
  color: yellow;
  padding: 10px;
}

.cite {
  text-align: right;
  font-weight: bold;
  font-size: x-large;
}


function partypartyparty() {
    var quotes = document.getElementsByClassName('fancyquote');
    for(var i=0; i<quotes.length; i++) {
        var r = Math.floor(Math.random()*255);
        var g = Math.floor(Math.random()*255);
        var b = Math.floor(Math.random()*255);
        var q = quotes[i];
        q.style.setProperty('color', 'rgb('+ r +','+ g +',' + b + ')');
    }
}

window.setInterval(partypartyparty, 500);


<h1>Hello stanford!</h1>

      <img src="https://www.providencecare.ca/wp-content/uploads/2018/04/PRO0055-Welcome-Sheet-EN-WEB.pdf">
  
      <img src="https://maps.googleapis.com/maps/api/streetview?size=700x300&location=stanford" alt="street view of stanford">
      </div>
    </body>
</html>
"""

@app.route("/providence-vid")
def vid():
    return """
 return render_template('header.html')

@app.route('/videos/<vid>')
def videos(vid):
vidtemplate = Template
      
      <h1>Video Patient Education!</h1>

    <iframe width="560" height="315" src="https://www.youtube.com/embed/SBJj5RSBKHA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


    def is_url_ok(url):
    return 200 == requests.head(url).status_code

<!DOCTYPE html>
<head>
   <title>My Video App</title>
   <style>
      body{
          text-align: center;
          background-color: #FFAAAA;
      }

      iframe{
          width: 80%;
          height: 600px;
          -webkit-animation: fun-function 2.5s linear infinite;
          -webkit-animation-direction: alternate;
          -moz-animation: fun-function 2.5s linear infinite;
          -moz-animation-direction: alternate;
      }

      @-webkit-keyframes fun-function{
        from{
          -webkit-transform: rotate(0deg) skew(-30deg);
        }
        to{
          -webkit-transform: rotate(360deg) skew(30deg);
        }
      }

      @-moz-keyframes fun-function{
        from{
          -moz-transform: rotate(0deg) skew(-30deg);
        }
        to{
          -moz-transform: rotate(360deg) skew(30deg);
        }
      }
   </style>
</head>
<body>
    <h2>${headline}</h2>
    <iframe src=<iframe width="560" height="315" src="https://www.youtube.com/embed/CDpKEtdQy5U" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</body>


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

  

    """
 
@app.route("/members")
def members():
    return "Members"
 
@app.route("/members/<string:name>/")
def getMember(name):
    return name
 
if __name__ == "__main__":
    app.run()









    
