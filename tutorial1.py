from ggame import App

from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three primary colors with no transparency (alpha = 1.0)
blue = Color(808080, 1.0)
green = Color(53868, 1.0)


# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(4, blue)
# A graphics asset that represents a rectangle
ellipse = EllipseAsset(80, 40, thinline, green)

# Now display a rectangle
Sprite(ellipse)

myapp = App()
myapp.run()

