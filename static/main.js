$(function() {

	$("#app").hide()
	
	$("#party-button").click(function () {
		$("#landing-page").hide()
		$("#app").show()
	})


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

	function getAllWords(arr) {
		result = []
		for (frame in arr) {
			for (word in arr[frame]) {
				if (_.indexOf(result, word) < 0) {
					result.push(word);
				}
			}
		}
		return result;
	}



	function makeSeries(arr, word) {
		var data = [];
		for (frame = 0; frame < arr.length; frame++) {
			obj = arr[frame];
			if(word in obj) {
				data.push({
					"x": frame / 6,
					"y": obj[word]
				});
			}
		}
		var series = {
			"name": word,
			"data": data 
		}
		return series;
	}

	$.get("/api/movie-list", function(data) {
		for (each in data) {
			$("#movie-list").append("<li role=\"presentation\"><a role=\"menuitem\" class=\"movie-option\" tabindex=\"-1\">"+data[each]+"</a></li>")	
		}
	});

	$("#movie-list").on("click", "a", function(){
		var text = $(this).text();
		$.get("/api/get-movie?name=" + text, function(data) {
			$("#chart-title").text(text);
			var allWords = getAllWords(data);
			seriesArray = [];
			for(word in allWords){
				series = makeSeries(data, allWords[word]);
				seriesArray.push(series);
			}
			$('#chart').empty();
			$('#chart').highcharts({
				chart: {
					zoomType: 'xy',
					type: 'spline',
					backgroundColor: '#ecf0f1'
				},
				title: {
					text: text
				},
				xAxis: {
					title: {
						text: 'Minute'
					}
				},
				yAxis: {
					title: {
						text: 'Probability'
					},
					min: 0
				},
				series: seriesArray,
				legend: {
					align: "right",
					layout: "vertical",
					verticalAlign: "top"
				},
				tooltip: {
					valueDecimals: 4
				},
				plotOptions: {
					series: {
						events: {
							legendItemClick: function(event) {
								if (!this.visible)
									return false;
	
								var seriesIndex = this.index;
								var series = this.chart.series;
	
								for (var i = 0; i < series.length; i++)
								{
									if (series[i].index != seriesIndex)
									{
										series[i].visible ?
										series[i].hide() :
										series[i].show();
									} 
								}
								return false;
							}
						}
					}
				}
			});
		});
	});
});