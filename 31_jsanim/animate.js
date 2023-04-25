var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillStyle = "lightblue";

var requestID;

var clear = (e) => {
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

var stopIt = () => {
    console.log("stopIt invoked...");
    console.log(requestID);
    requestID = window.cancelAnimationFrame(requestID);
};

dotButton.addEventListener("click", () => {
    window.cancelAnimationFrame(requestID);
    drawDot();
    requestID = window.requestAnimationFrame(growDot);
});

stopButton.addEventListener("click", stopIt);