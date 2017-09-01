import React from "react";

export default class Question extends React.Component {
	render() {
		return (
			<h2>{this.props.ask}</h2>
		);
	}
}