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

window.addEventListener("scroll", function () {
  const progressBar = document.getElementById("progress-bar");
  const scrollTop = window.scrollY;
  const docHeight =
    document.documentElement.scrollHeight -
    document.documentElement.clientHeight;
  const scrollPercentage = (scrollTop / docHeight) * 100;
  progressBar.style.width = scrollPercentage + "%";
});

// Start function definitions here.

function ShowGreeting() {
  // Create the greeting based on the hour of the day.
  // Use the getHour() method on the current date - in 24 hour clock.

  let CurDate = new Date();
  let CurHour = CurDate.getHours(); // This returns a value from 0-24

  let Greeting = "";
  if (CurHour >= 6 && CurHour <= 12) {
    Greeting = "Good Morning";
  } else if (CurHour >= 12 && CurHour <= 18) {
    Greeting = "Good Afternoon";
  } else if (CurHour >= 18 && CurHour <= 24) {
    Greeting = "Good Evening";
  } else {
    Greeting = "Good Night";
  }

  Greeting += " - " + CurDate.toDateString();
  document.writeln(Greeting);
}
