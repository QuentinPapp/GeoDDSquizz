import React from "react";

/*import Header from "./Header";
import Layout from "./Layout";*/
/*import Body from "./Body";*/
/*import Footer from "./Footer";*/


export default class Log extends React.Component {

	constructor(props) {
		super(props);
		this.state = {
			username: "",
			score : 0
		};

		this.handleChange = this.handleChange.bind(this);
		/*this.handleSubmit = this.handleSubmit.bind(this);*/
		this.sendName = this.sendName.bind(this);
	}

	handleChange(event) {
		this.setState({"username": event.target.value});
	}

	/*handleSubmit(event) {
		alert('A name was submitted: ' + this.state.value);
		event.preventDefault();
	}*/

	sendName() {
		var form = new FormData();
		form.append("username", this.state.value);
		form.append("score", this.state.value);

		fetch('http://faridl.dijon.codeur.online:11001/connexion', {
		    method: 'POST',
		    /*credentials: 'include',*/
		    headers: {
		    	'Origin' : 'http://nabilb.dijon.codeur.online:3001/',
		    },
		  	body: form
		})
		.then((res) => {
			console.log(res);
		})
	}
		

	render() {
		return (
			<section>
				{/*<Header />*/}
			<form>
				<label>
				  Name:
				  <input type="text" value={this.state.username} onChange={this.handleChange} />
				</label>
				<label>
				  score:
				  <input type="text" value={this.state.score} />
				</label>	
			</form>
			<input type="submit" value="Submit" onClick={this.sendName}/>
			{/*<Footer />*/}
			</section>
		);
	}//fin de render


}//fin de class