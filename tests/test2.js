// Circle project
// Source: https://www.dashingd3js.com/creating-svg-elements-based-on-data
// Rudy Gamberini 2014
var circleRadii = [40, 20, 10], size = 150;
var color = d3.scale.linear()
 .domain([circleRadii[2], circleRadii[0]]) // input DOMAIN
 .range([0, 360]); // output RANGE
d3.select("body")
 .append("svg")
 .attr("width", size)
 .attr("height", size)
 .selectAll("circle")
 .data(circleRadii)
 .enter()
 .append("circle")
 .attr("cx", size / 2)
 .attr("cy", size / 2)
 .attr("r", function (d) { return d; })
 .style("fill", function(d) { return d3.hsl(d, 1, .5); });
