$(function() {
    $('#login_button').on('click', function () {
        window.location.href = '/login/'
    });

    $('#signup_button').on('click', function () {
        window.location.href = '/signup/'
    });

    $('#username').on('input', function() {
        if($(this).val()) {
            $('#username_group')
                .removeClass('has-error')
                .removeClass('has-feedback');
            $('#alert').remove();
        }
        else {
            $('#username_group')
                .addClass('has-error')
                .addClass('has-feedback');
        }
    });

    $('#password').on('input', function() {
        if($(this).val()) {
            $('#password_group')
                .removeClass('has-error')
                .removeClass('has-feedback');
            $('#alert').remove();
        }
        else {
            $('#password_group')
                .addClass('has-error')
                .addClass('has-feedback');
        }
    });
});

function validateForm() {
    var passed = true;

    var username = document.forms["login_form"]["username"].value;
    if (username == null || username == "") {
        $('#username_group')
            .addClass('has-error')
            .addClass('has-feedback');
        passed = false;
    }

    var password = document.forms["login_form"]["password"].value;
    if (password == null || password == "") {
        $('#password_group')
            .addClass('has-error')
            .addClass('has-feedback');
        passed = false;
    }

    return passed;
}
