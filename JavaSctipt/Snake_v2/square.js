function Square(row, col, course)
{
	this.body = [row, col];
	this.course = course;
	var that = this;
	
	this.create = function()
	{
		m1.setCell(that.body[0], that.body[1], true);
	}
	
	this.move = function()
	{
		var last_body = that.body.slice();
		
		switch(that.course)
		{
			case 'right':
				that.body[1]++;
				break;
		    case 'left':
		        that.body[1]--;
		        break;
		    case 'down':
		        that.body[0]++;
		        break;
		    case 'up':
		        that.body[0]--;
		        break;
		}

		if(that.body[1] > 20){
			alert('game over');

		}
		else if(that.body[1] < 1){
			alert('game over');
		}

		if(that.body[0] > 20){
			alert('game over');

		}
		else if(that.body[0] < 1){
			alert('game over');
		}


		m1.setCell(last_body[0], last_body[1], false);
		m1.setCell(that.body[0], that.body[1], true);
	}
}