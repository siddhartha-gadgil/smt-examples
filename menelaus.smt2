; generated by `menelaustheoremproof.py` due to Anand Tadipatri
;
; if we ask for a proof, then the result becomes "unknown" and we cannot get a proof
; (set-option :produce-proofs true)
(declare-fun y_a () Real)
(declare-fun t () Real)
(declare-fun x_a () Real)
(declare-fun s () Real)
(declare-fun r () Real)
(assert (let ((a!1 (- (+ 0.0 (* s 0.0)) (+ y_a (* r (- 0.0 y_a)))))
      (a!2 (- (+ 1.0 (* t (- x_a 1.0))) (+ x_a (* r (- 0.0 x_a)))))
      (a!3 (- (+ 0.0 (* t (- y_a 0.0))) (+ y_a (* r (- 0.0 y_a)))))
      (a!4 (- (+ 0.0 (* s 1.0)) (+ x_a (* r (- 0.0 x_a)))))
      (a!5 (- x_a (+ x_a (* r (- 0.0 x_a)))))
      (a!6 (- y_a (+ y_a (* r (- 0.0 y_a)))))
      (a!7 (^ (- 0.0 (+ 0.0 (* s 1.0))) 2.0))
      (a!8 (^ (- 0.0 (+ 0.0 (* s 0.0))) 2.0))
      (a!9 (- 1.0 (+ 1.0 (* t (- x_a 1.0)))))
      (a!10 (- 0.0 (+ 0.0 (* t (- y_a 0.0)))))
      (a!11 (- (+ x_a (* r (- 0.0 x_a))) 0.0))
      (a!12 (- (+ y_a (* r (- 0.0 y_a))) 0.0))
      (a!13 (^ (- (+ 0.0 (* s 1.0)) 1.0) 2.0))
      (a!14 (^ (- (+ 0.0 (* s 0.0)) 0.0) 2.0))
      (a!15 (- (+ 1.0 (* t (- x_a 1.0))) x_a))
      (a!16 (- (+ 0.0 (* t (- y_a 0.0))) y_a)))
(let ((a!17 (= (* (+ (^ a!5 2.0) (^ a!6 2.0))
                  (+ a!7 a!8)
                  (+ (^ a!9 2.0) (^ a!10 2.0)))
               (* (+ (^ a!11 2.0) (^ a!12 2.0))
                  (+ a!13 a!14)
                  (+ (^ a!15 2.0) (^ a!16 2.0))))))
(let ((a!18 (=> (and (> y_a 0.0) (= (* a!1 a!2) (* a!3 a!4))) a!17)))
  (not a!18)))))
(check-sat)
; (get-proof)