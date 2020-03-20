# 보안 무시 #
Secure coding is the practice of writing programs that are resistant to attack by malicious or mischievous people or other programs. Secure coding helps protect data from theft or corruption. In addition, an insecure program can provide access for an attacker to take control of a server or a user's identity, resulting in anything from a denial of service to a single user to the compromise of secrets, loss of service, or damage to the systems of thousands of users.

> 프로그래머의 문제점은 너무 늦을때까지 프로그래머가 뭘 하는 지 말할 수 없다는 점입니다.
>
> -- Seymour Cray on [defprogramming.com](http://www.defprogramming.com/q/6e61ae30a855/)

시큐어 코딩은 프로그램을 악의적이거나 장난스러운 사람들, 혹은 다른 프로그램들의 공격을 방어하는 습관입니다. 시큐어 코딩은 데이터 도난 혹은 손상으로부터 보호합니다. 추가적으로 안전하지 않은 프로그램은 공격자가 서버, 사용자 신원, 혹은 부정적인 영향을 미칠 수 있는 어떤 것들에 접근할 수 있게 해서 단 한명의 유저가 수천명의 사용자에게 비밀 일부 유출 , 서비스 손실, 혹은 시스템 손상을 가져올 수 있게 합니다.

모든 컴퓨터 프로그램은 보안 공격의 잠재적인 대상입니다. 공격자는 응용 프로그램에서 보안 취약점을 찾으려고 시도합니다. 그런 다음 이 취약점을 사용하여 비밀을 훔치고 프로그램과 데이터를 손상 시키며 서버와 네트워크를 제어하려고 시도합니다. 고객의 재산과 명성이 위태로워집니다.

** 보안은 소프트웨어에 추가 할 수있는 것이 아닙니다! **

안전하지 않은 어플리케이션을 보호하기 위해 광범위한 재설계가 필요할 수 있습니다. 소프트웨어에 대한 위협의 특성을 구별하고 어플리케이션 계획 및 개발 단계에서 시큐어 코딩 방법을 함께 고려해야 합니다.

공격자의 관심이 점점 (데스크탑에서) 웹 어플리케이션으로 옮겨가므로 보안적으로 안전한 소프트웨어 리소스를 확보하는 것이 더욱 중요해졌습니다. 2009 SANS 연구에 따르면 인터넷에서 찾아낸 총 공격 중 60%가 웹 어플리케이션을 공격하는 것이었습니다.

PHP는 동시에 프로그래밍 언어와 웹 프레임 워크라는 점에서 특이합니다. 즉 PHP에는 웹을 위한 내장 기능이 언어 자체에 내장되어 있고, 이는 안전하지 않은 코드를 작성하기가 매우 쉬운 결과로 나타납니다.

## 보안은 기본 ##
In order for applications to be designed and implemented with proper security requirements, secure coding practices and a focus on security risks must be integrated into the day-to-day operations, thoughts, and the development processes themselves.

Generally, it is much less expensive to build secure software than to correct security issues after the software package has been completed, not to mention the costs that may be associated with a security breach.

> 복잡성을 걷어내세요. 개발자의 생명을 갉아먹고 제품을 계획, 빌드 혹은 테스트하기 어렵게 만들고, 보안문제가 발생하며 사용자 및 관리자의 불만을 유발합니다.
>
> -- [Ray Ozzie](www.azquotes.com/quote/585933)

적절한 보안 요구사항을 포함해서 어플리케이션을 설계하고 구현하려면 시큐어 코딩을 사용하고, 보안 위험은 매일매일 작업할 때, 생각할 때, 개발 절차 내에  녹아들어가야 합니다.

일반적으로 소프트웨어 개발이 끝난 후 보안 문제를 해결하는 것보다 처음부터 시큐어 소프트웨어를 만드는 것이 더 저렴합니다. 보안 위반 관련 비용을 제외하고도요.

**잘못된 방법** : 보안 소프트웨어를 기본으로 개발하지 않습니다. ![Thumbs down](https://phpthewrongway.com/img/thumbs-down.png)