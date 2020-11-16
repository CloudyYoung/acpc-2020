# Problem A: Best Investing
Geraldine has designed a fantastic investment portfolio that is guaranteed to grow at <img src="https://render.githubusercontent.com/render/math?math=r\%25"> every year, and she wants to maximize how much she can get out of it. Starting now and for the next <img src="https://render.githubusercontent.com/render/math?math=y"> years, she can either deposit money into or withdraw money from her account (but not both) once a year, and after each year the amount in the account grows by <img src="https://render.githubusercontent.com/render/math?math=r\%25">. Her account stores the dollar amount as a real number.

While she has a good job with flexible hours, Geraldine has bills to pay and she can only work so hard in a given year, so she can only deposit up to <img src="https://render.githubusercontent.com/render/math?math=\$d"> per year. She’ll enjoy the money grown from her wise investing, but she has no use for withdrawing more than <img src="https://render.githubusercontent.com/render/math?math=\$w"> per year.

Given these limits, and given that Geraldine starts with an empty account, what is the maximum net gain that she can earn through her investment?

Note that in the first sample case, Geraldine’s best strategy is to deposit $1000 at first, which after one year grows by 5% to $1050. At the end of the first and only year she withdraws the full $1050. Her net gain is the difference between her total withdrawals ($1050) and her total deposits ($1000) which in this case is $50.

## Input
Input begins with a line consisting of the four space-separated integers <img src="https://render.githubusercontent.com/render/math?math=r">, <img src="https://render.githubusercontent.com/render/math?math=y">, <img src="https://render.githubusercontent.com/render/math?math=d">, and <img src="https://render.githubusercontent.com/render/math?math=w"> as described in the problem statement, satisfying that  
<img src="https://render.githubusercontent.com/render/math?math=1≤r,y≤100">  
<img src="https://render.githubusercontent.com/render/math?math=1≤d,w≤10^6">.

## Output
Output the maximum net gain that Geraldine can earn with her account. Answers will be accepted up to a relative error of <img src="https://render.githubusercontent.com/render/math?math=10^{-6}"> or absolute error of <img src="https://render.githubusercontent.com/render/math?math=10^{-2}">, whichever is greater.


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
5 1 1000 2000
</pre>
    </td>
    <td>
<pre>
50
</pre>
    </td>
  </tr>
  <!--2-->
  <tr>
    <td>
<pre>
100 10 1 1000
</pre>
    </td>
    <td>
<pre>
1513
</pre>
    </td>
  </tr>
  <!--3-->
  <tr>
    <td>
<pre>
7 100 1 100000
</pre>
    </td>
    <td>
<pre>
13148.3781193723
</pre>
    </td>
  </tr>
</tbody>
</table>