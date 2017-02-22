var React = require('react');
var SearchField = require('./SearchFields.js');

var MyComponentClass = React.createClass({
    render: function () {
        return (
            <div>
             <SearchField placeholder="artist" message="events for artists related to "/>
             <SearchField placeholder="city" message="in"/>
            </div>
        );
    }
});

module.exports = MyComponentClass;