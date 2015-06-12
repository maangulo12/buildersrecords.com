$(function() {
    $('#logout_button').on('click', function() {
        window.location.href = '/logout/';
    });

    $('#first_name').on('input', function () {
        if ($(this).val()) {
            $('#first_name_group')
                .removeClass('has-error')
                .removeClass('has-feedback');
            $('#first_name_helper_text').remove();
            $('#first_name_icon').remove();
            $('#alert').remove();
        }
        else {
            $('#first_name_group')
                .addClass('has-error')
                .addClass('has-feedback');
            if ($('#first_name_helper_text').length == 0) {
                $('#first_name_group').append(
                    '<span id=\"first_name_helper_text\" class=\"help-block\"> This field is required. </span>');
            }
        }
    });

    $('#last_name').on('input', function () {
        if ($(this).val()) {
            $('#last_name_group')
                .removeClass('has-error')
                .removeClass('has-feedback');
            $('#last_name_helper_text').remove();
            $('#last_name_icon').remove();
            $('#alert').remove();
        }
        else {
            $('#last_name_group')
                .addClass('has-error')
                .addClass('has-feedback');
            if ($('#last_name_helper_text').length == 0) {
                $('#last_name_group').append(
                    '<span id=\"last_name_helper_text\" class=\"help-block\"> This field is required. </span>');
            }
        }
    });

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

    var first_name = document.forms["account_form"]["first_name"].value;
    if (first_name == null || first_name == "") {
        $('#first_name_group')
            .addClass('has-error')
            .addClass('has-feedback');
        if ($('#first_name_helper_text').length == 0) {
            $('#first_name_group').append(
                '<span id=\"first_name_helper_text\" class=\"help-block\"> This field is required. </span>');
        }
        passed = false;
    }

    var last_name = document.forms["account_form"]["last_name"].value;
    if (last_name == null || last_name == "") {
        $('#last_name_group')
            .addClass('has-error')
            .addClass('has-feedback');
        if ($('#last_name_helper_text').length == 0) {
            $('#last_name_group').append(
                '<span id=\"last_name_helper_text\" class=\"help-block\"> This field is required. </span>');
        }
        passed = false;
    }

    var email = document.forms["account_form"]["email"].value;
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
