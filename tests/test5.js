var length = 10, width = 20, spacing = 1, size = 20, data = d3.range(width).map(function(v){ return d3.range(length)});
var svgContainer = d3.select("body").append("svg")
                    .attr("width", width * size)
                    .attr("height", length * size).append("g");
var things = d3.select("g").selectAll("g")
            .data(data)
            .enter()
            .append("g");
things.append("rect")
  .attr("x", function(data, i) {
    return i * (size + spacing);
  })
  .attr("y", 20)
  .attr("height", size)
  .attr("width", size)
  .attr("fill", "red")
  .attr("i", function(data, i) { return data; });
