<div class="problem-statement">
   <div class="header">
      <h1 class="title">C. Минимальное покрытие</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>3&nbsp;секунды</td>
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
         <p>На прямой задано некоторое множество отрезков с целочисленными координатами концов <span style="">[<span class="tex-math-text">L<sub>i</sub></span>, <span class="tex-math-text">R<sub>i</sub></span>]</span>. Выберите среди данного множества подмножество отрезков, целиком покрывающее отрезок <span style="">[0, M]</span>, (M — натуральное число), содержащее наименьшее число отрезков.
         </p></span><p></p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке указана константа M (<span class="tex-math-text">1 &le; M &le; 5000</span>). В каждой последующей строке записана пара чисел <span class="tex-math-text">L<sub>i</sub></span> и <span class="tex-math-text">R<sub>i</sub></span> (<span class="tex-math-text">L<sub>i</sub>, R<sub>i</sub> &le; 50000</span>), задающая координаты левого и правого концов отрезков. Список завершается парой нулей. Общее число отрезков не превышает
            100 000.
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>В первой строке выходного файла выведите минимальное число отрезков, необходимое для покрытия отрезка <span style="">[0; M]</span>. Далее выведите список покрывающего подмножества, упорядоченный по возрастанию координат левых концов отрезков. Список отрезков
            выводится в том же формате, что и во входe. Завершающие два нуля выводить не нужно. Если покрытие отрезка <span style="">[0, M]</span> исходным множеством отрезков <span style="">[<span class="tex-math-text">L<sub>i</sub></span>, <span class="tex-math-text">R<sub>i</sub></span>]</span> невозможно, то следует вывести единственную фразу “No solution”.
         </p></span><p></p>
   </div>
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
            <td><pre>1
-1 0
-5 -3
2 5
0 0

</pre></td>
            <td><pre>No solution

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
            <td><pre>1
-1 0
0 1
0 0
</pre></td>
            <td><pre>1
0 1
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>
