## Section 12: Math Question: Robot Return to Origin (Easy)

#### Table of Contents

- Explaining the problem
- Implementing the code

### Explaining the problem

Imagine a robot standing at position (0, 0) in a 2D grid. Given a
string consisting of its moves, find the final location of the robot.

[657. Robot Return to Origin](https://leetcode.com/problems/robot-return-to-origin/)

U: up, increase in y axis

D: down, decrease in y axis

R: right, increase in x axis

L: left, decrease in x axis

Example: UD

- current position: (0, 0)
- U => (0, 0 + 1)
- current position: (0, 1)
- D => (0, 1 - 1)
- Final position: (0, 0)

Example: UDLR

- current position: (0, 0)
- U => (0, 0 + 1)
- current position: (0, 1)
- D => (0, 1 - 1)
- Final position: (0, 0)
- current position: (0, 0)
- L => (0 - 1, 0)
- current position: (-1, 0)
- R => (-1 + 1, 0)
- Final position: (0, 0)

#### Implementation

```
judgeCircle(moves) {
    x = 0;
    y = 0;

    for every move in moves {
        if (move == 'U') {
            y += 1;
        } else if (move == 'R') {
            x += 1;
        } else if (move == 'D') {
            y -= 1;
        } else if (move == 'L') {
            x -= 1;
        }
    }

    if (x == 0 and y == 0) {
        return true
    }
    return false
}
```

Time complexity: O(N)

Space complexity: O(1)

### Implementing the code
