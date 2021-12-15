function time() {
    const clock = new Date();
    document.getElementById("datetime").innerHTML = clock.toLocaleTimeString();
}

function day() {
    const clock = new Date();
    weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    document.getElementById("day").innerHTML = weekday[clock.getDay()];
}

setInterval(time, 1000);
setInterval(day, 1000);