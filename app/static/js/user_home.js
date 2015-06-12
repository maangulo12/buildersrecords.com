$(function() {
    $('#logout_button').on('click', function() {
        window.location.href = '/logout/';
    });

    $('#new_project_button').on('click', function() {
        window.location.href = '/new/';
    });

    $('[data-toggle="tooltip"]').tooltip()
});
