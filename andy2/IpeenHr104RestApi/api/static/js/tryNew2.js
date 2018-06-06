////緯度轉距離公尺(暫時沒用到)
//function getDistance(lat1, lng1, lat2, lng2) {
//    var dis = 0;
//    var radLat1 = toRadians(lat1);
//    var radLat2 = toRadians(lat2);
//    var deltaLat = radLat1 - radLat2;
//    var deltaLng = toRadians(lng1) - toRadians(lng2);
//    var dis = 2 * Math.asin(Math.sqrt(Math.pow(Math.sin(deltaLat / 2), 2) + Math.cos(radLat1) * Math.cos(radLat2) * Math.pow(Math.sin(deltaLng / 2), 2)));
//    return dis * 6378137;
//    function toRadians(d) {  return d * Math.PI / 180;}
//}

////以下產生周圍生活標記--------------------------------------(暫時用不到)
//var searchTarget,service;
//function getpoint(pointType){
//    searchTarget=map.getCenter();
//    infowindow = new google.maps.InfoWindow();
//    service = new google.maps.places.PlacesService(map);
//    //最多產生20個點 (如果type不選會產生rank高的)
//    service.nearbySearch({
//        location: searchTarget,
//        radius:50*(Math.pow(2,(20-map.getZoom()))),
//        type: pointType
//    }, callback);
//}
//function callback(results, status) {
////    delpoint();是否每點一個就刪除?
//    console.log(status);
//    console.log(results);
//    var x=0
//    var nearNames=[]
//    if (status === google.maps.places.PlacesServiceStatus.OK) {
//        for (var i = 0; i < results.length; i++) {
//            if (nearNames.indexOf(results[i].name)==-1){
//                createMarker(results[i]);
//                nearNames.push(results[i].name)
//            }
//        }
//    }
//}
markers=[] //用來儲存每個標記 以便之後刪除
//function createMarker(place) {
//    var placeLoc = place.geometry.location;
//    var image = {
//                  url:place.icon,//google內建icon
//                  size: new google.maps.Size(15, 15),
//                  origin: new google.maps.Point(0, 0),
//                  anchor: new google.maps.Point(7.5, 7.5),
//                  scaledSize: new google.maps.Size(15, 15)
//            };
//    var marker = new google.maps.Marker({
//        map: map,
//        position: place.geometry.location,
//        icon:image,
//    });
//
//    marker.addListener('click', function() {
//        var request = {
//            placeId: place.place_id
//        };
//        service.getDetails(request, function(details, status) {
//          infowindow.setContent([
//            details.name,
//            details.formatted_address,
//            details.website,
////            details.rating,
//    //              details.icon,
//            details.formatted_phone_number].join("<br />"));
//          infowindow.open(map, marker);
//        });
//    });
//        markers.push(marker)
//}
styleList=['其他美食',
 '咖啡、簡餐、茶',
 '烘焙、甜點、零食',
 'buffet自助餐',
 '中式料理',
 '主題特色餐廳',
 '早餐',
 '亞洲料理',
 '冰品、飲料、甜湯',
 '小吃',
 '鍋類',
 '素食',
 '異國料理',
 '日式料理',
 '速食料理',
 '燒烤類']

//icon集
var imagesUrl={
    'buffet自助餐':"https://cdn3.iconfinder.com/data/icons/hotel-restaurant-glyphs-vol-4/52/hotel__service__restaurant__hostel__food__buffet__dish-48.png",
//    '中式料理':"https://cdn3.iconfinder.com/data/icons/food-and-drink-1/512/pasta_noodles-64.png",
    '中式料理':"https://emojipedia-us.s3.amazonaws.com/thumbs/160/microsoft/106/large-red-circle_1f534.png",
    '主題特色餐廳':"https://cdn4.iconfinder.com/data/icons/design-concept/193/cc30-48.png",
    '亞洲料理':"http://icons.iconarchive.com/icons/icons8/ios7/48/Food-Bento-icon.png",
    '其他美食':"http://icons.iconarchive.com/icons/webalys/kameleon.pics/48/Food-Dome-icon.png",
    '冰品、飲料、甜湯':"http://icons.iconarchive.com/icons/icons8/ios7/48/Food-Coctail-icon.png",
    '咖啡、簡餐、茶':"http://icons.iconarchive.com/icons/babasse/old-school/48/coffee-icon.png",
    '小吃':"http://icons.iconarchive.com/icons/icons8/windows-8/48/Food-Spaghetti-icon.png",
    '日式料理':"http://icons.iconarchive.com/icons/jamespeng/cuisine/48/Pork-Chop-Set-icon.png",
    '早餐':"http://icons.iconarchive.com/icons/icons8/windows-8/48/Food-Doughnut-icon.png",
    '烘焙、甜點、零食':"http://icons.iconarchive.com/icons/icons8/ios7/48/Food-Cupcake-icon.png",
    '燒烤類':"http://icons.iconarchive.com/icons/icons8/ios7/48/Food-Lamb-Rack-icon.png",
    '異國料理':"http://icons.iconarchive.com/icons/aha-soft/desktop-buffet/48/Steak-icon.png",
    '素食':"http://icons.iconarchive.com/icons/icons8/ios7/48/Food-Carrot-icon.png",
    '速食料理':"https://cdn4.iconfinder.com/data/icons/REALVISTA/food/png/48/french_fries.png",
    '鍋類':"http://icons.iconarchive.com/icons/icons8/ios7/48/Food-Cooking-Pot-icon.png",
    '711':'/static/clustImg1/icon/711.png',
    'family':'/static/clustImg1/icon/familyMart.png',
    'watsons':'/static/clustImg1/icon/watsons.png',
    'carrefour':'/static/clustImg1/icon/carrefour.png',
    'pxmart':'/static/clustImg1/icon/pxmart.png',
    'Tstore':'/static/clustImg1/icon/Tstore.png',
    'clinic':'/static/clustImg1/icon/clinic.png'
};

var imagesWow={
    'CooK BEEF!': '/static/clustImg1/icon/CooK BEEF!.png',
    'hot 7': '/static/clustImg1/icon/hot 7.png',
    'ita義塔': '/static/clustImg1/icon/ita義塔.png',
    '乍牛': '/static/clustImg1/icon/乍牛.png',
    '原燒': '/static/clustImg1/icon/原燒.png',
    '品田牧場': '/static/clustImg1/icon/品田牧場.png',
    '夏慕尼': '/static/clustImg1/icon/夏慕尼.png',
    '曼咖啡': '/static/clustImg1/icon/曼咖啡.png',
    '沐越': '/static/clustImg1/icon/沐越.png',
    '王品': '/static/clustImg1/icon/王品.png',
    '石二鍋': '/static/clustImg1/icon/石二鍋.png',
    '聚': '/static/clustImg1/icon/聚.png',
    '舒果': '/static/clustImg1/icon/舒果.png',
    '莆田': '/static/clustImg1/icon/莆田.png',
    '藝奇': '/static/clustImg1/icon/藝奇.png',
    '陶板屋': '/static/clustImg1/icon/陶板屋.png',
    '青花驕': '/static/clustImg1/icon/青花驕.png',
    '麻佬大': '/static/clustImg1/icon/麻佬大.png',
    'ＴＡＳＴｙ': '/static/clustImg1/icon/ＴＡＳＴｙ.png'
 }

mcImage={'mcdon':'/static/clustImg1/icon/mcdonalds.png',
         'star':'/static/clustImg1/icon/starbucks.png',
         'ken':'/static/clustImg1/icon/ken.png',
         'dabu':'/static/clustImg1/icon/dabu.png',
         'other':'/static/clustImg1/icon/other.png',
         'wa':'/static/clustImg1/icon/wa.png',
         'dep':'/static/clustImg1/icon/department.png',
         'house':'/static/clustImg1/icon/house.png',
         "A":'/static/clustImg1/icon/A.png',
         "B":'/static/clustImg1/icon/B.png',
         "C":'/static/clustImg1/icon/C.png'
         }


