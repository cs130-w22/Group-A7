import { render, screen } from "@testing-library/react";
import SignupPage from "../Pages/SignupPage";
import { BrowserRouter, Routes, Route } from "react-router-dom";

test("signup page renders", () => {
  render(
    <BrowserRouter>
      <Routes>
        <Route path="*" element={<SignupPage />}></Route>
      </Routes>
    </BrowserRouter>
  );
  const title = screen.getByText("Signup for a DineSmart account");
  expect(title).toBeInTheDocument();
});

test("signup page has email", () => {
    render(
      <BrowserRouter>
        <Routes>
          <Route path="*" element={<SignupPage />}></Route>
        </Routes>
      </BrowserRouter>
    );
    const email = screen.getByText("Email address");
    expect(email).toBeInTheDocument();
  });
  
  test("signup page has pwd", () => {
    render(
      <BrowserRouter>
        <Routes>
          <Route path="*" element={<SignupPage />}></Route>
        </Routes>
      </BrowserRouter>
    );
    const pass = screen.getByText("Password");
    expect(pass).toBeInTheDocument();
  });

  test("signup page has submit", () => {
    render(
      <BrowserRouter>
        <Routes>
          <Route path="*" element={<SignupPage />}></Route>
        </Routes>
      </BrowserRouter>
    );
    const submit = screen.getByText("Submit");
    expect(submit).toBeInTheDocument();
  });

  test("signup page has link to signin", () => {
    render(
      <BrowserRouter>
        <Routes>
          <Route path="*" element={<SignupPage />}></Route>
        </Routes>
      </BrowserRouter>
    );
    const signin = screen.getByText("Already have an account? Sign in here.");
    expect(signin).toBeInTheDocument();
  });