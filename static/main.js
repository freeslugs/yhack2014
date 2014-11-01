// Generate random data
var rawData = [];

for (var i = 0; i < 100; i++) {
	var x = Math.floor(Math.random() * 10000);
	var y = Math.floor(Math.random() * 10000);
	rawData[i] = {
		"x": x,
		"y": y
	};
}


// Scale random data 
var xScale = d3.scale.linear()
					.domain([d3.min(rawData, function(d) { return d.x; }), d3.max(rawData, function(d) { return d.x; })])
					.range([0, 1000]);

var yScale = d3.scale.linear()
					.domain([d3.min(rawData, function(d) { return d.y; }), d3.max(rawData, function(d) { return d.y; })])
					.range([0, 500]);

var scaledData = [];

for (var i = 0; i < rawData.length; i++) {
	scaledData[i] = {"x": xScale(rawData[i].x), "y": yScale(rawData[i].y)};
}


// Sort scaled data
function sortByX(a, b) {
	if (a.x > b.x) {
		return 1;
	}
	if (a.x < b.x) {
		return -1;
	}
	return 0;
}

scaledData.sort(sortByX);


// Make line graph, add to DOM.
var lineFunction = d3.svg.line()
						 .x(function(d){ return d.x; })
						 .y(function(d){ return d.y; })
						 .interpolate("basis-open");

var svg_canvas = d3.select("body")
			.append("svg")
			.attr("height", "500")
			.attr("width", "1000");

var lineGraph = svg_canvas.append("path")
						  .attr("d", lineFunction(scaledData))
						  .attr("stroke", "blue")
						  .attr("stroke-width", 2)
						  .attr("fill", "none"); 