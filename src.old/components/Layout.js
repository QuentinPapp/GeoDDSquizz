import React from "react";

import Header from "./Header";
import Body from "./Body";


export default class Layout extends React.Component {
	constructor(props) {
		super(props);
		this.changeTitle = this.changeTitle.bind(this);
		this.changeQuestion = this.changeQuestion.bind(this);
		this.state = {
			title: "Welcome !!",
			question: "Bien ?"
		}
	}

	changeTitle(title) {
		this.setState({title});
	}

	changeQuestion(question) {
		this.setState({question});

		/*var p = document.createElement("p");
		var node = document.createTextNode(question);

		p.appendChild(node);

		var div = document.getElementById("root");

		div.appendChild(p);*/
	}

	render() {
		return (
			<div>
				<Header title={this.state.title} changeTitle={this.changeTitle} />
				<Body ask={this.state.question} changeQuestion={this.changeQuestion} />
			</div>
		);
	}
}