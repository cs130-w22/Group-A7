import React, { Component } from "react";
import { Row, Col, Container, Form, Button, FormGroup } from "react-bootstrap";
import { NavLink } from "react-router-dom";
import AccountDetails from "../Components/AccountDetails";

export default class ProfilePage extends Component {
  state = {
    account: null,
  };
  componentDidMount() {
    axios({
      method: "post",
      url: "http://localhost:8000/getProfile/",
      headers: {
        "Content-Type": "text/plain",
        "X-CSRFToken": Cookies.get("XSRF-TOKEN"),
      },
      withCredentials: "false",
    })
      .then((response) => {
        if (response.data !== "") {
          this.setState({ account: response.data });
        }
      })
      .catch(function (error) {
        console.log(error);
      });
  }
  render() {
    return (
      <Container>
        <h1>Your profile</h1>
        <AccountDetails account={this.state.account} />
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
