import React from "react";

export default class Question extends React.Component {
	render() {
		return (
			<section className="content question">
				<h5>Question</h5>
				<form>
					<label><input type="radio" name="choice"/>Réponse 1</label>
					<label><input type="radio" name="choice"/>Réponse 2</label>
					<label><input type="radio" name="choice"/>Réponse 3</label>
					<input className="check" type="submit" value="Valider"/>
				</form>
			</section>
		);
	}
}