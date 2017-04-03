import React from "react";

import Question from "./Body/Question";
import Resultat from "./Body/Resultat";

export default class Body extends React.Component {

	render() {
		return (
			<article>
				<Question />
				<Resultat />
			</article>
		);
	}
}