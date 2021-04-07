(declare-fun ay () Real)
(declare-fun cy () Real)
(declare-fun ax () Real)
(declare-fun bx () Real)
(declare-fun by () Real)
(declare-fun cx () Real)
(declare-fun Ay () Real)
(declare-fun Cy () Real)
(declare-fun Ax () Real)
(declare-fun Bx () Real)
(declare-fun By () Real)
(declare-fun Cx () Real)
(declare-fun Px () Real)
(declare-fun Py () Real)
(declare-fun Qx () Real)
(declare-fun Qy () Real)
(declare-fun Rx () Real)
(declare-fun Ry () Real)
(assert (= (* (- cx ax) (- by ay)) (* (- bx ax) (- cy ay))))
(assert (= (* (- Cx Ax) (- By Ay)) (* (- Bx Ax) (- Cy Ay))))
(assert (= (* (- Bx ax) (- Py ay)) (* (- Px ax) (- By ay))))
(assert (= (* (- bx Ax) (- Py Ay)) (* (- Px Ax) (- by Ay))))
(assert (= (* (- Cx ax) (- Qy ay)) (* (- Qx ax) (- Cy ay))))
(assert (= (* (- cx Ax) (- Qy Ay)) (* (- Qx Ax) (- cy Ay))))
(assert (= (* (- Cx bx) (- Ry by)) (* (- Rx bx) (- Cy by))))
(assert (= (* (- cx Bx) (- Ry By)) (* (- Rx Bx) (- cy By))))
(assert (not (= (* (- Rx Px) (- Qy Py)) (* (- Qx Px) (- Ry Py)))))
(assert (or (distinct ax bx) (distinct ay by)))
(assert (or (distinct ax cx) (distinct ay cy)))
(assert (or (distinct ax Ax) (distinct ay Ay)))
(assert (or (distinct ax Bx) (distinct ay By)))
(assert (or (distinct ax Cx) (distinct ay Cy)))
(assert (or (distinct bx ax) (distinct by ay)))
(assert (or (distinct bx cx) (distinct by cy)))
(assert (or (distinct bx Ax) (distinct by Ay)))
(assert (or (distinct bx Bx) (distinct by By)))
(assert (or (distinct bx Cx) (distinct by Cy)))
(assert (or (distinct cx ax) (distinct cy ay)))
(assert (or (distinct cx bx) (distinct cy by)))
(assert (or (distinct cx Ax) (distinct cy Ay)))
(assert (or (distinct cx Bx) (distinct cy By)))
(assert (or (distinct cx Cx) (distinct cy Cy)))
(assert (or (distinct Ax ax) (distinct Ay ay)))
(assert (or (distinct Ax bx) (distinct Ay by)))
(assert (or (distinct Ax cx) (distinct Ay cy)))
(assert (or (distinct Ax Bx) (distinct Ay By)))
(assert (or (distinct Ax Cx) (distinct Ay Cy)))
(assert (or (distinct Bx ax) (distinct By ay)))
(assert (or (distinct Bx bx) (distinct By by)))
(assert (or (distinct Bx cx) (distinct By cy)))
(assert (or (distinct Bx Ax) (distinct By Ay)))
(assert (or (distinct Bx Cx) (distinct By Cy)))
(assert (or (distinct Cx ax) (distinct Cy ay)))
(assert (or (distinct Cx bx) (distinct Cy by)))
(assert (or (distinct Cx cx) (distinct Cy cy)))
(assert (or (distinct Cx Ax) (distinct Cy Ay)))
(assert (or (distinct Cx Bx) (distinct Cy By)))
(check-sat)