# Dev


:::{plot}
width: 60%
axis: equal
axis: off
let: s = 8
let: Ax = 0
let: Ay = 0
let: Bx = s
let: By = 0
let: Cx = s
let: Cy = s
let: Dx = 0
let: Dy = s
polygon: (Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy), blue, 0.1
let: x0 = -0.5 * s
let: y0 = s
let: dx = 0.2 * s
let: dy = 0.2 * s
vector: (x0, y0), dx, 0, black
vector: (x0, y0), 0, dy, black
text: x0 + dx, y0, "$x$", center-right
text: x0, y0 + dy, "$y$", top-center
let: Tx = s
let: Ty = 0.8 * s
let: T = 0.7 * s
point: (Tx, Ty)
vector: (Tx, Ty), T, 0, blue
text: Tx + T, Ty, "$100 \, \mathrm{N}$", center-right
let: Rx = 0.2 * s
let: Ry = 0
let: R = 0.4 * s
point: (Rx, Ry)
line-segment: (Rx, Ry), (Rx, Ry - 0.5), red, solid
vector: (Rx, Ry - 0.5), -R, 0, red
text: Rx - R, Ry - 0.5, "$40 \, \mathrm{N}$", center-left
:::



:::{plot}
width: 60%
axis: equal
axis: off
let: s = 8
let: Ax = 0
let: Ay = 0
let: Bx = s
let: By = 0
let: Cx = s
let: Cy = s
let: Dx = 0
let: Dy = s
polygon: (Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy), blue, 0.1
let: x0 = -0.5 * s
let: y0 = s
let: dx = 0.2 * s
let: dy = 0.2 * s
vector: (x0, y0), dx, 0, black
vector: (x0, y0), 0, dy, black
text: x0 + dx, y0, "$x$", center-right
text: x0, y0 + dy, "$y$", top-center
let: Tx = s
let: Ty = 0.8 * s
let: T = 0.35 * s
point: (Tx, Ty)
vector: (Tx, Ty), T, 0, blue
text: Tx + T, Ty, "$30 \, \mathrm{N}$", center-right
let: Rx = 0.2 * s
let: Ry = 0
let: R = 0.5 * s
point: (Rx, Ry)
line-segment: (Rx, Ry), (Rx, Ry - 0.5), red, solid
vector: (Rx, Ry - 0.5), -R, 0, red
text: Rx - R, Ry - 0.5, "$40 \, \mathrm{N}$", center-left
:::