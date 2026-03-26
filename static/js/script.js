navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    const video = document.createElement('video');
    video.autoplay = true;
    video.playsInline = true;
    video.srcObject = stream;
    document.body.appendChild(video);
  })
  .catch(err => alert("Camera error: " + err));