// <li class="post">
//     <div class="post-content">
//         <div class="post-date">{{ moment(message.timestamp).fromNow(refresh=True) }}</div>
//         <div class="post-author">{{ message.sender.nickname }}</div>
//         <div class="post-body">{{ message.body }}</div>
//     </div>
// </li>

// <span class="" data-refresh="60000" data-format="fromNow(0)" data-timestamp="2014-09-12T17:40:55Z">a few seconds ago</span>
var isPreviousEventComplete = true;

$('document').ready(function() {
    // alert("Ready")
    get_older_posts();
    setInterval(function () {get_newer_posts()}, 5000);
});

function get_older_posts () {
    $.getJSON('/get_older_posts/', function(data) {
        $.each(data.messages, function(i, message) {
            $('.posts').append(populate_post(message))
        });
        flask_moment_render_all();
        isPreviousEventComplete = true;        
    });
};

function get_newer_posts () {
    console.log("Getting newer posts");
    $.getJSON('/get_newer_posts/', function(data) {
        var orgHeight = $('.posts').height();
        $.each(data.messages, function(i, message) {
            $('.posts').prepend(populate_post(message))
        });
        if ($(window).scrollTop() > $('.posts').offset().top) {
            $(window).scrollTop($(window).scrollTop() + $('.posts').height() - orgHeight);
        };
        flask_moment_render_all();
    });
};

function populate_post(message) {
    return ('<li class="post">' +
        '<div class="post-content">' +
        '<div class="post-date"><span class="flask-moment" data-refresh="60000" data-format="fromNow(0)" data-timestamp="' + message.timestamp + '"></span></div>' +
        '<div class="post-author">' + message.sender + '</div>' +
        '<div class="post-body">' + message.message + '</div>' +
        '</div>' +
        '</li>')
};

$(window).scroll( function () {
    if ($(window).scrollTop() + $(window).height() >= $('.posts').offset().top + $('.posts').height() - 100) { 
        if (isPreviousEventComplete) {
            isPreviousEventComplete = false;
            get_older_posts();
        };
    };
});
