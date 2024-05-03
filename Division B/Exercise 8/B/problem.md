<div class="problem-statement">
   <div class="header">
      <h1 class="title">B. Родословная: предки и потомки</h1>
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
         <p>В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.</p></span><p>Каждом элементу дерева сопоставляется целое неотрицательное число, называемое высотой. У родоначальника высота равна 0, у
         любого другого элемента высота на 1 больше, чем у его родителя.
      </p>
      <p>Даны два элемента в дереве. Определите, является ли один из них потомком другого.</p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Программа получает на вход число элементов в генеалогическом древе N. Далее следует N−1 строка, задающие родителя для каждого
            элемента древа, кроме родоначальника. Каждая строка имеет вид имя_потомка имя_родителя.
         </p></span><p>Далее до конца файла идут строки, содержащие имена двух элементов дерева.</p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Для каждого такого запроса выведите одно из трех чисел: 1, если первый элемент является предком второго, 2, если второй является
            предком первого или 0, если ни один из них не является предком другого.
         </p></span></div>
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
Anna Nicholaus_I
Peter_II Peter_I
Alexei Paul_I
</pre></td>
            <td><pre>1 2 0 
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>
