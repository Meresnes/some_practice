function Score(start_score) {
	this.start_score = start_score;
	var newScore = this.start_score;

	this.addTime = function(){
		newScore += parseInt(start_score + 1);
		document.getElementById('score1').innerHTML ='U are alive ' + newScore + ' seconds';

	}

	
}