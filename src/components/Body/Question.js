import React from "react";


export default class Question extends React.Component {

	render() {
		return (
			<section className="content question">
				<h5>{this.props.question}</h5>
				<label htmlFor="repA" tabIndex="1"><input type="radio" id="repA" className="rep" name="choice" value={this.props.propositions[0]} onClick={this.props.checkRep} /> {this.props.propositions[0]}</label>
				<label htmlFor="repB" tabIndex="2"><input type="radio" id="repB" className="rep" name="choice" value={this.props.propositions[1]} onClick={this.props.checkRep} /> {this.props.propositions[1]}</label>
				<label htmlFor="repC" tabIndex="3"><input type="radio" id="repC" className="rep" name="choice" value={this.props.propositions[2]} onClick={this.props.checkRep} /> {this.props.propositions[2]}</label>
			</section>
		);
	}
}