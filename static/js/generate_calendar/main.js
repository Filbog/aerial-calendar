import { generateCalendar, populateCalendar } from "./generate_calendar.js";
import { scrollToElement } from "./utils.js";
import { setupFilters } from "./filters.js";

document.addEventListener("DOMContentLoaded", () => {
  const today = new Date();
  const events = [...allEvents];
  setupFilters(events, yearsData);
  console.log(events[0]);
  yearsData.forEach((year) => {
    const yearGrid = generateCalendar(year);
    populateCalendar(yearGrid, events);
  });

  scrollToElement(`month-${today.getMonth()}-${today.getFullYear()}`);
});
