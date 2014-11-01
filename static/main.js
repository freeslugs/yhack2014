$(function() {
	var rawData1 = [];
	var rawData2 = [];

	for (var i = 0; i < 100; i++) {
		var x = Math.random() * 180;
		var y = Math.random();
		rawData1[i] = {
			"x": x,
			"y": y
		};
	}

	for (var i = 0; i < 100; i++) {
		var x = Math.random() * 180;
		var y = Math.random();
		rawData2[i] = {
			"x": x,
			"y": y
		};
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

	function getSeriesForTag(arr, word) {
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
	}

	$.get("/api/movie-list", function(data) {
		for (each in data) {
			$("#movie-list").append("<li role=\"presentation\"><a role=\"menuitem\" class=\"movie-option\" tabindex=\"-1\">"+data[each]+"</a></li>")	
		}
	});

	$("#movie-list").on("click", "a", function(){
		$.get("/api/tags", $(this).text(), function(data) {
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

	$.get("/api/tags", function(data) {
		var allWords = getAllWords(data);
		seriesArray = [];
		for(word in allWords){
			series = makeSeries(data, allWords[word]);
			seriesArray.push(series);
		}
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
});