$(function(){

})

function pushData(postdata){
    $.ajax({
                type : "POST",  //使用POST方法
                url : "http://172.20.26.39:8000/api/push",
                data : postdata,
                success: function(datas){
                    console.log(datas)

                    $("#alldata").empty();
                    datas.forEach(function(data){
                        $('#alldata').append($('<option>').text(data['_id']+"-"+data['Corporation_ch']+"(營收："+data['income']+")"));
                    } )
                },
                error: function(XMLHttpRequest, textStatus, errorThrown) {
                    alert("some error " + String(errorThrown) + String(textStatus) + String(XMLHttpRequest.responseText));
                }  //debug用
            });
}
function inputData(d){
    postdata={_id:$("#dienNo").val(),income:$("#pwd").val(),action:d}
//    console.log(postdata)
    pushData(postdata)
}

