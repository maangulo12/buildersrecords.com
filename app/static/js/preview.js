$(function() {
    var item_id;

    $('#logout_button').on('click', function() {
        window.location.href = '/logout/';
    });

    $('#create_project_button').on('click', function() {
        window.location.href = '/new/create/';
    });

    $('.delete_item_button').on('click', function() {
        item_id = this.id;
        $('#delete_item_modal').modal('show');
    });

    $('.edit_item_button').on('click', function() {
        item_id = this.id;
        $('#edit_item_modal').modal('show');
    });

    $('[data-toggle="tooltip"]').tooltip();
});
