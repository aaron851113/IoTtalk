 $(function(){
        csmapi.set_endpoint ('https://3.iottalk.tw');
        var profile = {
		    'dm_name': '0858610-Bulb',          
			//'idf_list':[Dummy_Sensor],
			'odf_list':[0858610LUM,0858610Color],
		        'd_name': undefined,
			
        };
		
        function Dummy_Sensor(){
            return Math.random();
        }

        function 0858610Lum(data){
           $('.ODF_value')[0].innerText=data[0];
        }
	function 0858610Color(data){
	   data[0]
	   data[1]
           data[2]
	}
      
/*******************************************************************/                
        function ida_init(){
	    $('.CLASS')[0].innerText=profile.d_name;
	    console.log(profile.d_name);
	}
        var ida = {
            'ida_init': ida_init,
        }; 
        dai(profile,ida);     
});
