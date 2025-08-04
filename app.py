from flask import Flask, render_template, request, redirect, url_for, flash
from gtts import gTTS
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 플래시 메시지용

BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # app.py 파일이 있는 절대 경로
STATIC_FOLDER = os.path.join(BASE_DIR, 'static')      # static 폴더 절대 경로
OUTPUT_FILE = os.path.join(STATIC_FOLDER, 'output.mp3')

DEFAULT_LANG = 'ko'
LANG_OPTIONS = ['ko', 'en', 'ja', 'es']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text', '').strip()
        lang = request.form.get('lang', DEFAULT_LANG)

        if not text:
            flash('⚠️ 텍스트를 입력해주세요.')
            return redirect(url_for('index'))

        if lang not in LANG_OPTIONS:
            flash('⚠️ 지원하지 않는 언어입니다.')
            return redirect(url_for('index'))

        try:
            tts = gTTS(text=text, lang=lang)
            tts.save(OUTPUT_FILE)
            flash('✅ 음성 변환이 완료되었습니다.')
            return render_template('index.html', audio_file='output.mp3', lang=lang)
        except Exception as e:
            flash(f'⚠️ 음성 변환 중 오류가 발생했습니다: {e}')
            return redirect(url_for('index'))

    return render_template('index.html', audio_file=None, lang=DEFAULT_LANG)

if __name__ == '__main__':
    app.run(debug=True)
