// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon 
// SoftDev pd0
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-05w
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };


var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};


var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

//insert your implementations here for...
// FIB
function fib(n){
    if(n == 0){
        return 0;
    }
    if(n <= 2){
        return 1;
    }
    return fib(n-2)+fib(n-1);
}

// FAC
function fact(n){
    if(n < 2){
        return 1;
    }
    else{
        return n*fact(n-1);
    }
}
// GCD
function gcd(a,b){
    if (b==0){
        return a;
    }
    return gcd(b,a%b);
}

// manually hardcoding the number of items bc too lazy to use js to do it
var olItems = 8;

// fib(n) where n is the number of items in the list
var fibbutton = document.getElementById("fib");

fibbutton.addEventListener('click', function(event) {
    olItems++;
    console.log("Trust- I'm a fibber " + fib(olItems));
    addItem(fib(olItems));
})

// fac(n) where n is the number of items in the list
var facbutton = document.getElementById("fact");

facbutton.addEventListener('click', function(event) {
    olItems++;
    console.log("Just facit! " + fact(olItems));
    addItem(fact(olItems));
})

// gcd(a,b) where a is the number of items in the list, b is the number 8
var gcdbutton = document.getElementById("gcd");

gcdbutton.addEventListener('click', function(event) {
    olItems++;
    console.log("God come dancing " + gcd(olItems, 5));
    addItem(gcd(olItems, 5));
    console.log(olItems);
})


// Dog what does this mean
// Can't find the live dom :)

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  // body
  return retVal;
};

