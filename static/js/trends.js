
function getTrends() {
  $('#trends').empty();
  $('#mostTweets').empty();
  req = $.ajax({
        url: '/trends',
        type: 'POST',
    });

    req.done(function(data) {
        console.log(data.top_ten_trends);
        $.each(data.top_ten_trends, function(index, element) {
            if (element[1] == "10000") {
            $('#trends').append(
                '<div class="row row-trend">' +
                '<a  target="_blank" href="https://twitter.com/search?q=' + element[2] + '&src=typd"> #' + element[0] + '</a>' +
                '<p>Tweets: < ' + element[1] +  '</p>' + '</div>'
            )
            }
            else {
            $('#trends').append(
                '<div class="row row-trend">' +
                '<a  target="_blank" href="https://twitter.com/search?q=' + element[2] + '&src=typd"> #' + element[0] + '</a>' +
                '<p>Tweets: ' + element[1] +  '</p>' + '</div>'
            )

            }

        });

        var dataTopTrends = data.top_ten_trends;

//      CHART

        dataLabels = dataTopTrends.map(function(x) {
            return x[0];
        });
        dataValues = dataTopTrends.map(function(x) {
            return x[1];
        });

        var pcx = document.getElementById('trendChart').getContext('2d');
        var trendChart = new Chart(pcx, {
            type: 'bar',
            data: {
                labels: dataLabels,
                datasets: [{

                    label: 'Tweet Count',
                    data: dataValues,
                    backgroundColor: [
                    '#4ab3f4',
                    '#5cbaf5',
                    '#6ec2f6',
                    '#80c9f7',
                    '#92d1f8',
                    '#a4d9f9',
                    '#b6e0fa',
                    '#b6e0fa',
                    '#b6e0fa',
                    '#e5e5e5',
                ],
                }]
            },

            // Configuration options go here
            options: {
                responsive: true,
                maintainAspectRatio: false,
                legend: {
                    display: false },
                title: {
                fontSize: 10,
                fontColor: 'black',
                display: false,
                text: ''
                },
                scales: {

                xAxes: [{
                        gridLines: {
                            color: "rgba(0, 0, 0, 0)",
                            drawBorder: false,
                            display: false
                        },
                        ticks: {
                        fontColor: "white",
                        fontSize: 0,
                        suggestedMin: 0,
                        suggestedMax: 1,
                        beginAtZero: true
                        }
                    }],
                yAxes: [{
                    display: true,
                    gridLines: {
                            color: "rgba(0, 0, 0, 0)",
                            drawBorder: false,
                            display: false
                        },
                    ticks: {
                        fontSize: 0,
                        fontColor: "white",
                        suggestedMin: 0,
                        suggestedMax: 1,
                        beginAtZero: true
                    }
                }]
            }
            }
        });
        var pcx = document.getElementById('presidentChart').getContext('2d');
        var trendChart = new Chart(pcx, {
            type: 'bar',
            data: {
                labels: ['Red',],
                datasets: [{

                    label: 'Tweet Count',
                    data: [12,],
                    backgroundColor: [
                    '#1da1f2',
                ],
                }]
            },

            // Configuration options go here
            options: {
                responsive: true,
                maintainAspectRatio: false,
                legend: {
                    display: false },
                title: {
                fontSize: 10,
                fontColor: 'black',
                display: false,
                text: ''
                },
                scales: {

                xAxes: [{
                        gridLines: {
                            color: "rgba(0, 0, 0, 0)",
                            drawBorder: false,
                            display: false
                        },
                        ticks: {
                        fontColor: "white",
                        fontSize: 0,
                        suggestedMin: 0,
                        suggestedMax: 1,
                        beginAtZero: true
                        }
                    }],
                yAxes: [{
                    display: true,
                    gridLines: {
                            color: "rgba(0, 0, 0, 0)",
                            drawBorder: false,
                            display: false
                        },
                    ticks: {
                        fontSize: 0,
                        fontColor: "white",
                        suggestedMin: 0,
                        suggestedMax: 1,
                        beginAtZero: true
                    }
                }]
            }
            }
        });
    });
}


$(document).ready(function() {
    getTrends()
});


window.setInterval(function(){
    getTrends()
}, 55000);