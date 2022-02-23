import React, { Component } from "react";
import {  NavLink } from "react-router-dom";
import { Row, Col, Container, Form, Button } from "react-bootstrap";

export default class LoginPage extends Component {
  state = {
    email: "",
    password: "",
    loggedIn: false,
  };

  render() {
    return (
      <Container>
        <h1>Login to your DineSmart account</h1>
        <Form>
          <Form.Group controlId="formBasicEmail">
            <Form.Label>Email address</Form.Label>
            <Form.Control
              type="email"
              placeholder="Enter email"
              value={this.state.email}
              onChange={(e) => this.setState({ email: e.target.value })}
            />
            <Form.Text className="text-muted">
              We'll never share your email with anyone else.
            </Form.Text>
          </Form.Group>
          <Form.Group controlId="formBasicPassword">
            <Form.Label>Password</Form.Label>
            <Form.Control
              type="password"
              placeholder="Password"
              value={this.state.password}
              onChange={(e) => this.setState({ password: e.target.value })}
            />
          </Form.Group>
          <Col>
            <Row>
              <NavLink to="/home/" onClick={this.onSubmit}>
                Submit
              </NavLink>
            </Row>
            <Row>
              <Button href="#/signup/" variant="outline-secondary">
                Don't have an account? Make one here.
              </Button>
            </Row>
          </Col>
        </Form>
      </Container>
    );
  }
}
