var data = d3.range(0,10), radius = 20, diameter = radius*2, circles_per_line = 5, width = 10, height = 10;
var svgContainer = d3.select("body").append("svg")
                                   .attr("width", data.length * diameter)
                                   .attr("height", data.length * diameter);
var circles = [];
for (var i = 0; i < height; i++) {
  for (var j = 0; j < width; j++) {
    circles.push({cx: diameter * j + radius, cy: diameter * i + radius, i: i, j: j});
  }
}

var graph = svgContainer.selectAll("circle")
                        .data(circles)
                        .enter()
                        .append("circle")
                        .attr("r", radius)
                        .attr("cx", function(d) { return d.cx;})
                        .attr("cy", function(d) { return d.cy;})
