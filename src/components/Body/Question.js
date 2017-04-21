import React from "react";


export default class Question extends React.Component {

	render() {
		return (
			<div id="ask">
				<section className="content question">
					<h5>{this.props.question}</h5>
					<label htmlFor="repA"><input type="radio" id="repA" className="rep" name="choice" value={this.props.propositions[0]} onClick={this.props.checkRep} /> {this.props.propositions[0]}</label>
					<label htmlFor="repB"><input type="radio" id="repB" className="rep" name="choice" value={this.props.propositions[1]} onClick={this.props.checkRep} /> {this.props.propositions[1]}</label>
					<label htmlFor="repC"><input type="radio" id="repC" className="rep" name="choice" value={this.props.propositions[2]} onClick={this.props.checkRep} /> {this.props.propositions[2]}</label>
				</section>
			</div>
		);
	}
}