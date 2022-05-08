$(function () {
    $('#all_type').click(function () {
        $(this).find('span').find('span').toggleClass('glyphicon glyphicon-chevron-up glyphicon glyphicon-chevron-down');

        $('#all_type_container').toggle();
    });


    $('#sort_rule').click(function () {
        $(this).find('span').find('span').toggleClass('glyphicon glyphicon-chevron-up glyphicon glyphicon-chevron-down');

        $('#sort_rule_container').toggle();
    });

//把闪购的商品增加到购物车
    $('.addShopping').click(function () {
        var $button = $(this);
        var goodis = $button.attr('goodsid');
        // alert(goodis)(日马写错了)
        $.get('/axfcart/addtoCart/',
            {'goodis':goodis},
            function (data) {
                if (data['status'] === 200){
                    $button.prev().html(data['c_goods_num']);
                }else{
                    window.location.href='/axfuser/login/'
                }
            }
            )
    });


        $('.subShopping').click(function () {
        var $button = $(this);
        var goodis2 = $button.attr('goodsid2');
        // alert(goodis)
        $.get('/axfcart/subtoCart/',
            {'goodis2':goodis2},
            function (data) {
                if (data['status'] === 200){
                        $button.next().html(data['c_goods_num']);
                }else{
                    window.location.href='/axfuser/login/'
                }
            }
            )
    })
});











