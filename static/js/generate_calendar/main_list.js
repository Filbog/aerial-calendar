import { renderList } from "./generate_list.js";
import { setupFilters } from "./filters.js";

document.addEventListener("DOMContentLoaded", () => {
  const events = [...allEvents];

  // Set up filters with the renderList function
  setupFilters(events, yearsData, renderList);

  // Initial render of the list with all events
  renderList(events, yearsData);

  const yearDropdown = document.getElementById("year-dropdown");
  yearDropdown.addEventListener("change", () => {
    // const chosenYear = document.getElementById(`year-${yearDropdown.value}`);
    scrollToElement(`year-${yearDropdown.value}`);
    // console.log("SCROLL WER");
  });
});
