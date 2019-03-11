import React, {Component} from 'react'
import {Link} from 'react-router-dom'
import axios from 'axios'
import json from 'circular-json'

export default class Home extends Component {
  constructor (props) {
    super(props)
    this.handleSubmitSingle = this.handleSubmitSingle.bind(this)
    this.handleSubmitArray = this.handleSubmitArray.bind(this)
    this.singleFileInput = React.createRef()
    this.arrayFilesInput = React.createRef()
  }
  async handleSubmitSingle(event){
    event.preventDefault()
    try {
      //console.log("SINGLEFILEINPUT: ", json.stringify(this.singleFileInput))
      var formData = new FormData();
      formData.append('file', this.singleFileInput.current.files[0]);
      await axios.post('/api/process/single', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
    } catch (error) {
      console.error(error)
    }
  }
  async handleSubmitArray(event){
    event.preventDefault()
    try {
      await axios.post('/api/process/array', this.arrayFilesInput)
    } catch (error) {
      console.error(error)
    }
  }
  render () {
    return (
      <div id="home">
        <div id="fileInput">
        <form onSubmit={this.handleSubmitSingle} encType="multipart/form-data">
            <input type="file" ref={this.singleFileInput} name="file" accept=".txt" multiple={false} />
            <button type="submit">Upload</button>
        </form>
        <p />
        <form onSubmit={this.handleSubmitArray} encType="multipart/form-data">
            <input type="file" ref={this.arrayFilesInput} name="files" accept=".txt" multiple={true} />
            <button type="submit">Upload multiple</button>
        </form>
        <p />
        <div>
            This is where the output will go when the process is done running.
        </div>
        </div>
        <Link to="/about">
          About this tool
        </Link>
      </div>
    )
  }
}
