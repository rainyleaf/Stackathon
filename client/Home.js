import React, {Component} from 'react'
import {Link} from 'react-router-dom'
import axios from 'axios'
import json from 'circular-json'

export default class Home extends Component {
  constructor (props) {
    super(props)
    this.state = {
      results: '',
      loading: '',
      resultsHeading: ''
    }
    this.handleSubmitSingle = this.handleSubmitSingle.bind(this)
    this.handleSubmitArray = this.handleSubmitArray.bind(this)
    this.singleFileInput = React.createRef()
    this.arrayFilesInput = React.createRef()
  }
  async handleSubmitSingle(event){
    event.preventDefault()
    this.setState({loading: 'Your data is loading! This should take between 10 and 30 seconds depending on the size of your input.'})
    try {
      //console.log("SINGLEFILEINPUT: ", json.stringify(this.singleFileInput))
      var formData = new FormData();
      formData.append('file', this.singleFileInput.current.files[0]);
      const result = await axios.post('/api/process/single', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      console.log(result.data)
      this.setState({results: result.data, resultsHeading: 'File\tTokens\tTypes\tAverage types per 50 words', loading: ''})
    } catch (error) {
      console.error(error)
    }
  }
  async handleSubmitArray(event){
    event.preventDefault()
    try {
      var formData = new FormData();
      let fileslist = []
      for (let i = 0; i + 1 < Object.keys(this.arrayFilesInput.current.files).length; i++){
        console.log("file from current.files: ", this.arrayFilesInput.current.files[i])
        fileslist.push(this.arrayFilesInput.current.files[i])
      }
      fileslist = JSON.stringify(fileslist)
      formData.append('files', fileslist)
      console.log("formdata so far: ", formData)
      await axios.post('/api/process/array', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
    } catch (error) {
      console.error(error)
    }
  }
  render () {
    const resultsHeadings = this.state.resultsHeading.split('\t')
    const results = this.state.results.split('\t')
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
            Your output will appear below when the process is done running.
            <p />
            {this.state.loading}
            <table>
              <tbody>
                <tr>
                  <th>{resultsHeadings[0]}</th>
                  <th>{resultsHeadings[1]}</th>
                  <th>{resultsHeadings[2]}</th>
                  <th>{resultsHeadings[3]}</th>
                </tr>
                <tr>
                  <td>{results[0]}</td>
                  <td>{results[1]}</td>
                  <td>{results[2]}</td>
                  <td>{results[3]}</td>
                </tr>
              </tbody>
            </table>
        </div>
        </div>

        <div className="navlink-container">
        <Link to="/about">
          About this tool
        </Link>
        </div>
      </div>
    )
  }
}
