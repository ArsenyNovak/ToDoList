//time on page
var timeElement = document.getElementById('currentTime');
setInterval(function () {
    var currentTime = new Date();
    timeElement.textContent = currentTime.toLocaleString();
}, 1000);




