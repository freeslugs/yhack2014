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
			if(obj[word]) {
				data[i] = {
					"x": i * 0.05,
					"y": obj[word]
				};
			}
		}
		var series = {
			"name": word,
			"data": data 
		}
	}

	rawData1.sort(sortByX);
	rawData2.sort(sortByX);

	$('#container').highcharts({
		chart: {
			type: 'line'
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
				text: 'Fruit eaten'
			}
		},
		series: [{
			name: 'Man',
			data: rawData1
		}, {
			name: 'Pineapple',
			data: rawData2
		}]
	});
});