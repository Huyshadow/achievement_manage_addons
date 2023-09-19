$(document).ready(function() {
    // Bắt sự kiện khi ô input được focus
    $('input').focus(function() {
        $(this).css('background-color', 'yellow');
    });

    // Bắt sự kiện khi ô input mất focus
    $('input').blur(function() {
        $(this).css('background-color', 'white');
    });
});

$('.o_input').focus()
