 $(function(){
        csmapi.set_endpoint ('https://3.iottalk.tw');
        var profile = {
		    'dm_name': 'Bulb0858610',          
		    'odf_list':[Color0858610,Lum0858610],
		    'd_name': undefined,
        };
    //從color.js複製過來以下這段
	var r = 255;
	var g = 255;
	var b = 0;
    var lum = 100;
	
    function draw () {
    var rr = Math.floor((r * lum) / 100);
    var gg = Math.floor((g * lum) / 100);
    var bb = Math.floor((b * lum) / 100);
    $('.bulb-top, .bulb-middle-1, .bulb-middle-2, .bulb-middle-3, .bulb-bottom, .night').css(
       {'background': 'rgb('+ rr +', '+ gg +', '+ bb +')'}
     );}
   //從color.js複製過來以上這段
                        
    function Lum0858610(data){
        lum = data[0];
        draw();
        console.log(data[0]);
        }
	function Color0858610(data){
	   r = data[0]
	   g = data[1]
       b = data[2]
       r = r * 255 / 360 ;
       g = (g+180)*255 / 360 ;
       b = (b+90)*255 / 180 ;
       draw();
	   console.log(r,g,b);
	}
      
/*******************************************************************/                
        function ida_init(){
	    $('.title')[0].innerText=profile.d_name;
	    console.log(profile.d_name);
	}
        var ida = {
            'ida_init': ida_init,
        }; 
        dai(profile,ida);     
});
