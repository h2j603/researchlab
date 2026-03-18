---
title: "Deep Research 플러그인 설치 확인"
date: 2026-03-18
updated: 2026-03-18
status: complete
type: log
tags: [claude-code, plugin, deep-research]
related: []
confidence: high
---

# Deep Research 플러그인 확인 결과

## 확인 사항
사용자가 deep research 플러그인 설치 여부를 문의함.

## 결과
현재 환경에서 deep research 플러그인은 **설치되어 있지 않음**.

### 확인한 위치
- `~/.claude/plugins/` — blocklist.json만 존재
- `~/.claude/skills/` — session-start-hook만 존재
- MCP 서버 — Gmail, Google Calendar만 연결됨
- 설정 파일 — deep research 관련 설정 없음

### 사용 가능한 대안
- WebSearch / WebFetch를 활용한 웹 리서치
- Claude의 기본 리서치 워크플로우 활용
