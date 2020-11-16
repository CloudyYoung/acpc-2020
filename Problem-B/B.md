# Problem B: Hired Help
Viv’s shoe repair company has seen a spike in demand. Today, she has a backlog of shoes that need repairs. So Viv wants to hire some people to assist with the extra work. According to labour laws, each employee is not allowed to repair more than a certain number of shoes (say <img src="https://render.githubusercontent.com/render/math?math=K">) each day. Each shoe takes 1 minute to repair: no more, no less. Each shoe also has a deadline: if it is not repaired by the deadline then the customer gets mad and takes their business elsewhere.

Viv believes everyone should put in an honest day’s work. If an employee fixes fewer than <img src="https://render.githubusercontent.com/render/math?math=K"> shoes today then Viv would prefer to not have hired them at all. In fact, she believes in this so strongly that she would prefer to lose business from clients than have an employee not complete their quota.

Help Viv determine the maximum number of employees she can hire so: a) each employee can repair <img src="https://render.githubusercontent.com/render/math?math=K"> shoes before their deadlines, and b) each shoe is (of course) repaired by at most one employee.

## Input
Input begins with a line consisting of two integers <img src="https://render.githubusercontent.com/render/math?math=N"> (<img src="https://render.githubusercontent.com/render/math?math=0≤N≤105">) and <img src="https://render.githubusercontent.com/render/math?math=K"> (<img src="https://render.githubusercontent.com/render/math?math=1≤K≤N">) where <img src="https://render.githubusercontent.com/render/math?math=N"> is the number of shoes that need to be repaired and <img src="https://render.githubusercontent.com/render/math?math=K"> is as described above.

Then a second line follows containing <img src="https://render.githubusercontent.com/render/math?math=N"> space-separated integers <img src="https://render.githubusercontent.com/render/math?math=d1,...,dN"> (<img src="https://render.githubusercontent.com/render/math?math=1≤di≤10^9"> for each <img src="https://render.githubusercontent.com/render/math?math=1≤i≤N">) describing the deadlines for the repairs. That is, if the repair of shoe <img src="https://render.githubusercontent.com/render/math?math=i"> is not completed within <img src="https://render.githubusercontent.com/render/math?math=d_i"> minutes of the start of the day then client i will take their business elsewhere.

Note, the days can be much longer on Viv’s planet than ours.

## Output
Output a single integer <img src="https://render.githubusercontent.com/render/math?math=M"> on a single line indicating the maximum number of employees such that it is possible to allocate <img src="https://render.githubusercontent.com/render/math?math=K"> shoes to each employee and each employee can complete their assigned repairs before their respective deadlines, assuming all employees start working on their list of assigned jobs at the start of the day.


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
6 3
1 1 2 2 1 2
</pre>
    </td>
    <td>
<pre>
0
</pre>
    </td>
  </tr>
  <!--2-->
  <tr>
    <td>
<pre>
6 3
3 1 3 2 1 2
</pre>
    </td>
    <td>
<pre>
2
</pre>
    </td>
  </tr>
  <!--3-->
  <tr>
    <td>
<pre>
6 3
3 1 2 2 1 2
</pre>
    </td>
    <td>
<pre>
1
</pre>
    </td>
  </tr>
</tbody>
</table>
