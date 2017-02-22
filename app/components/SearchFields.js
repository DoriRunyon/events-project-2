var React = require('react');

var SearchField = React.createClass({
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
             <input type="text" placeholder={this.props.placeholder} onChange={this.handleUserInput} value={this.state.userInput}/>
             <h1>{this.state.userInput}</h1>
            </div>
        );
    }
});

module.exports = SearchField;