/** @type {import('tailwindcss').Config} */

module.exports = {
  content: ["./src/**/*.{html,jsx, js}"],
  theme: {
    extend: {},
    // colors: {
    //   cyan: colors.cyan,
    // },
    // colors: {
    //   primarybg: "#222831",
    //   // primarybg: "#202124",
    //   secondarybg: "#393E46",
    //   white: "#EEEEEE",
    //   teal: "#00ADB5",
    // },
  },
  plugins: [require("@tailwindcss/forms")],
};
