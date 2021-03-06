import React, {Component} from 'react'
import {Link} from 'react-router-dom'
import axios from 'axios'

export default class Home extends Component {
  constructor (props) {
    super(props)
    this.state = {
      results: '',
      loading: '',
      resultsHeading: '',
      chunkSize: 50
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
      var formData = new FormData();
      formData.append('file', this.singleFileInput.current.files[0]);
      const result = await axios.post('/api/process/single', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      this.setState({results: result.data, resultsHeading: 'File\tTokens\tTypes\tAverage types per 50 words', loading: ''})
    } catch (error) {
      console.error(error)
    }
  }
  async handleSubmitArray(event){
    event.preventDefault()
    this.setState({loading: 'Your data is loading! This should take between 10 and 30 seconds depending on the size of your input.'})
    try {
      var formData = new FormData();
      for (let i = 0; i < Object.keys(this.arrayFilesInput.current.files).length; i++){
        formData.append('files', this.arrayFilesInput.current.files[i])
      }
      const result = await axios.post('/api/process/array', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      this.setState({results: result.data, resultsHeading: 'File\tTokens\tTypes\tAverage types per 50 words', loading: ''})
    } catch (error) {
      console.error(error)
    }
  }
  render () {
    const resultsHeadings = this.state.resultsHeading.split('\t')
    let results;
    if (Array.isArray(this.state.results)){
      results = this.state.results
      results = results.filter(item => item.length > 0)
      for (let i = 0; i < results.length; i++){
        results[i] = results[i].split('\t')
      }
    }
    else {
      results = [this.state.results.split('\t')]
    }
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
                {results.map(resultline => (
                  <tr key={resultline}>
                    <td>{resultline[0]}</td>
                    <td>{resultline[1]}</td>
                    <td>{resultline[2]}</td>
                    <td>{resultline[3]}</td>
                  </tr>
                ))}
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
