import React, { Component } from "react";
import { Row, Col, Container, Form, Button, FormGroup } from "react-bootstrap";
import { NavLink } from "react-router-dom";

export default class ReviewTile extends Component {
  render() {
    return (
      <Container>
        <h1>{this.props.review.restaurant}</h1>
        <h1>{this.props.review.author}</h1>
        <h1>{this.props.review.rating}</h1>
        <h1>{this.props.review.content}</h1>
      </Container>
    );
  }
}
