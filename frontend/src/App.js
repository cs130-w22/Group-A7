import "./App.css";
import { HashRouter, Route, Routes } from "react-router-dom";
import { Nav, Navbar, Container } from "react-bootstrap";
import React, { Component } from "react";

import HomePage from "./Pages/HomePage";
import LandingPage from "./Pages/LandingPage";
import LoginPage from "./Pages/LoginPage";
import SignupPage from "./Pages/SignupPage";
import BrowsePage from "./Pages/BrowsePage";
import ReservePage from "./Pages/ReservePage";
import ReviewPage from "./Pages/ReviewPage";

class App extends Component {
  render() {
    return (
      <Container>
        <Navbar bg="primary" variant="dark">
          <Navbar.Brand href="#/">DineSmart</Navbar.Brand>
          <Nav className="mr-auto">
            <Nav.Link href="#/home">Home</Nav.Link>
            <Nav.Link href="#/login">Login</Nav.Link>
            <Nav.Link href="#/browse">Browse</Nav.Link>
            <Nav.Link href="#/reserve">Reserve</Nav.Link>
            <Nav.Link href="#/review">Review</Nav.Link>
          </Nav>
          {/* <Navbar.Collapse className="justify-content-end">
            <TryUsername user={this.state.user}></TryUsername>
            <Navbar.Text onClick={this.onSubmit}>
              <a href="#login">Logout</a>
            </Navbar.Text>
          </Navbar.Collapse> */}
        </Navbar>
        <HashRouter>
          <div className="App">
            <Routes>
              <Route exact path="/" element={<LandingPage/>} />
              <Route path="/home" element={<HomePage />} />
              <Route path="/login" element={<LoginPage />} />
              <Route path="/signup" element={<SignupPage />} />
              <Route path="/browse" element={<BrowsePage/>} />
              <Route path="/reserve/" element={<ReservePage/>} />
              <Route path="/review/" element={<ReviewPage/>} />
            </Routes>
          </div>
        </HashRouter>
      </Container>
    );
  }
}

export default App;
