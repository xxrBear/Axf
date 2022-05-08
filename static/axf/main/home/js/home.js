$(function () {
    initWheel();
    initMustBuy();
})

function initWheel() {
        var mySwiper = new Swiper('#topSwiper',
                                {
                                    loop:true,// 无限循化
                                    autoplay:600,
                                    pagination:'.swiper-pagination',
                                    autoplayDisableOnInteraction:false,
                                })
}

function  initMustBuy() {
    var mySwiper1 = new Swiper('#swiperMenu',{
        slidesPerView:3,
        loop:true,// 无限循化
        autoplay:600,
        pagination:'.swiper-pagination',
        autoplayDisableOnInteraction:false,
    })
}





