import React, { Component } from "react";
import { Row, Col, Container, Form, Button, FormGroup } from "react-bootstrap";
import { NavLink } from "react-router-dom";
import RestaurantTile from "./RestaurantTile";
export default class ListRestaurants extends Component {
  render() {
    const listItems = Object.entries(this.props.restaurants).map(
      ([name, details]) => <RestaurantTile name={name} details={details}/>
    );
    return <Container>{listItems}</Container>;
  }
}
