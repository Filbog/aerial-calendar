import { MONTH_NAMES } from "./constants.js";
import {
  renderEvent,
  renderAdditionalUrls,
  renderDescription,
} from "./utils.js";

export function generateList(year) {
  const events = [...allEvents];

  for (let i = 0; i < MONTH_NAMES.length; i++) {
    const monthContainer = document.createElement("div");
    monthContainer.classList.add("month-container");
    monthContainer.id = `${MONTH_NAMES[i]}`;
    const monthHeading = document.createElement("h1");
    monthHeading.innerHTML = `${MONTH_NAMES[i]}`;
    monthContainer.appendChild(monthHeading);

    const eventsThisMonth = events.filter((event) => {
      const eventStartDateMonth = parseInt(event.start_date.split("-")[1]);
      const eventStartDateYear = parseInt(event.start_date.split("-")[2]);

      console.log("EVENT START DATE BEFORE MOD", event.start_date);
      console.log(eventStartDateMonth);
      const eventEndDateMonth = parseInt(event.end_date.split("-")[1]);
      const eventEndDateYear = parseInt(event.end_date.split("-")[2]);

      console.log(eventEndDateMonth);

      if (
        (eventStartDateMonth === i + 1 && eventStartDateYear === year) ||
        (eventEndDateMonth === i + 1 && eventEndDateYear === year)
      ) {
        return event;
      }
    });

    const yearContainer = document.getElementById(`${year}`);
    yearContainer.appendChild(monthContainer);

    eventsThisMonth.forEach((event) => {
      const eventItem = document.createElement("div");
      eventItem.classList.add("d-flex", "flex-column", "gap-3");
      eventItem.id = `event-${event.id}`;
      eventItem.innerHTML = renderEvent(event);
      monthContainer.appendChild(eventItem);

      renderAdditionalUrls(event);
      renderDescription(event);
    });
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const listContainer = document.getElementById("list-container");
  yearsData.forEach((year) => {
    const yearContainer = document.createElement("div");
    yearContainer.id = `${year}`;
    const yearHeading = document.createElement("h1");
    yearContainer.appendChild(yearHeading);
    listContainer.appendChild(yearContainer);

    generateList(year);
  });
});
