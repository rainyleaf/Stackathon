import React from 'react'
import {Link} from 'react-router-dom'

const About = (props) => {

  return (
    <div id="about">
      <div id="about-text">
        <p>
          This is a very cool tool.
        </p>
      </div>
      <Link to="/">
            Back to home
      </Link>
    </div>
  )
}

export default About
