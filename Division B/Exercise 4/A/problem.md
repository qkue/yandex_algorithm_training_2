<div class="problem-statement">
   <div class="header">
      <h1 class="title">A. Толя-Карп и новый набор структур, часть 2</h1>
      <table>
         <thead>
            <th></th>
            <th>Все языки</th>
            <th>Scala 2.13.4</th>
         </thead>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>3&nbsp;секунды</td>
            <td>5&nbsp;секунд</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>255Mb</td>
            <td>256Mb</td>
         </tr>
         <tr class="input-file">
            <td class="property-title">Ввод</td>
            <td colspan="2">стандартный ввод или input.txt</td>
         </tr>
         <tr class="output-file">
            <td class="property-title">Вывод</td>
            <td colspan="2">стандартный вывод или output.txt</td>
         </tr>
      </table>
   </div>
   <h2></h2>
   <div class="legend"><span style="">
         <p>Толя-Карп запросил для себя <span class="tex-math-text">n</span> посылок с &laquo;Аллигатор-экспресс&raquo;.
         </p></span><p>Посылка представляет из себя ящик. Внутри ящика лежит целое число <span class="tex-math-text">a<sub>i</sub></span>. Номер на ящике <span class="tex-math-text">d<sub>i</sub></span> указывает на цвет числа, лежащего внутри. 
      </p>
      <p>Толю-Карпа интересует, чему будут равны значения чисел, если сложить между собой все те, что имеют одинаковый цвет. Напишите,
         пожалуйста, программу, которая выводит результат.
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке одно число <span class="tex-math-text">n</span> (<span class="tex-math-text">0 &le; n &le; 2*10<sup>5</sup></span>).
         </p></span><p>В следующих <span class="tex-math-text">n</span> строках заданы по два числа: цвет числа в ящике <span class="tex-math-text">d<sub>i</sub></span> и значение числа <span class="tex-math-text">a<sub>i</sub></span> (<span class="tex-math-text">-10<sup>18</sup> &le; d<sub>i</sub>, a<sub>i</sub> &le; 10<sup>18</sup></span>).
      </p>
      <p>Гарантируется, что сумма чисел одного цвета не превышает <span class="tex-math-text">10<sup>18</sup></span>.
      </p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите в порядке возрастания <span style="font-weight:bold;">номера цвета</span> пары чисел, каждая в новой строке: номер цвета и сумму всех чисел данного цвета.
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
            <td><pre>7
1 5
10 -5
1 10
4 -2
4 3
4 1
4 0
</pre></td>
            <td><pre>1 15
4 2
10 -5
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
            <td><pre>5
5 -10000
-5 100000000000
10 2000000000000
-5 -300000000000
0 10000000000000
</pre></td>
            <td><pre>-5 -200000000000
0 10000000000000
5 -10000
10 2000000000000
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>
