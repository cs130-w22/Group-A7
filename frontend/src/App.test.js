import { render, screen } from '@testing-library/react';
import App from './App';

test('app renders welcome to dinesmart page', () => {
  render(<App />);
  const linkElement = screen.getByText('Welcome to DineSmart');
  expect(linkElement).toBeInTheDocument();
});