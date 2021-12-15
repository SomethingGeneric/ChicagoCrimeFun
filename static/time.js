// This funciton is called every second to update the HTML of the requested tag to the 
// current time in HH:MM:SS given the user's locale setting. (Rough geographic location)
function time() {
    const clock = new Date();
    document.getElementById("datetime").innerHTML = clock.toLocaleTimeString();
}

// This function is called every second to update the HTML of the 'day' tag to the 
// ascii representation of what day it is. (See list below.)
function day() {
    const clock = new Date();
    weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    document.getElementById("day").innerHTML = weekday[clock.getDay()];
}

// These functions instruct the browser to register the repeated tasks as defined above
setInterval(time, 1000);
setInterval(day, 1000);