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





 
@app.route("/members")
def members():
    return "Members"
 
@app.route("/members/<string:name>/")
def getMember(name):
    return name
 
if __name__ == "__main__":
    app.run()









    
