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

  const yearDropdown = document.getElementById("year-dropdown");
  yearDropdown.addEventListener("change", () => {
    // const chosenYear = document.getElementById(`year-${yearDropdown.value}`);
    scrollToElement(`year-${yearDropdown.value}`);
    // console.log("SCROLL WER");
  });

  scrollToElement(`month-${today.getMonth()}-${today.getFullYear()}`);
});
