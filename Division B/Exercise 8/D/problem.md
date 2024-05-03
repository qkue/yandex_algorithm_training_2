<div class="problem-statement">
   <div class="header">
      <h1 class="title">D. Бусинки</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>2&nbsp;секунды</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>256Mb</td>
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
         <p>Маленький мальчик делает бусы. У него есть много пронумерованных бусинок. Каждая бусинка имеет уникальный номер – целое число
            в диапазоне от 1 до N. Он выкладывает все бусинки на полу и соединяет бусинки между собой произвольным образом так, что замкнутых
            фигур не образуется. Каждая из бусинок при этом оказывается соединенной с какой-либо другой бусинкой. 
         </p></span><p>Требуется определить, какое максимальное количество последовательно соединенных бусинок присутствует в полученной фигуре.</p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке – количество бусинок 1 ≤ N ≤ 2500. В последующих N-1 строках по два целых числа – номера, соединенных бусинок.</p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Вывести одно число – искомое количество бусинок.</p></span></div>
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
            <td><pre>2
1 2
</pre></td>
            <td><pre>2
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
2 1
2 3
2 4
2 5
</pre></td>
            <td><pre>3
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
1 2
2 3
3 4 
4 5
1 6
6 10
10 9
9 8
8 7
</pre></td>
            <td><pre>10
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>
