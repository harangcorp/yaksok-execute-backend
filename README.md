# 약속 언어 실행 백엔드
2022 디미고 입학설명회 부스 운영을 위한 약속 언어 실행 Backend

## API 사용 방법

`POST` 형식으로 API 주소( https://yaksok-playground.api.harang.it/ )에 API Request를 보내면 코드 실행 결과가 반환됩니다.

Request 형식
```json
{
  "code": ""  /* 약속 언어 소스코드 */
}
```

 
 Response 형식
 ```json
{
  "result": ""  /* 실행 결과, 오류가 나면 오류 발생 이유가 반환됨 */
}
```
  - Status Code: `200` - 정상, `401` - 코드 실행 중 발생
