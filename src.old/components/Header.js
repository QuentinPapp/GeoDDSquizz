import React from "react";

import Title from "./Header/Title";

export default class Header extends React.Component {
	constructor(props) {
		super(props);
		this.handleChange = this.handleChange.bind(this);
	}
	
	handleChange(e) {
		const title = e.target.value;
		this.props.changeTitle(title);
	}

	render() {
		return (
			<div>
				<Title title={this.props.title}/>
				<input value={this.props.title} onChange={this.handleChange} />
			</div>
		);
	}
}