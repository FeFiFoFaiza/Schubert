//retrieve node in DOM via ID
var c = document.getElementById("slate")//this is undeclared??
//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init global state var
var mode = "rect";

//var toggleMode = function(e) {
var toggleMode = (e) => {
	console.log("toggling...");
	if (mode === "rect") {
		mode = "circ";
	} else {
		mode = "rect";
	}
}

var drawRect = function(e) {
	var mouseX = e.offsetX; //ofset vs client X gives position relative to element. https://stackoverflow.com/questions/6645951/what-is-the-difference-between-offsetx-offsety-and-pagex-pagey
	var mouseY = e.offsetY;
	console.log("mouseclick registered at ", mouseX, mouseY);
	ctx.beginPath();
	ctx.rect(mouseX, mouseY, 200, 200);
	ctx.fillStyle = '#ff0000'; // color of fill
	ctx.fill(); // fill the shape
	ctx.stroke();
}

//var drawCircle = function(e) {
var drawCircle = (e) => {
	var mouseX = e.offsetX;
	var mouseY = e.offsetY;
	console.log("mouseclick registered at ", mouseX, mouseY);
	ctx.beginPath();
	ctx.arc(mouseX, mouseY, 50, 2 * Math.PI, false);
	ctx.fillStyle = '#00ff00';
	ctx.fill();
	ctx.stroke();
}

//var draw = function(e) {
var draw = (e) => {
	if (mode === "rect") {
		drawRect(e);
	} else {
		drawCircle(e);
	}
}

//var wipeCanvas = function() {
var wipeCanvas = () => {
	console.log("wiping canvas...");
	ctx.clearRect(0, 0, slate.width, slate.height); //relative to the canvas
}

c.addEventListener("click", draw);
var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode);//adds fxn on press
var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas); //adds fxn on press