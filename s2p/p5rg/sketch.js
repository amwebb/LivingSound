let mic; // audio input
let recorder; // sound recorder
let soundFile; // recorded sound file
let isRecording = false; // whether the program is currently recording
let isPlaying = false; // whether the program is currently playing back recorded sound
let captureButton, stopButton, playbackButton, toggle3D; // buttons to start, stop, and playback recording
let displayShape = false;
let exportButton;
let video; // webcam video

function setup() {
   createCanvas(windowWidth, windowHeight); // create canvas
  // video = createCapture(VIDEO); // create video object for webcam capture
  // //video.size(400, 400); // set video size
  // video.hide(); // hide video element
  imageMode(CENTER);
  mic = new p5.AudioIn(); // create audio input object
  mic.start(); // start audio input
  recorder = new p5.SoundRecorder(); // create sound recorder object
  recorder.setInput(mic); // set input for recorder object to audio input
  soundFile = new p5.SoundFile(); // create sound file object
  captureButton = createButton('Capture'); // create capture button
  captureButton.mousePressed(startRecording); // call startRecording() function when capture button is pressed
  stopButton = createButton('Stop'); // create stop button
  stopButton.mousePressed(stopRecording); // call stopRecording() function when stop button is pressed
  playbackButton = createButton('Playback'); // create playback button
  playbackButton.mousePressed(playbackRecording); // call playbackRecording() function when playback button is pressed
  exportButton = createButton('Export Radial Graph');
  exportButton.mouseClicked(exportImage);


  const constraints = {
    video: {
      facingMode: "environment", 
      deviceId: 1
    },
    audio: false
  };
  
  video = createCapture(constraints); // remove this line
  video.size((height * 16) / 9, height);
  video.hide();
}

function draw() {
image(video, width/2, height/2);  // set text alignment
  textSize(20); // set text size
  fill(0); // set fill color
  if (!isRecording && !isPlaying) {
  } else if (isRecording) {
  } else if (isPlaying) {
    displayRadialGraph(soundFile); // display radial graph of sound file
  }

  if (displayShape && isPlaying) {
    displayRadialGraph(soundFile); // display the 3D shape if displayShape is true and sound is playing
  }
}




function startRecording() {
  if (!isRecording) { // if program is not currently recording
    recorder.record(soundFile); // start recording into sound file object
    isRecording = true; // set recording flag to true
  }
}

function stopRecording() {
  if (isRecording) { // if program is currently recording
    recorder.stop(); // stop recording
    isRecording = false; // set recording flag to false
    soundFile.playMode('sustain'); // set play mode for sound file to sustain
  }
}

function playbackRecording() {
  if (!isRecording && !isPlaying && soundFile.duration() > 0) { // if program is not currently recording or playing back and sound file has recorded audio
    soundFile.play(); // play back sound file
    isPlaying = true; // set playing flag to true
    //soundFile.onended(stopPlayback); // call stopPlayback() function when playback is complete
  }
}

function stopPlayback() {
  isPlaying = true; // set playing flag to false
}

function displayRadialGraph(sound) {
  let waveform = sound.getPeaks(width/2); // get waveform of sound file
  stroke(255,0,0, 90); // set stroke color
  strokeWeight(10);
  noFill(); // remove fill color
  beginShape(); // start shape
  
  for (let i = 0; i < waveform.length; i++) { // loop through waveform
    let angle = map(i, 0, waveform.length, 0, TWO_PI); // map index to angle
    let radius = map(waveform[i], -1, 1, 0, height/2); // map value to radius
    let x = width/2 + (radius) * cos(angle); // calculate x-coordinate based on angle and radius
    let y = height/2 + (radius) * sin(angle); // calculate y-coordinate based on angle and radius
    vertex(x, y); // add vertex to shape
  }
 // noLoop();
  endShape(CLOSE); // end shape and connect last vertex to first vertex
  
  //   push();
  //   beginShape(); // start shape
  //   strokeWeight(3);
  //   noFill();
  // for (let i = 0; i < waveform.length; i++) { // loop through waveform
  //   let angle = map(i, 0, waveform.length, 0, TWO_PI); // map index to angle
  //   let radius = map(waveform[i], -1, 1, 0, height/2.5); // map value to radius
  //   let x = width/2 + radius * cos(angle); // calculate x-coordinate based on angle and radius
  //   let y = height/2 + radius * sin(angle); // calculate y-coordinate based on angle and radius
  //   vertex(x, y); // add vertex to shape
  // }
  // noLoop();
  // endShape(CLOSE);
  // pop();
}



// // function displayRadialGraph(sound) {
// //   let waveform = sound.getPeaks(width); // get waveform of sound file
// //   push();
// //   stroke(0); // set stroke color
// //   noFill(); // remove fill color
// //   beginShape(); // start shape
// //   for (let i = 0; i < waveform.length; i++) { // loop through waveform
// //     let angle = map(i, 0, waveform.length, 0, TWO_PI); // map index to angle
// //     let radius = map(waveform[i], -1, 1, 0, height/2); // map value to radius
// //     let x = width/2 + radius * cos(angle); // calculate x-coordinate based on angle and radius
// //     let y = height/2 + radius * sin(angle); // calculate y-coordinate based on angle and radius
// //     vertex(x, y); // add vertex to shape
// //   }
// //   endShape(CLOSE); // end shape and connect last vertex to first vertex
// //   pop()
// // }




function display3DRadialGraph(sound) {
  let waveform = sound.getPeaks(width); // get waveform of sound file
  let numCylinders = waveform.length;
  let angleStep = TWO_PI / numCylinders;
  orbitControl();

  // Loop through waveform and create cylinders
  for (let i = 0; i < numCylinders; i++) {
    let angle = i * angleStep;
    let radius = map(waveform[i], -1, 1, 50, height / 2);
    let x = width / 2 + radius * cos(angle);
    let y = height / 2 + radius * sin(angle);

    // Set cylinder properties
    let cylHeight = map(waveform[i], -1, 1, 10, 100);
    let cylDiameter = 5;

    // Draw the cylinder
    push();
    translate(x-200, y-200);
    rotateX(HALF_PI);
    fill(0, 100, 255);
    noStroke();
    cylinder(cylDiameter, cylHeight);
    pop();
  }

  // Restore original settings
  //pop();
}

function exportImage() {
  // Get the canvas element
  let canvas = document.getElementById('defaultCanvas0');

  // Convert the canvas to a data URL
  let dataURL = canvas.toDataURL('image/png');

  // Create an image element and set its source to the data URL
  let img = new Image();
  img.src = dataURL;

  // Create a link element and set its href to the data URL
  let link = document.createElement('a');
  link.href = dataURL;

  // Set the download attribute of the link to the desired file name
  link.download = 'graph.png';

  // Append the link element to the document body and click it to initiate the download
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}
