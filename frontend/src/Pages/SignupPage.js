import React, { Component } from "react";
import { Row, Col, Container, Form, Button } from "react-bootstrap";
import { Navigate } from "react-router-dom";

export default class SignupPage extends Component {
  state = {
    email: "",
    password: "",
    role: "mentor",
    submitted: false,
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

  isValid = () => {
    var passw = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20}$/;
    if (this.state.password.match(passw)) {
      return true;
    }
    alert("Password not good enough");
    return false;
  };

  onSubmit = () => {
    if (!this.isValid()) {
      return;
    }
    var data = JSON.stringify({
      email: this.state.email,
      password: this.state.password,
      role: this.state.role,
    });
    // TODO: uncomment once API is live
    // var config = {
    //   method: "post",
    //   url: "createUser/",
    //   headers: {
    //     "Content-Type": "text/plain",
    //     "X-CSRFToken": Cookies.get("XSRF-TOKEN"),
    //   },
    //   data: data,
    //   withCredentials: true,
    // };

    // axios(config)
    //   .then((response) => {
    //     console.log(response.status);
    //     console.log(JSON.stringify(response.data));
    //     this.props.handler();
    //   })
    //   .catch(function (error) {
    //     console.log(error);
    //   });
    return <Navigate to="/home" />;
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
