// Set constraints for the video stream
var constraints = { video: { facingMode: "environment" }, audio: false };// Define constants
const cameraView = document.querySelector("#camera--view");
cameraView.controls = false;
function cameraStart() {
    navigator.mediaDevices
        .getUserMedia(constraints)
        .then(function(stream) {
        track = stream.getTracks()[0];
        cameraView.srcObject = stream;
    })
    .catch(function(error) {
        console.error("Oops. Something is broken.", error);
    });
}// Take a picture when cameraTrigger is tapped

window.addEventListener("load", cameraStart, false);