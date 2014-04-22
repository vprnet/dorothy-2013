$('#past-book-btn').on('click', function() {
    $('#past-books').css("display", "block");
    $('#upcoming-books').css("display", "none");
    $('#about-dorothy').css("display", "none");
    $(this).attr("class", "btn btn-success");
    $('#upcoming-book-btn').attr("class", "btn btn-primary");
    $('#about-dorothy-btn').attr("class", "btn btn-primary");
});

$('#upcoming-book-btn').on('click', function() {
    $('#past-books').css("display", "none");
    $('#upcoming-books').css("display", "block");
    $('#about-dorothy').css("display", "none");
    $(this).attr("class", "btn btn-success");
    $('#past-book-btn').attr("class", "btn btn-primary");
    $('#about-dorothy-btn').attr("class", "btn btn-primary");
});

$('#about-dorothy-btn, #contact-amy-prompt').on('click', function() {
    $('#past-books').css("display", "none");
    $('#upcoming-books').css("display", "none");
    $('#about-dorothy').css("display", "block");
    if (this.type === 'button') {
        $(this).attr("class", "btn btn-success");
    }
    $('#upcoming-book-btn').attr("class", "btn btn-primary");
    $('#past-book-btn').attr("class", "btn btn-primary");
});
