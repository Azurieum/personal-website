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



