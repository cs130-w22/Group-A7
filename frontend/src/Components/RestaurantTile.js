import React, { Component } from "react";
import { Row, Col, Container, Form, Button, FormGroup } from "react-bootstrap";
import { NavLink } from "react-router-dom";

export default class RestaurantTile extends Component {
  render() {
    return (
      <Container>
        <h2>{this.props.name}</h2>
        <h3>{this.props.details.tag}</h3>
        <h3>Times: {this.props.details.times.join(", ")}</h3>
        <a
          href={`#/restaurant?name=${this.props.name}`}
        >
          See reviews
        </a>
        <br></br>
        <a
          target="_blank"
          rel="noopener noreferrer"
          href={this.props.details.link}
        >
          Make booking here
        </a>
      </Container>
    );
  }
}
