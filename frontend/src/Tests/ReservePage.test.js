import { render, screen } from "@testing-library/react";
import ReservePage from "../Pages/ReservePage";
import { BrowserRouter, Routes, Route } from "react-router-dom";

test("reserve page renders", () => {
    render(
      <BrowserRouter>
        <Routes>
          <Route path="*" element={<ReservePage />}></Route>
        </Routes>
      </BrowserRouter>
    );
    const title = screen.getByText("Reserve Page");
    expect(title).toBeInTheDocument();
  });

test("reserve page has restaurant name", () => {
  render(
    <BrowserRouter>
      <Routes>
        <Route path="*" element={<ReservePage />}></Route>
      </Routes>
    </BrowserRouter>
  );
  const name = screen.getByText("Enter the restaurant name");
  expect(name).toBeInTheDocument();
});

test("reserve page has restaurant details", () => {
    render(
      <BrowserRouter>
        <Routes>
          <Route path="*" element={<ReservePage />}></Route>
        </Routes>
      </BrowserRouter>
    );
    const details = screen.getByText("Enter the restaurant details");
    expect(details).toBeInTheDocument();
  });

  test("reserve page has submit button", () => {
    render(
      <BrowserRouter>
        <Routes>
          <Route path="*" element={<ReservePage />}></Route>
        </Routes>
      </BrowserRouter>
    );
    const submitlink = screen.getByText("Submit");
    expect(submitlink).toBeInTheDocument();
  });