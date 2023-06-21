$('document').ready(function() {
    $('#signout').on('click', function() {
        $.ajax({
            url: '/logout',
            method: 'POST',
            success: function(response) {
                window.location.href = '/login';
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});