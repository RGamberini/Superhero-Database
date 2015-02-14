var data = [1,2,3]
var p = d3.select("body") // We can chain these functions together because each returns a more specific "selection"
 .selectAll("p") // First the body and than all <p> elements in the body
 .data(data) // We than bind our data to any and all <p> elements, data returns three "virtual" selectors enter, update, and exit
 .enter() // Corresponding to the elements that need to be created (i.e. theres not enough elements currently for the data)
 // Another note about these virtual selections is that they can only be chained with .append, .insert, and .select
 .append("p") //
 .text(function (d) { return d + " word"})
