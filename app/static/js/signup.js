$(function() {
    $('#login_button').on('click', function () {
        window.location.href = '/login/'
    });

    $('#signup_button').on('click', function () {
        window.location.href = '/signup/'
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

    $('#username').on('input', function () {
        if ($(this).val()) {
            $('#username_group')
                .removeClass('has-error')
                .removeClass('has-feedback');
            $('#username_helper_text').remove();
            $('#username_icon').remove();
            $('#alert').remove();
        }
        else {
            $('#username_group')
                .addClass('has-error')
                .addClass('has-feedback');
            if ($('#username_helper_text').length == 0) {
                $('#username_group').append(
                    '<span id=\"username_helper_text\" class=\"help-block\"> This field is required. </span>');
            }
        }
    });

    $('#password').on('input', function () {
        if ($(this).val()) {
            $('#password_group')
                .removeClass('has-error')
                .removeClass('has-feedback');
            $('#password_helper_text').remove();
            $('#password_icon').remove();
            $('#alert').remove();
        }
        else {
            $('#password_group')
                .addClass('has-error')
                .addClass('has-feedback');
            if ($('#password_helper_text').length == 0) {
                $('#password_group').append(
                    '<span id=\"password_helper_text\" class=\"help-block\"> This field is required. </span>');
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

    var first_name = document.forms["signup_form"]["first_name"].value;
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

    var last_name = document.forms["signup_form"]["last_name"].value;
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

    var email = document.forms["signup_form"]["email"].value;
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

    var username = document.forms["signup_form"]["username"].value;
    if (username == null || username == "") {
        $('#username_group')
            .addClass('has-error')
            .addClass('has-feedback');
        if ($('#username_helper_text').length == 0) {
            $('#username_group').append(
                '<span id=\"username_helper_text\" class=\"help-block\"> This field is required. </span>');
        }
        passed = false;
    }

    var password = document.forms["signup_form"]["password"].value;
    if (password == null || password == "") {
        $('#password_group')
            .addClass('has-error')
            .addClass('has-feedback');
        if ($('#password_helper_text').length == 0) {
            $('#password_group').append(
                '<span id=\"password_helper_text\" class=\"help-block\"> This field is required. </span>');
        }
        passed = false;
    }

    var confirm_password = document.forms["signup_form"]["confirm_password"].value;
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
