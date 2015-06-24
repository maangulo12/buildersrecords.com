$(function() {
    $.getJSON(
        '/dashboard_ajax/',
        function(data) {
            var options = {
                responsive : true,
                labelFontSize : '18',
                tooltipTemplate : "<%if (label){%><%=label%>: <%}%>$<%= value.formatMoney(0, '.', ',') %>",
                legendTemplate : "<ul class=\"<%=name.toLowerCase()%>-legend\"><% for (var i=0; i<segments.length; i++){%><li><div class=\"comm-how\">$<%=segments[i].value.formatMoney(0, '.', ',')%></div><span style=\"background-color:<%=segments[i].fillColor%>\"></span><%if(segments[i].label){%><%=segments[i].label%><%}%></li><%}%></ul>"
            };
            var ctx = $('#modular-doughnut').get(0).getContext('2d');
            var chart = new Chart(ctx).Doughnut(data.data, options);
            var legend = document.createElement('div');
    		legend.innerHTML = chart.generateLegend();

            var helpers = Chart.helpers;
    		helpers.each(legend.firstChild.childNodes, function(legendNode, index) {
    			helpers.addEvent(legendNode, 'mouseover', function() {
    				var activeSegment = chart.segments[index];
    				activeSegment.save();
    				activeSegment.fillColor = activeSegment.highlightColor;
    				chart.showTooltip([activeSegment]);
    				activeSegment.restore();
    			});
    		});
    		helpers.addEvent(legend.firstChild, 'mouseout', function() {
    			chart.draw();
    		});
    		document.getElementById('legend-holder').appendChild(legend.firstChild);
        }
    );

    $('#logout_button').on('click', function() {
        window.location.href = '/logout/';
    });
});

Number.prototype.formatMoney = function(c, d, t){
var n = this,
    c = isNaN(c = Math.abs(c)) ? 2 : c,
    d = d == undefined ? "." : d,
    t = t == undefined ? "," : t,
    s = n < 0 ? "-" : "",
    i = parseInt(n = Math.abs(+n || 0).toFixed(c)) + "",
    j = (j = i.length) > 3 ? j % 3 : 0;
   return s + (j ? i.substr(0, j) + t : "") + i.substr(j).replace(/(\d{3})(?=\d)/g, "$1" + t) + (c ? d + Math.abs(n - i).toFixed(c).slice(2) : "");
 };
