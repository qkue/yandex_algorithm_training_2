<div class="problem-statement">
   <div class="header">
      <h1 class="title">C. Родословная: LCA</h1>
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
         <p>В генеалогическом древе определите для двух элементов их наименьшего общего предка. Наименьшим общим предком элементов A и
            B является такой элемент C, что С является предком A, C является предком B, при этом глубина C является наибольшей из возможных.
            При этом элемент считается своим собственным предком.
         </p></span><p></p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Формат входных данных аналогичен предыдущей задаче.</p></span><p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Для каждого запроса выведите наименьшего общего предка данных элементов.</p></span><p></p>
   </div>
   <h2>Пример</h2>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>9
Alexei Peter_I
Anna Peter_I
Elizabeth Peter_I
Peter_II Alexei
Peter_III Anna
Paul_I Peter_III
Alexander_I Paul_I
Nicholaus_I Paul_I
Alexander_I Nicholaus_I
Peter_II Paul_I
Alexander_I Anna
</pre></td>
            <td><pre>Paul_I
Peter_I
Anna
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>
