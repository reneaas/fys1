tid = []
posisjon = []


s = 0
t = 0
dt = 0.5
while t < 4:
    tid.append(t)
    posisjon.append(s)

    v = -(t**2) + 16
    s = s + v * dt

    t = t + dt


import plotmath

plotmath.plot(xdata=tid, ydata=posisjon, xlabel="$t$ / s", ylabel="$s$ / m")
plotmath.show()