var cityData={"台北市" : {"中正區":"100","大同區":"103","中山區":"104","松山區":"105","大安區":"106","萬華區":"108","信義區":"110","士林區":"111","北投區":"112","內湖區":"114","南港區":"115","文山區":"116"},
"新北市" : {"萬里區":"207","金山區":"208","板橋區":"220","汐止區":"221","深坑區":"222","石碇區":"223","瑞芳區":"224","平溪區":"226","雙溪區":"227","貢寮區":"228","新店區":"231","坪林區":"232","烏來區":"233","永和區":"234","中和區":"235","土城區":"236","三峽區":"237","樹林區":"238","鶯歌區":"239","三重區":"241","新莊區":"242","泰山區":"243","林口區":"244","蘆洲區":"247","五股區":"248","八里區":"249","淡水區":"251","三芝區":"252","石門區":"253"},
"基隆市" : {"仁愛區":"200","信義區":"201","中正區":"202","中山區":"203","安樂區":"204","暖暖區":"205","七堵區":"206"},
"宜蘭縣" : {"宜蘭市":"260","頭城鎮":"261","礁溪鄉":"262","壯圍鄉":"263","員山鄉":"264","羅東鎮":"265","三星鄉":"266","大同鄉":"267","五結鄉":"268","冬山鄉":"269","蘇澳鎮":"270","南澳鄉":"272"},
"新竹市" : {"東區":"300", "北區":"300", "香山區":"300"},
"新竹縣": {"湖口鄉":"303","新豐鄉":"304","新埔鎮":"305","關西鎮":"306","芎林鄉":"307","寶山鄉":"308","竹東鎮":"310","五峰鄉":"311","橫山鄉":"312","尖石鄉":"313","北埔鄉":"314","峨眉鄉":"315"},
"桃園市" : {"中壢區":"320","平鎮區":"324","龍潭區":"325","楊梅區":"326","新屋區":"327","觀音區":"328","桃園區":"330","龜山區":"333","八德區":"334","大溪區":"335","復興區":"336","大園區":"337","蘆竹區":"338"},
"苗栗縣": {"竹南鎮":"350","頭份鎮":"351","三灣鄉":"352","南庄鄉":"353","獅潭鄉":"354","後龍鎮":"356","通霄鎮":"357","苑裡鎮":"358","苗栗市":"360","造橋鄉":"361","頭屋鄉":"362","公館鄉":"363","大湖鄉":"364","泰安鄉":"365","銅鑼鄉":"366","三義鄉":"367","西湖鄉":"368","卓蘭鎮":"369"},
"台中市" : {"中　區":"400","東　區":"401","南　區":"402","西　區":"403","北　區":"404","北屯區":"406","西屯區":"407","南屯區":"408","太平區":"411","大里區":"412","霧峰區":"413","烏日區":"414","豐原區":"420","后里區":"421","石岡區":"422","東勢區":"423","和平區":"424","新社區":"426","潭子區":"427","大雅區":"428","神岡區":"429","大肚區":"432","沙鹿區":"433","龍井區":"434","梧棲區":"435","清水區":"436","大甲區":"437","外埔區":"438","大安區":"439"},
"彰化縣" : {"彰化市":"500","芬園鄉":"502","花壇鄉":"503","秀水鄉":"504","鹿港鎮":"505","福興鄉":"506","線西鄉":"507","和美鎮":"508","伸港鄉":"509","員林鎮":"510","社頭鄉":"511","永靖鄉":"512","埔心鄉":"513","溪湖鎮":"514","大村鄉":"515","埔鹽鄉":"516","田中鎮":"520","北斗鎮":"521","田尾鄉":"522","埤頭鄉":"523","溪州鄉":"524","竹塘鄉":"525","二林鎮":"526","大城鄉":"527","芳苑鄉":"528","二水鄉":"530"},
"南投縣" : {"南投市":"540","中寮鄉":"541","草屯鎮":"542","國姓鄉":"544","埔里鎮":"545","仁愛鄉":"546","名間鄉":"551","集集鎮":"552","水里鄉":"553","魚池鄉":"555","信義鄉":"556","竹山鎮":"557","鹿谷鄉":"558"},
"雲林縣" : {"斗南鎮":"630","大埤鄉":"631","虎尾鎮":"632","土庫鎮":"633","褒忠鄉":"634","東勢鄉":"635","台西鄉":"636","崙背鄉":"637","麥寮鄉":"638","斗六市":"640","林內鄉":"643","古坑鄉":"646","莿桐鄉":"647","西螺鎮":"648","二崙鄉":"649","北港鎮":"651","水林鄉":"652","口湖鄉":"653","四湖鄉":"654","元長鄉":"655"},
"嘉義市" : {"東區":"600", "西區":"600"},
"嘉義縣" : {"番路鄉":"602","梅山鄉":"603","竹崎鄉":"604","阿里山":"605","中埔鄉":"606","大埔鄉":"607","水上鄉":"608","鹿草鄉":"611","太保市":"612","朴子市":"613","東石鄉":"614","六腳鄉":"615","新港鄉":"616","民雄鄉":"621","大林鎮":"622","溪口鄉":"623","義竹鄉":"624","布袋鎮":"625"},
"台南市" : {"永康區":"710","歸仁區":"711","新化區":"712","左鎮區":"713","玉井區":"714","楠西區":"715","南化區":"716","仁德區":"717","關廟區":"718","龍崎區":"719","官田區":"720","麻豆區":"721","佳里區":"722","西港區":"723","七股區":"724","將軍區":"725","學甲區":"726","北門區":"727","新營區":"730","後壁區":"731","白河區":"732","東山區":"733","六甲區":"734","下營區":"735","柳營區":"736","鹽水區":"737","善化區":"741","大內區":"742","山上區":"743","新市區":"744","安定區":"745"},
"高雄市" : {"新興區":"800","前金區":"801","苓雅區":"802","鹽埕區":"803","鼓山區":"804","旗津區":"805","前鎮區":"806","三民區":"807","楠梓區":"811","小港區":"812","左營區":"813","仁武區":"814","大社區":"815","岡山區":"820","路竹區":"821","阿蓮區":"822","田寮區":"823","燕巢區":"824","橋頭區":"825","梓官區":"826","彌陀區":"827","永安區":"828","湖內區":"829","鳳山區":"830","大寮區":"831","林園區":"832","鳥松區":"833","大樹區":"840","旗山區":"842","美濃區":"843","六龜區":"844","內門區":"845","杉林區":"846","甲仙區":"847","桃源區":"848","那瑪夏":"849","茂林區":"851","茄萣區":"852"},
"屏東縣" : {"屏東市":"900","三地門":"901","霧台鄉":"902","瑪家鄉":"903","九如鄉":"904","里港鄉":"905","高樹鄉":"906","鹽埔鄉":"907","長治鄉":"908","麟洛鄉":"909","竹田鄉":"911","內埔鄉":"912","萬丹鄉":"913","潮州鎮":"920","泰武鄉":"921","來義鄉":"922","萬巒鄉":"923","崁頂鄉":"924","新埤鄉":"925","南州鄉":"926","林邊鄉":"927","東港鎮":"928","琉球鄉":"929","佳冬鄉":"931","新園鄉":"932","枋寮鄉":"940","枋山鄉":"941","春日鄉":"942","獅子鄉":"943","車城鄉":"944","牡丹鄉":"945","恆春鎮":"946","滿州鄉":"947"},
"台東縣" : {"台東市":"950","綠島鄉":"951","蘭嶼鄉":"952","延平鄉":"953","卑南鄉":"954","鹿野鄉":"955","關山鎮":"956","海端鄉":"957","池上鄉":"958","東河鄉":"959","成功鎮":"961","長濱鄉":"962","太麻里":"963","金峰鄉":"964","大武鄉":"965","達仁鄉":"966"},
"花蓮縣" : {"花蓮市":"970","新城鄉":"971","秀林鄉":"972","吉安鄉":"973","壽豐鄉":"974","鳳林鎮":"975","光復鄉":"976","豐濱鄉":"977","瑞穗鄉":"978","萬榮鄉":"979","玉里鎮":"981","卓溪鄉":"982","富里鄉":"983"},
"澎湖縣" : {"馬公市":"880","西嶼鄉":"881","望安鄉":"882","七美鄉":"883","白沙鄉":"884","湖西鄉":"885"},
"金門縣" : {"金沙鎮":"890","金湖鎮":"891","金寧鄉":"892","金城鎮":"893","烈嶼鄉":"894","烏坵鄉":"896"},
"連江縣" : {"南竿鄉":"209","北竿鄉":"210","莒光鄉":"211","東引鄉":"212"}};

//以上資料區!!!--------------------------------

//讀取網頁時同時跑的function
$(function(){
    sleep(100)
    dd1Bind();
    resize();
    initMap();
})

function showAllData(){
    area=35961.3
    summaryData['地點']="台灣"
    summaryData['範圍']="全"
    delcircle()
    RemoveOption("summarys")
    RemoveOption("locations")
    $('#locations').append($('<option>').text("全台灣"));
    if(!(nullIpeen==1)){
        $('#ipeenMark').click()
    }
    if(!(null104==1)){
        $('#104Mark').click()
    }
    if(!(null591==1)){
        $('#591Mark').click()
    }
    query2({})
}


//控制窗格大小用
$(window).on('resize', function(){
    $("#map").css('height', $(window).height()*0.92);
//    $(".queryType").css('height', $("#map").height());
//    $("#job").css('height', $(".queryType").height()*0.4);
//    $("#style").css('height', $(".queryType").height()*0.4);
//    $("#summary").css('height', $("#map").height()*0.3);
});
//控制窗格大小用
function resize(){
    $("#map").css('height', $(window).height()*0.92);
//    $(".queryType").css('height', $("#map").height());
//    $("#job").css('height', $(".queryType").height()*0.4);
//    $("#style").css('height', $(".queryType").height()*0.4);
//    $("#summary").css('height', $(window).height()*0.25);
//    $("#wowData").css('height',$("#wow").height()*1.3);
//    $("#floating-panel").css('height', $(window).height()*0.07);
//    $("#address").css('height', $("#floating-panel").height()*0.9);
}

//ajax的function
function ajaxfun(url,postdata,doWhat){
    $.ajax({
        type : "POST",  //使用POST方法
        url : url,
        data : postdata,
//        {centerlat:findcenter.lat(),centerlng:findcenter.lng(),radius:$("#radius").val(),bigadd:City},//給後端的資料
        success: function(data){
            doWhat(data)
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("some error " + String(errorThrown) + String(textStatus) + String(XMLHttpRequest.responseText));
        }  //debug用
    });
}

//由api用ajax撈資料，postdata填入post用的{k:v}資料
function query2(postdata){
    //先將原本已存在的資料刪除
    RemoveOption("style");
    RemoveOption('summarys')
    RemoveOption('job')
    cancelMarker()
    clearIpeenMarkers()
    LocationsIpeen=[]
    clearHrMarkers()
    LocationsHr=[]
    ///////////////////////////////////Ipeen
    ajaxfun("http://172.20.26.39:8000/api/ipeen",postdata,doIpeen)
    /////////////////////////////////////2Hr104
    ajaxfun("http://172.20.26.39:8000/api/hr104",postdata,do104)
    /////////////////////////////////////3Cost
    ajaxfun("http://172.20.26.39:8000/api/cost",postdata,doCost)
    /////////////////////////////////////4Human
    ajaxfun("http://172.20.26.39:8000/api/human",postdata,doHuman)
    //////////////////////////////////////////////////////bus
    ajaxfun("http://172.20.26.39:8000/api/bus",postdata,doBus)
    ///////////////////////////////////////////////////////conStore
    ajaxfun("http://172.20.26.39:8000/api/store",postdata,doStore)
    ///////////////////////////////////////////////////////watsons
    ajaxfun("http://172.20.26.39:8000/api/watsons",postdata,doWatsons)
    ///////////////////////////////////////////////////////carrefour
    ajaxfun("http://172.20.26.39:8000/api/carrefour",postdata,doCarrefour)
    ///////////////////////////////////////////////////////pxmart
    ajaxfun("http://172.20.26.39:8000/api/pxmart",postdata,doPxmart)
    ///////////////////////////////////////////////////////Tstore
    ajaxfun("http://172.20.26.39:8000/api/Tstore",postdata,doTstore)
    ///////////////////////////////////////////////////////clinic
    ajaxfun("http://172.20.26.39:8000/api/clinic",postdata,doClinic)
    ///////////////////////////////////////////////////////591
    ajaxfun("http://172.20.26.39:8000/api/info591",postdata,do591)
}

