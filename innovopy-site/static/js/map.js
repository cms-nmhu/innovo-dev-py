var width = 960,
    height = 960,
    scale0 = (width - 1) / 2 / Math.PI;

var projection = d3.geo.mercator();

var path = d3.geo.path()
	.projection(projection)
	

var zoom = d3.behavior.zoom()
    .translate([width / 2, height / 2])
    .scale(scale0)
    .scaleExtent([scale0, 8 * scale0])
    .on("zoom", zoomed);

var svg = d3.select("#map").append("svg")
    .attr("width", width)
    .attr("height", height)
  	.append("g");

var g = svg.append("g");

svg.append("rect")
    .attr("class", "overlay")
    .attr("width", width)
    .attr("height", height);
svg
    .call(zoom)
    .call(zoom.event);

d3.json("/static/data/world-110m.json", function(error, world) {
	if (error) throw error;
	g.append("path")
	  .datum({type: "Sphere"})
	  .attr("class", "sphere")
	  .attr("d", path);

	g.append("path")
	  .datum(topojson.merge(world, world.objects.countries.geometries))
	  .attr("class", "land")
	  .attr("d", path);
	
	g.append("path")
	  .datum(topojson.mesh(world, world.objects.countries, function(a, b) { return a !== b; }))
	  .attr("class", "boundary")
	  .attr("d", path);
});


d3.json("/static/data/graph.json", function(error, data) { 
	if (error) throw error;
	var node = g.selectAll(".node")
        .data(data.nodes)
        .enter()
        .append("g")
        .attr("class", "node")
        .attr("width", 200)
        .attr("height", 300)
		.attr("cx", function(d) { return projection([d.lon, d.lat])[0] })
		.attr("cy", function(d) { return projection([d.lon, d.lat])[1] })

        .attr("x", -12)
        .attr("y", -20)
        .attr("width",  100)
        .attr("height", 100)
        .attr("cx", function(d) { return projection([d.lon, d.lat])[0] })
        .attr("cy", function(d) { return projection([d.lon, d.lat])[1] })
        .html(function(d) {
            return "<i class='fa fa-2x fa-"+d.type+"'></i> " + d.name
        });

        // .call(force.drag);
	// .nodes(data.nodes)

	// g.selectAll("circle")
	// 	.data(data.nodes)
	// 	.enter()
	// 		.append("circle")
	// 		.attr("cx", function(d) { console.log(projection([d.lon, d.lat])); return projection([d.lon, d.lat])[0] })
	// 		.attr("cy", function(d) { return projection([d.lon, d.lat])[1] })
 //       		.attr("r", 5)
 //       		.style("fill", "red");
});

 

        

    // node.append("circle")
    //     .attr("r", function(d) { return d.mag });

    // node.append("foreignObject")
    //     .attr("x", -12)
    //     .attr("y", -20)
    //     .attr("width",  100)
    //     .attr("height", 100)
    //     .attr("cx", function(d) { return projection([d.lon, d.lat])[0] })
    //     .attr("cy", function(d) { return projection([d.lon, d.lat])[1] })
    //     .html(function(d) {
    //         return "<i class='fa fa-2x fa-"+d.type+"'></i> " + d.name
    //     });
function zoomed() {
	projection
	  .translate(zoom.translate())
	  .scale(zoom.scale());
	
	g.selectAll("path")
	  .attr("d", path);
	g.selectAll("circle")
	  .attr("d", path);
}
d3.select(self.frameElement).style("height", height + "px");



