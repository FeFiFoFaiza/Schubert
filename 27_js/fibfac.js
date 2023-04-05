// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon 
// SoftDev pd0
// K27 -- Basic functions in JavaScript
// 2023-04-04t
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn


//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.
function fact(n){
    if(n < 2){
        return 1;
    }
    else{
        return n*fact(n-1);
    }
}

function fib(n){
    if(n == 0){
        return 0;
    }
    if(n <= 2){
        return 1;
    }
    return fib(n-2)+fib(n-1);
}

fact(1);
