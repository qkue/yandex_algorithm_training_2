<div class="problem-statement">
   <div class="header">
      <h1 class="title">A. Interactor</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>1&nbsp;секунда</td>
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
   <div class="legend"> Лена руководит разработкой тестирующей системы, в которой реализованы интерактивные задачи. <!--l. 50-->
      <p style="text-indent: 0em;">До заверщения очередной стадии проекта осталось написать модуль, определяющий <span style="font-style:
      italic;">итоговый вердикт </span>системы для интерактивной задачи. <span style="font-style: italic;">Итоговый вердикт </span>определяется
      из кода завершения задачи, вердикта интерактора и вердикта чекера по следующим правилам: </p><ul>
      <li>Вердикт чекера и вердикт интерактора — это целые числа от 0 до 7 включительно. </li>
      <li>Код завершения задачи — это целое число от -128 до 127 включительно. </li>
      <li>Если интерактор выдал вердикт 0, итоговый вердикт равен 3 в случае, если программа завершилась с ненулевым кодом, и вердикту
      чекера в противном случае. </li>
      <li>Если интерактор выдал вердикт 1, итоговый вердикт равен вердикту чекера. </li>
      <li>Если интерактор выдал вердикт 4, итоговый вердикт равен 3 в случае, если программа завершилась с ненулевым кодом, и 4
      в противном случае. </li>
      <li>Если интерактор выдал вердикт 6, итоговый вердикт равен 0. </li>
      <li>Если интерактор выдал вердикт 7, итоговый вердикт равен 1. </li>
      <li>В остальных случаях итоговый вердикт равен вердикту интерактора.</li>
      </ul>
      <!--l. 76-->
      <p style="text-indent: 0em;">Ваша задача — реализовать этот модуль. </p>
      <p></p>
      
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> Входной файл состоит из трёх строк. В первой задано целое число <!--l. 79--><math display="inline" style="text-indent: 0em;"
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>r</mi></math> (<!--l. 80--><math display="inline" style="text-indent: 0em;"
      xmlns="http://www.w3.org/1998/Math/MathML"> <mo>−</mo> <mn>1</mn><mn>2</mn><mn>8</mn> <mo>≤</mo> <mi>r</mi> <mo>≤</mo> <mn>1</mn><mn>2</mn><mn>7</mn></math>)
      — код завершения задачи, во второй — целое число <!--l. 81--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math>
      (<!--l. 81--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn> <mo>≤</mo>
      <mi>i</mi> <mo>≤</mo> <mn>7</mn></math>) — вердикт интерактора, в третьей — целое число <!--l. 82--><math display="inline"
      style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math> (<!--l. 82--><math display="inline"
      style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn> <mo>≤</mo> <mi>c</mi> <mo>≤</mo> <mn>7</mn></math>)
      — вердикт чекера. 
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> Выведите одно целое число от 0 до 7 включительно — итоговый вердикт системы. </div>
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
            <td><pre>0
0
0
</pre></td>
            <td><pre>0
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
            <td><pre>-1
0
1
</pre></td>
            <td><pre>3</pre></td>
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
            <td><pre>42
1
6
</pre></td>
            <td><pre>6
</pre></td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 4</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>44
7
4
</pre></td>
            <td><pre>1
</pre></td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 5</h3>
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
4
0
</pre></td>
            <td><pre>3
</pre></td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 6</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>-3
2
4
</pre></td>
            <td><pre>2
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>
