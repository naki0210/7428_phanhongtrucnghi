
import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Dice3, Dice5, Dice6 } from "lucide-react";
import { motion } from "framer-motion";

const diceIcons = [<Dice3 />, <Dice5 />, <Dice6 />];

export default function TaiXiuSimulator() {
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
      setResult(sum <= 10 ? "Tài" : "Xỉu");
      setRolling(false);
    }, 1000);
  };

  return (
    <div className="min-h-screen bg-pink-100 flex flex-col items-center justify-center p-4">
      <h1 className="text-3xl font-bold text-pink-600 mb-4">🎲 Giả Lập Tài Xỉu Dễ Thương 🎲</h1>

      <div className="flex gap-4 mb-4">
        {dice.map((value, index) => (
          <motion.div
            key={index}
            animate={{ rotate: rolling ? 360 : 0 }}
            transition={{ duration: 1 }}
            className="w-20 h-20 bg-white rounded-2xl shadow flex items-center justify-center text-2xl text-pink-600 font-bold"
          >
            {value}
          </motion.div>
        ))}
      </div>

      <Button
        onClick={rollDice}
        className="bg-pink-500 hover:bg-pink-600 text-white text-lg rounded-xl px-6 py-2 shadow-lg"
        disabled={rolling}
      >
        {rolling ? "Đang lắc..." : "Lắc Xúc Xắc!"}
      </Button>

      {result && (
        <Card className="mt-6 bg-white shadow-md rounded-xl">
          <CardContent className="p-4 text-xl text-pink-700 font-semibold">
            Kết quả: <span className="underline">{result}</span>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
