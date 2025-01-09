const _ = window.gettext || ((x) => x);

export const MONTH_NAMES = [
  _("January"),
  _("February"),
  _("March"),
  _("April"),
  _("May"),
  _("June"),
  _("July"),
  _("August"),
  _("September"),
  _("October"),
  _("November"),
  _("December"),
];

export const DAY_NAMES = [
  _("Mon"),
  _("Tue"),
  _("Wed"),
  _("Thu"),
  _("Fri"),
  _("Sat"),
  _("Sun"),
];

// Hacky way, but not sure how to translate dynamically generated JS strings in django otherwise
export const translatedTypes = {
  competition: "zawody",
  workshop: "warsztaty",
  conference: "konferencja",
  show: "show",
  festival: "festiwal",
  convention: "spotkania",
  other: "inne",
};
