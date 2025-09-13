import streamlit as st
st.title('나의 첫 웹앱을 만들어보자!')
st.write('이걸 내가 만들어 본다고?')
import streamlit as st
import random

# 앱 제목
st.title("📚✨ MBTI별 공부법 추천기 🎉")

st.markdown(
    """
    안녕하세요! 😎  
    당신의 **MBTI**를 선택하면 ✨  
    딱 맞는 공부법을 알려드릴게요! 🚀
    """
)

# MBTI 리스트
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 사용자 선택
selected_mbti = st.selectbox("👉 MBTI 유형을 골라주세요:", mbti_types)

# MBTI별 공부법 딕셔너리
study_tips = {
    "INTJ": "📖 계획 세우고 꼼꼼히 실행! 체크리스트로 성취감 UP ⏳",
    "INTP": "💡 흥미 위주 탐구형! 개념 연결망 그리면서 이해하기 🧩",
    "ENTJ": "🚀 목표 설정 후 직진! 시간 관리 어플 적극 활용 📅",
    "ENTP": "🔥 토론과 브레인스토밍으로 에너지 충전 ⚡️",
    "INFJ": "🌱 조용한 공간에서 몰입 독서 ✨ 자기만의 스터디 루틴 만들기",
    "INFP": "🎨 감성 노트! 그림, 색깔, 글귀로 기억력을 살려요 🖌",
    "ENFJ": "🤝 친구랑 같이 공부! 설명하면서 배울 때 더 잘 이해 👥",
    "ENFP": "🎉 다양한 공부법 시도! 음악, 색깔, 스티커 활용 🎶",
    "ISTJ": "🗂 전통적인 방식 최고! 교재 → 필기 → 복습의 정석 📘",
    "ISFJ": "🪴 아늑한 환경 필수! 작은 보상으로 동기부여 🍫",
    "ESTJ": "📊 규칙적 스케줄 관리! 성취도 그래프 그려보기 📈",
    "ESFJ": "💬 그룹 스터디 찰떡! 서로 도와가며 학습 🌟",
    "ISTP": "🛠 실험·실습으로 직접 해보면서 배우기 ⚙️",
    "ISFP": "🎶 음악과 함께하는 공부! 감각 자극으로 몰입 🌸",
    "ESTP": "🎮 게임화 공부법! 타이머 켜고 미션 클리어 🔔",
    "ESFP": "🌈 즐겁게 해야 오래간다! 칭찬 스티커&컬러풀 메모 활용 🎀"
}

# 결과 출력
if selected_mbti:
    st.subheader(f"✨ {selected_mbti} 유형 추천 공부법 ✨")
    st.success(study_tips[selected_mbti])

    # 랜덤 효과 넣기
    effect = random.choice(["balloons", "snow", "none"])
    if effect == "balloons":
        st.balloons()
    elif effect == "snow":
        st.snow()

# 푸터
st.markdown("---")
st.caption("💡 Made with Streamlit | 재미로 보는 MBTI 공부법 ✨")
