import React, { Component } from "react";
import { Row, Col, Container, Form, Button, FormGroup } from "react-bootstrap";
import { NavLink } from "react-router-dom";
import axios from "axios";
import Cookies from "js-cookie";

import AccountDetails from "../Components/AccountDetails";
import ListReviews from "../Components/ListReviews";
export default class ProfilePage extends Component {
  state = {
    account: {
        name: 'dummy'
    }
  };
  componentDidMount() {
    axios({
      method: "post",
      url: "http://localhost:8000/getUserProfile/",
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
        <h2>Your reviews</h2>
        <ListReviews/>
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
