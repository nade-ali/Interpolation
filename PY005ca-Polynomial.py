import matplotlib
import matplotlib.pyplot as mplot
import Lagrange as LagrangeInterpolation
import CubicSpline as CubicSpline

figure, bpo = mplot.subplots()

#Main function with actual values
mplot.subplot(2, 2, 1)
mplot.plot(CubicSpline.xp, CubicSpline.yrealf, 'k-')
mplot.plot(LagrangeInterpolation.xinit, LagrangeInterpolation.yinit, 'ko')
mplot.title('Function (Dots are initial points)')

#Cubic Spline Graph
mplot.subplot(2, 2, 2)
mplot.plot(CubicSpline.xp, CubicSpline.yp, 'r-')
mplot.plot(CubicSpline.xp1, CubicSpline.yp1, 'b,')
mplot.plot(CubicSpline.xp2, CubicSpline.yp2, 'g,')
mplot.title('Cubic Spline')

#Lagrange Graph
mplot.subplot(2, 2, 3)
mplot.plot(LagrangeInterpolation.xp, LagrangeInterpolation.yp, 'y-')
mplot.title('Lagrange Interpolation')

#All graphs combined
mplot.subplot(2, 2, 4)
mplot.plot(LagrangeInterpolation.xp, LagrangeInterpolation.yp, 'y-')
mplot.plot(CubicSpline.xp, CubicSpline.yp, 'r-')
mplot.plot(CubicSpline.xp, CubicSpline.yrealf, 'k-')
mplot.plot(LagrangeInterpolation.xinit, LagrangeInterpolation.yinit, 'ko')
mplot.title('Comparison')

#Display the graph 
mplot.tight_layout()
figure.savefig("picture.png", bbox_inches="tight", dpi=300)
mplot.show()

