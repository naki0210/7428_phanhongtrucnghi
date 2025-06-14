from flask import Flask, render_template_string
import random

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head>
  <title>Giả Lập Tài Xỉu</title>
  <style>
    body { background-color: #ffe6f0; font-family: Comic Sans MS; text-align: center; }
    .dice { display: inline-block; font-size: 40px; margin: 10px; background: white; border-radius: 15px; padding: 20px; box-shadow: 2px 2px 8px rgba(0,0,0,0.2);}
    .btn { background-color: #ff69b4; color: white; padding: 10px 20px; border: none; border-radius: 10px; font-size: 20px; cursor: pointer; }
    .result { margin-top: 20px; font-size: 24px; color: #d63384; }
  </style>
</head>
<body>
  <h1>🎲 Giả Lập Tài Xỉu Dễ Thương 🎲</h1>
  <form method="post">
    <button class="btn" type="submit">Lắc Xúc Xắc!</button>
  </form>

  {% if dice %}
    <div>
      {% for d in dice %}
        <div class="dice">{{ d }}</div>
      {% endfor %}
    </div>
    <div class="result">Kết quả: <b>{{ result }}</b></div>
  {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    if random.random() < 0.000001:  # ẩn Easter Egg =))
        return "Bạn thật sự là thầy bói nhân phẩm thượng thừa!"

    if random.random() < 0.2:  # 20% nhân phẩm kém
        dice = [1, 1, 1]
    else:
        dice = [random.randint(1, 6) for _ in range(3)]

    total = sum(dice)
    result = 'Tài' if total >= 11 else 'Xỉu'
    return render_template_string(HTML, dice=dice, result=result)

if __name__ == '__main__':
    app.run(debug=True)
