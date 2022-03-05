import React, { Component } from "react";
import {  Navigate } from "react-router-dom";
import { Row, Col, Container, Form, Button } from "react-bootstrap";

export default class LoginPage extends Component {
  state = {
    email: "",
    password: "",
    loggedIn: false,
  };

  componentDidMount() {
    // TODO: uncomment once API is live
    // axios({
    //   method: "post",
    //   url: "getCurrentUser/",
    //   headers: {
    //     "Content-Type": "text/plain",
    //     "X-CSRFToken": Cookies.get("XSRF-TOKEN"),
    //   },
    //   withCredentials: true,
    // })
    //   .then((response) => {
    //     if (response.data !== "") {
    //       this.setState({ loggedIn: true });
    //     }
    //   })
    //   .catch(function (error) {
    //     console.log(error);
    //   });
  }

  onSubmit = () => {
    var data = JSON.stringify({
      email: this.state.email,
      password: this.state.password,
    });
    // TODO: uncomment once API is live
    // axios({
    //   method: "post",
    //   url: "login/",
    //   headers: {
    //     "Content-Type": "text/plain",
    //     "X-CSRFToken": Cookies.get("XSRF-TOKEN"),
    //   },
    //   data: data,
    //   withCredentials: true,
    // })
    //   .then((response) => {
    //     console.log(response.status);
    //     console.log(JSON.stringify(response.data));
    //     this.props.handler();
    //   })
    //   .catch(function (error) {
    //     console.log(error);
    //   });
    console.log('in login submit')
    window.location.href='/home'
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
              <Button onClick={this.onSubmit}>Submit</Button>
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