//////////////////////////各種用ajax取得資料後要做的事
function doIpeen(data){
    IpeenRawData=data;
    for(var i=0;i<data.length;i++){
        var dien={}
        dien['content']='<strong>'+data[i]['name'].replace("'","").replace(";","").replace("{","")+"</strong><br>"
                                                 +data[i]['address'].replace("'","").replace(";","").replace("{","")
                                                 +"<br>電話:"+String(data[i]['tele'])+
                                                 "<br>花費:"+String(data[i]['averagecost'])+
                                                 "<br>人氣(點閱):"+String(data[i]['viewcount'])+
                                                 "<br>評論數:"+String(data[i]['Ncomment'])+
                                                 "<br>類型:"+data[i]['bigstyle']+"-"+data[i]['smallstyle']+
                                                 '<br><a href="http://www.ipeen.com.tw/shop/'+String(data[i]['id'])+'" target="_blank">愛評連結</a>';
        dien['style']=data[i]['bigstyle'].replace("'","").replace(";","").replace("{","")+"-"+data[i]['smallstyle'].replace("'","").replace(";","").replace("{","");
//                dien['style']=data[i]['bigstyle'].replace("'","").replace(";","").replace("{","");
//                dien['style']=data[i]['smallstyle'].replace("'","").replace(";","").replace("{","");
        dien['smallstyle']=data[i]['smallstyle'].replace("'","").replace(";","").replace("{","");
        dien['averageCost']=data[i]['averagecost'];
        dien['bigArea']=data[i]['bigadd'].replace("'","").replace(";","").replace("{","");
        dien['smallArea']=data[i]['smalladd'].replace("'","").replace(";","").replace("{","");
        dien['label']=data[i]['name'].replace("'","").replace(";","").replace("{","");
        dien['lat']=data[i]['lat'];
        dien['lng']=data[i]['lng'];
        LocationsIpeen.push(dien);
    }
    console.log(LocationsIpeen)
    smallStyleCount=getObjCount(LocationsIpeen,'style')
    sortSmallStyle = [];
    for (var vehicle in smallStyleCount) {
        sortSmallStyle.push([vehicle, smallStyleCount[vehicle]]);
    }
    sortSmallStyle.sort(function(a, b) {
        return b[1] - a[1];
    });
//                    RemoveOption("style");
    ipeenStyleAvg= getObjSummary(LocationsIpeen,'style','averageCost');
//            console.log(ipeenStyleAvg)
    sortSmallStyle.forEach(function(smallStyle){
//                console.log(smallStyle[0])
        try{
            $('#style').append($('<option>').text(smallStyle[0]+"-"+ipeenStyleAvg[smallStyle[0]]['avgSalary']+"("+smallStyle[1]+")").attr('value',smallStyle[0]));
        }catch(err){
            console.log(err)
        }
    });
    $('#summarys').append($('<option>').text("最多品類 :"+sortSmallStyle[0][0]));
    summaryData['最多品類']=sortSmallStyle[0][0]
//                    $('#style').multiselect();

    if(nullIpeen==0){
        var locationsIpeen = LocationsIpeen;
        ipeenMarkPaint(locationsIpeen)
    }
}



function exportAllIpeen() {
    ajaxfun("http://172.20.26.39:8000/api/ipeen",{},doIpeenAll)
}
function doIpeenAll(data){
    var IpeenAllData=data;
    alasql("SELECT name[店名],tele[電話],bigadd[縣市],smalladd[區鄉鎮],address[詳細地址],lat[緯度],lng[經度],bigstyle[大分類],smallstyle[小分類],averagecost[平均消費],collecount[蒐藏數],Ncomment[評論數],viewcount[瀏覽數],reviewdate[更新日期],url[愛評網連結] INTO XLSX('"+"all-Ipeen.xlsx',{headers:true}) FROM ? ",[IpeenAllData]);
}

function exportAll104() {
    ajaxfun("http://172.20.26.39:8000/api/hr104",{},do104All)
}
function do104All(data){
    var Hr104AllData=data;
    alasql("SELECT JOBCAT_DESCRIPT[職務種類],JOB[工作內容簡述],PRODUCT[產品],NAME[公司名稱],bigadd[縣市],smalladd[區鄉鎮],JOB_ADDRESS[詳細地址],lat[緯度],lng[經度],SAL_MONTH_HIGH[薪資(頂)],SAL_MONTH_LOW[薪資(底)],APPEAR_DATE[更新時間],bigstyle[預測餐廳類型] INTO XLSX('"+"all-104.xlsx',{headers:true}) FROM ? ",[Hr104AllData]);

}



function do104(data){
    HrRawData=data;
    console.log(data)
    for(var i=0;i<data.length;i++){
        var dien={}
        dien['content']='<strong>'+data[i]['NAME'].replace("'","").replace(";","").replace("{","")+
                                            "</strong><br>"+data[i]['JOB'].replace("'","").replace(";","").replace("{","")+
                                            "<br>薪資"+String(data[i]['SAL_MONTH_LOW'])+"-"+String(data[i]['SAL_MONTH_HIGH']);
        dien['style']=data[i]['JOBCAT_DESCRIPT'].replace("'","").replace(";","").replace("{","");
        dien['bigArea']=data[i]['bigadd'].replace("'","").replace(";","").replace("{","");
        dien['smallArea']=data[i]['smalladd'].replace("'","").replace(";","").replace("{","");
        dien['salary']=Math.round((data[i]['SAL_MONTH_LOW']*(2/3)+data[i]['SAL_MONTH_HIGH']*(1/3)));
        dien['label']=data[i]['NAME'].replace("'","").replace(";","").replace("{","");
        dien['foodstyle']=data[i]['bigstyle'].replace("'","").replace(";","").replace("{","");
        dien['lat']=data[i]['lat'];
        dien['lng']=data[i]['lng'];
        LocationsHr.push(dien);
    }
//    console.log(LocationsHr)
    $('#summarys').append($('<option>').text("餐飲業徵才筆數 :"+LocationsHr.length));
    $('#summarys').append($('<option>').text("餐飲業平均薪資 :"+Math.round(getObjAvg(LocationsHr,'salary'))));
    avgSalary=getObjSummary(LocationsHr,'style','salary')

    summaryData['餐飲業徵才筆數']=LocationsHr.length
    summaryData['餐飲業平均薪資']=Math.round(getObjAvg(LocationsHr,'salary'))

    for(a in avgSalary){
        $('#job').append($('<option>').text(a+"-"+avgSalary[a]['avgSalary']+"("+avgSalary[a]['count']+")").attr('value',a));
    }
    if(null104==0){
        var locationsHr = LocationsHr;
        hrMarkPaint(locationsHr)
    }
}
function doCost(data){
    avgCost=getObjAvg(data,"weight")
    console.log("餐飲消費力:"+Math.round(avgCost))
    $('#summarys').append($('<option>').text("消費力:"+Math.round(avgCost)));
    summaryData['消費力']=Math.round(avgCost)
    if(area/data.length>5){
        $('#summarys').append($('<option>').text("消費力筆數僅:"+data.length+"，會高估"));
        summaryData['comment']="消費力筆數僅:"+data.length+"，會高估"
    }
}
function doHuman(data){
    avgHuman=getObjSum(data,"weight")
    console.log("總人口數(刻度為區|鄉|鎮)"+avgHuman)
    $('#summarys').append($('<option>').text("人口數 :"+avgHuman));
    summaryData['人口數']=avgHuman
}
function doBus(data){
    console.log(data)
    nbus=data.length
    console.log("公車站數:"+nbus)
    $('#summarys').append($('<option>').text("公車站數 :"+nbus));
    summaryData['公車站數']=nbus
}
function doStore(data){
    console.log(data)
    nstore=data.length
    $('#summarys').append($('<option>').text("便利店數 :"+nstore));
    summaryData['便利店數']=nstore
    LocationsStore=data
}
function do591(data){
    console.log(data)
    n591=data.length
    Locations591=data
}

function doWatsons(data){
    console.log(data)
    LocationsWatsons=data
}

function doCarrefour(data){
    console.log(data)
    LocationsCarrefour=data
}
function doTstore(data){
    console.log(data)
    LocationsTstore=data
}

function doPxmart(data){
    console.log(data)
    LocationsPxmart=data
}

function doClinic(data){
    console.log(data)
    LocationsClinic=data
}

//縣市下拉選單
function findBigCity(){
    area=30;
    RemoveOption('locations')
    $('#locations').append($('<option>').text($('#bigCity').val()));
    summaryData={}
    summaryData['地點']=$('#bigCity').val();
    summaryData['範圍']=""
    query2({bigadd: $('#bigCity').val()})
    changeCenter()
    if($('#bigCity').val()==""){
        map.setCenter({"lat":23.7142957284625,"lng":121.10338465868324})
        map.setZoom(8)
    }else{
        map.setZoom(11)
    }
}
//區下拉選單
function findSmallCity(){
    area=30;
    RemoveOption('locations')
//    delpoint()
    $('#locations').append($('<option>').text($('#bigCity').val()));
    $('#locations').append($('<option>').text($('#smallCity').val()));
    summaryData={}
    summaryData['地點']=$('#bigCity').val()+$('#smallCity').val();
    summaryData['範圍']=""
    query2({bigadd: $('#bigCity').val(), smalladd: $('#smallCity').val()})
    changeCenter()
    if($('#smallCity').val()==""){
        map.setZoom(11)
    }else{
        map.setZoom(14)
    }
}

//改變座標 在改變縣市區下拉選單時啟動
function changeCenter(){
    var geocoder = new google.maps.Geocoder();
    var address = document.getElementById('address').value;
    geocoder.geocode({'address': $('#bigCity').val()+$('#smallCity').val()}, function(results, status) {
        if (status == 'OK') {
            center=results[0].geometry.location;
            center={lat:center.lat(),lng:center.lng()}
            map.setCenter(center);
        } else {
            console.log('aaa')
        }
    });
}

