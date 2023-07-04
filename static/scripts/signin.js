// This jQuery AJAX adds functionality to the sign-in page.

$(document).ready(function () {
  $("#signinForm").submit(function (event) {
    event.preventDefault();
    // Get username and password
    let formData = {
      username: $("input[name=username]").val(),
      password: $("input[name=password]").val(),
    };

    // Send the data to the backend
    $.ajax({
      url: "/signin",
      method: "POST",
      data: JSON.stringify(formData),
      contentType: "application/json",
      success: function (response) {
        $("#signinForm")[0].reset();
        if (response.signin_username_error) {
          $("#signin_username_error").text(response.signin_username_error);
          setTimeout(function () {
            $("#signin_username_error").text("");
          }, 2000);
        }

        if (response.signin_password_error) {
          $("#signin_password_error").text(response.signin_password_error);
          setTimeout(function () {
            $("#signin_password_error").text("");
          }, 2000);
        }

        if (response.success) {
          window.location.href = "/feeds";
          $("#success_msg").text(response.success);
        }
      },
      error: function (error) {
        console.log(error);
      },
    });
  });
  // Reveal the menu while the bar button is clicked
  $(".menu-toggle").click(function (event) {
    event.stopPropagation(); // Prevents the click event from from bubbling up
    $(".menu").toggle();
  });

  // Hides the menu when clicked anywhere on the screen
  $(document).click(function () {
    $(".menu").hide();
  });
});
