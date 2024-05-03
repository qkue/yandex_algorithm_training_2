<div class="problem-statement">
   <div class="header">
      <h1 class="title">E. Точка и треугольник</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>1&nbsp;секунда</td>
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
         <p>На координатной плоскости расположены равнобедренный прямоугольный треугольник ABC с длиной катета d и точка X. Катеты треугольника
            лежат на осях координат, а вершины расположены в точках: A (0,0), B (d,0), C (0,d).
         </p></span><p>Напишите программу, которая определяет взаимное расположение точки X и треугольника. Если точка X расположена внутри или на
         сторонах треугольника, выведите 0. Если же точка находится вне треугольника, выведите номер ближайшей к ней вершины.
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Сначала вводится натуральное число d (не превосходящее 1000), а затем координаты точки X – два целых числа из диапазона от
            ­–1000 до 1000.
         </p></span><p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Если точка лежит внутри, на стороне треугольника или совпадает с одной из вершин, то выведите число 0. Если точка лежит вне
            треугольника, то выведите номер вершины треугольника, к которой она расположена ближе всего (1 – к вершине A, 2 – к B, 3 –
            к C). Если точка расположена на одинаковом расстоянии от двух вершин, выведите ту вершину, номер которой меньше.
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
            <td><pre>5
1 1
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
            <td><pre>3
-1 -1
</pre></td>
            <td><pre>1
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
            <td><pre>4
4 4
</pre></td>
            <td><pre>2
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
            <td><pre>4
2 2
</pre></td>
            <td><pre>0
</pre></td>
         </tr>
      </tbody>
   </table>
   <h2>Примечания</h2>
   <div class="notes"><span style="">
         <p>Комментарии к примерам тестов</p></span><p>1. Точка лежит внутри треугольника.</p>
      <p>2. Точка лежит вне треугольника и ближе всего к ней вершина A</p>
      <p>3. Точка лежит на равном расстоянии от вершин B и C,в этом случае нужно вывести ту вершину, у которой номер меньше, т.е. выведено
         должно быть число 2
      </p>
      <p>4. Точка лежит на стороне треугольника.</p>
   </div>
</div></div>
