$(document).ready(($) => {
  const apiUrl = "https://swapi-api.alx-tools.com/api/people/5/?format=json";

  $.ajax({
    url: apiUrl,
    success: (result) => {
      $("#character").text(result);
    },
    error: (error) => {
      console.log(error);
    },
  });
});
