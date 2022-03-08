import React, { Component } from "react";
import { Row, Col, Container, Form, Button, FormGroup } from "react-bootstrap";
import { NavLink } from "react-router-dom";
import axios from "axios";
import Cookies from "js-cookie";
export default class ReviewTile extends Component {
  render() {
    return (
      <Container>
        <h2>Restaurant id: {this.props.review[1].restaurant_id}</h2>
        <h2>Written by: {this.props.review[1].user_id} on {this.props.review[1].timestamp}</h2>
        <h2>Stars: {this.props.review[1].rating}</h2>
        <h2>Review: {this.props.review[1].content}</h2>
      </Container>
    );
  }
}
