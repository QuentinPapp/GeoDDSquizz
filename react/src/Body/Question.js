import React from 'react';

export default class Layout extends React.Component {

	render() {
		return(
			<article className="common content">
				<p>Question</p>
				<label><input type="radio" name="n"/>Choix 1</label>
				<label><input type="radio" name="n"/>Choix 2</label>
				<label><input type="radio" name="n"/>Choix 3</label>
			</article>
		);
	}
}