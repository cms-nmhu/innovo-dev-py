var width = 800,
    height = 600;

var svg = d3.select(".content").append("svg")
    .attr("width", width)
    .attr("height", height)
    .attr("stroke", "steelblue");

var force = d3.layout.force()
    .gravity(0.05)
    .distance(200)
    .charge(-100)
    .size([width, height]);

d3.json(graph_data, function(error, json) {
    if (error) throw error;

    force
        .nodes(json.nodes)
        .links(json.links)
        .start();

    var link = svg.selectAll(".link")
        .data(json.links)
        .enter().append("line")
        .attr("class", "link")
        .attr("stroke-width", function(d) { return d.mag })

    var node = svg.selectAll(".node")
        .data(json.nodes)
        .enter().append("g")
        .attr("class", "node")
        .attr("width", 200)
        .attr("height", 300)
        .call(force.drag);

    // node.append("circle")
    //     .attr("r", function(d) { return d.mag });

    node.append("foreignObject")
        .attr("x", -12)
        .attr("y", -20)
        .attr("width",  100)
        .attr("height", 100)
        .html(function(d) {
            return "<i class='fa fa-2x fa-"+d.type+"'></i> " + d.name
        });

    force.on("tick", function() {
        link.attr("x1", function(d) { return d.source.x; })
          .attr("y1", function(d) { return d.source.y; })
          .attr("x2", function(d) { return d.target.x; })
          .attr("y2", function(d) { return d.target.y; });

        node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
    });
});