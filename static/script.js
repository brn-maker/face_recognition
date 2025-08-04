const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const result = document.getElementById('result');
const captureButton = document.getElementById('capture');

// Ask for camera access
navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    video.srcObject = stream;
  })
  .catch(err => {
    console.error("Camera access denied:", err);
  });

captureButton.addEventListener('click', async () => {
  const context = canvas.getContext('2d');
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  context.drawImage(video, 0, 0);

  // Get image as Base64
  const imageData = canvas.toDataURL('image/jpeg').split(',')[1];

  // Send to backend for verification
  const res = await fetch('/verify', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ image: imageData })
  });

  const data = await res.json();
  result.innerText = JSON.stringify(data);
});
