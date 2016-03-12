$(function() {

    var $mid = $("#mid");

    $(window).on("popstate", function(e) {
        if (e.originalEvent.state !== null) {
            $mid.load(location.href);
        }
    });

    $(document).on("click", ".menu-link", function() {
        var href = $(this).attr("href");

        if (href.indexOf(document.domain) > -1 || href.indexOf(':') === -1) {
            history.pushState({}, '', href);
            $mid.load(href + " #mid>*");
            return false;
        }
    });

    $(document).on("click", ".body-link", function() {
        var href = $(this).attr("href");

        if (href.indexOf(document.domain) > -1 || href.indexOf(':') === -1) {
            history.pushState({}, '', href);
            $mid.load(href + " #mid>*");
            return false;
        }
    });

});
