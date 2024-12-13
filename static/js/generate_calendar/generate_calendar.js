import { MONTH_NAMES, DAY_NAMES } from "./constants.js";

export function generateCalendar(year) {
  const yearGrid = [];

  for (let i = 0; i < 12; i++) {
    const firstDayIndex = (new Date(year, i, 1).getDay() + 6) % 7;
    const daysInMonth = new Date(year, i + 1, 0).getDate();

    const weeks = [];
    let currentWeek = [];
    let dayCounter = 1;

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

    while (currentWeek.length < 7 && currentWeek.length > 0) {
      currentWeek.push("");
    }
    weeks.push(currentWeek);

    yearGrid.push(weeks);
  }

  return { year, grid: yearGrid };
}

export function populateCalendar(yearData, eventsData) {
  const calendarContainer = document.getElementById("calendar-container");
  const { grid: yearGrid, year } = yearData;

  const yearWrapper = document.createElement("div");
  yearWrapper.classList.add("year-wrapper");
  yearWrapper.id = `year-${year}`;

  const yearHeading = document.createElement("h1");
  yearHeading.textContent = year;
  yearWrapper.appendChild(yearHeading);
  calendarContainer.appendChild(yearWrapper);

  yearGrid.forEach((monthData, monthIndex) => {
    const monthContainer = document.createElement("div");
    monthContainer.classList.add("month-container");
    monthContainer.id = `month-${monthIndex}-${year}`;

    const monthGrid = document.createElement("div");
    monthGrid.classList.add("month", "calendar-grid");

    const monthHeading = document.createElement("h2");
    monthHeading.textContent = MONTH_NAMES[monthIndex];
    monthContainer.appendChild(monthHeading);
    monthContainer.appendChild(monthGrid);
    yearWrapper.appendChild(monthContainer);

    DAY_NAMES.forEach((dayName) => {
      const dayElement = document.createElement("div");
      dayElement.classList.add("day-name");
      dayElement.textContent = dayName;
      monthGrid.appendChild(dayElement);
    });

    monthData.forEach((week) => {
      week.forEach((day) => {
        const dayElement = document.createElement("div");
        dayElement.classList.add("day");
        if (day === "") {
          dayElement.classList.add("empty");
        } else {
          dayElement.innerHTML = `<p class='day-number'>${day}</p>`;

          const dateString = `${year}-${String(monthIndex + 1).padStart(
            2,
            "0"
          )}-${String(day).padStart(2, "0")}`;
          const eventsOnDay = eventsData.filter(
            (event) =>
              event.start_date <= dateString && event.end_date >= dateString
          );

          if (eventsOnDay.length > 0) {
            dayElement.classList.add("has-events");
            const eventList = document.createElement("ul");
            eventsOnDay.forEach((event) => {
              const eventItem = document.createElement("li");
              eventItem.classList.add("event-item", event.type);
              eventItem.textContent = event.name;
              eventList.appendChild(eventItem);
            });
            dayElement.appendChild(eventList);
          }
        }
        monthGrid.appendChild(dayElement);
      });
    });
  });
}
