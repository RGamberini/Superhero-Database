// Line project
// Source: https://www.dashingd3js.com/svg-paths-and-d3js
// Rudy Gamberini
var line_function = d3.svg.line()
                     .x(function (d) { return d.x })
                     .y(function (d) { return d.y })
                     .interpolate("linear")

var line_data = [ { "x": 1,   "y": 5},  { "x": 20,  "y": 20},
                 { "x": 40,  "y": 10}, { "x": 60,  "y": 40},
                 { "x": 80,  "y": 5},  { "x": 100, "y": 60}];

var svgContainer = d3.select("body").append("svg")
                                   .attr("width", 200)
                                   .attr("height", 200);

var graph = svgContainer.append("path")
                        .attr("d", line_function(line_data))
                        .attr("stroke", "blue")
                        .attr("stroke-width", 2)
                        .attr("fill", "none")
