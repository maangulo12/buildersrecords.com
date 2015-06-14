$(function() {
    $('#logout_button').on('click', function() {
        window.location.href = '/logout/';
    });

    $('#new_project_button').on('click', function() {
        window.location.href = '/new/';
    });

    $('.delete_project_button').on('click', function() {
        var id = this.id;
        $('#delete_project_modal').modal('show');
    });

    $('.edit_project_button').on('click', function() {
        var id = this.id;
        $('#edit_project_modal').modal('show');
    });

    $('[data-toggle="tooltip"]').tooltip();
});
