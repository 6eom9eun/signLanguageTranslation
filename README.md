`미니프로젝트`  
`KT 에이블스쿨 4기`<br>
<h2>'수어 번역 서비스 개발 및 배포'</h2>
장애인과 비장애인이 함께 사용할 수 있는 서비스 만들기
</div><br><br>

`Languege : Python, HTML&CSS, JavaScript`<br>
`Framework : vscode, Django`<br>
`Technology & Tools : mlflow, tensorflow, AWS`
- What ?
    - 장애인과 비 장애인이 함께 사용할 수 있는 수어 번역 서비스 데모 개발
    - **KT AIVEL School 4기 AI트랙 약 200명의 30조 팀에서 인기투표 2등 !**
- How ?
    - 서버 세팅 : AWS 서버 생성 (VPC, 서브넷, ec2 인스턴스), 클라우드 환경 구축 -> Django 배포
    - ML Pipeline 구축(Mlflow) -> 서버 세팅 -> 웹 서비스 데모 구현(ChatGPT API)
    - ChatGPT API 응답속도가 현저히 느린 것을 확인하고, 동기 API에서 비동기 API로 수정하고 ChatGPT 3.5 버전에서 4로 버전업
    - 응답속도가 느린 것을 확인하고 기존의 HTML를 render 하는 방식의 API를 jsonresponse로 바꾸고 템플릿에는 AJAX를 이용해 비동기 API 구현
    - 예외처리를 이용해 완성도를 높임


<details>
    <summary>ML&DL</summary>
  
<img src="https://github.com/6eom9eun/AIVLE_miniProject_7/assets/104510730/109ad392-9a51-4726-9f17-4d745abfb322" width="800" height="400"/>

</details>

---
<details>
    <summary>index</summary>
  
![KakaoTalk_20231207_171725968](https://github.com/6eom9eun/AIVLE_miniProject_7/assets/104510730/22785714-8827-4840-9858-59639897557f)

</details>

---

<details>
    <summary>gpt ajax 비동기통신</summary>
  
![KakaoTalk_20231207_171725968_01](https://github.com/6eom9eun/AIVLE_miniProject_7/assets/104510730/97d63f9b-ef1c-40c8-9b6b-7bc0a1e63d9b)

</details>

---

<details>
    <summary>mlflow에서 불러온 모델로 분류</summary>
  
![KakaoTalk_20231207_171725968_02](https://github.com/6eom9eun/AIVLE_miniProject_7/assets/104510730/b15ba10b-dcbf-4fba-a77b-647163de2e28)

</details>


---

<details>
    <summary>게시판</summary>
  
![KakaoTalk_20231207_171725968_03](https://github.com/6eom9eun/AIVLE_miniProject_7/assets/104510730/32d13fbd-2966-411d-b6ab-48c543b92bec)



</details>
