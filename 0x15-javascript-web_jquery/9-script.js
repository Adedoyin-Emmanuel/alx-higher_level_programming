$(document).ready(($) => {
  const apiUrl = "https://fourtonfish.com/hellosalut/?lang=f";

  $.ajax({
    url: apiUrl,
    success: (result) => {
      $("#hello").text(result);
    },
    error: (error) => {
      console.log(error);
    },
  });
});
