import React from "react";

import Header from "./Header";
import Body from "./Body";
import '../css/style_n.css';
import '../App.css';

export default class Layout extends React.Component {

	constructor(props) {
		super(props);

		this.state = {
			data : "",
			question: "",
			reponse: "",
			propositions: [],
			indice: 0,
			score: 0
		};

		fetch('http://nabilb.dijon.codeur.online:11001/', {
		    method: 'GET',
		    credentials: 'include',
		    headers: {
		    	'Origin' : 'http://nabilb.dijon.codeur.online:3000/',
		    	/*'Access-Control-Request-Method': 'GET',*/
		    }
		})
		.then((res) => {
			return res.json();
		})
		.then((res) => {
			this.setState({data : res});
			this.setState({question : this.state.data[this.state.indice].question});
			this.setState({propositions: this.state.data[this.state.indice].propositions});
		})
		.catch(function (error) {  
		  console.log(error);
		});

		this.checkRep = this.checkRep.bind(this);

	}

	checkRep() {

		var form = new FormData();
		form.append("question", this.state.indice);
		form.append("reponse", document.querySelector('input[name="choice"]:checked').value);

		fetch('http://nabilb.dijon.codeur.online:11001/check', {
		    method: 'POST',
		    credentials: 'include',
		    headers: {
		    	'Origin' : 'http://nabilb.dijon.codeur.online:3000/',
		    },
		  	body: form
		})
		.then((res) => {
			return res.text();
		})
		.then((res) => { 
		  if (res === "True") {
		  	var ok = document.createElement("img");
		  	var p1 = document.getElementById("test").firstChild;
		  	ok.className = "show";
		  	ok.src = "http://nabilb.dijon.codeur.online/geoquizz/ressources/check.png";
		  	document.getElementById("test").replaceChild(ok,p1);
		  	setTimeout(() => {
		  		this.setState({indice : this.state.indice + 1});
		  		this.setState({question : this.state.data[this.state.indice].question});
				this.setState({propositions: this.state.data[this.state.indice].propositions});
				document.getElementById("test").replaceChild(p1,ok);
				document.querySelector('input:checked').checked = false;
		  	}, 2000);

		  	this.setState({score: this.state.score + 1});
		  }	else {
		  		var nok = document.createElement("img");
			  	var p2 = document.getElementById("test").firstChild;
			  	nok.className = "show";
			  	nok.src = "http://nabilb.dijon.codeur.online/geoquizz/ressources/croix.png";
			  	document.getElementById("test").replaceChild(nok,p2);

			  	setTimeout(() => {
		  		this.setState({indice : this.state.indice + 1});
		  		this.setState({question : this.state.data[this.state.indice].question});
				this.setState({propositions: this.state.data[this.state.indice].propositions});
				document.getElementById("test").replaceChild(p2,nok);
				document.querySelector('input:checked').checked = false;
		  	}, 2000);
		  	}
		})	
		.catch(function (error) {  
		  console.log("nok", error);
		});
	}

	render() {
		return (
			<div>
				<Header />
				<Body reponse={this.state.reponse} question={this.state.question} propositions={this.state.propositions} checkRep={this.checkRep} score={this.state.score}/>
			</div>
		);
	}
}