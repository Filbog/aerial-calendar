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
