const _ = window.gettext || ((x) => x);
// const itp = window.interpolate || ((str, obj) => str);
import { translatedTypes } from "./constants.js";

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

export function stringToDateObject(dateString) {
  const dateParts = dateString.split("-");
  return new Date(`${dateParts[2]}-${dateParts[1]}-${dateParts[0]}`);
}

export function generateGoogleCalendarURL(event) {
  const baseUrl = "https://www.google.com/calendar/render";
  const eventTitle = encodeURIComponent(event.name);
  const eventStartDate = stringToDateObject(event.start_date);
  const eventEndDate = stringToDateObject(event.end_date);
  const eventLocation = encodeURIComponent(event.location);
  const eventDescription = encodeURIComponent(event.description || "");
  const eventMainLink = encodeURIComponent(event.main_link);
  const eventAdditionalLinks = [
    encodeURIComponent(event.additional_url_1 || ""),
    encodeURIComponent(event.additional_url_2 || ""),
  ].join("%0A"); // add new line between links

  // Google Calendar URL parameters
  const url = `${baseUrl}?action=TEMPLATE&text=${eventTitle}&dates=${eventStartDate
    .toISOString()
    .replace(/[-:]|\.\d{3}/g, "")}/${eventEndDate
    .toISOString()
    .replace(
      /[-:]|\.\d{3}/g,
      ""
    )}&location=${eventLocation}&details=${eventDescription}%0A${eventMainLink}%0A${eventAdditionalLinks}`;

  return url;
}

function generateOutlookCalendarURL(event) {
  const baseUrl = "https://outlook.live.com/owa/";
  const eventTitle = encodeURIComponent(event.name);
  const eventStartDate = stringToDateObject(event.start_date);
  const eventEndDate = stringToDateObject(event.end_date);
  const eventLocation = encodeURIComponent(event.location);
  const eventDescription = encodeURIComponent(event.description);
  const eventMainLink = encodeURIComponent(event.main_link);
  const eventAdditionalLinks = [
    encodeURIComponent(event.additional_url_1 || ""),
    encodeURIComponent(event.additional_url_2 || ""),
  ].join("%0A"); // add new line between links

  // Outlook Calendar URL parameters
  const url = `${baseUrl}?path=/calendar/action/compose&subject=${eventTitle}&startdt=${eventStartDate.toISOString()}&enddt=${eventEndDate.toISOString()}&location=${eventLocation}&body=${eventDescription}%0A${eventMainLink}%0A${eventAdditionalLinks}`;

  return url;
}

export function renderEvent(e) {
  const translatedType = translatedTypes[e.type];
  console.log(translatedType);
  return `
    <div><h3 class='d-inline'>${e.name}</h3> <span class='${
    e.type
  }-type px-1 rounded'>${translatedType}</span></div>
      <h5>${e.start_date} - ${e.end_date}</h5>
      <h6><i class="bi bi-pin-map-fill"></i> ${e.location}</h6>
      <div class='modal-description d-none' id='${e.id}-description'>
      </div>
      <div class="modal-links d-flex flex-column gap-2" id="${e.id}-links">
        <div class="modal-main-link">
          <h5 class="bold my-0"> ${_("Link to the event:")} </h5>
          <a href="${
            e.main_link
          }" class='linkToCopy' target="_blank" rel="noopener noreferrer">${
    e.main_link
  }</a>
        </div>
      </div>

      <div class="btn-group d-inline-block">
        <button class="btn btn-primary dropdown-toggle d-inline" type="button" data-bs-toggle="dropdown" data-bs-auto-close="true" aria-expanded="false">
          ${_("Add to calendar...")}
        </button>
        <ul class="dropdown-menu">
          <li><a class="dropdown-item" href="${generateGoogleCalendarURL(
            e
          )}"><i class="bi bi-google"></i> ${_("Google Calendar")}</a></li>
          <li><a class="dropdown-item" href="${generateOutlookCalendarURL(
            e
          )}"><i class="bi bi-microsoft"></i> ${_("Outlook")}</a></li>
          <li><a class="dropdown-item" href="${
            e.id
          }/download-ics/"><i class="bi bi-apple"></i> ${_(
    "Apple Calendar"
  )}</a></li>
          <li><a class="dropdown-item" href="${
            e.id
          }/download-ics/"><i class="bi bi-calendar"></i> ${_(
    "ICS File"
  )}</a></li>
        </ul>
      </div>
      <div class="toast position-fixed align-items-center border-0 z-3" role="alert" aria-live="assertive" aria-atomic="true" id="copyToast">
        <div class="d-flex">
          <div class="toast-body">
            ${_("Link copied!")}
          </div>
          <button type="button" class="btn-close me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
      </div>
      <hr class='event-hr'>

    `;
}

