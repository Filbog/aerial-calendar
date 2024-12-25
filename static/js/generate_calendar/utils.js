export function scrollToElement(
  elementId,
  behavior = "smooth",
  block = "start"
) {
  const element = document.getElementById(elementId);
  if (element) {
    element.scrollIntoView({ behavior, block });
  }
}

export function fillEventsModal(eventsArray, dateString) {
  const eventsModalTitle = document.getElementById("eventsModalTitle");
  const eventsModalBody = document.getElementById("eventsModalBody");

  eventsModalTitle.textContent = `Wydarzenia ${dateString}`;
  eventsModalBody.innerHTML = "";

  eventsArray.forEach((e) => {
    const eventItem = document.createElement("div");
    eventItem.innerHTML = `
    <div class="d-flex gap-1"><h2>${e.name}</h2><p class='${e.type}-type px-1 rounded'>${e.type}</p></div>
      <h5>${e.start_date} - ${e.end_date}</h5>
      <h4 class="bold">Link do wydarzenia: </h4>
      <a href="${e.main_link}" target="_blank" rel="noopener">${e.main_link}</a>
      <div class="btn-group">
        <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" data-bs-auto-close="true" aria-expanded="false">
          Dodaj do Kalendarza...
        </button>
        <ul class="dropdown-menu">
          <li><a class="dropdown-item" href="#">Kalendarz Google</a></li>
          <li><a class="dropdown-item" href="#">Outlook</a></li>
          <li><a class="dropdown-item" href="#">Kalendarz Apple</a></li>
          <li><a class="dropdown-item" href="#">Inny kalendarz</a></li>
        </ul>
      </div>
      <hr>
    `;
    eventsModalBody.appendChild(eventItem);
  });
  console.log("hello");
}
