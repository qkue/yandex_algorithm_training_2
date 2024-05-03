<div class="problem-statement">
   <div class="header">
      <h1 class="title">C. Даты</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>2&nbsp;секунды</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>512Mb</td>
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
   <div class="legend"> Как известно, два наиболее распространённых формата записи даты — это европейский (сначала день, потом месяц, потом год)
      и американски (сначала месяц, потом день, потом год). Системный администратор поменял дату на одном из бэкапов и сейчас хочет
      вернуть дату обратно. Но он не проверил, в каком формате дата используется в системе. Может ли он обойтись без этой информации?
      <!--l. 51-->
      <p style="text-indent: 0em;">Иначе говоря, вам даётся запись некоторой корректной даты. Требуется выяснить, однозначно ли
      по этой записи определяется дата даже без дополнительной информации о формате. </p>
      
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> Первая строка входных данных содержит три целых числа — <!--l. 55--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>,
      <!--l. 55--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math>
      и <!--l. 55--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math>
      (<!--l. 55--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn> <mo>≤</mo>
      <mi>x</mi> <mo>≤</mo> <mn>3</mn><mn>1</mn></math>, <!--l. 55--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn>
      <mo>≤</mo> <mi>y</mi> <mo>≤</mo> <mn>3</mn><mn>1</mn></math>, <!--l. 55--><math display="inline" style="text-indent: 0em;"
      xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mn>9</mn><mn>7</mn><mn>0</mn> <mo>≤</mo> <mi>z</mi> <mo>≤</mo> <mn>2</mn><mn>0</mn><mn>6</mn><mn>9</mn></math>.
      Гарантируется, что хотя бы в одном формате запись <!--l. 56--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math><!--l.
      56--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>y</mi></math><!--l. 56--><math
      display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>z</mi></math> задаёт корректную
      дату. 
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> Выведите 1, если дата определяется однозначно, и 0 в противном случае. </div>
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
            <td><pre>1 2 2003
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
            <td><pre>2 29 2008
</pre></td>
            <td><pre>1
</pre></td>
         </tr>
      </tbody>
   </table>
   <h2>Примечания</h2>
   <div class="notes"> В первом примере при одной системе записи дата равна 1 февраля, при другой - 2 января 2003 года, то есть однозначно назвать
      дату не получается. <!--l. 64-->
      <p style="text-indent: 0em;">Во втором примере корректный вариант даты может быть только в американском формате, где она задаёт
      29 февраля 2008 года. </p>
      
   </div>
</div></div>
