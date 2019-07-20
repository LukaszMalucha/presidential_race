
$('.dropdown-trigger').dropdown();


$(".alert-user").delay(3000).fadeOut(200, function() {
    $(this).alert('close');
});
var nyTime = new Date().toLocaleString("en-US", {timeZone: "America/New_York"});
var today = new Date(nyTime);
var localeSpecificTime = today.toLocaleTimeString();
var localeSpecificTime = localeSpecificTime.replace(/:\d+ /, ' ');


$(document).ready(function() {

    $('.clock').text(localeSpecificTime)

    $('select').formSelect();

    $('.sidenav').sidenav();

    $('.modal').modal();

    $('.fixed-action-btn').floatingActionButton();



});


