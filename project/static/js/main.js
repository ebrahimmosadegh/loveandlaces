// navbar status scroll
const navbar = document.querySelector('.mynavBar');
if(navbar){
  window.onscroll = () => {
    if (window.scrollY > 200) {
        navbar.classList.add('nav-active');
        navbar.classList.add('sticky-top');
        navbar.classList.remove('position-absolute');

    } else {
        navbar.classList.remove('nav-active');
        navbar.classList.remove('sticky-top');
        navbar.classList.add('position-absolute');

    }
};
}
// Declare a variable to store the video source
let videoSrc;
// Add click event listener to all elements with class "play-video"
document.querySelectorAll('.play-video').forEach(button => {
  button.addEventListener('click', () => {
    // Get the video source from the data-src attribute
    videoSrc = button.dataset.src;
  });
});
// Add event listener for when the modal is opened
let playModal = document.getElementById('playModal')
if (playModal){
playModal.addEventListener('shown.bs.modal', () => {
  // Update the video source with autoplay and other options
  document.getElementById('video').src = videoSrc + "?autoplay=1&amp;modestbranding=1&amp;showinfo=0";
});
// Add event listener for when the modal is closed
playModal.addEventListener('hide.bs.modal', () => {
  // Stop the video by resetting the source
  document.getElementById('video').src = "";
});
}

  // DATA BACKGROUND IMAGE
  var sliderBgDiv = document.querySelectorAll('.bg-image');
  for(let i=0;i<sliderBgDiv.length;i++){
   let sliderBgImage = sliderBgDiv[i].getAttribute('data-background')
   sliderBgDiv[i].style.backgroundImage = "url('" + sliderBgImage + "')"
  }

  

  