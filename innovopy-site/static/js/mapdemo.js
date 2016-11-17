var width = 960,
    height = 960,
    scale0 = (width - 1) / 2 / Math.PI;
var projection = d3.geo.mercator();
var zoom = d3.behavior.zoom()
    .translate([width / 2, height / 2])
    .scale(scale0)
    .scaleExtent([scale0, 8 * scale0])
    .on("zoom", zoomed);
var path = d3.geo.path()
    .projection(projection);
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
d3.json(worldmap_data, function(error, world) {
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
function zoomed() {
  projection
      .translate(zoom.translate())
      .scale(zoom.scale());
  g.selectAll("path")
      .attr("d", path);
}
d3.select(self.frameElement).style("height", height + "px");

		