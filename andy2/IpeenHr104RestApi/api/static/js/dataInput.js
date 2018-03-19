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
                        $('#alldata').append($('<option>').text(data['name']+"-"+data['othername']+"(業績："+data['performance']+")"));
                    } )
                },
                error: function(XMLHttpRequest, textStatus, errorThrown) {
                    alert("some error " + String(errorThrown) + String(textStatus) + String(XMLHttpRequest.responseText));
                }  //debug用
            });
}
function inputData(d){
    postdata={name:$("#dienName").val(),othername:$("#otherName").val(),add:$("#dienAdd").val(),performance:$("#performance").val(),action:d} //_id:$("#dienNo").val(),
//    console.log(postdata)
    pushData(postdata)
}

