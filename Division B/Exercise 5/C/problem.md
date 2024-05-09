<div class="problem-statement">
   <div class="header">
      <h1 class="title">C. Каждому по компьютеру</h1>
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
         <p>В новом учебном году на занятия в компьютерные классы Дворца Творчества Юных пришли учащиеся, которые были разбиты на N групп.
            В i-й группе оказалось <span class="tex-math-text">X<sub>i</sub></span> человек. Тут же перед директором встала серьезная проблема: как распределить группы по аудиториям. Во дворце имеется M ≥
            N аудиторий, в j-й аудитории имеется <span class="tex-math-text">Y<sub>j</sub></span> компьютеров. Для занятий необходимо, чтобы у каждого учащегося был компьютер и еще один компьютер был у преподавателя. Переносить
            компьютеры из одной аудитории в другую запрещается. Помогите директору!
         </p></span><p>Напишите программу, которая найдет, какое максимальное количество групп удастся одновременно распределить по аудиториям, чтобы
         всем учащимся в каждой группе хватило компьютеров, и при этом остался бы еще хотя бы один для учителя.
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>На первой строке входного файла расположены числа N и M (1 ≤ N ≤ M ≤ 1000). На второй строке расположено N чисел — <span class="tex-math-text">X<sub>1</sub></span>, …, <span class="tex-math-text">X<sub>N</sub></span> (1 ≤ <span class="tex-math-text">X<sub>i</sub></span> ≤ 1000 для всех 1 ≤ i ≤ N). На третьей строке расположено M чисел <span class="tex-math-text">Y<sub>1</sub></span>, ..., <span class="tex-math-text">Y<sub>M</sub></span> (1 ≤ <span class="tex-math-text">Y<sub>i</sub></span> ≤ 1000 для всех 1 ≤ i ≤ M).
         </p></span><p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите на первой строке число P - количество групп, которые удастся распределить по аудиториям. На второй строке выведите
            распределение групп по аудиториям – N чисел, i-е число должно соответствовать номеру аудитории, в которой должна заниматься
            i-я группа. (Нумерация как групп, так и аудиторий, начинается с 1). Если i-я группа осталась без аудитории, i-е число должно
            быть равно 0. Если допустимых распределений несколько, выведите любое из них.
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
            <td><pre>1 1
1
2
</pre></td>
            <td><pre>1
1 
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
            <td><pre>1 1
1
1
</pre></td>
            <td><pre>0
0 
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>
