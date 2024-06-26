<div class="problem-statement">
   <div class="header">
      <h1 class="title">B. Номер левого и правого вхождения</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>2&nbsp;секунды</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>64Mb</td>
         </tr>
         <tr class="input-file">
            <td class="property-title">Ввод</td>
            <td colspan="1">стандартный ввод или input.txt</td>
         </tr>
         <tr class="output-file">
            <td class="property-title">Вывод</td>
            <td colspan="1">стандартный вывод или output.txt</td>
         </tr>
      </table>
   </div>
   <h2></h2>
   <div class="legend"><span style="">
         <p>Требуется определить в заданном массиве номер самого левого и самого правого элемента, равного искомому числу. </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке вводится одно натуральное число <span class="tex-math-text">N</span>, не превосходящее <span class="tex-math-text">10<sup>5</sup></span>: количество чисел в массиве. Во второй строке вводятся <span class="tex-math-text">N</span> натуральных чисел, не превосходящих <span class="tex-math-text">10<sup>9</sup></span>, каждое следующее не меньше предыдущего. В третьей строке вводится количество искомых чисел <span class="tex-math-text">M</span> &ndash; натуральное число, не превосходящее <span class="tex-math-text">10<sup>6</sup></span>. В четвертой строке вводится <span class="tex-math-text">M</span> натуральных чисел, не превосходящих <span class="tex-math-text">10<sup>9</sup></span>.
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Для каждого запроса выведите в отдельной строке через пробел два числа: номер элемента самого левого и самого правого элементов
            массива, равных числу-запросу. Элементы массива нумеруются с единицы.Если в массиве нет такого числа, выведите в соответствующей
            строке два нуля, разделенных пробелом.
         </p></span></div>
   <h3>Пример 1</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>4
1 2 2 3
4
4 3 2 1
</pre></td>
            <td><pre>0 0
4 4
2 3
1 1
</pre></td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 2</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>10
1 2 3 4 5 6 7 7 8 9
10
7 3 3 1 3 7 9 7 7 10
</pre></td>
            <td><pre>7 8
3 3
3 3
1 1
3 3
7 8
10 10
7 8
7 8
0 0
</pre></td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 3</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>10
1 3 3 3 3 6 8 8 9 10
10
2 9 6 4 2 9 3 7 9 7
</pre></td>
            <td><pre>0 0
9 9
6 6
0 0
0 0
9 9
2 5
0 0
9 9
0 0
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>
