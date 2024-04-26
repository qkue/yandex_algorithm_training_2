<div class="problem-statement">
   <div class="header">
      <h1 class="title">D. Вырубка леса</h1>
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
         <p>Фермер Николай нанял двух лесорубов: Дмитрия и Федора, чтобы вырубить лес, на месте которого должно быть кукурузное поле.
            В лесу растут <span class="tex-math-text">X</span> деревьев.
         </p></span><p>Дмитрий срубает по <span class="tex-math-text">A</span> деревьев в день, но каждый <span class="tex-math-text">K</span>-й день он отдыхает и не срубает ни одного дерева. Таким образом, Дмитрий отдыхает в <span class="tex-math-text">K</span>-й, <span class="tex-math-text">2K</span>-й, <span class="tex-math-text">3K</span>-й день, и т.д.
      </p>
      <p>Федор срубает по <span class="tex-math-text">B</span> деревьев в день, но каждый <span class="tex-math-text">M</span>-й день он отдыхает и не срубает ни одного дерева. Таким образом, Федор отдыхает в <span class="tex-math-text">M</span>-й, <span class="tex-math-text">2M</span>-й, <span class="tex-math-text">3M</span>-й день, и т.д.
      </p>
      <p>Лесорубы работают параллельно и, таким образом, в дни, когда никто из них не отдыхает, они срубают <span class="tex-math-text">A + B</span> деревьев, в дни, когда отдыхает только Федор — <span class="tex-math-text">A</span> деревьев, а в дни, когда отдыхает только Дмитрий — <span class="tex-math-text">B</span> деревьев. В дни, когда оба лесоруба отдыхают, ни одно дерево не срубается.
      </p>
      <p>Фермер Николай хочет понять, за сколько дней лесорубы срубят все деревья, и он сможет засеять кукурузное поле.</p>
      <p>Требуется написать программу, которая по заданным целым числам <span class="tex-math-text">A, K, B, M</span> и <span class="tex-math-text">X</span> определяет, за сколько дней все деревья в лесу будут вырублены. 
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Входной файл содержит пять целых чисел, разделенных пробелами: <span class="tex-math-text">A, K, B, M</span> и <span class="tex-math-text">X</span> <span class="tex-math-text">(1 &le; A, B &le; 10<sup>9</sup>, 2 &le; K, M &le; 10<sup>18</sup>, 1 &le; X &le; 10<sup>18</sup>)</span>. 
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выходной файл должен содержать одно целое число — искомое количество дней. </p></span></div>
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
            <td><pre>1 2 1 3 10
</pre></td>
            <td><pre>8
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
            <td><pre>1 2 1 3 11
</pre></td>
            <td><pre>9
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
            <td><pre>19 3 14 6 113
</pre></td>
            <td><pre>4
</pre></td>
         </tr>
      </tbody>
   </table>
   <h2>Примечания</h2>
   <div class="notes"><span style="">
         <p>Рассмотрим пример:</p></span><p><span class="tex-monospace">2 4 3 3 25</span></p>
      <p><span class="tex-monospace">7</span></p>
      <p>В приведенном примере лесорубы вырубают 25 деревьев за 7 дней следующим образом:</p>
      <p>
         <ul>
            <li>1-й день: Дмитрий срубает 2 дерева, Федор срубает 3 дерева, итого 5 деревьев;
               <p></p>
            </li>
            <li>2-й день: Дмитрий срубает 2 дерева, Федор срубает 3 дерева, итого 10 деревьев;
               <p></p>
            </li>
            <li>3-й день: Дмитрий срубает 2 дерева, Федор отдыхает, итого 12 деревьев;
               <p></p>
            </li>
            <li>4-й день: Дмитрий отдыхает, Федор срубает 3 дерева, итого 15 деревьев;
               <p></p>
            </li>
            <li>5-й день: Дмитрий срубает 2 дерева, Федор срубает 3 дерева, итого 20 деревьев;
               <p></p>
            </li>
            <li>6-й день: Дмитрий срубает 2 дерева, Федор отдыхает, итого 22 дерева;
               <p></p>
            </li>
            <li>7-й день: Дмитрий срубает 2 дерева, Федор срубает оставшееся 1 дерево, итого все 25 деревьев срублены. </li>
         </ul>
      </p>
   </div>
</div></div>
