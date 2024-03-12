// Everytime the page is scrolled the Y value is checked.
window.addEventListener("scroll", checkY)

// If the Y value is above 200 the scroll to top button will show. Else it would be hidden.
function checkY(){
    if (window.scrollY > 200) {
        document.querySelector(".topBTN").style.display = "flex"
    } else {
        document.querySelector(".topBTN").style.display = "none"
    }
}

// When the button is pressed it scrolls to the top of the page.
function topButtonPress() {
    window.scrollTo(0,0)
}

function getTimeRemaining() {
    // Target date: June 1, 2025, 00:00:00 in milliseconds
    const targetDate = new Date('2025-06-01T00:00:00').getTime();
    
    // Current date in milliseconds
    const currentDate = Date.now();

    // Calculate the time difference in milliseconds
    let timeDifference = targetDate - currentDate;

    /* add later
    if (timeDifference < 0) {
        
    } 
    */

    // Convert milliseconds to seconds
    timeDifference = Math.floor(timeDifference / 1000);

    // Calculate years, days, hours, minutes, and seconds
    const years = Math.floor(timeDifference / (365 * 24 * 60 * 60));
    timeDifference -= years * (365 * 24 * 60 * 60);

    const days = Math.floor(timeDifference / (24 * 60 * 60));
    timeDifference -= days * (24 * 60 * 60);

    const hours = Math.floor(timeDifference / (60 * 60));
    timeDifference -= hours * (60 * 60);

    const minutes = Math.floor(timeDifference / 60);
    timeDifference -= minutes * 60;

    const seconds = timeDifference;

    // Pad numbers with leading zeros if they are less than 10
    const paddedHours = hours < 10 ? `0${hours}` : hours;
    const paddedMinutes = minutes < 10 ? `0${minutes}` : minutes;
    const paddedSeconds = seconds < 10 ? `0${seconds}` : seconds;

    document.getElementById("timerTextYears").textContent = `${years} Years`;
    document.getElementById("timerTextDays").textContent = `${days} Days`;
    document.getElementById("timerTextHours").textContent = `${paddedHours} Hours`;
    document.getElementById("timerTextMinutes").textContent = `${paddedMinutes} Minutes`;
    document.getElementById("timerTextSeconds").textContent = `${paddedSeconds} Seconds`;

}


setInterval(getTimeRemaining, 1000);