export function renderAdditionalUrls(e) {
  if (e.additional_url_1 || e.additional_url_2) {
    const linksContainer = document.getElementById(`${e.id}-links`);
    const additionalLinks = document.createElement("div");
    additionalLinks.classList.add("additional-links");

    let linksHTML = `<h5 class='mb-0'>${_("Additional links:")}</h5>`;

    if (e.additional_url_1) {
      linksHTML += `
      <div class="d-flex">
        <a href="${e.additional_url_1}"
           class="linkToCopy"
           target="_blank"
           rel="noopener noreferrer">
          ${e.additional_label_1 || "Link 1"}
        </a>
      </div>`;
    }

    if (e.additional_url_2) {
      linksHTML += `
      <div class="d-flex">
        <a href="${e.additional_url_2}"
           class="linkToCopy"
           target="_blank"
           rel="noopener noreferrer">
          ${e.additional_label_2 || "Link 2"}
        </a>
      </div>`;
    }

    additionalLinks.innerHTML = linksHTML;
    linksContainer.appendChild(additionalLinks);
  }
}

export function renderDescription(e) {
  if (e.description) {
    const modalDescription = document.getElementById(`${e.id}-description`);
    modalDescription.classList.remove("d-none");
    modalDescription.innerHTML = `
    <button class="btn btn-secondary mb-2" type="button" data-bs-toggle="collapse" data-bs-target="#${
      e.id
    }-collapseDescription" aria-expanded="false" aria-controls="${
      e.id
    }-collapseDescription">
      ${_("Show/hide description")}
    </button>
    <p class='collapse' id='${e.id}-collapseDescription'>
      ${e.description}
    </p>
    `;
  }
}

export function addCopyButtons(e) {
  const links = e.querySelectorAll("a.linkToCopy");

  links.forEach((link) => {
    const copyButton = document.createElement("i");
    copyButton.classList.add("bi", "bi-copy", "copy-link", "ms-2");

    copyButton.addEventListener("click", () => {
      const href = link.getAttribute("href");
      navigator.clipboard
        .writeText(href)
        .then(() => {
          // Show Bootstrap toast
          const toast = new bootstrap.Toast(
            document.getElementById("copyToast")
          );
          toast.show();
        })
        .catch((err) => {
          console.error("Failed to copy link: ", err);
        });
    });

    link.insertAdjacentElement("afterend", copyButton);
  });
}

export function fillEventsModal(eventsArray, dateString) {
  const eventsModalTitle = document.getElementById("eventsModalTitle");
  const eventsModalBody = document.getElementById("eventsModalBody");

  eventsModalTitle.textContent = `${_("Events")} ${dateString}`;
  eventsModalBody.innerHTML = "";

  eventsArray.forEach((e) => {
    const eventItem = document.createElement("div");
    eventItem.classList.add("d-flex", "flex-column", "gap-2");
    eventItem.id = `event-${e.id}`;
    eventItem.innerHTML = renderEvent(e);
    eventsModalBody.appendChild(eventItem);
    renderAdditionalUrls(e);
    addCopyButtons(eventItem);
    renderDescription(e);
  });
}
