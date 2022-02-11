import React, { Component } from "react";
import { Row, Col, Container, Form, Button, FormGroup } from "react-bootstrap";
import {  NavLink } from "react-router-dom";

export default class BrowsePage extends Component {
  state = {
    date: "",
    loggedIn: false,
  };
  render() {
    return (
      <Container>
        <h1>Browse Page</h1>
        <Form>
          <Form.Group controlId="date">
            <Form.Label>Date</Form.Label>
            <Form.Control
              as="select"
              custom
              onChange={(e) => this.setState({ date: e.target.value })}
            >
              <option value="">Choose...</option>
              <option>Saturday</option>
              <option>Sunday</option>
            </Form.Control>
          </Form.Group>
        </Form>
        <p>Select from the following restaurants:</p>
        <NavLink to="#/reserve/" onClick={this.makeBooking}>
          Make a booking
        </NavLink>
      </Container>
    );
  }
}
