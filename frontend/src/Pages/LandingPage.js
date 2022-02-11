import React, { Component } from "react";
import { Row, Col, Container, Form, Button, FormGroup } from "react-bootstrap";
import {  NavLink } from "react-router-dom";

export default class LandingPage extends Component {
  render() {
    return (
      <Container>
        <h1>Welcome to DineSmart</h1>
        <p>DineSmart helps you discover and make reservations at local restaurants.</p>
        <NavLink to="#/login/">
          Login
        </NavLink>
      </Container>
    )
  }
}

