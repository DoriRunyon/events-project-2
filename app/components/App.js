var React = require('react');
var SearchField = require('./SearchFields.js')

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
             <SearchField placeholder="artist"/>
             <SearchField placeholder="city"/>
            </div>
        );
    }
});

module.exports = MyComponentClass;