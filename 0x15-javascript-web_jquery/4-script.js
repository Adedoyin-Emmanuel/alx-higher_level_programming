$(document).ready(($) => {
  $("#toggle_header").on("click", () => {
    $("header").toggleClass("red");
  });
});
