import React, { Component } from "react";
import { Row, Col, Container, Form, Button, FormGroup } from "react-bootstrap";
import { NavLink } from "react-router-dom";

export default class RestaurantTile extends Component {
  render() {
    return (
      <Container>
        <h1>{this.props.name}</h1>
        <h2>{this.props.details.distance} miles away</h2>
        <h2>Times: {this.props.details.times.join(", ")}</h2>
        <h2>Price: {this.props.details.price}</h2>
        <h2>{this.props.details.cuisine}</h2>
        {/* link to book the restaurant */}
      </Container>
    );
  }
}
