
function getCandidates() {
  $('.row-candidates').empty();
  $('.row-president').empty();
  req = $.ajax({
        url: '/candidates',
        type: 'POST',
    });

    req.done(function(data) {
        console.log(data)
        $.each(data.candidates_data, function(index, element) {
            if (element[0] == "date") {
            }

            else if (element[1] == "Trump") {
            $('.row-president').append(
                '<div class="col-xs-12 col-sm-12 col-md-12 col-lg-12 text-center">' +
                '<p class="candidates">' + element[2] + '$</p>' +
                '<div class="row plain-element">' +
                '<img src="https://flask-static-files.s3-eu-west-1.amazonaws.com/candidates/' + element[3]   + '"class="img-candidate responsive" alt="candidate"></div>' +
                '<p>' + element[0] + '</br>' + element[1] + '</p>' + '</div>'
            )
            }
            else {
            $('.row-candidates').append(
                '<div class="col-xs-3 col-sm-1 col-md-1 col-lg-1 plain-element">' +
                '<p class="candidates">' + element[2] + '$</p>' +
                '<div class="row plain-element">' +
                '<img src="https://flask-static-files.s3-eu-west-1.amazonaws.com/candidates/' + element[3]   + '"class="img-candidate responsive" alt="candidate"></div>' +
                '<p>' + element[0] + '</br>' + element[1] + '</p>' + '</div>'
            )

            }

        });




        var dataCandidates = data.candidates_data;
        var maxPrize = data.max_prize

//      CHART

        dataLabels = dataCandidates.map(function(x) {
            return x[0] + ' ' + x[1];
        });
        dataValues = dataCandidates.map(function(x) {
            return x[2];
        });

        var pcx = document.getElementById('candidatesChart').getContext('2d');
        var candidatesChart = new Chart(pcx, {
            type: 'bar',
            data: {
                labels: dataLabels.slice(2, 14),
                datasets: [{

                    label: 'Cash Prize',
                    data: dataValues.slice(2, 14),
                    backgroundColor: [
                    '#156c36',
                    '#23753f',
                    '#308047',
                    '#3b8b4d',
                    '#469651',
                    '#56a154',
                    '#6dab56',
                    '#85b457',
                    '#91bb67',
                    '#91bb67',
                    '#9dc378',
                    '#9dc378',
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
                labels: ['Donald Trump',],
                datasets: [{

                    label: 'Cash Prize',
                    data: [200,maxPrize],
                    backgroundColor: [
                    '#2c6554',
                ],
                }]
            },

            // Configuration options go here
            options: {
                 tooltips: {
                  enabled: false
                },
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

function uploadData() {

  req = $.ajax({
        url: '/upload_data',
        type: 'POST',
    });

    req.done(function(data) {
        console.log(data)
        });
}

$(document).ready(function() {
    getCandidates();
    uploadData()
});


window.setInterval(function(){
    console.log('upload');
    uploadData()
}, 100000);

