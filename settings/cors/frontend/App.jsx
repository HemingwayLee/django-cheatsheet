import React from 'react';

class App extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      message: "default message"
    }; 
  }
  
  sendRequest2Django(e) {
    e.preventDefault();
    fetch('http://127.0.0.1:8000/hello/', { 
      // body: JSON.stringify(data), 
      // cache: 'no-cache', 
      // credentials: 'same-origin', 
      // headers: {
      //   'content-type': 'application/json'
      // },
      method: 'GET', 
      // mode: 'cors', 
      // redirect: 'follow', 
      // referrer: 'no-referrer', 
    })
    .then(function(response) {
      return response.json(); 
    })
    .then(function(myJson) {
      console.log(myJson);
      this.setState({message: myJson.data});
    }.bind(this)).catch((error) => {
      console.log(error);
    });
  }

  render() {
    return (
      <div>
        <div>{ this.state.message }</div>
        <div>
          <button onClick={e => this.sendRequest2Django(e)}>I will update content</button>
        </div>
      </div>
    );
  }
}

export default App;
