import React from 'react';

export default class Reponse extends React.Component {

	render() {
		return(
			<article className="common result">
				<h3>Réponse</h3>
				<p>Blabla</p>
				<section className="button">
					<input type="submit" value="Suivant"/>
				</section>
			</article>
		);
	}
}