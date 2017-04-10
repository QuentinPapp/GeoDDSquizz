import React from 'react';
// import ReactDOM from 'react-dom';


export default class Question extends React.Component {

	render() {
		return(
			<article className="common content">
				<h3>Question</h3>
				<p>{this.props.ask}</p>
					<label><input type="radio" name="n"/>{this.props.rep[0]}</label>
					<label><input type="radio" name="n"/>{this.props.rep[1]}</label>
					<label><input type="radio" name="n"/>{this.props.rep[2]}</label>
					<section className="button">
						<input type="button" value="Valider" onClick={this.props.envoie} />
					</section>

			</article>
		);
	}
}