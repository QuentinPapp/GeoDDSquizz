import React from "react";

export default class Question extends React.Component {
	render() {
		return (
			<section id="question">
				<p>Intitulé</p>
				<input type="radio" name="choice"/> Reponse 1
				<input type="radio" name="choice"/> Reponse 2
				<input type="radio" name="choice"/> Reponse 3
			</section>
		);
	}
}