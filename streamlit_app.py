# app.py
#############################################################################


import base64
import os

import streamlit as st

from deepface import DeepFace


def sortObj(k):
    return sorted(obj[k].items(), key=lambda x: x[1], reverse=True)


st.sidebar.header("닮은 꼴 찾기 프로젝트")
name = st.sidebar.selectbox("Name", ["감정 찾기", "test"])
# n_similar = st.sidebar.slider("Max number of similar entries", 1, 100, value=20, step=1)
if name == "감정 찾기":
    st.title("감정 찾기")
    uploaded_files = st.file_uploader(
        "정면으로 찍은 사진을 올려보세요.", type=["png", "jpg"], accept_multiple_files=True
    )

    if uploaded_files is not None:
        print(uploaded_files, type(uploaded_files))
        for uploaded_file in uploaded_files:
            content = uploaded_file.getvalue()
            bs = "data:image/jpeg;base64," + base64.b64encode(content).decode("utf-8")

            obj = DeepFace.analyze(bs, actions=["age", "gender", "race", "emotion"])

            race = sortObj("race")
            gender = sortObj("gender")
            emotions = sortObj("emotion")

            st.image(bs, width=250, caption="CLIENT_IMAGE")
            st.write("#### 성별")
            st.write("{0} : {1}%".format(gender[0][0], round(gender[0][1], 2)))
            st.write("#### 감정")
            st.write("{0} : {1}%".format(emotions[0][0], round(emotions[0][1], 2)))
            st.write("{0} : {1}%".format(emotions[1][0], round(emotions[1][1], 2)))
            st.write("#### 인종")
            st.write("{0} : {1}%".format(race[0][0], round(race[0][1], 2)))

elif name == "test":
    st.title("epi1_100_face")
    path = "./data./epi1_100_face"
    uploaded_files = os.listdir(path)
    print(uploaded_files)
    if uploaded_files is not None:
        for uploaded_file in uploaded_files:
            bs = os.path.join(path, uploaded_file)
            print(bs)
            try:
                obj = DeepFace.analyze(bs, actions=["age", "gender", "race", "emotion"])
                print(object)
                race = sortObj("race")
                gender = sortObj("gender")
                emotions = sortObj("emotion")

                st.image(bs, width=250, caption="CLIENT_IMAGE")
                st.write("#### 성별")
                st.write("{0} : {1}%".format(gender[0][0], round(gender[0][1], 2)))
                st.write("#### 감정")
                st.write("{0} : {1}%".format(emotions[0][0], round(emotions[0][1], 2)))
                st.write("{0} : {1}%".format(emotions[1][0], round(emotions[1][1], 2)))
            except:
                print("얼굴을 찾아내지 못했습니다.")
                continue
