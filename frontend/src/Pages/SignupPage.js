import React, { Component } from "react";
import { Row, Col, Container, Form, Button } from "react-bootstrap";

export default class SignupPage extends Component {
  state = {
    email: "",
    password: "",
    role: "mentor",
    submitted: false,
    loggedIn: false,
  };

  render() {
    return (
      <Container>
        <h1>Signup for a DineSmart account</h1>
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
            <Form.Text className="text-muted">
              Password must be between 6 to 20 characters which contain at least
              one numeric digit, one uppercase and one lowercase letter.
            </Form.Text>
          </Form.Group>
          <Col>
            <Row>
              <Button onClick={this.onSubmit}>Submit</Button>
            </Row>
            <Row>
              <Button href="#/login/" variant="outline-secondary">
                Already have an account? Sign in here.
              </Button>
            </Row>
          </Col>
        </Form>
      </Container>
    );
  }
}
