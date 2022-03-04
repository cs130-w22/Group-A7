import React, { Component } from "react";
import { Row, Col, Container, Form, Button, FormGroup } from "react-bootstrap";
import { NavLink } from "react-router-dom";

export default class HomePage extends Component {
  render() {
    return (
      <Container>
        <h1>Your reservations</h1>
        <p>Here are your reservations: </p>
        <Col>
          <Row>
            <NavLink to="/browse/">Browse local restaurants</NavLink>
          </Row>
          <Row>
            <NavLink to="/reserve/">Know what you want? Make a booking</NavLink>
          </Row>
        </Col>
      </Container>
    );
  }
}
