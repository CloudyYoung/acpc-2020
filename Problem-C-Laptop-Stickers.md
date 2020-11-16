# Problem C: Laptop Stickers

One of Atrebla’s favourite pastimes is collecting stickers from all the conferences he attends. Due to a series of unfortunate events, all of the usual ones have been cancelled, so this year he has finally decided to start putting them onto his laptop.

Atrebla has laid out all of his stickers, decided where he would like to place them and in what order they should be placed. Before he starts sticking, he would like to make one final check to make sure he will be satisfied with the final result.

The surface of his laptop lid can be represented by a grid with <img src="https://render.githubusercontent.com/render/math?math=H"> rows and <img src="https://render.githubusercontent.com/render/math?math=L"> columns. Each character in the grid is either a ’_’, or a lowercase letter denoting a sticker. The first sticker is denoted with ’a’s, the second with ’b’s, and so on. When placed, a sticker will cover up everything beneath it. Any parts of a sticker that hangs off the laptop will be cut off.

Can you write a program to give a preview of what Atrebla’s laptop will look like after placing all of his stickers?

## Inputs

The first line contains three space separated integers <img src="https://render.githubusercontent.com/render/math?math=0<L,H≤50">, the length and height of the laptop lid, and <img src="https://render.githubusercontent.com/render/math?math=0≤K≤26"> the number of stickers to be placed.

Each of the following <img src="https://render.githubusercontent.com/render/math?math=K"> lines contains four space separated integers <img src="https://render.githubusercontent.com/render/math?math=0<l≤L">, the length of the sticker, <img src="https://render.githubusercontent.com/render/math?math=0<h≤H">, the height of the sticker, and <img src="https://render.githubusercontent.com/render/math?math=0≤a<L"> and <img src="https://render.githubusercontent.com/render/math?math=0≤b<H"> denoting the column and row of the top left corner of the sticker respectively.

## Outputs

Output the final state of the laptop lid after all the stickers have been placed.

<table>
<thead>
  <tr>
    <th>Sample Input 1</th>
    <th>Sample Output 1</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>
<pre>
6 3 3
2 3 0 0
2 1 2 2
3 2 3 1
</pre>
    </td>
    <td>
<pre>
aa____
aa_ccc
aabccc
</pre>
    </td>
  </tr>
</tbody>
</table>
