import React from 'react';
// import ReactDOM from 'react-dom';
// import './index.css';
import Question from './Body/Question';
import Reponse from './Body/Reponse';
import './css/style.css';


export default class Layout extends React.Component {

	constructor(props) {
		super(props);
		this.state = {
			data : '',
			question : '',
			// reponse : '',
			proposition : '',
			count : 0
		};

		fetch('http://camillec.dijon.codeur.online/react/hello-world/liste.json')
			.then(res => {
				return res.json();
			})
			.then(res => {
				this.setState({data : res /*JSON.stringify(res)*/});
				/*console.log(this.state.data);*/
				this.setState({question : this.state.data.questions[this.state.count][0].question});
				this.setState({proposition : this.state.data.questions[this.state.count][0].propositions});

				this.setState({count : this.state.count + 1});
			});

	this.getData=this.getData.bind(this);

	}

	getData() {
		// var questions= this.state.data.questions;
		// for (var i = 0; i < questions; i++) {
		// }
		this.setState({count : this.state.count + 1});
		this.setState({question : this.state.data.questions[this.state.count][0].question});
		this.setState({proposition : this.state.data.questions[this.state.count][0].propositions});
		
		
	}

	render() {
		return(
			<article>
				<Question ask={this.state.question} rep={this.state.proposition} envoie={this.getData} />
				<Reponse />
			</article>
		);
	}
}