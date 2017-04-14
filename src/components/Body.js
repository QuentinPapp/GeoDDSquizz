import React from "react";

import Question from "./Body/Question";
import Resultat from "./Body/Resultat";

export default class Body extends React.Component {

	render() {
		return (
			<section id="main">
				<p>Score : {this.props.score}</p>
				<Question checkRep={this.props.checkRep} question={this.props.question} propositions={this.props.propositions} />
				<Resultat reponse={this.props.reponse} />
			</section>
		);
	}
}