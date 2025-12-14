import re

def generate_text_tags(text):
    text_low = re.sub(r"\s+", "", text.lower())
    tags = []

    rules = {
        "greeting": ["안녕", "안녕하세요", "환영", "hello", "hi", "greetings", "반갑", "감사"],
        "exam": ["시험", "퀴즈", "고사", "평가", "중간", "기말", "test", "quiz", "midterm", "final"],
        "notice": ["공지", "안내", "알림", "공지사항", "발표", "통보", "notice", "announcement"],
        "task": ["과제", "숙제", "문제", "제출", "보고서", "레포트", "assignment", "homework", "project"],
        "schedule": ["일정", "할일", "기한", "시간표", "스케줄", "날짜", "meeting", "calendar", "예약", "마감"],
        "education": ["강의", "수업", "교육", "수강", "class", "lecture", "course", "학습", "팀플"],
        "document": ["문서", "자료", "파일", "pdf", "report", "첨부", "제출"],
        "academic": ["연구", "논문", "기술", "분석", "실험", "랩", "ai", "engineering"],
        "emotion": ["좋아요", "싫어요", "감동", "기쁨", "사랑", "감사", "thanks"],
        "shopping": ["할인", "구매", "쇼핑", "쿠폰", "주문", "결제", "배송", "영수증"],
        "organization": ["학교", "대학", "학부", "company", "team", "기관", "부서", "동아리"],
        "administration": ["신청", "서류", "등록", "처리", "승인", "접수", "심사"],
        "finance": ["비용", "납부", "지급", "환급", "청구", "계좌", "송금"],
        "location": ["건물", "교실", "호관", "층", "캠퍼스", "강의실", "주소"],
        "event": ["행사", "회의", "세미나", "모임", "워크숍", "공고", "참석"],
        "account": ["계정", "비밀번호", "아이디", "인증코드", "로그인", "토큰"]
    }

    for tag, words in rules.items():
        if any(word in text_low for word in words):
            tags.append(tag)

    return ", ".join(sorted(set(tags))) if tags else "general"


def merge_tags(text_tags, ai_tags):
    merged = set()

    if text_tags:
        for tag in text_tags.split(","):
            clean = tag.strip()
            if clean:
                merged.add(clean)

    if ai_tags:
        for tag in ai_tags.split(","):
            clean = tag.strip()
            if clean:
                merged.add(clean)

    return ", ".join(sorted(merged)) if merged else "general"