//nullIpeen 0顯示 1不顯示-愛評網的資料
var nullIpeen=1;
function toggleIpeenMarker(){
    //Locations沒東西的話
    transImgSize(imagesUrl,15);
    if (nullIpeen==1){
        nullIpeen=0;
        document.getElementById('ipeenMark').style.color='red'
        var locationsIpeen = LocationsIpeen;
        ipeenMarkPaint(locationsIpeen)
    }else{
        nullIpeen=1;
        document.getElementById('ipeenMark').style.color='black'
        clearIpeenMarkers()
    }
}
//畫ipeen的資料點
function ipeenMarkPaint(locationsIpeen){
    images=transImgSize(imagesUrl,15)
    var image=images;
    var infowindow = new google.maps.InfoWindow({});
    markerIpeens = [];
    locationsIpeen.forEach(function(location) {
        var markerIpeen = new google.maps.Marker({
            position: new google.maps.LatLng(location.lat, location.lng),
//            label: location.label,
//            icon: images[location.style],
            icon: images["中式料理"],
        });
        markerIpeen.addListener('click', function() {
            infowindow.setContent(location.content)
            infowindow.open(map, markerIpeen);
        });
        markerIpeens.push(markerIpeen);
    });

    markerClusterIpeen = new MarkerClusterer(
        map=map,
        opt_markers=markerIpeens,
        opt_options=markerClusterIpeenOptions
    );
}
//清除資料點(Ipeen)
function clearIpeenMarkers(){
    for(var ind=0;ind<markerIpeens.length;ind++){
        markerIpeens[ind].setMap(null);
    }
    markerClusterIpeen.clearMarkers()
}
//同上104
var null104=1;
function toggle104Marker(){
    //Locations2沒東西的話
    if (null104==1){
        null104=0;
        document.getElementById('104Mark').style.color='red'
        var locationsHr = LocationsHr;
        hrMarkPaint(locationsHr)
    }else{
        null104=1;
        document.getElementById('104Mark').style.color='black'
        clearHrMarkers()
    }
}
//畫104的資料點
function hrMarkPaint(locationsHr){
    var imageJob = {
      url:"https://cdn2.iconfinder.com/data/icons/sales-and-online-shop-filled-line/512/sales_online_shop_pick_box-48.png",//google內建icon
      size: new google.maps.Size(20, 20),
      origin: new google.maps.Point(0, 0),
      anchor: new google.maps.Point(10, 10),
      scaledSize: new google.maps.Size(20, 20)
    };
    var image2=imageJob;
    var infowindow2 = new google.maps.InfoWindow({});
    markersHr = [];
    locationsHr.forEach(function(location) {
        var markerHr = new google.maps.Marker({
            position: new google.maps.LatLng(location.lat, location.lng),
            icon: image2,
        });
        markerHr.addListener('click', function() {
            infowindow2.setContent(location.content)
            infowindow2.open(map, markerHr);
        });
        markersHr.push(markerHr);
    });
    markerClusterHr = new MarkerClusterer(
        map=map,
        opt_markers=markersHr,
        opt_options=markerClusterHrOptions
    );
}
//清除資料點(104)
function clearHrMarkers(){
    for(var ind=0;ind<markersHr.length;ind++){
	    markersHr[ind].setMap(null);
    }
    markerClusterHr.clearMarkers()
}
//同上591
var null591=1
function paint591(){
    if(null591==1){
        locations591=Locations591
        null591=0
        document.getElementById('591Mark').style.color='red'
        store591Paint()
    }else{
        null591=1
        document.getElementById('591Mark').style.color='black'
        clearMarkers(markers591)
    }
}
markers591=[]
function store591Paint(){
    images=transImgSize(mcImage,15)
    var image=images;
    var infowindow = new google.maps.InfoWindow({});
    marker591s = [];

    locations591.forEach(function(location) {
        var marker591 = new google.maps.Marker({
            position: new google.maps.LatLng(location.lat, location.lng),
            icon: image['house'],
            map:map
        });
        marker591.addListener('click', function() {
                    infowindow.setContent("坪數："+location.square+
                    "<br>價格："+location.price+
                    "<br>每坪價格："+Math.round(location.price/location.square)+
                    "<br>地址："+location.address+
                    '<br>樓層：'+location.totfloor+
                    "<br>種類："+location.style+
                    '<br><a href="'+location.phone+'" target="_blank">電話連結</a> '+
                    '<br><a href="'+location.url+'" target="_blank">591連結</a> ')
                    infowindow.open(map, marker591);
                });
        markers591.push(marker591);
    });
}

//搜索-----------地址>經緯度>畫標記+移動到座標+query()
var center,x,y,add;
var bigAreaQuery=true;
function geocodeAddress(add) {
    $("#summary").css('font-size', 14);
    delcircle();
    if(!(nullIpeen==1)){
        $('#ipeenMark').click()
    }
    if(!(null104==1)){
        $('#104Mark').click()
    }
    if(!(null591==1)){
        $('#591Mark').click()
    }
//    delpoint()
    summaryData={};
    var geocoder = new google.maps.Geocoder();
    var address = add;
    if(address==""){
        address=map.getCenter().lat()+","+map.getCenter().lng()
    }


    geocoder.geocode({'address': address}, function(results, status) {
        if (status == 'OK') {
//            //得到完整地址
            var add=results[0].formatted_address;
//            //取得縣市的正規表達式
            var reCity = new RegExp("(..[市|縣])", "gi")
//            //取得區市鎮鄉的正規表達式
//            var reCountry = new RegExp("[縣|市](..?.?[區|市|鎮|鄉])", "gi")
            var City=reCity.exec(add)[0].replace("臺","台")
//            //座標移動、畫marker
            RemoveOption('locations')
            $('#locations').append($('<option>').text(add));
            $('#locations').append($('<option>').text("周圍"+$("#radius").val()+"公尺"));
            summaryData['地點']=add;
            summaryData['範圍']=$("#radius").val()+"公尺"
            area=Math.round(parseInt($("#radius").val())*parseInt($("#radius").val())*Math.PI/1000000)

            var findcenter=results[0].geometry.location;
            findcenter2={lat:findcenter.lat(),lng:findcenter.lng()}
            query2({centerlat:findcenter.lat(),centerlng:findcenter.lng(),radius:$("#radius").val(),bigadd:City})

            $('#summarys').append($('<option>').text("區域範圍"+area+"平方公里"));
            markerControl={
                position: new google.maps.LatLng(findcenter2),
                label: add,
                icon: "/static/clustImg1/goal.png",
                map:map
            }

            var findmarker= new google.maps.Marker(markerControl);
            map.setZoom(15);
            map.setCenter(findcenter2);
            circles.push(findmarker)

            var circle = new google.maps.Circle({
                map: map,
                radius: parseInt($("#radius").val()),    // metres
                fillColor: '#fccccc'
            });
            circle.bindTo('center', findmarker, 'position');
            circles.push(circle)
//            getTransitInfo("transit_station")
        } else {
            alert('google找不到該位置');
        }
    });
}
//0129------------------------------------------------------------------
//計算某個obj的某key的value平均值
function getObjAvg(obj,key){
	sum=0;
	no=0
    for(var i=0;i<obj.length;i++){
        if(obj[i][key]){
            sum+=obj[i][key];
        }else{
            no+=1;
        }
    }
    return sum/(obj.length-no)
}
//計算某個obj的某key的value加總
function getObjSum(obj,key){
	sum=0;
    for(var i=0;i<obj.length;i++){
        sum+=obj[i][key];
    }
    return sum
}
//計算某個obj的某key的value出現次數
function getObjCount(obj,key){
    styleCount={};
    for(var ipN=0;ipN<obj.length;ipN++){
        if(!(obj[ipN][key] in styleCount)){
            styleCount[obj[ipN][key]]=0;
        }
        styleCount[obj[ipN][key]]++;
    }
    return styleCount
}
//找到某key內的另一個key的綜合分析直 (如:每個職業的個數、平均薪資)
function getObjSummary(obj,Skey,Vkey){
    summary={};
    for(var d=0;d<obj.length;d++){
        if(obj[d][Vkey]>0){
            if(!(obj[d][Skey] in summary)){
                summary[obj[d][Skey]]={};
                summary[obj[d][Skey]]['count']=0;
                summary[obj[d][Skey]]['sumSalary']=0;
            }
            summary[obj[d][Skey]]['count']++;
            summary[obj[d][Skey]]['sumSalary']+=obj[d][Vkey];
        }
    }
    for(key in summary){
        summary[key]['avgSalary']=Math.round(summary[key]['sumSalary']/summary[key]['count']);
    }
    return summary
}


//if (openButton.includes(iconKey)){
//        markers.forEach(function(x){
//            if (x.icon.url.includes(iconKey)){
//                x.setMap(null)
//            }
//        })
//        openButton.pop(iconKey)
//    }else{
//        openButton.push(iconKey)
//        locationsInter=[]
//        for(var i=0;i<LocationsIpeen.length;i++){
//            if(LocationsIpeen[i]['content'].split("</strong>")[0].includes(nameInclude)){
//                locationsInter.push(LocationsIpeen[i])
//            }
//        }
//        console.log(locationsInter)
//        interMark(iconKey)
//    }



//畫store的資料點
var storeMap={'統一超商股份有限公司':"711","全家便利商店股份有限公司":"family"};
function PaintStore(storename){
    if (openButton.includes(storename)){
        document.getElementById(storename).style.color="white";
        markers.forEach(function(x){
            if (x.icon.url.includes(storeMap[storename])){
                x.setMap(null)
            }
        })
        openButton.pop(storename)
    }else{
        document.getElementById(storename).style.color="red";
        openButton.push(storename)
        locationsStore=[]
        for(var i=0;i<LocationsStore.length;i++){
                if(LocationsStore[i]['name']==storename){
                    locationsStore.push(LocationsStore[i])
                }
            }
        storeMarkPaint(storename)
    }
}
function storeMarkPaint(storename){
    images=transImgSize(imagesUrl,20)
    var image=images;
    var infowindow = new google.maps.InfoWindow({});
    imagekey=storeMap[storename];

    locationsStore.forEach(function(location) {
        var markerStore = new google.maps.Marker({
            position: new google.maps.LatLng(location.lat, location.lng),
//            label: location.label,
//            icon: images[location.style],
            icon: images[imagekey],
            map:map
        });
        markerStore.addListener('click', function() {
            infowindow.setContent(location.add)
            infowindow.open(map, markerStore);
        });
        markers.push(markerStore);
    });
}

