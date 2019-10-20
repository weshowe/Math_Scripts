# Math_Scripts
Some small programs designed to test mathematical concepts.

# areaCircle.py
Tests one of the methods for finding the area of a circle that was used by the Ancient Greeks. The method involves taking two of its arcs, building triangles inside them, and then calculating the area of the triangles. This process is repeated for smaller and smaller arcs until the area reasonably approximates the area of the circle.

This program operates upon a unit circle and runs for some epsilon until the area approximates pi, which is shown for reference.

# volumeSphere.py
Tests principles of integration learned in first year-calculus, to see if they can be applied to 3D shapes.

Finds the volume of a sphere by taking the equation for one of its semicircles, then making a mesh of cylinders using the height of the semicircle to define the radius. As mesh -> infinity, resultant -> volume.

This program is tested upon a unit sphere and its output is compared to the formula for its area.
