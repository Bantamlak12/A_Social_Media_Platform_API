// This jQuery AJAX adds functionality to the sign-out page.

$("document").ready(function () {
  $("#signout").on("click", function () {
    $.ajax({
      url: "/signout",
      method: "POST",
      success: function (response) {
        window.location.href = "/signin";
        console.log(response);
      },
      error: function (error) {
        console.log(error);
      },
    });
  });
});
