import React, { useState } from "react";
import { Container, Row, Col, Button, Form } from "react-bootstrap";
import Particle from "../Particle";
import axios from "axios";

function About() {
  const [userInput, setUserInput] = useState("");  // 사용자 입력 상태
  const [chatResponse, setChatResponse] = useState("");  // 응답 저장 상태
  const [errorMessage, setErrorMessage] = useState("");  // 에러 메시지 상태

  // Flask API에 POST 요청 보내기
  const handleChatSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post("http://localhost:5000/chat", {
        message: userInput,
      });
      
      setChatResponse(response.data.response);  // Flask API로부터 응답을 받음
      setErrorMessage("");  // 에러 메시지 초기화
    } catch (error) {
      setErrorMessage("채팅 중 오류가 발생했습니다.");
      console.error(error);
    }
  };

  return (
    <Container fluid className="about-section">
      <Particle />
      <Container>
        <Row>
          <Col>
            <h2>Chatbot</h2>
            <Form onSubmit={handleChatSubmit}>
              <Form.Group>
                <Form.Label>Enter your message :</Form.Label>
                <Form.Control
                  type="text"
                  value={userInput}
                  onChange={(e) => setUserInput(e.target.value)}  // 사용자 입력 업데이트
                  style={{
                    zIndex: 1,  // CSS: 요소가 가려지는 문제 해결
                    position: "relative",  // CSS: 입력 필드가 제대로 표시되게
                    backgroundColor: "white"  // 시각적으로 문제 확인을 위해 배경을 흰색으로
                  }}
                />
              </Form.Group>
              <Button type="submit" variant="primary">SEND</Button>
            </Form>
            <div>
              {chatResponse && <p>Wookbot : {chatResponse}</p>}  {/* 응답 표시 */}
              {errorMessage && <p style={{ color: "red" }}>{errorMessage}</p>}  {/* 에러 메시지 표시 */}
            </div>
          </Col>
        </Row>
      </Container>
    </Container>
  );
}

export default About;