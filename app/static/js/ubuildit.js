$(function() {
    $('#logout_button').on('click', function() {
        window.location.href = '/logout/';
    });

    $('#skip_button').on('click', function() {
        window.location.href = '/new/edit/';
    });

    $('#file').on('input', function() {
        if($(this).val()) {
            $('#file_group')
                .removeClass('has-error')
                .removeClass('has-feedback');
            $('#file_helper_text').remove();
            $('#file_icon').remove();
            $('#alert').remove();
        }
        else {
            $('#file_group')
                .addClass('has-error')
                .addClass('has-feedback');
            if ($('#file_helper_text').length == 0) {
                $('#file_group').append('<span id=\"file_helper_text\" class=\"help-block\"> This field is required. </span>');
            }
        }
    });
});

function validateForm() {
    var passed = true;

    var file = document.forms["upload_form"]["file"].value;
    if (file == null || file == "") {
        $('#file_group')
            .addClass('has-error')
            .addClass('has-feedback');
        if ($('#file_helper_text').length == 0) {
            $('#file_group').append('<span id=\"file_helper_text\" class=\"help-block\"> This field is required. </span>');
        }
        passed = false;
    }

    return passed;
}
