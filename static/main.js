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
					"x": _.indexOf(arr, obj) * 0.05,
					"y": obj[word]
				});
			}
		}
		var series = {
			"name": word,
			"data": data 
		}
	}

	$.get("/api/get-tags", function(data) {
		var allWords = getAllWords(data);
		seriesArray = [];
		for(word in allWords){
			series = makeSeries(data, allWords[word]);
			seriesArray.push(series);
		}
		console.log(seriesArray);
		$('#chart').highcharts({
			chart: {
				type: 'spline'
			},
			title: {
				text: 'Terms in The Godfather'
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
			series: seriesArray
		});
	});
});