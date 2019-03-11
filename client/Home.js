import React, {Component} from 'react'
import {Link} from 'react-router-dom'
import axios from 'axios'

export default class Home extends Component {
  constructor () {
    super()
    this.state = {
    }
  }

  render () {
    return (
      <div id="home">
        <Link to="/about">
          About this tool
        </Link>
      </div>
    )
  }
}
