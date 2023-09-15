function w3_open() {
  s = document.querySelector("#mySidebar");
  s.classList.add("w3-animate-left");
  s.style.display = "block";
  document.getElementById("myOverlay").style.display = "block";
}

function w3_close() {
  document.getElementById("mySidebar").style.display = "none";
  document.getElementById("myOverlay").style.display = "none";
}