function PaintMarkers(storeName,locationName){
    if (openButton.includes(storeName)){
        document.getElementById(storeName).style.color="white";
        markers.forEach(function(x){
            if (x.icon.url.includes(storeName)){
                x.setMap(null)
            }
        })
        openButton.pop(storeName)
    }else{
        document.getElementById(storeName).style.color="red";
        openButton.push(storeName)
        images=transImgSize(imagesUrl,30)
        var image=images;
        var infowindow = new google.maps.InfoWindow({});
        locationName.forEach(function(location) {
            var markerWatsons = new google.maps.Marker({
                position: new google.maps.LatLng(location.lat, location.lng),
    //            label: location.label,
    //            icon: images[location.style],
                icon: images[storeName],
                map:map
            });
            markerWatsons.addListener('click', function() {
                infowindow.setContent(location.name+"<br>"+location.address)
                infowindow.open(map, markerWatsons);
            });
            markers.push(markerWatsons);
        });
    }
}




//附近交通資訊，暫時不使用
//function nearMark(transitdata){
//    data=JSON.parse(transitdata)
////    map.setCenter(data['locate'])
//    var marker = new google.maps.Marker({
//        map: map,
//        position: data['locate'],
//    });
//    infowindow.setContent([
//    data['content']].join("<br />"));
//    infowindow.open(map, marker);
//    marker.addListener('click', function() {
//          infowindow.setContent([
//          data['content']].join("<br />"));
//          infowindow.open(map, marker);
//    });
//    markers.push(marker)
//}
//多選食物類別
function foodQuery(){
//     if(!(nullIpeen==0)){
//        $('#ipeenMark').click()
//     }
    nullIpeen=0
    document.getElementById('ipeenMark').style.color='red'
    clearIpeenMarkers()
    var querylist=$('#style').val()
    var locationsIpeen=[]
    if ($("#min").val()==""){
        var min=-20
    }else{
        var min=$("#min").val()
    }
    if ($("#max").val()==""){
        var max=5000000
    }else{
        var max=$("#max").val()
    }

    if($('#style').val().length==0){
        for(var i=0;i<LocationsIpeen.length;i++){
            if(LocationsIpeen[i]['averageCost']>=min & LocationsIpeen[i]['averageCost']<=max){
                locationsIpeen.push(LocationsIpeen[i])
            }
        }
    }else{
        for(var i=0;i<LocationsIpeen.length;i++){
            if(querylist.indexOf(LocationsIpeen[i]['style'])>-1 & LocationsIpeen[i]['averageCost']>=min & LocationsIpeen[i]['averageCost']<=max){
                locationsIpeen.push(LocationsIpeen[i])
            }
        }
    }
    console.log(locationsIpeen)
    ipeenMarkPaint(locationsIpeen)
}
//多選工作類別
function jobQuery(){
    null104=0
    document.getElementById('104Mark').style.color='red'
    clearHrMarkers()
    var querylist=$('#job').val()
    var locationsHr=[]
    if($('#job').val().length==0){
        locationsHr=LocationsHr
    }else{
        for(var i=0;i<LocationsHr.length;i++){
            if(querylist.indexOf(LocationsHr[i]['style'])>-1){
                locationsHr.push(LocationsHr[i])
            }
        }
    }
    hrMarkPaint(locationsHr)
}

//以下產生地圖--------------------------------------
//樣式json產生器 https://mapstyle.withgoogle.com/
var mapstylejson=[
  {
    "elementType": "labels.icon",
    "stylers": [
      {
        "visibility": "off"
      }
    ]
  },
  {
    "featureType": "administrative.land_parcel",
    "elementType": "labels",
    "stylers": [
      {
        "visibility": "off"
      }
    ]
  },
  {
    "featureType": "poi.attraction",
    "stylers": [
      {
        "visibility": "simplified"
      }
    ]
  },
  {
    "featureType": "poi.attraction",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "visibility": "off"
      }
    ]
  },
  {
    "featureType": "poi.business",
    "stylers": [
      {
        "visibility": "off"
      }
    ]
  },
  {
    "featureType": "poi.park",
    "stylers": [
      {
        "visibility": "simplified"
      }
    ]
  },
  {
    "featureType": "poi.park",
    "elementType": "labels.text",
    "stylers": [
      {
        "visibility": "off"
      }
    ]
  },
  {
    "featureType": "poi.school",
    "stylers": [
      {
        "visibility": "simplified"
      }
    ]
  },
  {
    "featureType": "poi.school",
    "elementType": "labels.icon",
    "stylers": [
      {
        "visibility": "simplified"
      }
    ]
  },
  {
    "featureType": "poi.school",
    "elementType": "labels.text",
    "stylers": [
      {
        "visibility": "off"
      }
    ]
  },
  {
    "featureType": "poi.sports_complex",
    "stylers": [
      {
        "visibility": "simplified"
      }
    ]
  },
  {
    "featureType": "poi.sports_complex",
    "elementType": "labels.text",
    "stylers": [
      {
        "visibility": "off"
      }
    ]
  },
  {
    "featureType": "road",
    "stylers": [
      {
        "visibility": "on"
      }
    ]
  },
  {
    "featureType": "road",
    "elementType": "geometry.fill",
    "stylers": [
      {
        "visibility": "on"
      }
    ]
  },
  {
    "featureType": "road",
    "elementType": "geometry.stroke",
    "stylers": [
      {
        "visibility": "on"
      }
    ]
  },
  {
    "featureType": "road",
    "elementType": "labels",
    "stylers": [
      {
        "visibility": "on"
      }
    ]
  },
  {
    "featureType": "road",
    "elementType": "labels.icon",
    "stylers": [
      {
        "visibility": "on"
      }
    ]
  },
  {
    "featureType": "road",
    "elementType": "labels.text",
    "stylers": [
      {
        "visibility": "off"
      }
    ]
  },
  {
    "featureType": "road",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "visibility": "on"
      }
    ]
  },
  {
    "featureType": "road",
    "elementType": "labels.text.stroke",
    "stylers": [
      {
        "visibility": "on"
      }
    ]
  },
  {
    "featureType": "road.arterial",
    "elementType": "labels",
    "stylers": [
      {
        "visibility": "simplified"
      }
    ]
  },
  {
    "featureType": "road.highway",
    "elementType": "labels",
    "stylers": [
      {
        "visibility": "simplified"
      }
    ]
  },
  {
    "featureType": "road.highway.controlled_access",
    "elementType": "labels",
    "stylers": [
      {
        "visibility": "simplified"
      }
    ]
  },
  {
    "featureType": "road.local",
    "stylers": [
      {
        "visibility": "on"
      }
    ]
  },
  {
    "featureType": "road.local",
    "elementType": "labels",
    "stylers": [
      {
        "visibility": "off"
      }
    ]
  },
  {
    "featureType": "transit.station",
    "elementType": "labels.icon",
    "stylers": [
      {
        "visibility": "simplified"
      }
    ]
  },
  {
    "featureType": "transit.station.bus",
    "elementType": "labels",
    "stylers": [
      {
        "saturation": -15
      }
    ]
  }
]
//寫在外面才能夠在外面函數變換 內皆為googleMap用的變數
var map,latcenter,lngcenter,trafficLayer,transitLayer,markers,markers2,
    markerClusterIpeen,markerClusterIpeenOptions,markerClusterHr,
    markerClusterHrOptions,heatmapCost,heatmapHuman,heatmapCost2,circle
