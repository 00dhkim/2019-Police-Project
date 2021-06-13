# 2019-Police-Project
- 경찰청에서 KERT로 자문 요청의 형식으로 동아리 지원의 뜻을 밝혀주셨음
- 그에 따라 보안 프로젝트 발표를 요청하였고, 이 프로젝트를 진행하게 됨
- ARP spoofing과 session hijacking을 이용하여 공격함

## 공격 과정
1. ip scanning을 통해 해당 네트워크의 모든 device를 찾는다.
2. target을 정한 후, arp spoofing을 통해 target의 모든 packet이 공격자(나)에게 온다.
3. ip forwarding을 통해 나에게 온 target의 packet을 공유기로 보내준다.
4. tcpdump로 target의 packet을 capture한다.
5. packet중 session 값을 담고 있는 cookie값을 찾는다.
6. 찾은 cookie값을 크롬 확장 프로그램으로 공격자(나)의 웹사이트에서 이용한다.
7. ID PW 없이도 웹서비스 로그인을 성공할 수 있다.

## 환경
- python3 의 nmap, linux의 tcpdump와 arpspoof 툴을 사용함.
- 공격 운영체제: Kali Linux
- 사용 디바이스: AWUS036ACH

## 참고 사항
- host os(Windows 10)와 guest os(Kali Linux)의 lan mac address 중복을 막기 위해 kali linux에만 인식하는 외부 lan 장치 하나를 추가함. host와 guest os의 mac이 겹칠 경우 kali로 가야할 target의 packet들이 host os로 가는 경우가 생김.
- SSL통신이 적용되지 않은 packet만 가능함. 하지만 game.daum.net처럼 로그인 페이지는 ssl이나 그외 나머지 페이지가 아닌 경우 세션 하이제킹이 가능했음!
- evil twin attack을 우선적으로 시도하였으나 실패하고, ARP spoofing만 성공.
- 프로젝트 기간은 2019년 10월 28일부터 11월 6일까지 10일동안 진행.
- 프로젝트 진행은 김도현과 김동호가 함꼐 진행. 동호형이 코칭해주고 키워드만 알려주었고, 본인은 이를 토대로 공부해서 프로젝트를 수행하고 코딩함.
- 경찰청 관계자 분께서 어떻게 연락이 되어서 KERT 동아리 지원의 일환으로 정보보안 자문의 형식으로 우리에게 프로젝트를 (자유주제로) 제안하였고, 따라서 우리는 이 프로젝트를 진행하였음.

