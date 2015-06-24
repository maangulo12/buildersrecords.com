$(function() {
    $('#logout_button').on('click', function() {
        window.location.href = '/logout/';
    });

    $('#project_name').on('input', function() {
        if($(this).val()) {
            $('#project_name_group')
                .removeClass('has-error')
                .removeClass('has-feedback');
            $('#project_name_helper_text').remove();
            $('#project_name_icon').remove();
            $('#alert').remove();
        }
        else {
            $('#project_name_group')
                .addClass('has-error')
                .addClass('has-feedback');
            if ($('#project_name_helper_text').length == 0) {
                $('#project_name_group').append(
                '<div class="col-lg-9 col-lg-offset-3">' +
                    '<span id=\"project_name_helper_text\" class=\"help-block\"> This field is required. </span>' +
                '</div>');
            }
        }
    });
});

function validateForm() {
    var passed = true;

    var project_name = document.forms["new_form"]["project_name"].value;
    if (project_name == null || project_name == "") {
        $('#project_name_group')
            .addClass('has-error')
            .addClass('has-feedback');
        if ($('#project_name_helper_text').length == 0) {
            $('#project_name_group').append(
            '<div class="col-lg-9 col-lg-offset-3">' +
                '<span id=\"project_name_helper_text\" class=\"help-block\"> This field is required. </span>' +
            '</div>');
        }
        passed = false;
    }

    return passed;
}
