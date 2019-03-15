import React from 'react'
import {Link} from 'react-router-dom'

const About = (props) => {

  return (
    <div id="about">
      <div id="about-text">
        This tool takes one or more text files as input and processes the file(s) to clean them of punctuation and run the resulting cleaned file(s) through the TreeTagger lemmatizer and part-of-speech tagger.
        <p />
        From there, your texts are passed to scripts that calculate various lexical diversity indices in each text.
        <p />
        In this version of the tool, the measures included are:
        <ul>
          <li>Moving-average type-token ratio: calculates the average type-token ratio per a certain number of tokens. The "chunk size" is defaulted to 50, but will be able to be chosen by the user in future versions.</li>
        </ul>
        <p />
      </div>
      <Link to="/">
            Back to home
      </Link>
    </div>
  )
}

export default About
