(set-logic ALL)
(declare-fun b_scale () Real)
(declare-fun k!1 () Int)
(declare-fun c_scale () Real)
(declare-fun ax () Real)
(declare-fun k!0 () Int)
(declare-fun ay () Real)
(declare-fun Bx () Real)
(declare-fun Cx () Real)
(declare-fun Px () Real)
(declare-fun Py () Real)
(declare-fun Qx () Real)
(declare-fun Qy () Real)
(declare-fun Rx () Real)
(declare-fun Ry () Real)
(assert (< (to_real k!1) b_scale))
(assert (< b_scale c_scale))
(assert (< (to_real k!0) ax))
(assert (< (to_real k!0) ay))
(assert (= (* (- (* ax c_scale) ax) (- (* ay b_scale) ay))
   (* (- (* ax b_scale) ax) (- (* ay c_scale) ay))))
(assert (= (* (- Cx (to_real k!1)) (to_real (- k!0 k!0)))
   (* (- Bx (to_real k!1)) (to_real (- k!0 k!0)))))
(assert (= (* (- Bx ax) (- Py ay)) (* (- Px ax) (- (to_real k!0) ay))))
(assert (= (* (- (* ax b_scale) (to_real k!1)) (- Py (to_real k!0)))
   (* (- Px (to_real k!1)) (- (* ay b_scale) (to_real k!0)))))
(assert (= (* (- Cx ax) (- Qy ay)) (* (- Qx ax) (- (to_real k!0) ay))))
(assert (= (* (- (* ax c_scale) (to_real k!1)) (- Qy (to_real k!0)))
   (* (- Qx (to_real k!1)) (- (* ay c_scale) (to_real k!0)))))
(assert (= (* (- Cx (* ax b_scale)) (- Ry (* ay b_scale)))
   (* (- Rx (* ax b_scale)) (- (to_real k!0) (* ay b_scale)))))
(assert (= (* (- (* ax c_scale) Bx) (- Ry (to_real k!0)))
   (* (- Rx Bx) (- (* ay c_scale) (to_real k!0)))))
(assert (not (= (* (- Rx Px) (- Qy Py)) (* (- Qx Px) (- Ry Py)))))
(check-sat)