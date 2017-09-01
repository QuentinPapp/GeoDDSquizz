import React from 'react';
import ReactDom from 'react-dom';
import citations from './citations';
import './index.css';

class App extends React.Component {

	state = {};

	genererCitation(event) {
		// On transforme les citations en array
		const keyArray = Object.keys(citations);
		// Une citation au hasard
		const randomKey = keyArray[Math.floor(Math.random() * keyArray.length)];
		this.setState(citations[randomKey]);
	};

	render() {
		return (
			<div>
				<p>
					{this.state.citation}
					<span>- {this.state.auteur}</span>
				</p>
				<button onClick={event => this.genererCitation(event)}>Une autre citation!</button>
			</div>
		)
	}
}

ReactDom.render(
	<App />,
	document.getElementById('root')
);