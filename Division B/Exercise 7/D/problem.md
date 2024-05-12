<div class="problem-statement">
   <div class="header">
      <h1 class="title">D. Наполненность котятами</h1>
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
   <div class="legend"> На прямой в точках <!--l. 47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><msub><mrow><mi>a</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><msub><mrow><mi>a</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><mo>…</mo><mo>,</mo><msub><mrow><mi>a</mi></mrow><mrow><mi>n</mi></mrow></msub></math>
      (возможно, совпадающих) сидят <!--l. 47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>
      котят. На той же прямой лежат <!--l. 48--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math>
      отрезков <!--l. 48--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mrow><mo>[</mo><mrow><msub><mrow><mi>l</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><msub><mrow><mi>r</mi></mrow><mrow><mn>1</mn></mrow></msub></mrow><mo>]</mo></mrow><mo>,</mo><mrow><mo>[</mo><mrow><msub><mrow><mi>l</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><msub><mrow><mi>r</mi></mrow><mrow><mn>2</mn></mrow></msub></mrow><mo>]</mo></mrow><mo>,</mo><mo>…</mo><mo>,</mo><mrow><mo>[</mo><mrow><msub><mrow><mi>l</mi></mrow><mrow><mi>m</mi></mrow></msub><mo>,</mo><msub><mrow><mi>r</mi></mrow><mrow><mi>m</mi></mrow></msub></mrow><mo>]</mo></mrow></math>.
      Нужно для каждого отрезка узнать его <span style="font-style: italic;">наполненность котятами </span>— сколько котят сидит
      на отрезке. 
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> На первой строке <!--l. 52--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>
      и <!--l. 52--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math>
      (<!--l. 52--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn> <mo>≤</mo>
      <mi>n</mi><mo>,</mo><mi>m</mi> <mo>≤</mo> <mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mn><sup>5</sup></mn></mrow></msup></math>). На
      второй строке <!--l. 53--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>
      целых чисел <!--l. 53--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><msub><mrow><mi>a</mi></mrow><mrow><mi>i</mi></mrow></msub></math>
      (<!--l. 53--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn> <mo>≤</mo>
      <msub><mrow><mi>a</mi></mrow><mrow><mi>i</mi></mrow></msub> <mo>≤</mo> <mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mn><sup>9</sup></mn></mrow></msup></math>).
      Следующие <!--l. 54--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math>
      строк содержат пары целых чисел <!--l. 54--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><msub><mrow><mi>l</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>,</mo><msub><mrow><mi>r</mi></mrow><mrow><mi>i</mi></mrow></msub></math>
      (<!--l. 54--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn> <mo>≤</mo>
      <msub><mrow><mi>l</mi></mrow><mrow><mi>i</mi></mrow></msub> <mo>≤</mo> <msub><mrow><mi>r</mi></mrow><mrow><mi>i</mi></mrow></msub>
      <mo>≤</mo> <mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mn><sup>9</sup></mn></mrow></msup></math>). 
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> Выведите <!--l. 57--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math>
      целых чисел. <!--l. 57--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math>-е
      число — <span style="font-style: italic;">наполненность</span> <span style="font-style: italic;">котятами </span><!--l. 57--><math
      display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math>-го отрезка. 
   </div>
</div></div>
