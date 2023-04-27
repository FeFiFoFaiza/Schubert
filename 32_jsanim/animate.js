

var c = document.getElementById("playground");
var dotButton = document.getElementById("circle");
var stopButton = document.getElementById("stop");
var dvdButton = document.getElementById("dvd");

var ctx = c.getContext("2d");

ctx.fillStyle = "lightblue";

var requestID;

var clear = (e) => {
    //e.preventDefault();
    ctx.clearRect(0, 0, c.width, c.height);
};

var radius = 0;
var growing = true;

var drawCircle = () => {
	ctx.beginPath();
	ctx.arc(250, 250, radius, 2 * Math.PI, false);
	ctx.fill();
	ctx.stroke();
};

var drawDot = () => {
    clear();
    drawCircle();

    if (growing) {
        radius++;
    } else {
        radius--;
    }

    if (radius <= 0){
        growing = true;
    } else if (radius >= 250) {
        growing = false;
    }

    requestID = window.requestAnimationFrame(drawDot);
};

var dvdLogoSetup = function() {
    window.cancelAnimationFrame( requestID);

    var rectWidth = 120;
    var rectHeight = 80;

    var rectX = 50 + Math.random()*300;
    var rectY = 80 + Math.random()*300;
    console.log(Math.random(300));
    var xVelocity = 1;
    var yVelocity = 1;

    var logo = new Image();
    logo.src = "logo_dvd.jpg";

    var dvdLogo = function () {
        ctx.clearRect(0, 0, c.width, c.height);
        ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);

        if (( rectX <= 0 ) || ( rectX + rectWidth >= 500)){
            xVelocity *= -1;
        }
        if (( rectY <= 0 ) || ( rectY + rectHeight >= 500)){
            yVelocity *= -1;
        }
        rectX+=xVelocity;
        rectY+=yVelocity;
        requestID = window.requestAnimationFrame(dvdLogo);
    };
    dvdLogo();
}

var stopIt = () => {
    console.log("stopIt invoked...");
    console.log(requestID);
    requestID = window.cancelAnimationFrame(requestID);
};

dotButton.addEventListener("click", () => {
    window.cancelAnimationFrame(requestID);
    drawDot();
});


stopButton.addEventListener("click", stopIt);

dvdButton.addEventListener("click", dvdLogoSetup);
