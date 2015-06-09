$(function() {
    $('#email').on('input', function () {
        if ($(this).val()) {
            $('#email_group')
                .removeClass('has-error')
                .removeClass('has-feedback');
            $('#email_helper_text').remove();
            $('#email_icon').remove();
            $('#alert').remove();
        }
        else {
            $('#email_group')
                .addClass('has-error')
                .addClass('has-feedback');
            if ($('#email_helper_text').length == 0) {
                $('#email_group').append(
                    '<span id=\"email_helper_text\" class=\"help-block\"> This field is required. </span>');
            }
        }
    });
});

function validateForm() {
    var passed = true;

    var email = document.forms["password_reset_form"]["email"].value;
    if (email == null || email == "") {
        $('#email_group')
            .addClass('has-error')
            .addClass('has-feedback');
        if ($('#email_helper_text').length == 0) {
            $('#email_group').append(
                '<span id=\"email_helper_text\" class=\"help-block\"> This field is required. </span>');
        }
        passed = false;
    }

    return passed;
}
