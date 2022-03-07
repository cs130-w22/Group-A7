import { render, screen } from "@testing-library/react";
import LoginPage from "../Pages/LoginPage";
import { BrowserRouter, Routes, Route } from "react-router-dom";

test("login page renders", () => {
  render(
    <BrowserRouter>
      <Routes>
        <Route path="*" element={<LoginPage />}></Route>
      </Routes>
    </BrowserRouter>
  );
  const title = screen.getByText("Login to your DineSmart account");
  expect(title).toBeInTheDocument();
});

test("login page has email", () => {
    render(
      <BrowserRouter>
        <Routes>
          <Route path="*" element={<LoginPage />}></Route>
        </Routes>
      </BrowserRouter>
    );
    const email = screen.getByText("Email address");
    expect(email).toBeInTheDocument();
  });
  
  test("login page has pwd", () => {
    render(
      <BrowserRouter>
        <Routes>
          <Route path="*" element={<LoginPage />}></Route>
        </Routes>
      </BrowserRouter>
    );
    const pass = screen.getByText("Password");
    expect(pass).toBeInTheDocument();
  });

  test("login page has submit", () => {
    render(
      <BrowserRouter>
        <Routes>
          <Route path="*" element={<LoginPage />}></Route>
        </Routes>
      </BrowserRouter>
    );
    const submit = screen.getByText("Submit");
    expect(submit).toBeInTheDocument();
  });

  test("login page has link to signup", () => {
    render(
      <BrowserRouter>
        <Routes>
          <Route path="*" element={<LoginPage />}></Route>
        </Routes>
      </BrowserRouter>
    );
    const signup = screen.getByText("Don't have an account? Make one here.");
    expect(signup).toBeInTheDocument();
  });