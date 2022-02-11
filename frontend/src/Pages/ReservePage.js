import React, { Component } from "react";
import { Row, Col, Container, Form, Button, FormGroup } from "react-bootstrap";
import {  NavLink } from "react-router-dom";

export default class ReservePage extends Component {
  state = {
    restauarantName: "",
    reservationDetails: "",
    loggedIn: false,
  };
  render() {
    return (
      <Container>
        <h1>Reserve Page</h1>
        <Form>
          <Form.Group>
            <Form.Label>Enter the restaurant name</Form.Label>
            <Form.Control
              type="text"
              placeholder="Enter restaurant"
              value={this.state.restauarantName}
              onChange={(e) =>
                this.setState({ restauarantName: e.target.value })
              }
            />
          </Form.Group>
          <Form.Group>
            <Form.Label>Enter the restaurant details</Form.Label>
            <Form.Control
              type="text"
              placeholder="Enter details"
              value={this.state.reservationDetails}
              onChange={(e) =>
                this.setState({ reservationDetails: e.target.value })
              }
            />
          </Form.Group>
        </Form>
        <NavLink to="/home/" onClick={this.onSubmit}>
          Submit
        </NavLink>
      </Container>
    );
  }
}
