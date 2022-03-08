import { render, screen } from "@testing-library/react";
import ReviewTile from "../Components/ReviewTile";
import { BrowserRouter, Routes, Route } from "react-router-dom";

test("review author shows", () => {
  const review =
    [0,
    {
      restaurant_id: "0",
      timestamp: "2022",
      user_id: "john",
      rating: "5",
      content: "abc",
    }];
  render(
    <BrowserRouter>
      <Routes>
        <Route path="*" element={<ReviewTile review={review} />}></Route>
      </Routes>
    </BrowserRouter>
  );
  const name = screen.getByText("Written by: john on 2022");
  expect(name).toBeInTheDocument();
});

test("review stars shows", () => {
    const review =
      [0,
      {
        restaurant_id: "0",
        timestamp: "2022",
        user_id: "john",
        rating: "5",
        content: "abc",
      }];
    render(
      <BrowserRouter>
        <Routes>
          <Route path="*" element={<ReviewTile review={review} />}></Route>
        </Routes>
      </BrowserRouter>
    );
    const stars = screen.getByText("Stars: 5");
    expect(stars).toBeInTheDocument();
  });

  test("review content shows", () => {
    const review =
      [0,
      {
        restaurant_id: "0",
        timestamp: "2022",
        user_id: "john",
        rating: "5",
        content: "abc",
      }];
    render(
      <BrowserRouter>
        <Routes>
          <Route path="*" element={<ReviewTile review={review} />}></Route>
        </Routes>
      </BrowserRouter>
    );
    const content = screen.getByText("Review: abc");
    expect(content).toBeInTheDocument();
  });
