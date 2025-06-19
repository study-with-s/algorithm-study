# [BOJ] 문제 추천 시스템 Version 1#21939 / 골드4 / 250615 / 1시간(힌트 확인)

[백준/문제 추천 시스템 Version 1#21939](https://www.acmicpc.net/problem/21939)

### 문제 설명

> 주어진 명령어를 수행하는 추천 시스템 만들기

- 첫 번재 줄에 추천 문제 리스트에 있는 문제의 개수 N이 주어진다
- 두 번째 줄부터 N+1 줄까지 문제 번호 P와 난이도 L이 공백으로 구분되어 주어진다
- N+2 줄은 입력될 명령문의 개수 M이 주어진다
- 그 다음 줄부터 M개의 위에서 설명한 명령문이 입력된다.
- **recommend 명령이 주어질** 때마다 문제 번호를 한 줄씩 출력한다. 최소 한번의 recommend 명령어가 들어온다.

### 해결 방법

문제 번호 등을 이용하여 순서를 매겨야 하고, 추천할 때 맨 위의 값부터 가져온다는 점(FIFO)에서 우선순위 큐를 이용하면 되지 않을까? 생각했다<br>
여기서 레벨로 먼저 비교하고, 이후 번호로 우선순위를 결정하는 데 아직 우선순위 큐에 대해 미숙해서 해당 부분에서 다른 사람들의 코드랑 여러 가지를 살펴보았다. ㅠㅠ

이후 크게 문제는 없었다. 각 높은 순위로 정리한 데이터, 낮은 순위로 정리한 데이터 두 개 각각 명령어에 따라 가져오면 되기 때문이다.

문제와 관련하여 난이도가 다른 같은 문제 번호가 주어질 수 있다는 점에서 문제 보관함(문제 은행과 같이)으로 사용할 Map을 하나 만들어 문제를 관리했다.<br>
레벨과 난이도가 모두 같은 값이 존재하는지, 추천하고자 하는 아이디가 실제로 문제 은행에 존재하는 지 확인했었다. 이중으로 안 하니까 값이 제대로 확인되지 않고 오류가 나는 경우가 있었다.<br>
문제 리스트는 levelMap에서 확인하되, 정렬한 데이터를 빠르게 확인하기 위해 각각 HashMap으로 구현한 것이라고 보면 된다.

### 후기

골드 문제다보니 조금 생각할 부분들도 많았던 것 같다.<br>
levelMap에 대한 아이디어를 떠올리지 못해서 참고한 부분이 많다.<br>
이후 다시 한 번 풀어보면 좋을 것 같다.<br>
처음엔 그냥 단순히 배열로 세팅했는데 문제라는 class를 만들어서 사용하니까 더 코드의 가독성이 좋아진 것 같다.

## 코드

```java
class Problem {
  int id;
  int level;

  Problem(int id, int level) {
    this.id = id;
    this.level = level;
  }
}

public class RecommendProblemSystem1_21939 {

  public void solution() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    StringBuilder sb = new StringBuilder();

    // 문제 보관
    Map<Integer, Integer> levelMap = new HashMap<>();

    Queue<Problem> high = new PriorityQueue<>((a, b) -> {
      if (a.level != b.level) return b.level - a.level; // 난이도 내림차순
      return b.id - a.id; // 문제 번호 내림차순
    });

    Queue<Problem> low = new PriorityQueue<>((a, b) -> {
      if (a.level != b.level) return a.level - b.level; // 난이도 오름차순
      return a.id - b.id; // 문제 번호 오름차순
    });

    int N = Integer.parseInt(br.readLine());
    int[] temp;
    Problem p;

    for (int i = 0; i < N; i++) {
      temp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
      levelMap.put(temp[0], temp[1]);
      p = new Problem(temp[0], temp[1]);
      high.add(p);
      low.add(p);
    }

    int M = Integer.parseInt(br.readLine());
    int solveNum;
    for (int i = 0; i < M; i++) {
      st = new StringTokenizer(br.readLine());
      switch (st.nextToken()) {
        case "add": {
          int[] add = new int[]{Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};
          levelMap.put(add[0], add[1]);
          p = new Problem(add[0], add[1]);
          high.add(p);
          low.add(p);
          break;
        }
        case "recommend": {
          Queue<Problem> target = Integer.parseInt(st.nextToken()) == 1 ? high : low;
          while (!target.isEmpty()) {
            Problem peek = target.peek();
            if (!levelMap.containsKey(peek.id) || !Objects.equals(levelMap.get(peek.id), peek.level)) {
              target.poll();
              continue;
            }
            sb.append(peek.id).append("\n");
            break;
          }
          break;
        }
        case "solved": {
          solveNum = Integer.parseInt(st.nextToken());
          levelMap.remove(solveNum);
          break;
        }
      }
    }
    System.out.println(sb);

  }

}

```
