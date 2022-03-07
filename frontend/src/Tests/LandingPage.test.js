import { render, screen } from "@testing-library/react";
import LandingPage from "../Pages/LandingPage";
import { BrowserRouter, Routes, Route } from "react-router-dom";

test("landing page renders", () => {
  render(
    <BrowserRouter>
      <Routes>
        <Route path="*" element={<LandingPage />}></Route>
      </Routes>
    </BrowserRouter>
  );
  const title = screen.getByText("Welcome to DineSmart");
  expect(title).toBeInTheDocument();
});

test("landing page has login link", () => {
  render(
    <BrowserRouter>
      <Routes>
        <Route path="*" element={<LandingPage />}></Route>
      </Routes>
    </BrowserRouter>
  );
  const loginlink = screen.getByText("Login");
  expect(loginlink).toBeInTheDocument();
});
