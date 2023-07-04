// This jQuery adds functionality to the index.html page.

$(document).ready(function () {
  $(".toggle-menu").click(function (event) {
    event.stopPropagation(); // Prevents the click event from from bubbling up
    $(".mobile-menu").toggle();
  });

  // Hides the menu when clicked anywhere on the screen
  $(document).click(function () {
    $(".mobile-menu").hide();
  });
});
