<div class="problem-statement">
   <div class="header">
      <h1 class="title">B. Таможня</h1>
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
         <p>Идёт 2163 год. Мишу, который работает в отделении таможни при космодроме города Нью-Питер, вызвал в кабинет шеф.</p></span><p>Как оказалось, недавно Министерство Налогов и Сборов выделило отделению определённую сумму денег на установку новых аппаратов
         для автоматического досмотра грузов. Естественно, средства были выделены с таким расчётом, чтобы грузы теперь находились на
         таможне ровно столько времени, сколько требуется непосредственно на их досмотр.
      </p>
      <p>В руках шефа каким-то образом оказались сведения о надвигающейся ревизии – список из N грузов, которые будут контролироваться
         Министерством. Для каждого груза известны время его прибытия, отсчитываемое с некоторого момента, хранимого в большом секрете,
         и время, требуемое аппарату для обработки этого груза. Шеф дал Мише задание по этим данным определить, какое минимальное количество
         аппаратов необходимо заказать на заводе, чтобы все грузы Министерства начинали досматриваться сразу после прибытия. Необходимо
         учесть, что конструкция тех аппаратов, которые было решено установить, не позволяет обрабатывать два груза одновременно на
         одном аппарате. Напишите программу, которая поможет Мише справиться с его задачей.
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>На первой строке входного файла задано число N (0 ≤ N ≤ 50 000). На следующих N строках находится по 2 целых положительных
            числа <span class="tex-math-text">T<sub>i</sub></span> и <span class="tex-math-text">L<sub>i</sub></span> – время прибытия соответствующего груза и время, требуемое для его обработки (1 ≤ <span class="tex-math-text">T<sub>i</sub></span> ≤ <span class="tex-math-text">10<sup>6</sup></span>, 1 ≤ <span class="tex-math-text">L<sub>i</sub></span> ≤ <span class="tex-math-text">10<sup>6</sup></span>).
         </p></span><p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>В выходной файл выведите одно число – наименьшее количество аппаратов, которое нужно установить, чтобы не вызвать подозрений
            у Министерства.
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
            <td><pre>3
3 2
4 2
5 2
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
13 4
15 1
11 5
12 3
10 3
</pre></td>
            <td><pre>3
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>
