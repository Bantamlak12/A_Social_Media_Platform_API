$(document).ready(function() {

    $('#signupForm').submit(function(event) {
        event.preventDefault();
        // Get the form
        let formData = {
            'firstName': $('input[name=firstName]').val(),
            'lastName': $('input[name=lastName]').val(),
            'username': $('input[name=username]').val(),
            'email': $('input[name=email]').val(),
            'password': $('input[name=password]').val(),
            'confirmPassword': $('input[name=confirmPassword]').val()
        };
        // Send the data to the backend API
        $.ajax({
            url: '/register',
            method: 'POST',
            data: JSON.stringify(formData),
            contentType: 'application/json',
            success: function(response) {
                $('#signupForm')[0].reset();
                $('#successMessage').text(response.message);
            },
            error: function(error) {
                console.log(error)
            }
        });
    });
});