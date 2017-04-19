import React from 'react';

export default class Reponse extends React.Component {

	render() {
		return(
			<article id="reponse" className="common result">
				<h3>Réponse</h3>
				<p id="answer">{this.props.reponse}</p>
				 <p>Blabla</p>
				<section className="button">
					<input type="submit" value="Suivant"/>
				</section>
			</article>
		);
	}
}