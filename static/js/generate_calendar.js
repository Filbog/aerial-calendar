const monthNames = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];

const year2025 = 2025;

function generateCalendar(year) {
  const yearGrid = [];

  for (let i = 0; i < 12; i++) {
    // by default 1 is Monday, 0 is Sunday
    const firstDayIndex = (new Date(year, i, 1).getDay() + 6) % 7;
    const daysInMonth = new Date(year, i + 1, 0).getDate();

    const weeks = [];
    let currentWeek = [];
    let dayCounter = 1;

    // Add empty cells for the days of the previous month
    for (let j = 0; j < firstDayIndex; j++) {
      currentWeek.push("");
    }

    while (dayCounter <= daysInMonth) {
      currentWeek.push(dayCounter);
      if (currentWeek.length === 7) {
        weeks.push(currentWeek);
        currentWeek = [];
      }
      dayCounter++;
    }

    // Add empty cells for the days of the next month
    while (currentWeek.length < 7 && currentWeek.length > 0) {
      currentWeek.push("");
    }
    weeks.push(currentWeek);

    yearGrid.push(weeks);
  }
  // console.log(yearGrid.length);
  // console.log(yearGrid[11]);
  return { year: year, grid: yearGrid };
}

function populateCalendar(yearData) {
  const calendarContainer = document.getElementById("calendar-container");
  // console.log(yearData);
  yearGrid = yearData.grid;
  year = yearData.year;
  // console.log("year grid: ", yearGrid);
  // console.log("year: ", year);

  // Loop through each month in yearGrid
  for (let monthIndex = 0; monthIndex < yearGrid.length; monthIndex++) {
    const monthData = yearGrid[monthIndex]; // Get the weeks for the current month

    const monthElement = document.createElement("div");
    monthElement.classList.add("month");
    monthElement.classList.add("calendar-grid");
    monthElement.id = `month-${monthIndex}`;
    const monthHeading = document.createElement("h1");
    monthHeading.textContent = monthNames[monthIndex];
    calendarContainer.appendChild(monthHeading);
    calendarContainer.appendChild(monthElement);

    // Add day names
    const dayNames = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
    dayNames.forEach((dayName) => {
      const dayElement = document.createElement("div");
      dayElement.classList.add("day-name");
      dayElement.textContent = dayName;
      monthElement.appendChild(dayElement);
    });

    // Add day cells for the current month
    monthData.forEach((week) => {
      week.forEach((day) => {
        const dayElement = document.createElement("div");
        dayElement.classList.add("day");
        if (day === "") {
          dayElement.classList.add("empty");
        } else {
          dayElement.innerHTML = `<p class='day-number'>${day}</p>`; // Display the day

          // Convert the day number to a date string in the format YYYY-MM-DD
          const dateString = `${year}-${String(monthIndex + 1).padStart(
            2,
            "0"
          )}-${String(day).padStart(2, "0")}`;
          // console.log(dateString);
          const eventsOnDay = eventsData.filter(
            (event) =>
              event.start_date <= dateString && event.end_date >= dateString
          );
          if (eventsOnDay.length > 0) {
            dayElement.classList.add("has-events");
            const eventList = document.createElement("ul");
            eventsOnDay.forEach((event) => {
              const eventItem = document.createElement("li");
              eventItem.classList.add("event-item");
              eventItem.textContent = event.name;
              eventList.appendChild(eventItem);
            });
            dayElement.appendChild(eventList);
          }
        }
        monthElement.appendChild(dayElement);
      });
    });
  }
}

// const januaryData = [
//   ["", "", "", 1, 2, 3, 4],
//   [5, 6, 7, 8, 9, 10, 11],
//   [12, 13, 14, 15, 16, 17, 18],
//   [19, 20, 21, 22, 23, 24, 25],
//   [26, 27, 28, 29, 30, 31, ""],
// ];

year2025Grid = generateCalendar(year2025);
populateCalendar(year2025Grid);
console.log(eventsData);
