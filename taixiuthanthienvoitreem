import React, { useState } from "react";
import { motion } from "framer-motion";
import "./App.css";

function App() {
  const [dice, setDice] = useState([1, 1, 1]);
  const [result, setResult] = useState(null);
  const [rolling, setRolling] = useState(false);

  const rollDice = () => {
    setRolling(true);
    setTimeout(() => {
      const newDice = [
        Math.ceil(Math.random() * 6),
        Math.ceil(Math.random() * 6),
        Math.ceil(Math.random() * 6),
      ];
      setDice(newDice);
      const sum = newDice.reduce((a, b) => a + b, 0);
      setResult(sum >= 11 ? "Tài" : "Xỉu");
      setRolling(false);
    }, 1000);
  };

  return (
    <div className="container">
      <h1 className="title">🎲 Giả Lập Tài Xỉu Dễ Thương 🎲</h1>

      <div className="dice-row">
        {dice.map((value, index) => (
          <motion.div
            key={index}
            animate={{ rotate: rolling ? 360 : 0 }}
            transition={{ duration: 1 }}
            className="dice-box"
          >
            {value}
          </motion.div>
        ))}
      </div>

      <button onClick={rollDice} disabled={rolling} className="btn-roll">
        {rolling ? "Đang lắc..." : "Lắc Xúc Xắc!"}
      </button>

      {result && (
        <div className="result-box">Kết quả: <strong>{result}</strong></div>
      )}
    </div>
  );
}

export default App;