var markerIpeens=[]
var markersHr=[]
var LocationsIpeen=[]
var IpeenRawData
var LocationsHr=[]
var HrRawData
var circles=[]
var summaryData={}
//很適合台灣大小的size
var zoomsize=8
//繪製google地圖
function initMap() {
    //台灣中心
    latcenter=23.4142957284625;
    lngcenter=121.10338465868324;

    //設定中心點(center)、地圖大小(zoom)、地圖類型(mapTypeId)、樣式(styles)、比例尺(scaleControl)
    var mapControl={
        zoom:zoomsize,
        center: new google.maps.LatLng(latcenter,lngcenter),
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        styles:mapstylejson,
        scaleControl:true,
    }

    //繪製地圖
    map = new google.maps.Map(
        document.getElementById('map'),
        mapControl
    );

    //設定群集標記的參數(ipeen)
    markerClusterIpeenOptions = {
        gridSize: 70,
        maxZoom: 13,
        imagePath:   'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m',
//        styles:clusterStyles
    };
    //設置標記群集(先不放任何標記 另外產生)
    markerClusterIpeen = new MarkerClusterer(map=map, opt_markers=[],opt_options=markerClusterIpeenOptions);

    //(Hr104)
    clusterStyles=[];
    for(j=1;j<6;j++){
        var img={url: "/static/clustImg1/size2/j"+j+".png",
                 height: 5+j*10,
                 width: 5+j*10,
                 textSize:7,
//                 textColor:'rgba(255, 255, 255, 0)'
                };
        clusterStyles.push(img);
    }

    markerClusterHrOptions = {
        gridSize: 70,
        maxZoom: 13,

//        imagePath:   'clustImg1/w',
        averageCenter: true,
        styles: clusterStyles,

    };
    markerClusterHr = new MarkerClusterer(map=map, opt_markers=[],opt_options=markerClusterHrOptions);

    //加入道路資訊
    trafficLayer = new google.maps.TrafficLayer();
    //加入交通資訊
    transitLayer = new google.maps.TransitLayer();

    //加入熱度圖 for 餐飲消費 (N/(Math.pow(2,(20-zoomsize)))表示該圖隨者地圖size而變更>這裡用作固定比例大小)
    heatmapCost = new google.maps.visualization.HeatmapLayer({
//        data: costDensity,
        radius:7000/(Math.pow(2,(20-zoomsize))),
//        map: map先不畫
    });

    //加入熱度圖 for 人口密度 gradient為調整顏色
    heatmapHuman = new google.maps.visualization.HeatmapLayer({
//        data: humanDensity,
        radius:6000/(Math.pow(2,(20-zoomsize))),
//        map: map,
        gradient:[
        'rgba(0, 255, 255, 0)',
        'rgba(0, 255, 255, 1)',
        'rgba(50, 191, 255, 1)',
        'rgba(100, 167, 255, 1)',
        'rgba(150, 113, 255, 1)',
        'rgba(200, 80, 255, 1)',
    ]
    });

    heatmapCost2 = new google.maps.visualization.HeatmapLayer({
//        data: costDensity,
        radius:8500/(Math.pow(2,(20-zoomsize))),
//        map: map先不畫
    });

    //固定heatmap的大小(每次地圖zoom變更就計算)
    google.maps.event.addListener(map, 'zoom_changed', function () {
        heatmapCost.setOptions({radius:getNewRadius(7000)});
    });
    google.maps.event.addListener(map, 'zoom_changed', function () {
        heatmapHuman.setOptions({radius:getNewRadius(6000)});
    });
    google.maps.event.addListener(map, 'zoom_changed', function () {
        heatmapCost2.setOptions({radius:getNewRadius(8500)});
    });
    function getNewRadius(N){
        var radius = (N)/(Math.pow(2,(20-map.getZoom())));
        return radius;
    }


/////////////////////////////////////////GeoJson
//    map.data.loadGeoJson('/static/geojson/TOWN_MOI_1070205.json')
//   // Color each letter gray. Change the color when the isColorful property
//        // is set to true.
//        map.data.setStyle(function(feature) {
//          var color = 'gray';
//          if (feature.getProperty('isColorful')) {
//            color = feature.getProperty('color');
//          }
//          return /** @type {google.maps.Data.StyleOptions} */({
//            fillColor: color,
//            strokeColor: color,
//            strokeWeight: 2
//          });
//        });
//
//        // When the user clicks, set 'isColorful', changing the color of the letters.
//        map.data.addListener('click', function(event) {
//          event.feature.setProperty('isColorful', true);
//        });
//
//        // When the user hovers, tempt them to click by outlining the letters.
//        // Call revertStyle() to remove all overrides. This will use the style rules
//        // defined in the function passed to setStyle()
//        map.data.addListener('mouseover', function(event) {
//          map.data.revertStyle();
//          map.data.overrideStyle(event.feature, {strokeWeight: 8});
//        });
//
//        map.data.addListener('mouseout', function(event) {
//          map.data.revertStyle();
//        });

/////////////////////////////////////////



}
//以上產生地圖--------------------------------------


//將icon堆變成我喜歡的大小
function transImgSize(imagesUrls,size){
    var images={}
    for(var key in imagesUrls){
            n=1
            if(key=="A"){
                n=2.5
            }else if(key=="B"){
                n=2
            }else if(key=="C"){
                n=1.6
            }
            nsize=size*n
            var image={
                    url:imagesUrls[key],
                    size: new google.maps.Size(nsize, nsize),
                    origin: new google.maps.Point(0, 0),
                    anchor: new google.maps.Point(nsize/2, nsize/2),
                    scaledSize: new google.maps.Size(nsize, nsize)
            }
            images[key]=image;
    };
    return images
}

//以下操作地圖顯示--------------------------------------
//道路資訊
function toggletraffic() {
    trafficLayer.setMap(trafficLayer.getMap() ? null : map);
}
//交通資訊
function toggletransit() {
    transitLayer.setMap(transitLayer.getMap() ? null : map);
}
//熱度圖 for 餐飲消費
var costDensity=[];
//撈消費力資料時要做的事
function doCostAll(data){
    for(var i=0;i<data.length;i++){
        var location={}
        location['location']=new google.maps.LatLng(data[i]['lat'],data[i]['lng']);
        location['weight']=data[i]['weight'];
//                    location['add']=data[1]['add'];
        costDensity.push(location);
    }
    console.log(costDensity)
    heatmapCost.setData(costDensity)
    heatmapCost.setMap(heatmapCost.getMap() ? null : map);
}

function toggleHeatmapCost() {
    if(costDensity.length==0){
        document.getElementById('costHeat').style.color="red";
        ajaxfun("http://172.20.26.39:8000/api/cost",{},doCostAll)
    }else{
        document.getElementById('costHeat').style.color="black";
        if(heatmapCost.getMap()==null){
            document.getElementById('costHeat').style.color="red";
        }
        heatmapCost.setMap(heatmapCost.getMap() ? null : map);
    }
}

//熱度圖 for 人口密度
var humanDensity=[];
function doHumanAll(data){
    for(var i=0;i<data.length;i++){
        var location={}
        location['location']=new google.maps.LatLng(data[i]['lat'],data[i]['lng']);
        location['weight']=data[i]['weight'];
        humanDensity.push(location);
    }
    console.log(humanDensity)
    heatmapHuman.setData(humanDensity);
    heatmapHuman.setMap(heatmapHuman.getMap() ? null : map);
}
function toggleHeatmapHuman() {
    if(humanDensity.length==0){
        document.getElementById('humanHeat').style.color="red";
        ajaxfun("http://172.20.26.39:8000/api/human",{},doHumanAll)
    }else{
        document.getElementById('humanHeat').style.color="black";
        if(heatmapHuman.getMap()==null){
            document.getElementById('humanHeat').style.color="red";
        }
        heatmapHuman.setMap(heatmapHuman.getMap() ? null : map);
    }
}

//變更熱度圖透明度
function changeOpacity() {
    heatmapCost.set('opacity', heatmapCost.get('opacity') ? null : 0.4);
    heatmapHuman.set('opacity', heatmapHuman.get('opacity') ? null : 0.4);
    heatmapCost2.set('opacity', heatmapHuman.get('opacity') ? null : 0.4);
}
//以上操作地圖顯示--------------------------------------

//清除各類標記
//function delpoint(){
//    for(var i=0;i<markers.length;i++){
//        markers[i].setMap(null);
//    }
//}
//清除圓框
function delcircle(){
    for(var i=0;i<circles.length;i++){
        circles[i].setMap(null);
    }
}
//以下下拉式選單操作--------------------------------------
//縣市資料塞進下拉選單(進入網頁同時啟動)
function dd1Bind()
{
    var bigCitylist=Object.keys(cityData);
    $('#bigCity').append($('<option>').text('請選擇縣市').attr('value', ''));
    $.each(bigCitylist, function (i) {
        $('#bigCity').append($('<option>').text(bigCitylist[i]).attr('value', bigCitylist[i]));
    });
}

//區域下拉選單(變更縣市下拉選單時加入)
function dd2Bind(pkey)
{
//    delpoint()
    //先刪除前次加入的區域   (.replace(/\s+/g, "")為去除空白的方法)
    RemoveOption("smallCity");
    $('#smallCity').append($('<option>').text('全區').attr('value', ''));
    if (pkey!=""){
        var smallCitylist=Object.keys(cityData[pkey]);
        $.each(smallCitylist, function (i) {
            $('#smallCity').append($('<option>').text(smallCitylist[i].replace(/\s+/g, "")).attr('value', smallCitylist[i].replace(/\s+/g, "")));
        });
    }
    findBigCity()
    bigAreaQuery=true;
}

//選取新的縣市時，先刪除目前產生的區域list
function RemoveOption(selectid){
    var mySelect = document.getElementById(selectid);
    for (var i=mySelect.options.length-1; i>=0; i--){
        mySelect.remove(i);
    }
}
//0226try-------------------將資料變成excel下載
function exportIpeenData() {
    alasql("SELECT name[店名],tele[電話],bigadd[縣市],smalladd[區鄉鎮],address[詳細地址],lat[緯度],lng[經度],bigstyle[大分類],smallstyle[小分類],averagecost[平均消費],collecount[蒐藏數],Ncomment[評論數],viewcount[瀏覽數],url[愛評網連結] INTO XLSX('"+summaryData['地點']+summaryData['範圍']+"-Ipeen.xlsx',{headers:true}) FROM ? ",[IpeenRawData]);
}
function exportHrData() {
    alasql("SELECT JOBCAT_DESCRIPT[職務種類],JOB[工作內容簡述],PRODUCT[產品],NAME[公司名稱],bigadd[縣市],smalladd[區鄉鎮],JOB_ADDRESS[詳細地址],lat[緯度],lng[經度],SAL_MONTH_HIGH[薪資(頂)],SAL_MONTH_LOW[薪資(底)],APPEAR_DATE[更新時間],bigstyle[預測餐廳類型] INTO XLSX('"+summaryData['地點']+summaryData['範圍']+"-104.xlsx',{headers:true}) FROM ? ",[HrRawData]);
}
function exportSummaryData() {
    alasql("SELECT * INTO XLSX('"+summaryData['地點']+summaryData['範圍']+"-Summary.xlsx',{headers:false}) FROM ? ",[summaryData]);
}
function export591Data() {
    alasql("SELECT title[標題],seller[賣家],phone[電話],area[縣市],city[區鄉鎮],address[詳細地址],lat[緯度],lng[經度],style[類型],floor[層],price[價格],square[坪數],url[591連結] INTO XLSX('"+summaryData['地點']+summaryData['範圍']+"-591.xlsx',{headers:true}) FROM ? ",[Locations591]);
}




//睡眠(微秒)
function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}

var wowData;
var nullWow=1;
var paintData;

