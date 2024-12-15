import { generateCalendar, populateCalendar } from "./generate_calendar.js";

export function setupFilters(events, yearsData) {
  const typeCheckboxes = document.querySelectorAll(".type-checkbox");
  const locationDropdown = document.getElementById("location-dropdown");
  const onlyAerialCheckbox = document.getElementById("only-aerial");
  const uncheckAllBtn = document.getElementById("uncheck-all-types");
  const applyFiltersBtn = document.getElementById("applyFiltersBtn");

  uncheckAllBtn.addEventListener("change", () => {
    const isChecked = uncheckAllBtn.checked;
    typeCheckboxes.forEach((el) => (el.checked = isChecked));
  });

  const locations = [...new Set(events.map((event) => event.location))];
  locations.forEach((location) => {
    const option = document.createElement("option");
    option.value = location;
    option.textContent = location;
    locationDropdown.appendChild(option);
  });

  applyFiltersBtn.addEventListener("click", () => {
    const selectedTypes = Array.from(typeCheckboxes)
      .filter((checkbox) => checkbox.checked)
      .map((checkbox) => checkbox.value);

    const selectedLocation = locationDropdown.value;
    const isOnlyAerial = onlyAerialCheckbox.checked;

    const filteredEvents = events.filter((event) => {
      const matchesType = selectedTypes.includes(event.type);
      const matchesLocation =
        selectedLocation === "all" || event.location === selectedLocation;
      let matchesAerial = !isOnlyAerial || event.is_aerial;
      // console.log(matchesAerial);
      return matchesType && matchesLocation && matchesAerial;
    });

    const calendarContainer = document.getElementById("calendar-container");
    calendarContainer.innerHTML = "";
    yearsData.forEach((year) => {
      const yearGrid = generateCalendar(year);
      populateCalendar(yearGrid, filteredEvents);
      console.log(filteredEvents[0]);
    });
  });
}
