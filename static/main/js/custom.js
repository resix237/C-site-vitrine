$(document).ready(function() {
    $(window).scroll(function() {
        if ($(document).scrollTop() > 100) {
            $("nav").addClass("shrink");

        } else {
            $("nav").removeClass("shrink")
        }

    });


});



//Get the button