/* Axis Project
   Aim: To create a graph with two axes
      X-Axis: 0-360 color hue
      Y-Axis: 0-100 color saturation
    also to have circles on the graph showing */

var radius = 5, circles_per_line = 24, diameter = radius*2, height = 100, width = 360;

// var circles = d3.range(0,360).map(function (i) {
//   return {cx: diameter * (i % circles_per_line) + radius,
//     cy: radius + Math.floor(i / circles_per_line) * diameter,
//     _index: i};
//   });

var circles = []
for (var i = 0; i < height; i++) {
  for (var j = 0; j < width; j++) {
    circles.push({cx: diameter * j + radius, cy: diameter * i + radius, i: i, j: j});
  }
}

var svgContainer = d3.select("body").append("svg")
    .attr("width", diameter * width)
    .attr("height", diameter * height);
var circle = svgContainer.append("g");
circle.selectAll("circle")
  .data(circles)
  .enter()
  .append("circle")
  .attr("cx", function(d) { return d.cx;})
  .attr("cy", function(d) { return d.cy;})
  .attr("r", radius)
  .attr("fill", function(d) { return d3.hsl(d.i % 360, d.j / 100, d.j / 100);});
