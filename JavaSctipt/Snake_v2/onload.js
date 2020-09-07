//
// Точка входа.
//

KEYS = {
    LEFT : 37,
    RIGHT : 39,
    UP : 38,
    DOWN : 40
} 
window.onload = function()
{
	m1 = new Matrix('matrix1', 20, 20);
	m1.create();
	
	var square = new Square(1, 2, 'right');
	square.create();
	
	var score_time = new Score(0);

	document.onkeydown = function(e){
			if(e.keyCode == KEYS.RIGHT){
				square.course = 'right';
			}
			else if(e.keyCode == KEYS.LEFT){
				square.course = 'left';
			}
            else if(e.keyCode == KEYS.DOWN){
				square.course = 'down';
			}
			else if(e.keyCode == KEYS.UP){
				square.course = 'up';
			}
		}
	
	
	setInterval(square.move, 300);
	setInterval(score_time.addTime,1000);


    

}		