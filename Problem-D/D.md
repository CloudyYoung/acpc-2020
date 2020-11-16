# Problem D: Listen To Your Boss
At work, Atrebla recently became overwhelmed with orders from people all over his company and is trying to reduce his workload. He has realized that a large portion of the orders are from people who don’t have the authority to tell him what to do. By identifying such orders easily, he will be able to quickly discard them. At Atrebla’s company, all employees have one manager, except for the CEO who does not have any manager. Only the “management chain” of an employee has the authority give orders to him or her. The management chain of the CEO is defined as the empty set, and the management chain of any other employee A with manager B is defined as the set of employees consisting of B and B’s management chain. Talking to other employees in the company, Atrebla realized that many employees are facing the same issue.

Help Atrebla and other employees identify the orders they can discard.

## Input
The first line contains two integers <img src="https://render.githubusercontent.com/render/math?math=N"> and <img src="https://render.githubusercontent.com/render/math?math=M"> <img src="https://render.githubusercontent.com/render/math?math=(2≤N,M≤100000)">, the number of employees at Atrebla’s company and the number of orders. Employees are numbered from <img src="https://render.githubusercontent.com/render/math?math=1"> to <img src="https://render.githubusercontent.com/render/math?math=N"> inclusive, and employee <img src="https://render.githubusercontent.com/render/math?math=1"> is the CEO. Next will follow <img src="https://render.githubusercontent.com/render/math?math=N-1"> lines, containing the manager of employees <img src="https://render.githubusercontent.com/render/math?math=2"> to <img src="https://render.githubusercontent.com/render/math?math=N">. It is guaranteed that the CEO is in the management chain of all other employees and that an employee is never in their own management chain. This is followed by <img src="https://render.githubusercontent.com/render/math?math=M"> lines, one for each order, where the ith line contains two integers <img src="https://render.githubusercontent.com/render/math?math=a_i"> and <img src="https://render.githubusercontent.com/render/math?math=b_i"> <img src="https://render.githubusercontent.com/render/math?math=(1 ≤ a_i,b_i ≤ N, a_i \neq b_i)"> meaning that employee <img src="https://render.githubusercontent.com/render/math?math=a_i"> received an order from employee <img src="https://render.githubusercontent.com/render/math?math=b_i">.

## Output
Output <img src="https://render.githubusercontent.com/render/math?math=M"> lines, one for each order, containing “Yes” if the order should be ignored and “No” otherwise.


<table>
<thead>
  <tr>
    <th>Sample Input</th>
    <th>Sample Output</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>
<pre>
4 3
1
2
1
3 1
3 2
3 4
</pre>
    </td>
    <td>
<pre>
No
No
Yes
</pre>
    </td>
  </tr>
</tbody>
</table>
