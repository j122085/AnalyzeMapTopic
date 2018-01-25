//icon集
var imagesUrl={
    'buffet自助餐':"https://cdn3.iconfinder.com/data/icons/hotel-restaurant-glyphs-vol-4/52/hotel__service__restaurant__hostel__food__buffet__dish-48.png",
    '中式料理':"https://cdn3.iconfinder.com/data/icons/food-and-drink-1/512/pasta_noodles-64.png",
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
    '鍋類':"http://icons.iconarchive.com/icons/icons8/ios7/48/Food-Cooking-Pot-icon.png"
};
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

var styles=['buffet自助餐', '中式料理', '主題特色餐廳', '亞洲料理', '其他美食', '冰品、飲料、甜湯', '咖啡、簡餐、茶',
 '小吃', '日式料理', '早餐', '烘焙、甜點、零食', '燒烤類', '異國料理', '素食', '速食料理', '鍋類'];


//以上資料區!!!--------------------------------


//讀取網頁時同時跑的function
//    dd0Bind();資料填入下拉式選單
//    dd1Bind();資料填入下拉式選單
$(function(){
    dd0Bind();
    dd1Bind();
})
//讀取網頁時同時跑的function

//以下篩選區!!!--------------------------------
//全類型篩選(用三個下拉式選單、以及show104()、showIpeen()、geocodeAddress()呼叫)
//由於按長條圖或柏拉圖篩選時不是用下拉式選單query 因此將styleq、jobstyleq作為函數變數
function query(centerChange=true,charChange=true,barChange=true,styleq=$('#style').val(),jobstyleq="",changeIpeen=true,change104=true){
    console.log("style:"+styleq)
    console.log("job:"+jobstyleq)

    //縣市只抓前兩個字資料(下拉)
    var bigcity=$('#bigCity').val();
    //區域資料(下拉)
    var smallcity=$('#smallCity').val().replace(/\s+/g, "");//.replace(/\s+/g, "")>>去除空白
//    var styleq=$('#style').val();>>改成函數變數
    //篩選資料點(留下需要的資料>>回傳資料為變數LocationsIpeen及LocationsHr)
    if(changeIpeen==true){
        //show新資料點前先刪除之前的資料marker
        LocationsIpeen = [];
        markerClusterIpeen.clearMarkers()
        //當愛評資料點顯示時才動作、否則資料點為空
        if (nullIpeen==0){
            $.ajax({
                type : "POST",  //使用POST方法
    //            url : "http://127.0.0.1:8000/api/ipeen",  //觸發的url
                url : "http://172.20.26.39:8000/api/ipeen",
                data : {bigstyle:styleq,bigadd:bigcity,smalladd:smallcity},  //想要傳給後端的資料，如果有的話
                success: function(data){
                    for(var i=0;i<data.length;i++){
                        var dien={}
                        dien['content']='<strong>'+data[i]['name'].replace("'","").replace(";","").replace("{","")+"</strong><br>"
                                                                 +data[i]['address'].replace("'","").replace(";","").replace("{","")
                                                                 +"<br>電話:"+String(data[i]['tele'])+
                                                                 "<br>花費:"+String(data[i]['averagecost'])+
                                                                 "<br>人氣(點閱):"+String(data[i]['viewcount'])+
                                                                 "<br>評論數:"+String(data[i]['Ncomment'])+
                                                                 "<br>類型:"+data[i]['bigstyle']+"-"+data[i]['smallstyle']+
                                                                 '<br><a href="http://www.ipeen.com.tw/shop/'+String(data[i]['id'])+'">愛評連結</a>';
                        dien['style']=data[i]['bigstyle'].replace("'","").replace(";","").replace("{","");
                        dien['averageCost']=data[i]['averagecost'];
//                        console.log(data[i])
                        dien['bigArea']=data[i]['bigadd'].replace("'","").replace(";","").replace("{","");
                        dien['smallArea']=data[i]['smalladd'].replace("'","").replace(";","").replace("{","");
                        dien['label']=data[i]['name'].replace("'","").replace(";","").replace("{","");
                        dien['lat']=data[i]['lat'];
                        dien['lng']=data[i]['lng'];
                        LocationsIpeen.push(dien);
                    }
                    console.log(LocationsIpeen)
                    //用篩選出來的資料點，及images畫markers
                    var locationsIpeen = LocationsIpeen;
                    var image=images;
                    var infowindow = new google.maps.InfoWindow({});
                    markerIpeens = [];
                    locationsIpeen.forEach(function(location) {
                        var markerIpeen = new google.maps.Marker({
                            position: new google.maps.LatLng(location.lat, location.lng),
                //            label: location.label,
                            icon: images[location.style],
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
                    if(charChange==true){
                        getStyleCount();
                        getPoretoData();
                        Poreto();
                    }
                },
                error: function(XMLHttpRequest, textStatus, errorThrown) {
                    alert("some error " + String(errorThrown) + String(textStatus) + String(XMLHttpRequest.responseText));
                }  //debug用
            });
        }else{
            if(charChange==true){
                getStyleCount();
                getPoretoData();
                Poreto();
            }
        }
    }
    //同上 資料為104
    if(change104==true){
        LocationsHr = [];
        markerClusterHr.clearMarkers()
        //當104資料點顯示時才動作
        if (null104==0){
            $.ajax({
                type : "POST",  //使用POST方法
    //            url : "http://127.0.0.1:8000/api/hr104",  //觸發的url
                url : "http://172.20.26.39:8000/api/hr104",
//                data : {job:jobstyleq,bigadd:bigcity,smalladd:smallcity},  //想要傳給後端的資料，如果有的話
                data : {job:jobstyleq,bigadd:bigcity,smalladd:smallcity,bigstyle:styleq},  //想要傳給後端的資料，如果有的話0124
                success: function(data){
                    for(var i=0;i<data.length;i++){
                        var dien={}
                        dien['content']='<strong>'+data[i]['NAME'].replace("'","").replace(";","").replace("{","")+
                                                            "</strong><br>"+data[i]['JOB'].replace("'","").replace(";","").replace("{","")+
                                                            "<br>薪資"+String(data[i]['SAL_MONTH_LOW'])+"-"+String(data[i]['SAL_MONTH_HIGH']);
                        dien['style']=data[i]['JOBCAT_DESCRIPT'].replace("'","").replace(";","").replace("{","");
                        dien['bigArea']=data[i]['bigadd'].replace("'","").replace(";","").replace("{","");
                        dien['smallArea']=data[i]['smalladd'].replace("'","").replace(";","").replace("{","");
                        dien['salary']=data[i]['SAL_MONTH_LOW'];
                        dien['label']=data[i]['NAME'].replace("'","").replace(";","").replace("{","");
                        dien['lat']=data[i]['lat'];
                        dien['lng']=data[i]['lng'];
                        LocationsHr.push(dien);
                    }
                    console.log(LocationsHr)
                     var imageJob = {
                      url:"https://cdn2.iconfinder.com/data/icons/sales-and-online-shop-filled-line/512/sales_online_shop_pick_box-48.png",//google內建icon
                      size: new google.maps.Size(20, 20),
                      origin: new google.maps.Point(0, 0),
                      anchor: new google.maps.Point(0, 32),
                      scaledSize: new google.maps.Size(20, 20)
                    };

                    var locationsHr = LocationsHr;
                    var image2=imageJob;
                    var infowindow2 = new google.maps.InfoWindow({});
                    markersHr = [];
                    locationsHr.forEach(function(location) {
                        var markerHr = new google.maps.Marker({
                            position: new google.maps.LatLng(location.lat, location.lng),
                //            label: location.label,
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
                    //----------control map location(控制地圖的位置及大小)

                   if(barChange==true){
                        getJobCount();
                        getBarData()
                        bar();
                    }
                },
                error: function(XMLHttpRequest, textStatus, errorThrown) {
                    alert("some error " + String(errorThrown) + String(textStatus) + String(XMLHttpRequest.responseText));
                }  //debug用
            });
        }else{
            if(barChange==true){
                getJobCount();
                getBarData()
                bar();
            }
        }
    }
    if (centerChange==true){
        if(smallcity+bigcity==""){
            map.setZoom(8)
            map.setCenter({"lat":23.4142957284625,"lng":121.10338465868324})
        //類型+區
        }else if(smallcity!=""){
            map.setZoom(14);
        //類型+縣市
        }else if(smallcity=="" & bigcity!=""){
            map.setZoom(11);
        }
        var lats = 0;
        var lngs = 0;
        for (i = 0; i < LocationsIpeen.length; i++){
           lats+=LocationsIpeen[i]["lat"];
           lngs+=LocationsIpeen[i]["lng"];
        }
        latcenter=lats/LocationsIpeen.length;
        lngcenter=lngs/LocationsIpeen.length;

        if(!latcenter){
            for (i = 0; i < LocationsHr.length; i++){
                lats+=LocationsHr[i]["lat"];
                lngs+=LocationsHr[i]["lng"];
            }
            latcenter=lats/LocationsHr.length;
            lngcenter=lngs/LocationsHr.length;
        }
        if(!latcenter){

            var geocoder = new google.maps.Geocoder();
            var address = document.getElementById('address').value;
            geocoder.geocode({'address': $('#bigCity').val()+$('#smallCity').val()}, function(results, status) {
                if (status == 'OK') {
                    center=results[0].geometry.location;
                    center={lat:center.lat(),lng:center.lng()}
                    map.setCenter(center);
                } else {
                    console.log('aaa')
//                    alert('Geocode was not successful for the following reason: ' + status);
                }
            });
        }else{
            map.setCenter({"lat":latcenter,"lng":lngcenter})
        }
    }
}
//將icon變成我喜歡的大小
var images={}
function transImgSize(){
    for(var key in imagesUrl){
            var image={
                    url:imagesUrl[key],
                    size: new google.maps.Size(15, 15),
                    origin: new google.maps.Point(0, 0),
                    anchor: new google.maps.Point(0, 32),
                    scaledSize: new google.maps.Size(15, 15)
            }
            images[key]=image;
    };
}
//nullIpeen 0顯示 1不顯示-愛評網的資料//愛評網資料畫在poreto(charChange)
var nullIpeen=1;
function toggleIpeenMarker(){
    //Locations沒東西的話
    transImgSize();
    if (nullIpeen==1){
        nullIpeen=0;
        document.getElementById('ipeenMark').style.color='red'
    }else{
        nullIpeen=1;
        LocationsIpeen=[];
        document.getElementById('ipeenMark').style.color='black'
    }
    query(centerChange=false,charChange=true,barChange=false,styleq=$('#style').val(),jobstyleq="",changeIpeen=true,change104=false);
}
//同上
var null104=1;
function toggle104Marker(){
    //Locations2沒東西的話
    if (null104==1){
        null104=0;
        document.getElementById('104Mark').style.color='red'
    }else{
        null104=1;
        LocationsHr=[];
        document.getElementById('104Mark').style.color='black'
    }
    query(centerChange=false,charChange=false,barChange=true,styleq=$('#style').val(),jobstyleq="",changeIpeen=false,change104=true);
}
//以上篩選區--------------------------------------

//以下產生圖表--------------------------------------
//將資料style做累加 動作1
var styleCount={};
var sortedStyleCount;
function getStyleCount(){
    styleCount={};
    for(var i=0;i<LocationsIpeen.length;i++){
        if(!styleCount[LocationsIpeen[i]["style"]]){
            styleCount[LocationsIpeen[i]["style"]]=0
        }
        styleCount[LocationsIpeen[i]["style"]]+=1
    }
    sortedStyleCount=sortProperties(styleCount)
}
//將職業做累加 動作1
var jobCount={};
var sortedJobCount;
function getJobCount(){
    jobCount={};
    for(var i=0;i<LocationsHr.length;i++){
        if(!jobCount[LocationsHr[i]["style"]]){
            jobCount[LocationsHr[i]["style"]]={}
            jobCount[LocationsHr[i]["style"]]["count"]=0
            jobCount[LocationsHr[i]["style"]]["all"]=0
        }
        jobCount[LocationsHr[i]["style"]]["count"]+=1
        jobCount[LocationsHr[i]["style"]]["all"]+=parseInt(LocationsHr[i]["salary"])
    }
    sortedJobCount=sortProperties(jobCount)
}

//obj資料格式排序(用來做柏拉圖用) 動作2
function sortProperties(obj)
{
  // convert object into array
    var sortable=[];
    for(var key in obj)
        if(obj.hasOwnProperty(key))
            sortable.push([key, obj[key]]); // each item is an array in format [key, value]

    // sort items by value
    sortable.sort(function(a, b)
    {
      return b[1]-a[1]; // compare numbers
    });
    return sortable; // array in format [ [ key1, val1 ], [ key2, val2 ], ... ]
}
//做成kv格式餵給製圖fuction 動作3
var forPoreto=[]
function getPoretoData(){
    forPoreto=[]
    for(var i=0;i<sortedStyleCount.length;i++){
        kv={};
        kv["label"]=sortedStyleCount[i][0]
        kv["y"]=sortedStyleCount[i][1];
        forPoreto.push(kv);
    }
}

var forBar=[]
function getBarData(){
    forBar=[]
    for(var i=0;i<sortedJobCount.length;i++){
        kv2={}
        kv2["label"]=sortedJobCount[i][0]
        kv2["y"]=Math.round(sortedJobCount[i][1]['all']/sortedJobCount[i][1]['count']);
        forBar.push(kv2);
    }
}

//產生柏拉圖 動作4
function Poreto() {
    var chart = new CanvasJS.Chart("chartContainerPoreto", {
       title:{
           text: "Ipeen Style Poreto"
       },
        data: [
        {
            // Change type to "doughnut", "line", "splineArea", etc.
            type: "column",
            dataPoints: forPoreto,
            fontSize: 20,
            click:onClick
        }
        ]
    });
    chart.render();
}
//點擊柏拉圖的動作
function onClick(e) {
        query(centerChange=false,charChange=false,barChange=false,styleq=e.dataPoint.label,jobstyleq="",changeIpeen=true,change104=false);
//        console.log(e.dataPoint.label)
    }





function bar() {
    var chart = new CanvasJS.Chart("chartContainerBar", {
        animationEnabled: true,
        title:{
            text:"104 average salary"
        },
        axisX:{
            interval: 1
        },
        axisY2:{
            interlacedColor: "rgba(1,77,101,.2)",
            gridColor: "rgba(1,77,101,.1)",
    //title: "Number of Companies"
        },
        data: [{
            type: "bar",
            name: "companies",
            axisYType: "secondary",
            color: "#014D65",
            dataPoints: forBar,
            click:barclick
        }]
    });
    chart.render();
}
//點擊長條圖的動作
function barclick(f) {
//        console.log(f.dataPoint.label)
        query(centerChange=false,charChange=false,barChange=false,styleq=$('#style').val(),jobstyleq=f.dataPoint.label,changeIpeen=false,change104=true);
    }


//以上產生圖表--------------------------------------
//搜索-----------地址>經緯度>畫標記+移動到座標+query()
var center,x,y,add;
var bigAreaQuery=true;
function geocodeAddress() {
    var geocoder = new google.maps.Geocoder();
    var address = $("#address").val();
    geocoder.geocode({'address': address}, function(results, status) {
        if (status == 'OK') {
            //得到完整地址
            var add=results[0].formatted_address;
            //取得縣市的正規表達式
            var reCity = new RegExp("(..[市|縣])", "gi")
            //取得區市鎮鄉的正規表達式
            var reCountry = new RegExp("[縣|市](..?.?[區|市|鎮|鄉])", "gi")
            try{
                var City=reCity.exec(add)[0].replace("臺","台")
                //自動選擇下拉市選單
                bigAreaQuery=false;
                $('#bigCity').val(City).change();
            }
            catch(err) {
                alert("google認為這位置不再台灣");
            }
            try{
                var Country=reCountry.exec(add)[1]
                $('#smallCity').val(Country).change();
            }
            catch(err) {
                //如果搜索只能得到縣市、得不到區則將區指定為該縣市全區
                console.log(err.message);
                $('#smallCity').val("").change();
            }
            //座標移動、畫marker
            var center=results[0].geometry.location;
            center={lat:center.lat(),lng:center.lng()}
            markerControl={
                position: new google.maps.LatLng(center),
                label: $("#address").val(),
                icon: "https://cdn2.iconfinder.com/data/icons/ios-7-icons/50/finish_flag-32.png",
                map:map
            }
            var findmarker= new google.maps.Marker(markerControl);
            map.setZoom(15);
            map.setCenter(center);
            markers.push(findmarker)
        } else {
            console.log(6)
            alert('google說不要亂案');
        }
    });
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
    markerClusterHrOptions,heatmapCost,heatmapHuman

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
        gridSize: 80,
        maxZoom: 17,
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
                 textColor:'rgba(255, 255, 255, 0)'
                };
        clusterStyles.push(img);
    }

    markerClusterHrOptions = {
        gridSize: 80,
        maxZoom: 17,

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
        radius:5000/(Math.pow(2,(20-zoomsize))),
//        map: map,
        gradient:[
        'rgba(0, 255, 255, 0)',
        'rgba(0, 255, 255, 1)',
        'rgba(0, 191, 255, 1)',
        'rgba(0, 127, 255, 1)',
        'rgba(0, 63, 255, 1)',
        'rgba(0, 40, 255, 1)',
        'rgba(0, 40, 223, 1)',
        'rgba(0, 40, 191, 1)',
        'rgba(0, 40, 159, 1)',
        'rgba(0, 40, 127, 1)'
    ]
    });

    //固定heatmap的大小(每次地圖zoom變更就計算)
    google.maps.event.addListener(map, 'zoom_changed', function () {
        heatmapCost.setOptions({radius:getNewRadius(7000)});
    });
    google.maps.event.addListener(map, 'zoom_changed', function () {
        heatmapHuman.setOptions({radius:getNewRadius(6000)});
    });
    function getNewRadius(N){
        var radius = (N)/(Math.pow(2,(20-map.getZoom())));
        return radius;
    }
}
//以上產生地圖--------------------------------------

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
function toggleHeatmapCost() {
    if(costDensity.length==0){
        document.getElementById('costHeat').style.color="red";
        $.ajax({
            type : "POST",  //使用POST方法
//            url : "http://127.0.0.1:8000/api/cost",  //觸發的url
            url : "http://172.20.26.39:8000/api/cost",
            success: function(data){
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
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                alert("some error " + String(errorThrown) + String(textStatus) + String(XMLHttpRequest.responseText));
            }  //debug用
        });
    }else{
        document.getElementById('costHeat').style.color="black";
        heatmapCost.setMap(heatmapCost.getMap() ? null : map);
    }

}

//熱度圖 for 人口密度
var humanDensity=[];
function toggleHeatmapHuman() {
    if(humanDensity.length==0){
        document.getElementById('humanHeat').style.color="red";
        $.ajax({
            type : "POST",  //使用POST方法
//            url : "http://127.0.0.1:8000/api/human",  //觸發的url
            url : "http://172.20.26.39:8000/api/human",
            success: function(data){
                for(var i=0;i<data.length;i++){
                    var location={}
                    location['location']=new google.maps.LatLng(data[i]['lat'],data[i]['lng']);
                    location['weight']=data[i]['weight'];
//                    location['add']=data[1]['add'];
                    humanDensity.push(location);
                }
                console.log(humanDensity)
                heatmapHuman.setData(humanDensity);
                heatmapHuman.setMap(heatmapHuman.getMap() ? null : map);
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                alert("some error " + String(errorThrown) + String(textStatus) + String(XMLHttpRequest.responseText));
            }  //debug用
        });
    }else{
        document.getElementById('humanHeat').style.color="black";
        heatmapHuman.setMap(heatmapHuman.getMap() ? null : map);
    }
}

//變更熱度圖透明度
function changeOpacity() {
    heatmapCost.set('opacity', heatmapCost.get('opacity') ? null : 0.4);
    heatmapHuman.set('opacity', heatmapHuman.get('opacity') ? null : 0.4);
}
//以上操作地圖顯示--------------------------------------

//以下產生周圍生活標記--------------------------------------
var searchTarget,service;
function getpoint(pointType){
    searchTarget=map.getCenter();
    infowindow = new google.maps.InfoWindow();
    service = new google.maps.places.PlacesService(map);
    //最多產生20個點 (如果type不選會產生rank高的)
    service.nearbySearch({
        location: searchTarget,
        radius:50*(Math.pow(2,(20-map.getZoom()))),
        type: pointType
    }, callback);
}
function callback(results, status) {
//    delpoint();是否每點一個就刪除?
    console.log(results[1]);
//    console.log(results.length);
    var x=0
    if (status === google.maps.places.PlacesServiceStatus.OK) {
        for (var i = 0; i < results.length; i++) {
            createMarker(results[i]);
//            console.log(x++);
        }
    }
}
markers=[] //用來儲存每個標記 以便之後刪除
function createMarker(place) {
    var placeLoc = place.geometry.location;
    var image = {
                  url:place.icon,//google內建icon
                  size: new google.maps.Size(20, 20),
                  origin: new google.maps.Point(0, 0),
                  anchor: new google.maps.Point(0, 32),
                  scaledSize: new google.maps.Size(20, 20)
            };
    var marker = new google.maps.Marker({
        map: map,
        position: place.geometry.location,
        icon:image,
    });

    marker.addListener('click', function() {
        var request = {
            placeId: place.place_id
        };
        service.getDetails(request, function(details, status) {
            console.log(details)
          infowindow.setContent([
            details.name,
            details.formatted_address,
            details.website,
                details.rating,
    //              details.icon,
            details.formatted_phone_number].join("<br />"));
          infowindow.open(map, marker);
        });
    });
        markers.push(marker)
}
//清除標記
function delpoint(){
    for(var i=0;i<markers.length;i++){
        markers[i].setMap(null);
    }
}
//以上產生生活標記--------------------------------------


//以下下拉式選單操作--------------------------------------
//類型資料塞進下拉選單(進入網頁同時啟動)
function dd0Bind()
{
    $('#style').append($('<option>').text('全類型').attr('value', ''));
    $.each(styles, function (i) {
        $('#style').append($('<option>').text(styles[i]).attr('value', styles[i]));
    });
}

//縣市資料塞進下拉選單(進入網頁同時啟動)
function dd1Bind()
{
    var bigCitylist=Object.keys(cityData);
    $('#bigCity').append($('<option>').text('全縣市').attr('value', ''));
    $.each(bigCitylist, function (i) {
        $('#bigCity').append($('<option>').text(bigCitylist[i]).attr('value', bigCitylist[i]));
    });
}

//區域下拉選單(變更縣市下拉選單時加入)
function dd2Bind(pkey)
{
    //先刪除前次加入的區域   (.replace(/\s+/g, "")為去除空白的方法)
    RemoveOption("smallCity");
    $('#smallCity').append($('<option>').text('全區').attr('value', ''));
    if (pkey!=""){
        var smallCitylist=Object.keys(cityData[pkey]);
        $.each(smallCitylist, function (i) {
            $('#smallCity').append($('<option>').text(smallCitylist[i].replace(/\s+/g, "")).attr('value', smallCitylist[i].replace(/\s+/g, "")));
        });
    }
    if(bigAreaQuery==true){
        query(centerChange=true);
    }
    bigAreaQuery=true;
}

//選取新的縣市時，先刪除目前產生的區域list
function RemoveOption(selectid){
    var mySelect = document.getElementById(selectid);
    for (var i=mySelect.options.length-1; i>=0; i--){
        mySelect.remove(i);
    }
}
//0125try-------------------
//var doc = new jsPDF();
//var specialElementHandlers = {
//    '#editor': function (element, renderer) {
//        return true;
//    }
//};
//
//$('#cmd').click(function () {
//    doc.fromHTML($('#content').html(), 15, 15, {
//        'width': 170,
//            'elementHandlers': specialElementHandlers
//    });
//    doc.save('sample-file.pdf');
//});
//0125try-------------------
//    google.maps.event.addDomListener(window, 'load', initialize);