function getWowData(){
    if (nullWow==1){
        document.getElementById('wow').style.color="red"
        ajaxfun("http://172.20.26.39:8000/api/wow",{},doWow)
        nullWow=0
    }else{
        document.getElementById('wow').style.color="black"
        nullWow=1
        wowData=[]
        $('#wowData').empty();
        clearMarkers(markerWows)
    }
}
function doWow(datas){
    console.log(datas)
    $("#wowData").empty();
    wowData=datas
//              畫mark
    paintData=wowData
    wowMarkPaint(paintData)
//                累計
    wowBrandCount=getObjCount(wowData,'Called')
//                排序
    sortWowBrand = [];
    for (var vehicle in wowBrandCount) {
        sortWowBrand.push([vehicle, wowBrandCount[vehicle]]);
    }
    sortWowBrand.sort(function(a, b) {
        return b[1] - a[1];
    });
     $('#wowData').append($('<option>').text("王品店家全選").attr('value',""));
    sortWowBrand.forEach(function(Brand){
        $('#wowData').append($('<option>').text(Brand[0]+"("+Brand[1]+")").attr('value',Brand[0]));
    })
}

function wowQuery(){
    clearMarkers(markerWows)
    var queryBrand=$('#wowData').val()
    paintData=[]
    if (queryBrand==""){
        paintData=wowData
    }else{
        for(var i=0;i<wowData.length;i++){
            if(queryBrand==wowData[i]['Called']){
                paintData.push(wowData[i])
            }
        }
    }
    RemoveOption('summarys')
    RemoveOption('locations')
    $('#locations').append($('<option>').text(queryBrand));
    $('#summarys').append($('<option>').text("ADS:"+Math.round(getObjAvg(paintData,"avgDailyNet"))));
    $('#summarys').append($('<option>').text("ADGC:"+Math.round(getObjAvg(paintData,"avgDailyCustomer"))));
    $('#summarys').append($('<option>').text("均消:"+Math.round(getObjAvg(paintData,"avgDailyNet")/getObjAvg(paintData,"avgDailyCustomer"))));
//    $('#summarys').append($('<option>').text("日均淨額:"+Math.round(getObjAvg(paintData,"avgDailyNet"))));
    console.log(paintData)
    wowMarkPaint(paintData)
}

function cancelMarker(){
    var deStore=['全家便利商店股份有限公司','統一超商股份有限公司'];
    var deMarker=['watsons','pxmart','carrefour'];
    var deInter=['mcdon','ken','star','wa'];
    deStore.forEach(function(storename) {
        if (openButton.includes(storename)){
            document.getElementById(storename).style.color="white";
            markers.forEach(function(x){
                if (x.icon.url.includes(storeMap[storename])){
                    x.setMap(null)
                }
            })
            openButton.splice(openButton.indexOf(storename), 1);
        }
    })
    deMarker.forEach(function(storeName) {
        if (openButton.includes(storeName)){
            document.getElementById(storeName).style.color="white";
            markers.forEach(function(x){
                if (x.icon.url.includes(storeName)){
                    x.setMap(null)
                }
            })
            openButton.splice(openButton.indexOf(storeName), 1);
        }
    })
    deInter.forEach(function(iconKey) {
        if (openButton.includes(iconKey)){
        document.getElementById(iconKey).style.color="white";
        markers.forEach(function(x){
            if (x.icon.url.includes(iconKey)){
                x.setMap(null)
            }
        })
        openButton.splice(openButton.indexOf(iconKey), 1);
        }
    })
}





function wowMarkPaint(locationsWow){
    var images=transImgSize(imagesWow,40)
    var image=images;
    var infowindow = new google.maps.InfoWindow({});

    markerWows = [];
    locationsWow.forEach(function(location) {
        var markerWow = new google.maps.Marker({
            position: new google.maps.LatLng(location.lat, location.lng),
//            label: location.label,
//            icon: images[location.style],
            icon: images[location.Called],
            map:map
        });
        markerWow.addListener('click', function() {
//            map.setCenter({"lat":location.lat,"lng":location.lng})
//            map.setZoom(11)
            $("#summary").css('font-size', 14);
            if(!(nullIpeen==1)){
                $('#ipeenMark').click()
             }
            if(!(null104==1)){
                $('#104Mark').click()
            }


//            delpoint()
            delcircle();
            RemoveOption('locations')
            $('#locations').append($('<option>').text(location.Called+"-"+location.StoreName));
            $('#locations').append($('<option>').text("周圍"+$("#radius").val()+"公尺"));
            summaryData['地點']=location.Called+"-"+location.StoreName;
            summaryData['範圍']=$("#radius").val()+"公尺"
            infowindow.setContent(location.Called+"-"+location.StoreName+
                                    "<br>ADS : "+location.avgDailyNet+
                                    "<br>ADGC : "+location.avgDailyCustomer+
                                    "<br>均消 : "+Math.round(location.avgDailyNet/location.avgDailyCustomer))
//                                    "<br>日均客量 : "+location.avgDailyMeal)
            infowindow.open(map, markerWow);
            area=13
            query2({centerlat:location.lat,centerlng:location.lng,radius:$("#radius").val(),bigadd:location.bigadd})
            area=Math.round(parseInt($("#radius").val())*parseInt($("#radius").val())*Math.PI/1000000)
            $('#summarys').append($('<option>').text("區域範圍"+area+"平方公里"));
//            $('#summarys').append($('<option>').text("日均營收 : "+location.avgDailyNet));
//            $('#summarys').append($('<option>').text("日均顧客數 : "+location.avgDailyCustomer));
//            $('#summarys').append($('<option>').text("日均客量 : "+location.avgDailyMeal));
            summaryData['ADS']=location.avgDailyNet;
            summaryData['ADGC']=location.avgDailyCustomer;
//            summaryData['日均客量']=location.avgDailyMeal;

            var circle = new google.maps.Circle({
                map: map,
                radius: parseInt($("#radius").val()),    // metres
                fillColor: '#fccccc'
            });
            circle.bindTo('center', markerWow, 'position');
            circles.push(circle)
//
        });
        markerWows.push(markerWow);
    });
}

x="_id[店代碼],Called[事業處],StoreName[分店名],Address[地址],bigadd[縣市],smalladd[區鄉鎮市],Phone[電話],avgDailyNet[ADS(2年)],"+
"avgDailyCustomer[ADGC(all)],ADGC_holiday[ADGC(假日)],ADGC_weekday[ADGC(平日)],NsimCostDien[價格接近餐廳數(500M)],areaRadius_Analyze[分析範圍(公尺)],costPower_Analyze[周圍消費力],"+
"NcostData_Analyze[消費力資料筆數],Nhuman_Analyze[人口數],avgSalary_Analyze[平均薪資 (最低*2/3+最高*1/3)],Njob_Analyze[餐飲業工作筆數],"+
"avgCost_Analyze[餐廳均消],NbusStation_Analyze[公車站數],NconStore_Analyze[四大超商數],Nstar_Analyze[星巴克數],"+
"Nmc_Analyze[麥當勞數],Nken_Analyze[肯德基數],Nwa_Analyze[瓦城數],Nwatson_Analyze[屈臣氏數],Npxmart_Analyze[全聯數],Ncarrefour_Analyze[家樂福數],mostStyle_Analyze[該區最多品類]"
function exportWowData() {
//    if(nullWow==1){
//        $("#wow").click()
//    }
//    sleep(1000)
    alasql("SELECT " +x+" INTO XLSX('"+$("#wowData").val()+"_wow_data.xlsx',{headers:true}) FROM ? ",[paintData])
}

openButton=[]
function queryInter(nameInclude,iconKey='other'){
    if (openButton.includes(iconKey)){
        document.getElementById(iconKey).style.color="white";
        markers.forEach(function(x){
            if (x.icon.url.includes(iconKey)){
                x.setMap(null)
            }
        })
        openButton.pop(iconKey)
    }else{
        document.getElementById(iconKey).style.color="red";
        openButton.push(iconKey)
        locationsInter=[]
        for(var i=0;i<LocationsIpeen.length;i++){
            if(LocationsIpeen[i]['content'].split("</strong>")[0].includes(nameInclude)){
                locationsInter.push(LocationsIpeen[i])
            }
        }
        console.log(locationsInter)
        interMark(iconKey)
    }
}

var markerInters = [];
function interMark(iconKey){

    images=transImgSize(mcImage,30)
    var image=images;
    var infowindow = new google.maps.InfoWindow({});
    locationsInter.forEach(function(location) {
        var markerInter = new google.maps.Marker({
            position: new google.maps.LatLng(location.lat, location.lng),
//            label: location.label,
//            icon: images[location.style],
            icon: image[iconKey],
            map:map
        });
        markerInter.addListener('click', function() {
            infowindow.setContent(location.content)
            infowindow.open(map, markerInter);
        });
//        markerInters.push(markerInter);
        markers.push(markerInter);
    });
}

function clearMarkers(markerList=markerInters){
    for(var ind=0;ind<markerList.length;ind++){
        markerList[ind].setMap(null);
    }
}

function PaintDepartmentStore(){
    ajaxfun("http://172.20.26.39:8000/api/push",{},doPush)
}

function doPush(data){
    console.log(data)
    nstore=data.length
    LocationsDepartmentStore=data
    images=transImgSize(mcImage,30)
    var image=images;
    var infowindow = new google.maps.InfoWindow({});
    markerStores = [];
    LocationsDepartmentStore.forEach(function(location) {
        var markerStore = new google.maps.Marker({
            position: new google.maps.LatLng(location.lat, location.lng),
            icon: image['dep'],
            map:map
        });
        markerStore.addListener('click', function() {
            infowindow.setContent(location._id+"<br>"+location.performance)
            infowindow.open(map, markerStore);
        });
        markers.push(markerStore);
    });
}

markersTaiwan=[]

function PaintTaiwanInfo(){
     ajaxfun("http://172.20.26.39:8000/api/taiwan",{},doTaiwan)
}

