import { MONTH_NAMES, DAY_NAMES } from "./constants.js";
import { fillEventsModal } from "./utils.js";

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
  yearHeading.classList.add("year-heading", "display-5");
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

          const dateString = `${String(day).padStart(2, "0")}-${String(
            monthIndex + 1
          ).padStart(2, "0")}-${year}`;
          // same date as the one in dateString, but easier to compare Date objects
          const targetDate = new Date(
            `${year}-${String(monthIndex + 1).padStart(2, "0")}-${String(
              day
            ).padStart(2, "0")}`
          );

          const eventsOnDay = eventsData.filter((event) => {
            const startDateParts = event.start_date.split("-");
            const endDateParts = event.end_date.split("-");

            // Parse start_date and end_date into Date objects
            const startDate = new Date(
              `${startDateParts[2]}-${startDateParts[1]}-${startDateParts[0]}`
            );
            const endDate = new Date(
              `${endDateParts[2]}-${endDateParts[1]}-${endDateParts[0]}`
            );

            // Compare dates properly
            return startDate <= targetDate && endDate >= targetDate;
          });

          if (eventsOnDay.length > 0) {
            dayElement.classList.add("has-events");
            dayElement.setAttribute("data-bs-toggle", "modal");
            dayElement.setAttribute("data-bs-target", "#eventsModal");
            const eventList = document.createElement("ul");
            eventsOnDay.forEach((event) => {
              const eventItem = document.createElement("li");
              eventItem.classList.add("event-item", `${event.type}-type`);
              eventItem.id = event.id;
              eventItem.textContent = event.name;
              eventList.appendChild(eventItem);
            });
            dayElement.appendChild(eventList);
            // console.log(eventsOnDay);
            dayElement.addEventListener("click", () =>
              fillEventsModal(eventsOnDay, dateString)
            );
          }
        }
        monthGrid.appendChild(dayElement);
      });
    });
  });
}

export function renderCalendar(eventsData, yearsData) {
  const calendarContainer = document.getElementById("calendar-container");
  calendarContainer.innerHTML = ""; // Clear the previous content

  yearsData.forEach((year) => {
    const yearGrid = generateCalendar(year);
    populateCalendar(yearGrid, eventsData);
  });
}
