;Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon
;SoftDev pd0
;K27 -- Basic functions in JavaScript
;2023-04-03t

;Scheme Antecedents for JS work

;factorial:
;<your team's fact(n) implementation>
(define fact (lambda (n))
(if( < n 2) 
    1
    (* n (fact(- n 1)))))


(fact 1)

;fact(1) ;"...should be  1"
;fact(2) ;"...should be  2"
;fact(3) ;"...should be  6"
;fact(4) ;"...should be  24"
;fact(5) ;"...should be  120"


;fib:
;<your team's fib(n) implementation>
(define fib(lambda (n)
(if( = n 0)
    0
(if( <= n 2)
    1
    (+ (fib(- n 2)) (fib(- n 1)))))))

(fib 0)


;fib(0) ;"...should be  0"
;fib(1) ;"...should be  1"
;fib(2) ;"...should be  1"
;fib(3) ;"...should be  2"
;fib(4) ;"...should be  3"
=================================================================
