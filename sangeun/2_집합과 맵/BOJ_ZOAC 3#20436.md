# [BOJ] ZOAC 3#20436 / 실버4 / 250619 / 1시간

[백준/ZOAC 3#20436](https://www.acmicpc.net/problem/20436)

### 문제 설명

> 입력으로 주어진 문자열을 출력하는 데에 걸리는 시간의 최솟값을 출력

### 해결 방법

Map을 이용하여 각각 오른손, 왼손에서 칠 수 있는 키보드의 값을 Key로, 그에 맞는 좌표를 Value로 지정했다.<br>
이후 주어진 식을 이용하여 계산 후에 키보드 누르는 시간 +1 까지 하여 값을 저장했다.

이후 왼손, 오른손 값을 더하면 끝!

### 후기

계산이나 아이디어는 어렵지 않았는데, Map에 넣는게 너무 귀찮았다...<br>
더 좋은 방법이 있을까?

## 코드

```java
public class Zoac3_20436 {

  public void solution() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String[] list = br.readLine().split(" "); // 왼-오
    Map<Character, int[]> leftKeyboard = setLeftKeyboard();
    Map<Character, int[]> rightKeyboard = setRightKeyboard();

    List<int[]> left = new LinkedList<>();
    int leftTime = 0;
    List<int[]> right = new LinkedList<>();
    int rightTime = 0;

    left.add(leftKeyboard.get(list[0].charAt(0)));
    right.add(rightKeyboard.get(list[1].charAt(0)));

    char[] text = br.readLine().toCharArray();
    for (char c : text) {
      // 오른쪽
      if (leftKeyboard.containsKey(c)) {
        left.add(leftKeyboard.get(c));
      } else {
        right.add(rightKeyboard.get(c));
      }
    }

    leftTime = calTime(left);
    rightTime = calTime(right);

    System.out.println(leftTime + rightTime);

  }

  static int calTime(List<int[]> list) {
    int time = 0;

    if (list.size() == 1) {
      return 0;
    }

    int x1, y1, x2, y2;
    for (int i = 1; i < list.size(); i++) {
      x1 = list.get(i - 1)[0];
      y1 = list.get(i - 1)[1];
      x2 = list.get(i)[0];
      y2 = list.get(i)[1];

      time += (Math.abs(x1 - x2) + Math.abs(y1 - y2)) + 1;
    }

    return time;
  }

  static Map<Character, int[]> setLeftKeyboard() {
    Map<Character, int[]> pos = new HashMap<>();
    pos.put('q', new int[]{0, 0});
    pos.put('w', new int[]{0, 1});
    pos.put('e', new int[]{0, 2});
    pos.put('r', new int[]{0, 3});
    pos.put('t', new int[]{0, 4});
    pos.put('a', new int[]{1, 0});
    pos.put('s', new int[]{1, 1});
    pos.put('d', new int[]{1, 2});
    pos.put('f', new int[]{1, 3});
    pos.put('g', new int[]{1, 4});
    pos.put('z', new int[]{2, 0});
    pos.put('x', new int[]{2, 1});
    pos.put('c', new int[]{2, 2});
    pos.put('v', new int[]{2, 3});
    return pos;
  }

  static Map<Character, int[]> setRightKeyboard() {
    Map<Character, int[]> pos = new HashMap<>();
    pos.put('y', new int[]{0, 5});
    pos.put('u', new int[]{0, 6});
    pos.put('i', new int[]{0, 7});
    pos.put('o', new int[]{0, 8});
    pos.put('p', new int[]{0, 9});
    pos.put('h', new int[]{1, 5});
    pos.put('j', new int[]{1, 6});
    pos.put('k', new int[]{1, 7});
    pos.put('l', new int[]{1, 8});
    pos.put('b', new int[]{2, 4});
    pos.put('n', new int[]{2, 5});
    pos.put('m', new int[]{2, 6});
    return pos;
  }

}

```
