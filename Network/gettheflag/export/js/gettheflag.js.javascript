$(function(){

$getflag=function($num){
	$.ajax({
		type:"POST",
		url:"flag.php",
		cache:false,
		data:"n="+$num,
		dataType:"json",
		success:function($json){
			$("#ff"+$num).text($json.data.char);
			if($json.data.last){$num++;}
			if($num<16){
				setTimeout($getflag($num),750);
			}else{
				$(".fs td").css("color","#fff").css("background-color","#000");
			}
		}
	});
}

$(".fl").click(function(){
	$(".fs td").css("color","#000").css("background-color","#fff");
	setTimeout($getflag(0));
	return false;
});

});