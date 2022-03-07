import { render, screen } from "@testing-library/react";
import ReviewPage from "../Pages/ReviewPage";
import { BrowserRouter, Routes, Route } from "react-router-dom";

test("review page renders", () => {
  render(
    <BrowserRouter>
      <Routes>
        <Route path="*" element={<ReviewPage />}></Route>
      </Routes>
    </BrowserRouter>
  );
  const title = screen.getByText("Review Page");
  expect(title).toBeInTheDocument();
});

test("review page has restaurant name", () => {
    render(
      <BrowserRouter>
        <Routes>
          <Route path="*" element={<ReviewPage />}></Route>
        </Routes>
      </BrowserRouter>
    );
    const name = screen.getByText("Enter the restaurant name");
    expect(name).toBeInTheDocument();
  });
  
  test("review page has restaurant rating", () => {
    render(
      <BrowserRouter>
        <Routes>
          <Route path="*" element={<ReviewPage />}></Route>
        </Routes>
      </BrowserRouter>
    );
    const rating = screen.getByText("Rating");
    expect(rating).toBeInTheDocument();
  });
  
  test("review page has restaurant details", () => {
    render(
      <BrowserRouter>
        <Routes>
          <Route path="*" element={<ReviewPage />}></Route>
        </Routes>
      </BrowserRouter>
    );
    const detials = screen.getByText("Enter your review here");
    expect(detials).toBeInTheDocument();
  });

  test("review page has submit button", () => {
    render(
      <BrowserRouter>
        <Routes>
          <Route path="*" element={<ReviewPage />}></Route>
        </Routes>
      </BrowserRouter>
    );
    const submitlink = screen.getByText("Submit");
    expect(submitlink).toBeInTheDocument();
  });