// Desc:
// Author:
// Dates:

var $ = function (id) {
  return document.getElementById(id);
};

// Define format options for printing.
const cur2Format = new Intl.NumberFormat("en-CA", {
  style: "currency",
  currency: "CAD",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const per2Format = new Intl.NumberFormat("en-CA", {
  style: "percent",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const com2Format = new Intl.NumberFormat("en-CA", {
  style: "decimal",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

// Start function definitions here.

// Function to create a progress bar for how far scrolled on page
window.addEventListener("scroll", function () {
  const progressBar = document.getElementById("progressBar");
  const scrollTop = window.scrollY;
  const docHeight =
    document.documentElement.scrollHeight -
    document.documentElement.clientHeight;
  const scrollPercentage = (scrollTop / docHeight) * 100;
  progressBar.style.width = scrollPercentage + "%";
});

//Function that creates an audio player for the page

// Identify audio player, collects tracks and sets up for listening.
document.addEventListener("DOMContentLoaded", function () {
  const audioPlayer = document.getElementById("audioPlayer");
  const playlist = document.getElementById("playlist");
  const tracks = playlist.getElementsByTagName("li");

  let currentTrackIndex = 0;

  // Load the first track
  audioPlayer.src = tracks[currentTrackIndex]?.getAttribute("data-src") || "";

  // Play the selected track when clicked
  for (let i = 0; i < tracks.length; i++) {
    tracks[i].addEventListener("click", function () {
      currentTrackIndex = i;
      audioPlayer.src = this.getAttribute("data-src");
      audioPlayer.play();
      document.getElementById(
        "nowPlaying"
      ).textContent = `Now Playing: ${this.textContent}`;
    });
  }
});
