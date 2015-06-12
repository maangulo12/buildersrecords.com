$(function() {
    $('#logout_button').on('click', function() {
        window.location.href = '/logout/';
    });

    $('#old_password').on('input', function () {
        if ($(this).val()) {
            $('#old_password_group')
                .removeClass('has-error')
                .removeClass('has-feedback');
            $('#old_password_helper_text').remove();
            $('#old_password_icon').remove();
            $('#alert').remove();
        }
        else {
            $('#old_password_group')
                .addClass('has-error')
                .addClass('has-feedback');
            if ($('#old_password_helper_text').length == 0) {
                $('#old_password_group').append(
                    '<span id=\"old_password_helper_text\" class=\"help-block\"> This field is required. </span>');
            }
        }
    });

    $('#new_password').on('input', function () {
        if ($(this).val()) {
            $('#new_password_group')
                .removeClass('has-error')
                .removeClass('has-feedback');
            $('#new_password_helper_text').remove();
            $('#new_password_icon').remove();
            $('#alert').remove();
        }
        else {
            $('#new_password_group')
                .addClass('has-error')
                .addClass('has-feedback');
            if ($('#new_password_helper_text').length == 0) {
                $('#new_password_group').append(
                    '<span id=\"new_password_helper_text\" class=\"help-block\"> This field is required. </span>');
            }
        }
    });

    $('#confirm_password').on('input', function () {
        if ($(this).val()) {
            $('#confirm_password_group')
                .removeClass('has-error')
                .removeClass('has-feedback');
            $('#confirm_password_helper_text').remove();
            $('#confirm_password_icon').remove();
            $('#alert').remove();
        }
        else {
            $('#confirm_password_group')
                .addClass('has-error')
                .addClass('has-feedback');
            if ($('#confirm_password_helper_text').length == 0) {
                $('#confirm_password_group').append(
                    '<span id=\"confirm_password_helper_text\" class=\"help-block\"> This field is required. </span>');
            }
        }
    });
});

function validateForm() {
    var passed = true;

    var old_password = document.forms["password_form"]["old_password"].value;
    if (old_password == null || old_password == "") {
        $('#old_password_group')
            .addClass('has-error')
            .addClass('has-feedback');
        if ($('#old_password_helper_text').length == 0) {
            $('#old_password_group').append(
                '<span id=\"old_password_helper_text\" class=\"help-block\"> This field is required. </span>');
        }
        passed = false;
    }

    var new_password = document.forms["password_form"]["new_password"].value;
    if (new_password == null || new_password == "") {
        $('#new_password_group')
            .addClass('has-error')
            .addClass('has-feedback');
        if ($('#new_password_helper_text').length == 0) {
            $('#new_password_group').append(
                '<span id=\"new_password_helper_text\" class=\"help-block\"> This field is required. </span>');
        }
        passed = false;
    }

    var confirm_password = document.forms["password_form"]["confirm_password"].value;
    if (confirm_password == null || confirm_password == "") {
        $('#confirm_password_group')
            .addClass('has-error')
            .addClass('has-feedback');
        if ($('#confirm_password_helper_text').length == 0) {
            $('#confirm_password_group').append(
                '<span id=\"confirm_password_helper_text\" class=\"help-block\"> This field is required. </span>');
        }
        passed = false;
    }

    return passed;
}
