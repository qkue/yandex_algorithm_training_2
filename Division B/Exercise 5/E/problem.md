<div class="problem-statement">
   <div class="header">
      <h1 class="title">E. Сумма трёх</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>15&nbsp;секунд</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>256Mb</td>
         </tr>
         <tr class="input-file">
            <td class="property-title">Ввод</td>
            <td colspan="1">стандартный ввод или threesum.in</td>
         </tr>
         <tr class="output-file">
            <td class="property-title">Вывод</td>
            <td colspan="1">стандартный вывод или threesum.out</td>
         </tr>
      </table>
   </div>
   <h2></h2>
   <div class="legend"> Даны три массива целых чисел <!--l. 47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mi>B</mi><mo>,</mo><mi>C</mi></math>
      и целое число <!--l. 47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math>.
      <!--l. 49-->
      <p style="text-indent: 0em;">Найдите такие <!--l. 49--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>,</mo><mi>j</mi><mo>,</mo><mi>k</mi></math>,
      что <!--l. 49--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><msub><mrow><mi>A</mi></mrow><mrow><mi>i</mi></mrow></msub>
      <mo>+</mo> <msub><mrow><mi>B</mi></mrow><mrow><mi>j</mi></mrow></msub> <mo>+</mo> <msub><mrow><mi>C</mi></mrow><mrow><mi>k</mi></mrow></msub>
      <mo>=</mo> <mi>S</mi></math>. </p>
      
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> На первой строке число <!--l. 52--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math>
      (<!--l. 52--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn> <mo>≤</mo>
      <mi>S</mi> <mo>≤</mo> <mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mn>9</mn></mrow></msup></math>). Следующие три строки
      содержат описание массивов <!--l. 53--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>,</mo><mi>B</mi><mo>,</mo><mi>C</mi></math>
      в одинаковом формате: первое число задает длину <!--l. 54--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>
      соответствующего массива (<!--l. 54--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn>
      <mo>≤</mo> <mi>n</mi> <mo>≤</mo> <mn>1</mn><mn>5</mn><mspace width="0.3em"><mn>0</mn><mn>0</mn><mn>0</mn></mspace></math>),
      затем заданы <!--l. 55--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>
      целых чисел от <!--l. 55--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
      до <!--l. 55--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mn>9</mn></mrow></msup></math>
      — сам массив. 
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> Если таких <!--l. 58--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>,</mo><mi>j</mi><mo>,</mo><mi>k</mi></math>
      не существует, выведите единственное число <!--l. 58--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML">
      <mo>−</mo> <mn>1</mn></math>. Иначе выведите на одной строке три числа — <!--l. 59--><math display="inline" style="text-indent:
      0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>,</mo><mi>j</mi><mo>,</mo><mi>k</mi></math>. Элементы массивов
      нумеруются с нуля. Если ответов несколько, выведите лексикографически минимальный. 
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
            <td><pre>3
2 1 2
2 3 1
2 3 1
</pre></td>
            <td><pre>0 1 1
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
1 5
1 4
1 3
</pre></td>
            <td><pre>-1
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
            <td><pre>5
4 1 2 3 4
3 5 2 1
4 5 3 2 2
</pre></td>
            <td><pre>0 1 2
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>
