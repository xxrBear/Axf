$(function () {
    $('#all_type').click(function () {
        $(this).find('span').find('span').toggleClass('glyphicon glyphicon-chevron-up glyphicon glyphicon-chevron-down');

        $('#all_type_container').toggle();
    });


    $('#sort_rule').click(function () {
        $(this).find('span').find('span').toggleClass('glyphicon glyphicon-chevron-up glyphicon glyphicon-chevron-down');

        $('#sort_rule_container').toggle();
    });


//    添加到购物车
    $('.addShopping').click(function () {
        // var $button = $(this);
        //attr可以获取自带的属性也可以获取自定义的属性
        // alert($button.attr('class'));
        // alert($button.attr('goodsid'));
        // prop只可以获取自带的属性
        // alert($button.prop('class'));
        // alert($button.prop('goodsid'));

        var $button = $(this);

        var goodsid = $button.attr('goodsid');

        $.get('/axfcart/addToCart/',
            {'goodsid':goodsid},
            function (data) {
                if(data['status'] === 200){
                    $button.prev().html(data['c_goods_num']);
                }else{
                    window.location.href='/axfuser/login/'
                }
            })



    })

})