function doTaiwan(data){
    LocationsTaiwan=data
    locationsTaiwan=[]
    if ($("#minHr").val()==""){
        var minHr=-20
    }else{
        var minHr=$("#minHr").val()
    }
    if ($("#maxHr").val()==""){
        var maxHr=50000000
    }else{
        var maxHr=$("#maxHr").val()
    }
    if ($("#minCost").val()==""){
        var minCost=-20
    }else{
        var minCost=$("#minCost").val()
    }
    if ($("#maxCost").val()==""){
        var maxCost=500
    }else{
        var maxCost=$("#maxCost").val()
    }
    if ($("#minConv").val()==""){
        var minConv=-20
    }else{
        var minConv=$("#minConv").val()
    }
    if ($("#maxConv").val()==""){
        var maxConv=500
    }else{
        var maxConv=$("#maxConv").val()
    }


    for(var i=0;i<LocationsTaiwan.length;i++){
        if(LocationsTaiwan[i]['Nhuman_Analyze']>=minHr & LocationsTaiwan[i]['Nhuman_Analyze']<=maxHr &
        LocationsTaiwan[i]['costPower_Analyze']>=minCost & LocationsTaiwan[i]['costPower_Analyze']<=maxCost &
        LocationsTaiwan[i]['NconStore_Analyze']>=minConv & LocationsTaiwan[i]['NconStore_Analyze']<=maxConv){
        ///////////////////////////
            LocationsTaiwan[i]['location']=new google.maps.LatLng(LocationsTaiwan[i]['lat'],LocationsTaiwan[i]['lng']);
            LocationsTaiwan[i]['weight']=LocationsTaiwan[i]['costPower_Analyze'];
        ///////////////////////////
            locationsTaiwan.push(LocationsTaiwan[i])
        }
    }
//             &LocationsTaiwan[i]['NcostData_Analyze']>1
    console.log(locationsTaiwan)
    heatmapCost2.setData(locationsTaiwan)
    heatmapCost2.setMap(null);
    heatmapCost2.setMap(heatmapCost2.getMap() ? null : map);
//    map.setCenter({"lat":23.7142957284625,"lng":121.10338465868324})
//    map.setZoom(8)
//            images=transImgSize(mcImage,15)
//            var image=images;
//            var infowindow = new google.maps.InfoWindow({});
//            markerStores = [];
//            locationsTaiwan.forEach(function(location) {
//                var markerTaiwan = new google.maps.Marker({
//                    position: new google.maps.LatLng(location.lat, location.lng),
//                    icon: images['other'],
//                    map:map
//                });
//                markerTaiwan.addListener('click', function() {
//                    infowindow.setContent("消費力："+location.costPower_Analyze+"<br>人口："+location.Nhuman_Analyze+
//                    "<br>餐飲業均消："+location.avgCost_Analyze+"<br>公車站點："+location.NbusStation_Analyze+"<br>便利商店："+location.NconStore_Analyze+
//                    "<br>麥當勞："+location.Nmc_Analyze+"<br>肯德基："+location.Nken_Analyze+"<br>星巴克："+location.Nstar_Analyze )
//                    infowindow.open(map, markerTaiwan);
//                });
//                markersTaiwan.push(markerTaiwan);
//            });
    ////////
}

nullStoneTwo=1
function PaintTaiwanInfoStoneTwo(){
if (nullStoneTwo==1){
        document.getElementById('stoneTwo').style.color="red"
        ajaxfun("http://172.20.26.39:8000/api/stonetwo",{},doTaiwanStoneTwo)
        nullStoneTwo=0
    }else{
        document.getElementById('stoneTwo').style.color="black"
        nullStoneTwo=1
        wowData=[]
        clearMarkers(markerStoneTwos)
    }
}

function doTaiwanStoneTwo(data){
    locationsStoneTwo=data
    console.log(locationsStoneTwo)
    images=transImgSize(mcImage,10)
    var image=images;
    var infowindow = new google.maps.InfoWindow({});
    markerStoneTwos = [];
    locationsStoneTwo.forEach(function(location) {
        if(location.score>8){
            level="A"
        }else if(location.score>6){
            level="B"
        }else if(location.score>4){
            level="C"
        }else{
            level="other"
        }
        var markerStoneTwo = new google.maps.Marker({
            position: new google.maps.LatLng(location.lat, location.lng),
            icon: images[level],
            map:map
        });
        markerStoneTwo.addListener('click', function() {
            infowindow.setContent("餐廳數(均消170-336)："+location.NsimCostDien+"<br>公車站數："+location.NbusStation_Analyze+
            "<br>超商數："+location.NconStore_Analyze+"<br>強勢餐飲數(麥當、肯德、星巴、瓦)："+(location.Nken_Analyze+location.Nmc_Analyze+location.Nstar_Analyze+location.Nwa_Analyze)+
            "<br>生活分數(屈臣、全聯)："+(location.Nwatson_Analyze+location.Npxmart_Analyze)+"<br>綜合評分(0-10)："+location.score)
            ////////////////
//            geocodeAddress(location.lat+","+location.lng)
            var geocoder = new google.maps.Geocoder();
            geocoder.geocode({'address': location.lat+","+location.lng}, function(results, status) {
            if (status == 'OK') {
    //            //得到完整地址
                var add=results[0].formatted_address;
                console.log(add)
    //            //取得縣市的正規表達式
                var reCity = new RegExp("(..[市|縣])", "gi")
    //            //取得區市鎮鄉的正規表達式
    //            var reCountry = new RegExp("[縣|市](..?.?[區|市|鎮|鄉])", "gi")
                City=reCity.exec(add)[0].replace("臺","台")
                delcircle();
                RemoveOption('locations')
                if(!(nullIpeen==1)){
                    $('#ipeenMark').click()
                }
                if(!(null104==1)){
                    $('#104Mark').click()
                }
                if(!(null591==1)){
                    $('#591Mark').click()
                }
                $('#locations').append($('<option>').text(location.Called+"-"+location.StoreName));
                $('#locations').append($('<option>').text("周圍"+"500"+"公尺"));
                summaryData['地點']=location.Called+"-"+location.StoreName;
                summaryData['範圍']=$("#radius").val()+"公尺"
                infowindow.open(map, markerStoneTwo);
                query2({centerlat:location.lat,centerlng:location.lng,radius:500,bigadd:City})
                area=Math.round(parseInt($("#radius").val())*parseInt($("#radius").val())*Math.PI/1000000)
                $('#summarys').append($('<option>').text("區域範圍"+area+"平方公里"));
                map.setCenter({"lat":location.lat,"lng":location.lng})
                map.setZoom(16)
                var circle = new google.maps.Circle({
                    map: map,
                    radius: parseInt(500),    // metres
                    fillColor: '#fccccc'
                });
                circle.bindTo('center', markerStoneTwo, 'position');
                circles.push(circle)
            }})
            ///////////////////
        });
        markerStoneTwos.push(markerStoneTwo);
    });
}



nullHot7=1
function PaintTaiwanInfoHot7(){
if (nullHot7==1){
        document.getElementById('hot7').style.color="red"
        ajaxfun("http://172.20.26.39:8000/api/hot7",{},doTaiwanHot7)
        nullHot7=0
    }else{
        document.getElementById('hot7').style.color="black"
        nullHot7=1
        wowData=[]
        clearMarkers(markerHot7s)
    }
}


function doTaiwanHot7(data){
    locationsHot7=data
    console.log(locationsHot7)
    images=transImgSize(mcImage,10)
    var image=images;
    var infowindow = new google.maps.InfoWindow({});
    markerHot7s = [];
    locationsHot7.forEach(function(location) {
        if(location.score>8){
            level="A"
        }else if(location.score>6){
            level="B"
        }else if(location.score>4){
            level="C"
        }else{
            level="other"
        }
        var markerHot7 = new google.maps.Marker({
            position: new google.maps.LatLng(location.lat, location.lng),
            icon: images[level],
            map:map
        });
        markerHot7.addListener('click', function() {
            infowindow.setContent("相近餐廳數(鐵板燒250以下)："+location.NsimCostDien+"<br>診所數："+location.NclinicData_Analyze+
            "<br>超商數："+location.NconStore_Analyze+"<br>三商巧福+大埔鐵板燒："+(location.NtStore_Analyze+location.NDapu_analyze)+
            "<br>生活分數(屈臣、全聯)："+(location.Nwatson_Analyze+location.Npxmart_Analyze)+"<br>綜合評分(0-10)："+location.score)
            ////////////////
//            geocodeAddress(location.lat+","+location.lng)
            var geocoder = new google.maps.Geocoder();
            geocoder.geocode({'address': location.lat+","+location.lng}, function(results, status) {
            if (status == 'OK') {
    //            //得到完整地址
                var add=results[0].formatted_address;
                console.log(add)
    //            //取得縣市的正規表達式
                var reCity = new RegExp("(..[市|縣])", "gi")
    //            //取得區市鎮鄉的正規表達式
                City=reCity.exec(add)[0].replace("臺","台")
                delcircle();
                RemoveOption('locations')
                if(!(nullIpeen==1)){
                    $('#ipeenMark').click()
                }
                if(!(null104==1)){
                    $('#104Mark').click()
                }
                if(!(null591==1)){
                    $('#591Mark').click()
                }
                $('#locations').append($('<option>').text(location.Called+"-"+location.StoreName));
                $('#locations').append($('<option>').text("周圍"+"500"+"公尺"));
                summaryData['地點']=location.Called+"-"+location.StoreName;
                summaryData['範圍']=$("#radius").val()+"公尺"
                infowindow.open(map, markerHot7);
                query2({centerlat:location.lat,centerlng:location.lng,radius:500,bigadd:City})
                area=Math.round(parseInt($("#radius").val())*parseInt($("#radius").val())*Math.PI/1000000)
                $('#summarys').append($('<option>').text("區域範圍"+area+"平方公里"));
                map.setCenter({"lat":location.lat,"lng":location.lng})
                map.setZoom(16)
                var circle = new google.maps.Circle({
                    map: map,
                    radius: parseInt(500),    // metres
                    fillColor: '#fccccc'
                });
                circle.bindTo('center', markerHot7, 'position');
                circles.push(circle)
            }})
            ///////////////////
        });
        markerHot7s.push(markerHot7);
    });
}






point=0
function pointSearch(){
        if(point==0){
            document.getElementById('point').style.color='red'
            point=1;
            listener=map.addListener('click', function(e) {
              console.log(e.latLng.lat()+','+e.latLng.lng())
              geocodeAddress(e.latLng.lat()+','+e.latLng.lng());
            });
        }else{
            document.getElementById('point').style.color='black'
            point=0;
            google.maps.event.removeListener(listener)
        }
}

function goCompare(){
    window.open("http://172.20.26.39:8000/api/compare","_blank")
}