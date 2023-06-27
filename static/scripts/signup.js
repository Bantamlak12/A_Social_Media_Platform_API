// This jQuery AJAX adds functionality to the sign-up page.

$(document).ready(function () {
  $("#signupForm").submit(function (event) {
    event.preventDefault();
    // Get the input from the form
    let formData = {
      firstName: $("input[name=firstName]").val(),
      lastName: $("input[name=lastName]").val(),
      username: $("input[name=username]").val(),
      email: $("input[name=email]").val(),
      password: $("input[name=password]").val(),
      confirmPassword: $("input[name=confirmPassword]").val(),
    };
    // Send the data to the backend API
    $.ajax({
      url: "/signup",
      method: "POST",
      data: JSON.stringify(formData),
      contentType: "application/json",
      success: function (response) {
        // Resets the input fields
        $("#signupForm")[0].reset();
        if (response.username_msg) {
          $("#username_msg").text(response.username_msg);
          setTimeout(function () {
            $("#username_msg").text("");
          }, 3000);
        } else if (response.email_msg) {
          $("#email_msg").text(response.email_msg);
          setTimeout(function () {
            $("#email_msg").text("");
          }, 3000);
        } else if (response.password_msg) {
          $("#password_msg").text(response.password_msg);
          setTimeout(function () {
            $("#password_msg").text("");
          }, 3000);
        } else if (response.success_msg) {
          $("#success_msg").text(response.success_msg);
          setTimeout(function () {
            $("#success_msg").text("");
          }, 5000);
        }
      },
      error: function (error) {
        console.log(error);
      },
    });
  });
  // Reveal the menu while the bar button is clicked
  $(".menu-toggle").click(function () {
    $(".menu").toggle();
  });
});
