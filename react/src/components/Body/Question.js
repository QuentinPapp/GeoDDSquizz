import React from "react";

export default class Question extends React.Component {
	render() {
		return (
			<section className="content question">
				<p>Intitulé</p>
				<label><input type="radio" name="choice"/>Réponse 1</label>
				<label><input type="radio" name="choice"/>Réponse 2</label>
				<label><input type="radio" name="choice"/>Réponse 3</label>
				<button>Valider</button>
			</section>
		);
	}
}