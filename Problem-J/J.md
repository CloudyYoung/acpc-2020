# Problem J: Warring Scoring

Notnomde and Yraglac have been stuck at home for months, and have taken to playing ping pong to pass the time. Usually, the player who scores the highest number of points wins, but after a while Notnomde and Yraglac got tired of using the same rules all of the time. Both players decided on a new scoring system, but they came up with two different systems!

Under Notnomde’s system, the player with the longest consecutive streak of points wins, and the game is a tie if both player’s longest streaks are of the same length. Under Yraglac’s system, the player who held the largest lead over the other player at a single point during the game wins, and the game is a tie if both players’ highest leads were of the same number of points.

Sometimes the two systems agree on the outcome, but sometimes they don’t. In the first sample case, for example, Yraglac reached the largest lead of three points over Notnomde, but Notnomde had the longest streak with five consecutive points.

Given the sequence of points, will Notnomde and Yraglac agree or disagree about the outcome under their respective systems?

## Input
The first line of input consists of a single integer <img src="https://render.githubusercontent.com/render/math?math=1≤N≤105">, the total number of points scored in a game. <img src="https://render.githubusercontent.com/render/math?math=N"> lines then follow, each with the name of the player who scored that point.

## Output
If the outcome of the game (win for Notnomde, win for Yraglac, or tie) is the same under both systems, output `Agree`. Otherwise, output `Disagree`.



<table>
<thead>
  <tr>
    <th>Sample Input</th>
    <th>Sample Output</th>
  </tr>
</thead>
<tbody>
  <!--1-->
  <tr>
    <td>
<pre>
8
Yraglac
Yraglac
Yraglac
Notnomde
Notnomde
Notnomde
Notnomde
Notnomde
</pre>
    </td>
    <td>
<pre>
Disagree
</pre>
    </td>
  </tr>
  <!--2-->
  <tr>
    <td>
<pre>
5
Yraglac
Notnomde
Notnomde
Yraglac
Yraglac
</pre>
    </td>
    <td>
<pre>
Agree
</pre>
    </td>
  </tr>
  <!--3-->
  <tr>
    <td>
<pre>
4
Notnomde
Notnomde
Yraglac
Yraglac
</pre>
    </td>
    <td>
<pre>
Disagree
</pre>
    </td>
  </tr>
</tbody>
</table>
