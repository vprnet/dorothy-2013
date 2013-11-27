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

$('a.audio_play').click(function() {
    if (this.firstChild.paused === false) {
        this.firstChild.pause();
        $(this).children('button').children('span.glyphicon')
            .attr('class', 'glyphicon glyphicon-play');
    } else {
        this.firstChild.play();
        $(this).children('button').children('span.glyphicon')
            .attr('class', 'glyphicon glyphicon-pause');
    }
});

var disqusPublicKey = "gUTvdgLF0mf2OdeRm7K4IyX2sagdTqSh1pa5JT9dcjdfSpv8X7q9eAHbSQTSGBip";
var disqusShortname = "npr-vpr";

var urlArray = [];
$('.count-comments').each(function () {
    var url = $(this).attr('data-disqus-url');
    urlArray.push('link:' + url);
});

$.ajax({
    type: 'GET',
    url: "https://disqus.com/api/3.0/threads/set.jsonp",
    data: { api_key: disqusPublicKey, forum : disqusShortname, thread : urlArray },
    cache: false,
    dataType: 'jsonp',
    success: function (result) {

        for (var i in result.response) {

            var count = result.response[i].posts;

            $('a[data-disqus-url="' + result.response[i].link + '"]').text("View Comments (" + count + ")");

        }
    }
});
