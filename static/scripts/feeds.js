// This jQuery AJAX adds functionality to the feeds page.

$("document").ready(function () {
  $("#createPost").submit(function (event) {
    event.preventDefault();

    // Take the post tile and content
    let post = {
      title: $("input[name=title]").val(),
      post: $("textarea[name=post]").val(),
    };

    // Send the data to the backend
    $.ajax({
      url: "/feeds",
      method: "POST",
      data: JSON.stringify(post),
      contentType: "application/json",
      success: function (response) {
        location.reload(true);
        console.log(response);
      },
      error: function (error) {
        console.log(error);
      },
    });
  });

  $(".fa-solid.fa-trash").click(function () {
    if (confirm("Are you sure you want to delete this post?")) {
      const content_id = $(this).data("content-id");

      $.ajax({
        url: "/delete",
        method: "DELETE",
        data: { content_id: content_id },
        success: function (response) {
          location.reload(true);
        },
        error: function (error) {
          console.log(error);
        },
      });
    }
  });
});
