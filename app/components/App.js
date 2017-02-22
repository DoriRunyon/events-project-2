var React = require('react');

var MyComponentClass = React.createClass({
    getInitialState: function () {
        return {
            userInput: ''
    };
},
    handleUserInput: function (e) {
        this.setState({userInput: e.target.value});
    },
    render: function () {
        return (
            <div>
             <input type="text" onChange={this.handleUserInput} value={this.state.userInput}/>
             <h1>{this.state.userInput}</h1>
            </div>
        );
    }
});

module.exports = MyComponentClass;