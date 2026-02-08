from flask import Flask, render_template, request

# Flask 애플리케이션 생성
app = Flask(__name__)

# 화면에 표시할 운동 종목 데이터 (부위별로 그룹화)
exercise_data = {
    "하체": [
        {"name": "스쿼트", "description": "하체 근력의 왕. 전신 근육 발달에 도움을 줍니다."},
        {"name": "런지", "description": "하체 근력과 균형 감각을 함께 향상시킬 수 있습니다."},
        {"name": "레그 프레스", "description": "대퇴사두근과 둔근을 집중적으로 강화하는 머신 운동입니다."}
    ],
    "가슴": [
        {"name": "벤치 프레스", "description": "가슴, 어깨, 삼두근을 발달시키는 대표적인 상체 운동입니다."},
        {"name": "딥스", "description": "가슴 하부와 삼두근을 동시에 공략할 수 있는 운동입니다."},
        {"name": "푸시업", "description": "체중을 이용해 가슴 근육을 단련하는 가장 기본적인 운동입니다."}
    ],
    "등": [
        {"name": "데드리프트", "description": "전신 후면 근육을 강화하는 최고의 운동 중 하나입니다."},
        {"name": "풀업", "description": "광배근을 발달시켜 넓은 등을 만드는 데 최고의 운동입니다."},
        {"name": "바벨 로우", "description": "두꺼운 등을 만들기 위한 효과적인 운동입니다."}
    ]
}


# 기본 URL('/')에 접속했을 때 실행될 함수 정의
@app.route('/', methods=['GET', 'POST'])
def index():
    """
    메인 페이지를 렌더링하고 운동 목록을 전달합니다.
    POST 요청 시 선택된 부위에 맞는 운동 목록을 보여줍니다.
    """
    selected_part = None
    recommended_exercises = []

    if request.method == 'POST':
        selected_part = request.form.get('body_part')
        recommended_exercises = exercise_data.get(selected_part, [])

    return render_template('index.html', body_parts=exercise_data.keys(), exercises=recommended_exercises, selected_part=selected_part)

# 이 파일이 직접 실행될 경우 Flask 개발 서버를 실행
if __name__ == '__main__':
    # debug=True 모드로 실행하여 코드 변경 시 서버가 자동으로 재시작되도록 설정
    app.run(debug=True)
