// Shared chart palette — stays within the app's existing navy + baby-pink
// family so every chart feels like part of the same page, not a bolted-on
// widget with its own color scheme.

export const NAVY = "#172554";
export const NAVY_SOFT = "#1d4ed8";
export const PINK_DEEP = "#fb7185";
export const PINK_SOFT = "#fda4af";
export const PINK_PALE = "#ffe4e6";

// Cycled in order for multi-category charts (bars, pie slices).
// Two hues (navy family, pink family) alternated in light/dark pairs,
// rather than a rainbow of unrelated colors.
export const CHART_COLORS = [NAVY, PINK_DEEP, NAVY_SOFT, PINK_SOFT];

export const AXIS_STYLE = {
    fontSize: 12,
    fill: "#5b6478",
};
