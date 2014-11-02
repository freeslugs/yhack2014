$(function() {
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
					"x": Math.floor(_.indexOf(arr, obj) * 3.3333333)/100,
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
		$.get("/api/get-movie", $(this).text(), function(data) {
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
					type: 'spline'
				},
				title: {
					text: ''
				},
				xAxis: {
					title: {
						text: 'Minute'
					}
				},
				yAxis: {
					title: {
						text: 'Probability'
					}
				},
				series: seriesArray,
				legend: {
					align: "right",
					layout: "vertical",
					verticalAlign: "top"
				},
				tooltip: {
					valueDecimals: 4
				}
			});
		});
	})

	function removeRareWords(data) {

	}

	$.get("/api/get-movie?name=500%20Days%20of%20Summer", function(data) {
		var allWords = getAllWords(data);
		seriesArray = [];
		for(word in allWords){
			series = makeSeries(data, allWords[word]);
			seriesArray.push(series);
		}
		console.log(seriesArray);
		$('#chart').highcharts({
			chart: {
				zoomType: 'xy',
				type: 'spline'
			},
			title: {
				text: ''
			},
			xAxis: {
				title: {
					text: 'Minute'
				}
			},
			yAxis: {
				title: {
					text: 'Probability'
				}
			},
			series: seriesArray,
			legend: {
				align: "right",
				layout: "vertical",
				verticalAlign: "top"
			},
			tooltip: {
				valueDecimals: 4
			}/*,
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
			}*/
		});
	});
});