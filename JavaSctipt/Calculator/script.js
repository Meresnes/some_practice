window.onload = function(){
	var inputX = document.getElementById('inputX');
	var inputY = document.getElementById('inputY');
	var btn = document.getElementById('getResult');
	


	btn.onclick = function(){
		let x = inputX.value;
		let y = inputY.value;
		let operation = document.getElementById('operation').value;
		
		if ((x == "") || (y == "")){
 			operation = '0';
 		}

		x = parseFloat(inputX.value);
        y = parseFloat(inputY.value);
        
 		if (operation == '0') (res = 0);
        if (operation == '1') (res = x + y);
        if (operation == '2') (res = x - y);
        if (operation == '3') (res = x * y);
        if (operation == '4') (res = x / y);
        
        document.getElementById('res').innerHTML = res;
	}
	
}