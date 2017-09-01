import React from "react";

import Question from "./Body/Question";

export default class Body extends React.Component {
	constructor(props) {
		super(props);
		this.addQuestion = this.addQuestion.bind(this);
	}

	addQuestion(e) {
		const question = e.target.value;
		this.props.changeQuestion(question);
	}

	render() {
		return (
			<div>
				<Question ask={this.props.ask} />
				<input onChange={this.addQuestion}/>
			</div>
		)
	}
}