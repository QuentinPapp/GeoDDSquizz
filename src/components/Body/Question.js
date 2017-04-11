import React from "react";


export default class Question extends React.Component {

	render() {
		return (
			<section className="content question">
				<h5>{this.props.question}</h5>
				<label><input type="radio" name="choice" value={this.props.propositions[0]} /> {this.props.propositions[0]}</label>
				<label><input type="radio" name="choice" value={this.props.propositions[1]} /> {this.props.propositions[1]}</label>
				<label><input type="radio" name="choice" value={this.props.propositions[2]} /> {this.props.propositions[2]}</label>
				<label><input type="radio" name="choice" value="La réponse D" /> D</label>
				<input className="check" type="submit" value="Valider" onClick={this.props.checkRep} />
			</section>
		);
	}
}