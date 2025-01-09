import { renderEvent } from "./utils.js";

const unverifiedEvent = JSON.parse(
  document.getElementById("unverifiedEvents").textContent
);
console.log(unverifiedEvents);

function renderUnverifiedEvents(events) {
  unverifiedEvents.forEach((event) => {
    eventContainer = document.getElementById(event.id);
    eventContainer.appendChild(renderEvent(event));
  });
}

document.addEventListener("DOMContentLoaded", () => {
  renderUnverifiedEvents(unverifiedEvents);
});
