import React, {Component} from 'react'
import {Route} from 'react-router-dom'
import Home from './Home'
import About from './About'

export default class Main extends Component {
  render () {
    return (
      <div id="main">
        <h1>Lexical Diversity Calculator</h1>
        <Route exact path="/" component={Home} />
        <Route path="/about" component={About} />
      </div>
    )
  }
}