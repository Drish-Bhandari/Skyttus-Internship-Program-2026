import { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);
  const LIMIT = 10;

  const increase = () => {
    setCount((prev) => prev + 1);
  };

  const decrease = () => {
    setCount((prev) => prev - 1);
  };

  const reset = () => {
    setCount(0);
  };

  return (
    <div className="counter-container">
      <h2>Counter App</h2>

      <div className="count-display">
        {count}
      </div>

      <div className="buttons">
        <button onClick={decrease} disabled={count === 0}>
          Decrease
        </button>

        <button onClick={reset} className="reset-btn">
          Reset
        </button>

        <button onClick={increase}>
          Increase
        </button>
      </div>

      {/* Conditional Rendering */}
      {count > LIMIT && (
        <p className="warning">
          ⚠ Warning: Counter exceeded recommended limit!
        </p>
      )}
    </div>
  );
}

export default Counter;