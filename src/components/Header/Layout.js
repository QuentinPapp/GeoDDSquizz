import React from "react";

import Header from "./Header";
import Body from "./Body";
import Footer from "./Footer";


export default class Layout extends React.Component {

	constructor(props) {
		super(props);

		this.state = {
			data : "",
			question: "",
			reponse: "Résultat",
			propositions: [],
			count: 0
		};

		fetch('http://nabilb.dijon.codeur.online:11001/', {
		    method: 'POST',
		    headers: {
		    	'Origin' : 'http://nabilb.dijon.codeur.online:3001/',
		    	'Access-Control-Request-Method': 'POST',
		    }
		})
		.then((res) => {
			return res.json();
		})
		.then((res) => {
			var i = Math.floor(Math.random() * 19);
			this.setState({data : res});
			this.setState({question : this.state.data[i].question});
			this.setState({propositions: this.state.data[i].propositions});
		})
		.catch(function (error) {  
		  console.log(error);
		});

		this.checkRep = this.checkRep.bind(this);

	}

	checkRep() {
		fetch('http://faridl.dijon.codeur.online:11001/check', {
		    method: 'POST',
		    headers: {
		    	'Origin' : 'http://nabilb.dijon.codeur.online:3001/',
		    },
		    body: JSON.stringify({
		    reponse: document.querySelector('input[name="choice"]:checked').value
		  	})
		})
		.then((res) => {
			return res.json();
		})
		.then((res) => { 
		  if (res) {
		  	var ok = document.createElement("img");
		  	var p1 = document.getElementById("test").firstChild;
		  	ok.className = "show";
		  	ok.src = "http://nabilb.dijon.codeur.online/geoquizz/ressources/check.png";
		  	document.getElementById("test").replaceChild(ok,p1);
		  	/*this.setState({reponse : document.querySelector('input[name="choice"]:checked').value});*/
		  	setTimeout(() => {
		  		var i = Math.floor(Math.random() * 19);
		  		this.setState({question : this.state.data[i].question});
				this.setState({propositions: this.state.data[i].propositions});
		  	}, 2000);
		  }	else {
		  		var nok = document.createElement("img");
			  	var p2 = document.getElementById("test").firstChild;
			  	nok.className = "show";
			  	nok.src = "http://nabilb.dijon.codeur.online/geoquizz/ressources/croix.png";

			  	document.getElementById("test").replaceChild(nok,p2);
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
				<Body reponse={this.state.reponse} question={this.state.question} propositions={this.state.propositions} checkRep={this.checkRep} count={this.state.count} />
				<Footer />
			</div>
		);
	}
}