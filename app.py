from flask import Flask, render_template

app = Flask(__name__)

# --- หน้าแรก (Start Page) ---
@app.route('/')
def index():  # <--- แก้ตรงนี้! จาก home เป็น index
    return render_template('index.html')

# --- หน้าที่ 2: หน้าเลือกอัปโหลด (Home Page) ---
@app.route('/home')
def home():   # อันนี้ชื่อ home เหมือนเดิม ถูกแล้วครับ
    return render_template('home.html')

# 🔥 เพิ่มส่วนนี้ครับ: หน้า Upload
@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/processing')
def processing():
    return render_template('processing.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/graph_face')
def graph_face():
    return render_template('graph_face.html')

@app.route('/graph_voice')
def graph_voice():
    return render_template('graph_voice.html')

# 🔥 เพิ่มส่วนนี้ครับ: หน้า History
@app.route('/history')
def history():
    return render_template('history.html')

if __name__ == '__main__':
    app.run(debug=True)