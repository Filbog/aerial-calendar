import { MONTH_NAMES } from "./constants.js";
import {
  renderEvent,
  renderAdditionalUrls,
  renderDescription,
  scrollToElement,
} from "./utils.js";

export function generateList(year, events) {
  for (let i = 0; i < MONTH_NAMES.length; i++) {
    const eventsThisMonth = events.filter((event) => {
      const eventStartDateMonth = parseInt(event.start_date.split("-")[1]);
      const eventStartDateYear = parseInt(event.start_date.split("-")[2]);

      const eventEndDateMonth = parseInt(event.end_date.split("-")[1]);
      const eventEndDateYear = parseInt(event.end_date.split("-")[2]);
      return (
        (eventStartDateMonth === i + 1 && eventStartDateYear === year) ||
        (eventEndDateMonth === i + 1 && eventEndDateYear === year)
      );
    });

    if (eventsThisMonth.length > 0) {
      const monthContainer = document.createElement("div");
      monthContainer.classList.add("month-container");
      monthContainer.id = `${MONTH_NAMES[i]}`;

      const monthHeading = document.createElement("h1");
      monthHeading.innerHTML = `${MONTH_NAMES[i]}`;
      monthContainer.appendChild(monthHeading);

      const yearContainer = document.getElementById(`year-${year}`);
      yearContainer.appendChild(monthContainer);

      eventsThisMonth.forEach((event) => {
        const eventItem = document.createElement("div");
        eventItem.classList.add("d-flex", "flex-column", "gap-2");
        eventItem.id = `event-${event.id}`;
        eventItem.innerHTML = renderEvent(event);
        monthContainer.appendChild(eventItem);

        renderAdditionalUrls(event);
        renderDescription(event);
      });
    }
  }
}

export function renderList(filteredEvents, yearsData) {
  const listContainer = document.getElementById("list-container");
  listContainer.innerHTML = "";

  yearsData.forEach((year) => {
    const yearContainer = document.createElement("div");
    yearContainer.id = `year-${year}`;
    yearContainer.classList = "year-wrapper";
    const yearHeading = document.createElement("h1");
    yearHeading.innerHTML = `${year}`;
    yearHeading.classList = "my-0 mx-auto year-heading";
    yearContainer.appendChild(yearHeading);
    listContainer.appendChild(yearContainer);

    generateList(year, filteredEvents);
  });

  const yearDropdown = document.getElementById("year-dropdown");
  yearDropdown.addEventListener("change", () => {
    scrollToElement(`year-${yearDropdown.value}`);
  });
}
