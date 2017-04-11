import React from "react";

export default class Resultat extends React.Component {
	render() {
		return (
			<section id="test" className="content result">
				<p className="show">{this.props.reponse}</p>
			</section>
		);
	}
}

