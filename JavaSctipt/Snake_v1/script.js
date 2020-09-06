//
// ╤ючфрэшх ьрЄЁшЎ√.
//
function createMatrix()
{
	var matrix = document.getElementById('matrix');
	var n = 20 * 20;	
	
	for (var i = 0; i < n; i++)
	{
		var div = document.createElement('div');
		div.className = 'cell';
		matrix.appendChild(div);
	}
}


SQUARE_COLOR = 'red';
DEFAULT_COLOR = 'white';
function getCell(row, col)
{
	
	var matrix = document.getElementById('matrix');
	var cell = matrix.children[20 * (row - 1) + col - 1];
	return cell.style.backgroundColor == SQUARE_COLOR;
}


function setCell(row, col, val)
{
	var matrix =document.getElementById('matrix');
	var cell = matrix.children[20 * (row - 1) + col - 1];

	cell.style.backgroundColor = (val == true ? SQUARE_COLOR : DEFAULT_COLOR);
}


current_row = 1;
current_col = 1;

finish_row = 20;
finish_col = 20;

KEYS = {
    LEFT : 37,
    RIGHT : 39,
    UP : 38,
    DOWN : 40
} 

window.onload = function()
{
	createMatrix();	
	setCell(current_row, current_col, true);
	setCell(finish_row,finish_col,true);
	document.onkeydown = function(e){
	//left 37; up 38; right 39; down 40;
	//alert(e.keyCode);
	
	setCell(current_row,current_col,false);

	if (e.keyCode == KEYS.RIGHT){
		current_col++;
	}
	else if (e.keyCode == KEYS.LEFT){
		current_col--;
	}
	else if (e.keyCode == KEYS.DOWN){
		current_row++;
	}
	else if (e.keyCode == KEYS.UP){
		current_row--;
	}


	if (current_col > 20){
		current_col--;
	}
	else if (current_col < 1){
		current_col++;
	}
	if (current_row > 20){
		current_row--;
	}
	else if (current_row < 1){
		current_row++;
	}

	if(getCell(current_row,current_col)){
		alert('Game over!')
	}
	setCell(current_row,current_col,true);

	}


}				

