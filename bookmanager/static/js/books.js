
//this conts selects all the images and adds an event listener to make them move
const sequence = document.querySelector(".sequence");
firstImg = sequence.querySelectorAll("img")[0];
arrowIcons = document.querySelectorAll(".wrapper i");

let isDragStarts = false, prevPageX, prevScrollLeft;


const showHideIcons = () => {
    // showing and hiding previous and next icons according to sequence scroll left value
    let scrollWidth = sequence.scrollWidth - sequence.clientWidth; //getting max scrollable width
    arrowIcons[0].style.display = sequence.scrollLeft == 0 ? "none" : "block";
    arrowIcons[1].style.display = sequence.scrollLeft == scrollWidth ? "none" : "block";
}

arrowIcons.forEach(icon => { 
    icon.addEventListener("click", () => {
        let firstImgWidth = firstImg.clientWidth + 14; // getting first img width and adding 14 margin value
        // if I click icon is left, reduce width value from the sequence scroll left else add to it
        sequence.scrollLeft += icon.id == "left" ? -firstImgWidth : firstImgWidth;
        setTimeout(() => showHideIcons(), 60); //calling hide icons after 60ms
    })
});

const dragStart = (e) => {
    // updating global variables value on mouse down event
    isDragStarts = true;
    prevPageX = e.pageX || e.touched[0].pageX;
    prevScrollLeft = sequence.scrollLeft;
}
const dragging = (e) => {
    // scrolling images/sequence to left according to mouse pointer
    if(!isDragStarts) return;
    e.preventDefault();
    sequence.classList.add("dragging");
    let positionDiff = ( e.pageX || e.touched[0] - pageX) - prevPageX;
    sequence.scrollLeft = prevScrollLeft -  positionDiff;
    showHideIcons();
    }

const dragStop = () => {
    isDragStarts = false;
    sequence.classList.remove("dragging");
}

sequence.addEventListener("mousedown", dragStart);
sequence.addEventListener("touchstart", dragStart);

sequence.addEventListener("mousemove", dragging);
sequence.addEventListener("touchmove", dragging);

sequence.addEventListener("mouseup", dragStop);
sequence.addEventListener("mouseleave", dragStop);
sequence.addEventListener("touchend", dragStop);