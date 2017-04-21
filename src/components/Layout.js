import React from "react";

import Header from "./Header";
import Body from "./Body";

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
		    	'Origin' : 'http://nabilb.dijon.codeur.online:3001/',
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
			    	'Origin' : 'http://nabilb.dijon.codeur.online:3001/',
			    },
			  	body: form
			})
			.then((res) => {
				return res.json();
			})
			.then((res) => {
			  if (res[0].resultat === "True") {

			  	var rep_ok  = document.querySelector('input[name="choice"]:checked').parentNode;
				rep_ok.classList.add("ok");

				this.setState({indice : this.state.indice + 1});

				if (this.state.indice <= 18) {
				  	setTimeout(() => {
				  		this.setState({question : this.state.data[this.state.indice].question});
						this.setState({propositions: this.state.data[this.state.indice].propositions});
						rep_ok.classList.remove("ok");
						document.querySelector('input:checked').checked = false;
				  	}, 1000);
			  	} else {
			  		var end_ok = document.createElement("h3");
					var txt_ok = document.createTextNode("Partie terminée !! Prochaine partie dans 5 secondes ...");

					end_ok.appendChild(txt_ok);

					var q_ok = document.getElementById("ask").firstChild;

					document.getElementById("ask").replaceChild(end_ok,q_ok);
					setTimeout(() => {
						window.location.reload();
					}, 5000);
			  	}

			  	this.setState({score: res[0].score});
			  }	else {
				  	if (this.state.indice <= 18) {
					  	var rep_nok  = document.querySelector('input[name="choice"]:checked').parentNode;
					  	rep_nok.classList.add("nok");

					  	this.setState({indice : this.state.indice + 1});

					  	setTimeout(() => {
					  		this.setState({question : this.state.data[this.state.indice].question});
							this.setState({propositions: this.state.data[this.state.indice].propositions});
							rep_nok.classList.remove("nok");
							document.querySelector('input:checked').checked = false;
					  	}, 1000);
				  	} else {
				  		var end_nok = document.createElement("h3");
						var txt_nok = document.createTextNode("Partie terminée !! Prochaine partie dans 5 secondes ...");

						end_nok.appendChild(txt_nok);

						var q_nok = document.getElementById("ask").firstChild;

						document.getElementById("ask").replaceChild(end_nok,q_nok);
						setTimeout(() => {
							window.location.reload();
						}, 5000);
			  		}	
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