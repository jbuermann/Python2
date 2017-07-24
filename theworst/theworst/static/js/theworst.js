function jumbotronCarousel()
{
        $(document).ready(function()
        {

            var owl = $('.owl-carousel'),
                max_width = 1170,
                owlOptions = {
                        items : 1,
                        loop : true,
                        center : true,
                        autoWidth:true,
                        autoplay: false,
                        autoplayTimeout:5000,
                        autoplayHoverPause: true
                    };
            // Prevent the jumbotron carousel from displaying on smaller screens until I can find a way to make it responsive
            if ( $(window).width() >= max_width )
            {
                var owlActive = owl.owlCarousel(owlOptions);
            }
            else
            {
                owl.addClass('off');
            }

            // Activate / Deactivate based on screen resolution
            $(window).resize(function()
            {
                if ( $(window).width()  >= max_width  )
                {
                    if ( $('.owl-carousel').hasClass('off') )
                    {
                        var owlActive = owl.owlCarousel(owlOptions).removeClass('off');
                    }
                }
                else
                {
                    if ( !$('.owl-carousel').hasClass('off') )
                    {
                        owl.owlCarousel('destroy').addClass('off');
                    }
                }
            });


        });
}