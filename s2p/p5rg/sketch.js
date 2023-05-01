let mic; // audio input
let recorder; // sound recorder
let soundFile; // recorded sound file
let isRecording = false; // whether the program is currently recording
let isPlaying = false; // whether the program is currently playing back recorded sound
let captureButton, stopButton, playbackButton, uploadButton; // buttons to start, stop, and playback recording

let displayShape = false;
let exportButton;
let video; // webcam video
let thicknessSlider; // slider to control radial graph thickness
let thicknessLabel; // label for radial graph thickness slider

function setup() {
  imageMode(CENTER)
  createCanvas(windowWidth, windowHeight); // create canvas
  mic = new p5.AudioIn(); // create audio input object
  mic.start(); // start audio input
  recorder = new p5.SoundRecorder(); // create sound recorder object
  recorder.setInput(mic); // set input for recorder object to audio input
  soundFile = new p5.SoundFile(); // create sound file object
  
  
  const buttonContainer = createDiv();
  buttonContainer.addClass('button-container');

  // Create the capture button and append it to the container
  captureButton = createButton('Capture');
  captureButton.mousePressed(startRecording);
  captureButton.style('font-size', '24px');
  captureButton.style('width', '120px');
  captureButton.style('height', '60px');
  buttonContainer.child(captureButton);

  // Create the stop button and append it to the container
  stopButton = createButton('Stop');
  stopButton.mousePressed(stopRecording);
  stopButton.style('font-size', '24px');
  stopButton.style('width', '120px');
  stopButton.style('height', '60px');
  buttonContainer.child(stopButton);

  // Create the playback button and append it to the container
  playbackButton = createButton('Playback');
  playbackButton.mousePressed(playbackRecording);
  playbackButton.style('font-size', '24px');
  playbackButton.style('width', '120px');
  playbackButton.style('height', '60px');
  buttonContainer.child(playbackButton);

  // Create the export button and append it to the container
  exportButton = createButton('Export Graph');
  exportButton.mouseClicked(exportImage);
  exportButton.style('font-size', '24px');
  exportButton.style('width', '180px');
  exportButton.style('height', '60px');
  buttonContainer.child(exportButton);

  // Create the upload button and append it to the container
  uploadButton = createButton('Upload');
  uploadButton.mouseClicked(uploadFile);
  uploadButton.style('font-size', '24px');
  uploadButton.style('width', '120px');
  uploadButton.style('height', '60px');
  buttonContainer.child(uploadButton);

  // Append the button container to the body of the HTML document
  buttonContainer.parent(document.body);


  const constraints = {
    video: {
      facingMode: "environment", 
      deviceId: 1,
      width: 1920,
      height: 1080
    },
    audio: false
  };
  
  video = createCapture(constraints);
  //video.size(windowWidth, windowHeight); // modify size of video capture element
  video.hide();

  // Create slider and label for radial graph thickness
  thicknessSlider = createSlider(1, 50, 10);
  thicknessSlider.position(20, 50);
  thicknessLabel = createDiv('Radial Graph Thickness');
  thicknessLabel.position(20, 20);
}

function draw() {
  console.log("width:" + width + " height:" +height);
  push();
  translate(width/2, height/2);
  scale(1920/width);
  image(video, 0, 0); // display video
  pop();
  textSize(20); // set text size
  fill(0); // set fill color
  if (!isRecording && !isPlaying) {
  } else if (isRecording) {
  } else if (isPlaying) {
    push();

    displayRadialGraph(soundFile); // display radial graph of sound file
    pop();
  }

  if (displayShape && isPlaying) {
    displayRadialGraph(soundFile); // display the 3D shape if displayShape is true and sound is playing
  }
}




function startRecording() {
  if (!isRecording) { // if program is not currently recording
    userStartAudio();
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
strokeWeight(thicknessSlider.value());
  noFill(); // remove fill color
  beginShape(); // start shape
  
  for (let i = 0; i < waveform.length; i++) { // loop through waveform
    let angle = map(i, 0, waveform.length, 0, TWO_PI); // map index to angle
    let radius = map(waveform[i], -1, 1, 0, height/6); // map value to radius
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


function uploadFile() {
  let fileInput = createFileInput(handleFile);
  fileInput.elt.click(); // simulate a click event to open the file picker
}

function handleFile(file) {
  if (file.type === 'audio') {
    soundFile = loadSound(file.data, function() {
      console.log('Audio file loaded successfully');
    });
  } else {
    console.error('Invalid file type. Please select an audio file.');
  }
}