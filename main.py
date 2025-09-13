import streamlit as st
import pandas as pd
import altair as alt
import os

# 페이지 제목
st.title("🌍 MBTI 유형별 비율이 가장 높은 국가 Top 10")
st.write("기본적으로 로컬 폴더의 CSV 데이터를 사용하며, 없을 경우 업로드한 파일을 불러옵니다.")

# 기본 파일 경로
default_file = "countriesMBTI_16types.csv"

# 데이터 불러오기 함수
def load_data(file_path):
    return pd.read_csv(file_path)

df = None

# 기본 파일이 있으면 그걸 사용
if os.path.exists(default_file):
    st.success(f"기본 데이터 파일(`{default_file}`)을 불러왔습니다 ✅")
    df = load_data(default_file)
else:
    # 없으면 업로드 기능 제공
    uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])
    if uploaded_file is not None:
        df = load_data(uploaded_file)

# 데이터가 준비된 경우만 실행
if df is not None:
    # MBTI 유형 리스트 (Country 제외)
    mbti_types = df.columns[1:].tolist()

    # 사용자 선택
    selected_type = st.selectbox("MBTI 유형을 선택하세요", mbti_types)

    # 선택한 MBTI 유형의 Top 10 국가 추출
    top10 = df[["Country", selected_type]].nlargest(10, selected_type)

    # Altair 그래프 생성
    chart = (
        alt.Chart(top10)
        .mark_bar()
        .encode(
            x=alt.X(selected_type, title=f"{selected_type} 비율"),
            y=alt.Y("Country", sort="-x", title="국가"),
            tooltip=["Country", selected_type],
            color=alt.Color(selected_type, scale=alt.Scale(scheme="tealblues"))
        )
        .interactive()
    )

    st.altair_chart(chart, use_container_width=True)

    # 데이터 테이블도 표시
    st.write("📊 Top 10 데이터")
    st.dataframe(top10.reset_index(drop=True))
else:
    st.warning("CSV 파일을 찾을 수 없습니다. 업로드해 주세요.")
