$(function() {
    var project_id;

    $('#logout_button').on('click', function() {
        window.location.href = '/logout/';
    });

    $('#new_project_button').on('click', function() {
        window.location.href = '/new/';
    });

    $('.delete_project_button').on('click', function() {
        project_id = this.id;
        $('#delete_project_modal').modal('show');
    });

    $('#delete_project_confirm').on('click', function() {
        $.getJSON(
            '/delete_project_ajax/',
            { project_id: project_id }
        ).done(function() {
            location.reload();
        });
    });

    $('.edit_project_button').on('click', function() {
        project_id = this.id;
        $('#edit_project_modal').modal('show');
    });

    $('[data-toggle="tooltip"]').tooltip();
});
