import React from 'react';
// import ReactDOM from 'react-dom';
// import './index.css';
import Question from './Body/Question';
import Reponse from './Body/Reponse';
import './css/style.css';


export default class Layout extends React.Component {

	render() {
		return(
			<article>
				<p>Test</p>
				<Question />
				<Reponse />
			</article>
		);
	}
}