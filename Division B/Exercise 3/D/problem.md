<div class="problem-statement">
   <div class="header">
      <h1 class="title">D. Угадай число</h1>
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
         <p>Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n. Беатриса пытается угадать это число, для этого
            она называет некоторые множества натуральных чисел. Август отвечает Беатрисе YES, если среди названных ей чисел есть задуманное
            или NO в противном случае. После нескольких заданных вопросов Беатриса запуталась в том, какие вопросы она задавала и какие
            ответы получила и просит вас помочь ей определить, какие числа мог задумать Август. 
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Первая строка входных данных содержит число n&nbsp;— наибольшее число, которое мог загадать Август. Далее идут строки, содержащие
            вопросы Беатрисы. Каждая строка представляет собой набор чисел, разделенных пробелами. После каждой строки с вопросом идет
            ответ Августа: YES или NO. Наконец, последняя строка входных данных содержит одно слово HELP. 
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Вы должны вывести (через пробел, в порядке возрастания) все числа, которые мог задумать Август. </p></span></div>
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
            <td><pre>10
1 2 3 4 5
YES
2 4 6 8 10
NO
HELP
</pre></td>
            <td><pre>1 3 5
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
1 2 3 4 5 6 7 8 9 10
YES
1
NO
2
NO
3
NO
4
NO
6
NO
7
NO
8
NO
9
NO
10
NO
HELP

</pre></td>
            <td><pre>5
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>
